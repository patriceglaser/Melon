import json
from collections import Counter
import itertools
import time
import datetime

file_name = 'data/EtherscanExcluder_excluded_person_dict.json'


with open(file_name) as json_file:
    person_dict = json.load(json_file)
# del 'meta_data' to loop thorugh all keys
del person_dict['meta_data']

# save data or not
bSave = True

t = time.time()

###############################################################################
#  check that 'num_connections' == length of arrays
###############################################################################

print('Consistency check')

for person in person_dict:
    for level in ['level0', 'level1', 'level2']:
        length_array = [ \
            person_dict[person][level]['num_connections'], \
            len(person_dict[person][level]['person_B_list']), \
            len(person_dict[person][level]['connection_path']), \
            len(person_dict[person][level]['transaction_hash']) \
            ]
        if len(set(length_array)) != 1:
            print('Issue for address {} in level {}'.format(person, level))

del person
del level
del length_array



###############################################################################
#  get unique transactions with other person
#  (on level 1,2 transactions are counted as 4 for following scenario:
#       person_A --> person_C       hash: 1
#           person_C --> person_B   hash: 2
#           person_C --> person_B   hash: 3
#           person_C --> person_B   hash: 4)
# --> transaction hash for person_C --> person_B must also be unique
###############################################################################

print('Create unique_person_dict')

# create a person_dict with only unique transactions
unique_person_dict = person_dict.copy()

for person in unique_person_dict:

    # level 0
    # all transactions hashes need to be unique
    this_dict = unique_person_dict[person]['level0']
    if len(this_dict['transaction_hash'])!= len(set(this_dict['transaction_hash'])):
        # there are mutiple transactions with the same hash
        count = Counter(this_dict['transaction_hash'])
        # count looks like {'hash1': 1, 'hash2': 2, ...} = {key: value}
        # delete multiples
        for key, value in count.items():
            # delete until only one is left
            while value>1:
                hash_index = this_dict['transaction_hash'].index(key)
                this_dict['num_connections'] -= 1
                this_dict['person_B_list'].pop(hash_index)
                this_dict['connection_path'].pop(hash_index)
                this_dict['transaction_hash'].pop(hash_index)
                value -= 1
        del count
        del key
        del value
        del hash_index
        
        
    # level 1
    # for the same person_B, I need to check that I do not have the same person_C
    this_dict = unique_person_dict[person]['level1']
    unique_person_B_list = set(this_dict['person_B_list'])
    indices_to_delete_list = []
    for person_B in unique_person_B_list:
        person_C_dict = {}
        for connection_index, connection in enumerate(this_dict['connection_path']):
            # connection = (person_C, person_B)
            if connection[1] == person_B:
                person_C = connection[0]
                if person_C not in person_C_dict:
                    person_C_dict[person_C] = True
                else:
                    # person_C was already used. Delete its entry
                    indices_to_delete_list.append(connection_index)

    # delete indices starting from the back. If I start from the beginning,
    # indices will be wrong as all indices start to shift
    indices_to_delete_list.sort(reverse=True)
    for index in indices_to_delete_list:
        this_dict['num_connections'] -= 1
        this_dict['person_B_list'].pop(index)
        this_dict['connection_path'].pop(index)
        this_dict['transaction_hash'].pop(index)

    # level 2
    # for the same person_B, I need to check that I do not have the same person_C & person_D
    this_dict = unique_person_dict[person]['level2']
    unique_person_B_list = set(this_dict['person_B_list'])
    indices_to_delete_list = []
    for person_B in unique_person_B_list:
        person_C_and_D_dict = {}
        for connection_index, connection in enumerate(this_dict['connection_path']):
            # connection = (person_C, person_D, person_B)
            if connection[2] == person_B:
                person_C = connection[0]
                person_D = connection[1]
                person_C_and_D = (person_C, person_D)
                person_D_and_C = (person_D, person_C)
                if (person_C_and_D not in person_C_and_D_dict) & (person_D_and_C not in person_C_and_D_dict):
                    person_C_and_D_dict[person_C_and_D] = True
                    person_C_and_D_dict[person_D_and_C] = True
                else:
                    # person_C and person_D was already used. Delete its entry
                    indices_to_delete_list.append(connection_index)
                    
                    
        del connection_index, connection

    # delete indices starting from the back. If I start from the beginning,
    # indices will be wrong as all indices start to shift
    indices_to_delete_list.sort(reverse=True)
    for index in indices_to_delete_list:
        this_dict['num_connections'] -= 1
        this_dict['person_B_list'].pop(index)
        this_dict['connection_path'].pop(index)
        this_dict['transaction_hash'].pop(index)
        

del person
del this_dict
del unique_person_B_list
del indices_to_delete_list
del person_B, person_C, person_C_and_D, person_C_and_D_dict, person_C_dict




###############################################################################
# Check network
# which person_A has with which person_B a lot of contacts
###############################################################################


#the result of this is used in FM. 
print('Create network_dict')

# assume very simple model and do not count how many person_A has contact with person_B
# binaris contacts: person_A has contact with person_B or not
# all person that are in contact with person_A or its person_Bs will be in one group

# put person that have transaction with each other in groups
# network_dict = {'Group': [list of persons in contact]}
# save IDs here
network_dict = {}

#this is for clustering
level_list = ['level0', 'level1', 'level2']
for level_index in range(len(level_list)):
    level = level_list[level_index]
    network_dict[level] = {}


    # create groups of person_A with its unique person_B
    group_list = []
    for person_name in unique_person_dict:
        person = unique_person_dict[person_name][level]
        new_group = [person_name] + person['person_B_list']
        if level_index > 0:
            # merge with lower level
            lower_level = level_list[level_index-1]
            lower_level_person_B_list = unique_person_dict[person_name][lower_level]['person_B_list']
            new_group += lower_level_person_B_list
                
        # every member is only once in the list
        new_group = [ind for ind in set(new_group)]
        group_list.append(new_group)
        # have only unique entries
        # group_list = [ind for ind in set(group_list)]
        # group_list = list(set(group_list))

    merge_made = True

    while (merge_made) & (len(group_list)>1):
        old_group_list = group_list.copy()
        group_list = []

        possible_merge_list = list(itertools.combinations(old_group_list, 2))

        # per default no merge is made
        merge_made = False

        for possible_merge_index, possible_merge in enumerate(possible_merge_list):
            # check if any element in the two groups is the same. If so merge them
            merge = possible_merge[0] + possible_merge[1]
            merge.sort()
            if len(merge) != len(set(merge)):
                # one element is double. Merge!
                group_list.append(list(set(merge)))
                merge_made = True

                # remove merged items from old_group_list
                old_group_list.remove(possible_merge[0])
                old_group_list.remove(possible_merge[1])
                # add remaining members to group_list
                group_list.extend(old_group_list)
                break
            if possible_merge_index == len(possible_merge_list)-1:
                # last permutation was tested and no merge worked --> done
                # and will leave the while loop
                group_list = old_group_list

    # no further merges are done. Looks like I am done
    for group_index, group in enumerate(group_list):
        network_dict[level][group_index] = group

        
        
        
        
if bSave:
    elapsed = time.time() - t
    currentDT = datetime.datetime.now()  
            
    network_dict['meta_data'] = {'Time of execution' : currentDT.strftime("%Y%m%d_%H%M%S"), 
                                'elapsed time (min)' : elapsed/60}
    
    file_name = 'data/EtherscanAnalyzer_network_dict.json'
    
    with open(file_name, 'w') as fp:
        json.dump(network_dict, fp,  indent=4)      
              
    

del level
del group_list
del person_name
del person
del merge_made
del old_group_list
del possible_merge_list
del possible_merge_index
del possible_merge
del merge
del group
del group_index
del index
del new_group    


