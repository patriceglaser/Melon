###############################################################################
#  Function definitions
###############################################################################

def get_page_source(person_to_check):
    global source_page_dict
    global dict_lookups
    global url_lookups
    
    
    if person_to_check in source_page_dict:
        page_source = source_page_dict[person_to_check]
        # check if site was correctly loaded
        dict_lookups += 1
    else:
        url = pre_url + person_to_check
        page_source = scraper.get(url).content.decode("utf-8")
        
        # check if site was correctly loaded
        str = 'Contract Address {}'.format(person_to_check)
        additional_time_factor = 1
        while str not in page_source and additional_time_factor!=6:
            time.sleep(2*additional_time_factor)
            additional_time_factor += 1
            page_source = scraper.get(url).content.decode("utf-8")
            
        source_page_dict[person_to_check] = page_source
        url_lookups += 1
        # print to show activity
        print('*'*random.randint(1,5))
        
    return page_source



###############################################################################
# main script
###############################################################################

import json
import cfscrape 
import datetime      
import random  
import time

# save data or not
bSave = True

file_name = 'data/EtherscanScraper_person_dict.json'

with open(file_name) as json_file:
    person_dict = json.load(json_file)
# del 'meta_data' to loop thorugh all keys
del person_dict['meta_data']

t = time.time()



###############################################################################
# convert entries in 'connection_path' and 'transaction_hash' to tuples
# tuples keeps pairs together (person_C, person_B)
###############################################################################
print('Convert to tuples')

for person in person_dict:
    for level in ['level1', 'level2']:
        path = person_dict[person][level]['connection_path']
        person_dict[person][level]['connection_path'] = [tuple(entry) for entry in path]
        trans = person_dict[person][level]['transaction_hash']
        person_dict[person][level]['transaction_hash'] = [tuple(entry) for entry in trans]

del person
del level
del path
del trans



###############################################################################
#  setup  exclude list
###############################################################################
print('setup exclude list')

exclude_list_txt = open('exclude_list.txt', 'r')
exclude_list = [line.split(',')[0] for line in exclude_list_txt.readlines()]        
        
# additionally exclude addresses that have either 'Public Name Tag', 'Creator Address'
# or 'View Token Tracker Page' on etherscan
        
exlcude_url_types = ['Public Name Tag', 'Creator Address','View Token Tracker Page']
pre_url = 'https://etherscan.io/address/'
scraper = cfscrape.create_scraper()
# for every address save source_page here to not query mutliple times for the same address
source_page_dict = {}
dict_lookups = 0
url_lookups = 0



###############################################################################
#  exclude melon addresses as person_C and person_D
###############################################################################
print('Find addresses to exclude')

level_1_delete_list = {}
level_2_delete_list = {}
for person in person_dict:
    # level 1
    level_1_delete_list[person] = []
    for entry_index, entry in enumerate(person_dict[person]['level1']['connection_path']):
        # convert from tuple to list
        entry_as_list = [ind for ind in entry]
        # entry_as_list = (person_C, person_B)
        gr = []
        # only person_C
        gr.append(entry_as_list[0])
        gr.extend(exclude_list)
        if (len(gr) != len(set(gr))):
            # this address is in exclude list
            level_1_delete_list[person].append(entry_index)
        else:
            # check if address must be exlcuded due to exlcude_url_types
            person_to_check = entry_as_list[0]
            page_source = get_page_source(person_to_check)
            if any(x in page_source for x in exlcude_url_types):
                # exclude
                level_1_delete_list[person].append(entry_index)
            
    # level 2
    level_2_delete_list[person] = []
    for entry_index, entry in enumerate(person_dict[person]['level2']['connection_path']):
        # convert from tuple to list
        entry_as_list = [ind for ind in entry]
        # entry_as_list = (person_C, person_D, person_B)
        gr = []
        # only person_C and person_D
        gr.extend(entry_as_list[:2])
        gr.extend(exclude_list)
        if (len(gr) != len(set(gr))):
            level_2_delete_list[person].append(entry_index)
        else:
            # check if address must be exlcuded due to exlcude_url_types
            person_to_check = entry_as_list[0]
            page_source = get_page_source(person_to_check) 
            if any(x in page_source for x in exlcude_url_types):
                # exclude
                level_2_delete_list[person].append(entry_index)
            else:
                # maybe person_D can be excluded. Do not check person_D if person_C
                # already leads to an exclusion
                person_to_check = entry_as_list[1]
                page_source = get_page_source(person_to_check)
                if any(x in page_source for x in exlcude_url_types):
                    # exclude
                    level_2_delete_list[person].append(entry_index)


print('Delete addresses')

num_level1_deletions = 0
num_level2_deletions = 0
for person in person_dict:
    # level 1
    level_1_delete_list[person].sort(reverse=True)
    index_to_delete_list = level_1_delete_list[person]
    for index in index_to_delete_list:
        person_dict[person]['level1']['num_connections'] -= 1
        del person_dict[person]['level1']['person_B_list'][index]
        del person_dict[person]['level1']['connection_path'][index]
        del person_dict[person]['level1']['transaction_hash'][index]
        num_level1_deletions += 1
        
    # level 2
    level_2_delete_list[person].sort(reverse=True)
    index_to_delete_list = level_2_delete_list[person]
    for index in index_to_delete_list:
        person_dict[person]['level2']['num_connections'] -= 1
        del person_dict[person]['level2']['person_B_list'][index]
        del person_dict[person]['level2']['connection_path'][index]
        del person_dict[person]['level2']['transaction_hash'][index]
        num_level2_deletions += 1
            
        
        
print('Test deletions')    

# test if all addresses are excluded
for person in person_dict:
    # Level 1
    for entry_index, entry in enumerate(person_dict[person]['level1']['connection_path']):
        # if entry[0] in exclude_list:
        entry_as_list = [ind for ind in entry]
        # entry_as_list = (person_C, person_B)
        gr = []
        # only person_C
        gr.append(entry_as_list[0])
        gr.extend(exclude_list)
        if len(gr) != len(set(gr)):
            print('Still there')
    # level 2
    for entry_index, entry in enumerate(person_dict[person]['level2']['connection_path']):
        # entry = (person_C, person_D, person_B)
        #if (entry[0] in exclude_list) | (entry[1] in exclude_list):
        entry_as_list = [ind for ind in entry]
        # entry_as_list = (person_C, person_D, person_B)
        gr = []
        # only person_C and person_D
        gr.extend(entry_as_list[:2])
        gr.extend(exclude_list)
        if len(gr) != len(set(gr)):
            print('Still there')
         
            
del exclude_list
del level_1_delete_list
del level_2_delete_list
del entry_index
del entry
del person
del entry_as_list
del gr
del index_to_delete_list



###############################################################################
#  Save struct
###############################################################################

print('Save struct')

elapsed = time.time() - t
if bSave:
    currentDT = datetime.datetime.now()        
        
    excluded_person_dict = person_dict
    excluded_person_dict['meta_data'] = {'Time of execution' : currentDT.strftime("%Y%m%d_%H%M%S"), 
                                'elapsed time (min)' : elapsed/60,
                                'number level 1 deletions' : num_level1_deletions,
                                'number level 2 deletions' : num_level2_deletions,
                                'number etherscan dict look ups' : dict_lookups,
                                'number etherscan queries' : url_lookups}
                           
    file_name = 'data/EtherscanExcluder_excluded_person_dict.json'
    
    with open(file_name, 'w') as fp:
        json.dump(excluded_person_dict, fp,  indent=4)
        
        
print('---------- DONE ------------')   