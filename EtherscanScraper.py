###############################################################################
#  Function definitions
###############################################################################

def pullFundManager():

    from graphqlclient import GraphQLClient
    import json

    client = GraphQLClient('https://api.thegraph.com/subgraphs/name/melonproject/melon')

    result = client.execute('''
    {
       funds(first: 300, orderBy: name, orderDirection: asc) {
       name
       isShutdown
          manager {
            id
          }
          }
    }
    ''')
    JSON = json.loads(result)

    return JSON



def get_partner_info_from_etherscan(address, number_transactions, APIkey):
    import requests
    import certifi

    url = "https://api.etherscan.io/api?module=account&action=txlist&address=" + address + \
            "&startblock=0&endblock=99999999&page=1&offset=" + str(number_transactions) + \
                "&sort=desc&apikey=" + APIkey

    response = requests.get(url, verify=certifi.where())
    # convert to json
    address_content = response.json()
    result = address_content.get("result")

    # list of addresses with whom you had contact (can be 'to' or 'from', not distinguished)
    transaction_addresses = []
    transaction_hash = []
    
    for transaction in result:

        tx_from = transaction.get("from")
        tx_to = transaction.get("to")
        hash_ID = transaction.get("hash")

        # add partner address to list
        if tx_from == address:
            if tx_to != '':
                transaction_addresses.append(tx_to)
                transaction_hash.append(hash_ID)
        else:
            if tx_from != '':
                transaction_addresses.append(tx_from)
                transaction_hash.append(hash_ID)
        
              
        if len(transaction_addresses) != len(transaction_hash):
            raise Exception("len(transaction_addresses) != len(transaction_hash)")

    return transaction_addresses, transaction_hash

    

def get_partner_address_and_transaction_hash(person):

    global partner_address_lookup_dict
    global partner_transaction_hash_lookup_dict
    global number_transactions
    global APIkey
    global num_look_up
    global num_etherscan

    if person in partner_address_lookup_dict:
        partner_addresses_list = partner_address_lookup_dict[person]
        transaction_hash_list = partner_transaction_hash_lookup_dict[person]
        num_look_up +=1
    else:
        partner_addresses_list, transaction_hash_list = get_partner_info_from_etherscan(person, number_transactions, APIkey)
        partner_address_lookup_dict[person] = partner_addresses_list
        partner_transaction_hash_lookup_dict[person] = transaction_hash_list
        num_etherscan += 1

    return partner_addresses_list, transaction_hash_list




###############################################################################
# main script
###############################################################################

import time
import json
import datetime

number_transactions = 400
# etherscan API key
APIkey = 'ZSWNNPPC5JITQPFYTC8UDFPZYT7CS6989W'
num_look_up = 0
num_etherscan = 0

t = time.time()

print()
print('------------------- START --------------------')
print()


# dictionary that contains ALL information
person_dict = {}

#these are only fund managers
person_list = []

# initialize two structs above
json_data = pullFundManager()['data']['funds']
for fund in json_data:
    name = fund['name']
    manager_ID = fund['manager']['id']
    #is_shutdown= fund['isShutdown']

    # use only active funds
    if (manager_ID not in person_list): # & (not is_shutdown):
        # for every level I save every connection between person_A (person_list)
        # and person_B as well as the path from person_A to person_B (only relevant
        # at higher levels). I also save the respective transaction_hash to check if
        # I have connections multiple times in my list.
        person_dict[manager_ID] = {
            'name': name,
            'level0' : {'num_connections':0, 'person_B_list':[], 'connection_path':[], 'transaction_hash':[]},
            'level1' : {'num_connections':0, 'person_B_list':[], 'connection_path':[], 'transaction_hash':[]},
            'level2' : {'num_connections':0, 'person_B_list':[], 'connection_path':[], 'transaction_hash':[]}
            }
        person_list.append(manager_ID)

del fund
del manager_ID
#del is_shutdown
del json_data

# function get_partner_info_from_etherscan() takes longest time (connection with www)
# save result of get_partner_info_from_etherscan in dict
partner_address_lookup_dict = {}
# list of all transactions_ID (same order as partner address)
partner_transaction_hash_lookup_dict = {}


# person a & b is level 0
# person c is level 1
# person d is level 2
# inititalize to savely delete them later
person_A_index = []
person_A = []
person_B_index = []
person_B = []
person_C_index = []
person_C = []
person_D_index = []
person_D = []
person_E_index = []
person_E = []
person_C_address_list = []
person_C_transaction_hash_list = []
person_D_address_list = []
person_D_transaction_hash_list = []
person_E_address_list = []
person_E_transaction_hash_list = []
potential_person_B_list = []
connection_path = []
transaction_hash = []




################################################################################
# loop over each fund manager and get partners on etherscan
################################################################################

# need to go through all fund manager in level 0, then 1, then 2. This is because
# it can happen, that one finds a connection in level 2 before it is found in
# level 0, and then one has both entries

for person_A_index, person_A in enumerate(person_list):
    
    print('{}/{} person addresses. Current: {}'.format(person_A_index+1, len(person_list), person_A))

    # list which person_B need to be checked
    potential_person_B_list = person_list.copy()
    # do not check for person_A itself
    potential_person_B_list.remove(person_A)
    
    
    ################################################################################
    # LEVEL 0
    ################################################################################
    print('\t+++ Level 0 +++')

    person_C_address_list, person_C_transaction_hash_list = get_partner_address_and_transaction_hash(person_A)

    for person_B_index, person_B in enumerate(potential_person_B_list):

        for person_C_index, person_C in enumerate(person_C_address_list):
                if person_B == person_C:
                    connection_path = person_C
                    transaction_hash = person_C_transaction_hash_list[person_C_index]

                    person_dict[person_A]['level0']['num_connections'] += 1
                    person_dict[person_A]['level0']['person_B_list'].append(person_C)
                    person_dict[person_A]['level0']['connection_path'].append(connection_path)
                    person_dict[person_A]['level0']['transaction_hash'].append(transaction_hash)
                    

    ################################################################################
    # LEVEL 1
    ################################################################################
    print('\t\t+++ Level 1 +++')

    for person_C_index, person_C in enumerate(person_C_address_list):

        person_D_address_list, person_D_transaction_hash_list = get_partner_address_and_transaction_hash(person_C)

        for person_B_index, person_B in enumerate(potential_person_B_list):

            for person_D_index, person_D in enumerate(person_D_address_list):
                    if person_B == person_D:
                        connection_path = (person_C, person_D)
                        transaction_hash = (person_C_transaction_hash_list[person_C_index], \
                                            person_D_transaction_hash_list[person_D_index])

                        person_dict[person_A]['level1']['num_connections'] += 1
                        person_dict[person_A]['level1']['person_B_list'].append(person_D)
                        person_dict[person_A]['level1']['connection_path'].append(connection_path)
                        person_dict[person_A]['level1']['transaction_hash'].append(transaction_hash)
                        

    ################################################################################
    # LEVEL 2
    ################################################################################
    print('\t\t\t+++ Level 2 +++')
    
    for person_C_index, person_C in enumerate(person_C_address_list):

        for person_D_index, person_D in enumerate(person_D_address_list):

            person_E_address_list, person_E_transaction_hash_list = get_partner_address_and_transaction_hash(person_D)

            for person_B_index, person_B in enumerate(potential_person_B_list):

                for person_E_index, person_E in enumerate(person_E_address_list):
                        if person_B == person_E:
                            connection_path = (person_C, person_D, person_E)
                            transaction_hash = (person_C_transaction_hash_list[person_C_index], \
                                                person_D_transaction_hash_list[person_D_index], \
                                                person_E_transaction_hash_list[person_E_index])

                            person_dict[person_A]['level2']['num_connections'] += 1
                            person_dict[person_A]['level2']['person_B_list'].append(person_E)
                            person_dict[person_A]['level2']['connection_path'].append(connection_path)
                            person_dict[person_A]['level2']['transaction_hash'].append(transaction_hash)




################################################################################
# Saving
################################################################################

elapsed = time.time() - t
currentDT = datetime.datetime.now()
 
person_dict['meta_data'] = {'Time of execution' : currentDT.strftime("%Y%m%d_%H%M%S"), 
                            'elapsed time (min)' : elapsed/60,
                            'number transactions checked' : number_transactions,
                            'number etherscan dict look ups' : num_look_up,
                            'number etherscan queries' : num_etherscan}

                            

file_name = 'data/EtherscanScraper_person_dict.json'

with open(file_name, 'w') as fp:
    json.dump(person_dict, fp,  indent=4)


del person_A_index
del person_A
del person_B_index
del person_B
del person_C_index
del person_C
del person_D_index
del person_D
del person_E_index
del person_E
del person_C_address_list
del person_C_transaction_hash_list
del person_D_address_list
del person_D_transaction_hash_list
del person_E_address_list
del person_E_transaction_hash_list
del potential_person_B_list
del connection_path
del transaction_hash
del APIkey
del currentDT, elapsed, file_name, t
del num_etherscan, num_look_up, number_transactions
del partner_address_lookup_dict, partner_transaction_hash_lookup_dict
del person_list



print()
print('------------------- DONE --------------------')