def pullAssetsPrices():
    # pullData queries the melon protocol and returns a JSON file
    
    from graphqlclient import GraphQLClient
    import json
    
    client = GraphQLClient('https://api.thegraph.com/subgraphs/name/melonproject/melon')
    
    result = client.execute('''
    {
        assets(orderBy: name, orderDirection: asc) {
      name
      priceHistory (first: 1000) {
        price
        timestamp
      }
    }      
    }
    ''')
    JSON = json.loads(result)
    
    return JSON



def pullFundCounts():
    # pullData queries the melon protocol and returns a JSON file
    
    from graphqlclient import GraphQLClient
    import json
    
    client = GraphQLClient('https://api.thegraph.com/subgraphs/name/melonproject/melon')
    
    result = client.execute('''
    {
        fundCounts(first: 1000) {
      active
      nonActive
      timestamp
    }
    }
    ''')
    JSON = json.loads(result)
    
    return JSON



def pullAuM():
    # pullData queries the melon protocol and returns a JSON file
    
    from graphqlclient import GraphQLClient
    import json
    
    client = GraphQLClient('https://api.thegraph.com/subgraphs/name/melonproject/melon')
    
    result = client.execute('''
    {
        melonNetworkHistories(first: 1000) {
      gav
      timestamp
    }
    }
    ''')
    JSON = json.loads(result)
    
    return JSON



def pullExchangesData():
    # pullData queries the melon protocol and returns a JSON file
    
    from graphqlclient import GraphQLClient
    import json
    
    client = GraphQLClient('https://api.thegraph.com/subgraphs/name/melonproject/melon')
    
    result = client.execute('''
    {
       exchangeAdapters {
      createdAt
      exchange {
        name
      }
      takesCustody
      removedFromRegistry
      removedFromRegistryAt
    }
    }
    ''')
    JSON = json.loads(result)
    
    return JSON



def pullFundsData():
    # pullData queries the melon protocol and returns a JSON file
    
    from graphqlclient import GraphQLClient
    import json
    
    client = GraphQLClient('https://api.thegraph.com/subgraphs/name/melonproject/melon')
    
    result = client.execute('''
    {
       funds(first: 300, orderBy: name, orderDirection: asc) {
            name
            id
            sharePrice
            allocatedFees
            createdAt
            currentDailySharePrice
            feesInDenominationAsset
            feesInShares
            gav
            gavPerShareNetManagementFee
            isShutdown
            lastCalculationsUpdate
            nav
            previousDailySharePrice
            shutdownAt
            totalSupply
            validPrice
            version {
                id
                name
            }
            vault {
            id
            }
            trading {
            id
          }
          slug {
            id
          }
          share {
            id
          }
          registry {
            id
          }
          priceSource {
            id
          }
          policyManager {
            id
          }
          participation {
            id
          }
          manager {
            id
          }
          accounting {
            id
          }
          feeManager {
            id
            managementFee {
              managementFeeRate
            }
            performanceFee {
              performanceFeeRate
              performanceFeePeriod
            }
          }
          
          }
    }
    ''')
    JSON = json.loads(result)
    
    return JSON



def pullTradesData():    
    from graphqlclient import GraphQLClient
    import json
    
    client = GraphQLClient('https://api.thegraph.com/subgraphs/name/melonproject/melon')
    
    result = client.execute('''
    { 
          trades(where: {methodName_not: "cancelOrder"}, first:1000) {
          id
          amountBought
          amountSold
          assetBought {
            name
          }
          assetSold {
            name
          }
          exchange {
            name
          }
          timestamp
          methodName
          gasPrice
          gasUsed
          trading {
            fund {
              id
              }
            }
        }
      }
      
    ''')
    JSON = json.loads(result)
    
    return JSON



def pullInvestmentsData():    
    from graphqlclient import GraphQLClient
    import json
    
    client = GraphQLClient('https://api.thegraph.com/subgraphs/name/melonproject/melon')
    
    result = client.execute('''
    { 
        funds(first: 300, orderBy: name, orderDirection: asc) {
          investments {
            history(first: 1000, where: {action_not_contains: "Redemption"}) {
              action
              amount
              timestamp
              sharePrice
              shares
              id
              asset {
                name
              }
            }
          }
          name
          id
        }     
    }
    ''')
    JSON = json.loads(result)
    
    return JSON



def pullHoldingsData():    
    from graphqlclient import GraphQLClient
    import json
    
    client = GraphQLClient('https://api.thegraph.com/subgraphs/name/melonproject/melon')
    
    result = client.execute('''
    {       
        funds(first: 300, orderBy: name, orderDirection: asc) {
          name
          id
          holdings {
            amount
            asset {
              name
            }
          }
        }
    }
    ''')
    JSON = json.loads(result)
    
    return JSON



def pullInvestorsData():    
    from graphqlclient import GraphQLClient
    import json
    
    client = GraphQLClient('https://api.thegraph.com/subgraphs/name/melonproject/melon')
    
    result = client.execute('''
    {       
        investors (first:1000) {
            id
            investmentHistory {
                id
                }
            }
        
    }
    ''')
    JSON = json.loads(result)
    
    return JSON



def pullAssetMasterData():
    from graphqlclient import GraphQLClient
    import json
    
    client = GraphQLClient('https://api.thegraph.com/subgraphs/name/melonproject/melon')
    
    result = client.execute('''
    {       
        assets {
          url
          symbol
          reserveMin
          removedFromRegistryAt
          removedFromRegistry
          name
          lastPriceValid
          lastPriceUpdate
          lastPrice
          id
          decimals
          createdAt
        }
        
    }
    ''')
    JSON = json.loads(result)
    
    return JSON




###############################################################################
#  CoinGecko
###############################################################################

import time
import datetime

from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()


result = cg.get_coin_market_chart_range_by_id(id='ethereum', vs_currency='usd', from_timestamp=1550942960, to_timestamp=time.time())



###############################################################################
#  Main script
###############################################################################

import pandas as pd
import numpy as np
from collections import Counter
import json

bSave = True



##############################################################################
# Load default plotting values
##############################################################################

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import rc
import json

file_name = 'PlotStyle_20200525.json'

with open(file_name) as json_file:
    plot_style = json.load(json_file)
    
for style in plot_style:
    mpl.rcParams[style] = plot_style[style]
    
# plt.rcParams["font.family"] = 'CMU Serif'
rc('font', **{'family': 'serif', 'serif': ['Computer Modern'], 'size':12.0})
# rc('font.size' : 12.0)
rc('text', usetex=True)

plt.close('all')



###############################################################################
#  Create AuM dataframe
###############################################################################

data_dict = pullAuM()
AuM_dict = data_dict['data']['melonNetworkHistories']

# integreate into a dataframe
df_AuM = pd.DataFrame(
    index = [entry['timestamp'] for entry in AuM_dict],
    data = {
    'date':                     [entry['timestamp'] for entry in AuM_dict],       
    'AuM':                     [entry['gav'] for entry in AuM_dict],
    

    }).rename_axis('Timestamp')

del data_dict
del AuM_dict



###############################################################################
#  Create exchanges dataframe
###############################################################################

data_dict = pullExchangesData()
exchanges_dict = data_dict['data']['exchangeAdapters']

# integreate into a dataframe
df_exchanges = pd.DataFrame(
    index = [entry['exchange']['name'] for entry in exchanges_dict],
    data = {
    'Name':                     [entry['exchange']['name'] for entry in exchanges_dict],
    'takesCustody':             [entry['takesCustody'] for entry in exchanges_dict],
    'removedFromRegistry':      [entry['removedFromRegistry'] for entry in exchanges_dict],
    'removedFromRegistryAt':    [entry['removedFromRegistryAt'] for entry in exchanges_dict],
    'createdAt':                [entry['createdAt'] for entry in exchanges_dict],
    }).rename_axis('ExchangeName')

del data_dict
del exchanges_dict



###############################################################################
#  Create asset dataframe
###############################################################################

data_dict = pullAssetMasterData()
assets_dict = data_dict['data']['assets']

# integreate into a dataframe
df_assets = pd.DataFrame(
    index = [entry['name'] for entry in assets_dict],
    data = {
    'assetID':                       [entry['id'] for entry in assets_dict],
    'url':                      [entry['url'] for entry in assets_dict],
    'symbol':                   [entry['symbol'] for entry in assets_dict],
    'reserveMin':               [entry['reserveMin'] for entry in assets_dict],
    'removedFromRegistryAt':    [entry['removedFromRegistryAt'] for entry in assets_dict],
    'removedFromRegistry':      [entry['removedFromRegistry'] for entry in assets_dict],
    'lastPriceValid':           [entry['lastPriceValid'] for entry in assets_dict],
    'lastPriceUpdate':          [entry['lastPriceUpdate'] for entry in assets_dict],
    'lastPrice':                [int(entry['lastPrice']) for entry in assets_dict],
    'decimals':                 [entry['decimals'] for entry in assets_dict],
    'createdAt':                [entry['createdAt'] for entry in assets_dict],
    }).rename_axis('AssetName')

del data_dict
del assets_dict



###############################################################################
#  Create fundcount dataframe
###############################################################################

data_dict = pullFundCounts()
counts_dict = data_dict['data']['fundCounts']

# integreate into a dataframe
df_counts = pd.DataFrame(
    index = [entry['timestamp'] for entry in counts_dict],
    data = {
    'date':                       [entry['timestamp'] for entry in counts_dict],
    'active':                       [entry['active'] for entry in counts_dict],
    'nonActive':                    [entry['nonActive'] for entry in counts_dict],
    }).rename_axis('Timestamp')

del data_dict
del counts_dict



###############################################################################
#  Create fund dataframe
###############################################################################

data_dict = pullFundsData()
funds_dict = data_dict['data']['funds']

# integreate into a dataframe
df_funds = pd.DataFrame(
    index = [entry['name'] for entry in funds_dict],
    data = {
    'fundID':                       [entry['id'] for entry in funds_dict],
    'sharePrice':               [entry['sharePrice'] for entry in funds_dict],
    'allocatedFees':            [entry['allocatedFees'] for entry in funds_dict],
    'createdAt':                [entry['createdAt'] for entry in funds_dict],
    'currentDailySharePrice':   [entry['currentDailySharePrice'] for entry in funds_dict],
    'feesInDenominationAsset':  [entry['feesInDenominationAsset'] for entry in funds_dict],
    'feesInShares':             [entry['feesInShares'] for entry in funds_dict],
    'gav':                      [entry['gav'] for entry in funds_dict],
    'gavPerShareNetManagementFee':[entry['gavPerShareNetManagementFee'] for entry in funds_dict],
    'isShutdown':               [entry['isShutdown'] for entry in funds_dict],
    'lastCalculationsUpdate':   [entry['lastCalculationsUpdate'] for entry in funds_dict],
    'nav':                      [entry['nav'] for entry in funds_dict],
    'previousDailySharePrice':  [entry['previousDailySharePrice'] for entry in funds_dict],
    'shutdownAt':               [entry['shutdownAt'] for entry in funds_dict],
    'totalSupply':              [entry['totalSupply'] for entry in funds_dict],
    'validPrice':               [entry['validPrice'] for entry in funds_dict],
    'version_name':             [entry['version']['name'] for entry in funds_dict],
    'version_id':               [entry['version']['id'] for entry in funds_dict],
    'vault':                    [entry['vault']['id'] for entry in funds_dict],
    'trading':                  [entry['trading']['id'] for entry in funds_dict],
    'slug':                     [entry['slug']['id'] for entry in funds_dict],
    'share':                    [entry['share']['id'] for entry in funds_dict],
    'registry':                 [entry['registry']['id'] for entry in funds_dict],
    'priceSource':              [entry['priceSource']['id'] for entry in funds_dict],
    'policyManager':            [entry['policyManager']['id'] for entry in funds_dict],
    'participation':            [entry['participation']['id'] for entry in funds_dict],
    'manager':                  [entry['manager']['id'] for entry in funds_dict],
    'accounting':               [entry['accounting']['id'] for entry in funds_dict],
    'feeManager':               [entry['feeManager']['id'] for entry in funds_dict],
    'managementFee':            [(int(entry['feeManager']['managementFee']['managementFeeRate'])/10**18) for entry in funds_dict],
    'performanceFee':           [(int(entry['feeManager']['performanceFee']['performanceFeeRate'])/10**18) for entry in funds_dict],
    'performanceFeePeriod':     [entry['feeManager']['performanceFee']['performanceFeePeriod'] for entry in funds_dict]
    }).rename_axis('FundName')

del data_dict
del funds_dict



###############################################################################
#  Create trades dataframe
###############################################################################

data_dict = pullTradesData()
trades_dict = data_dict['data']['trades']

# integreate into a dataframe
df_trades = pd.DataFrame(
    index = [entry['trading']['fund']['id'] for entry in trades_dict],
    data = {
    'fundId':               [entry['trading']['fund']['id'] for entry in trades_dict],    
    'amountBought':         [int(entry['amountBought']) for entry in trades_dict],
    'amountSold':           [int(entry['amountSold']) for entry in trades_dict],
    'assetBought':          [entry['assetBought']['name'] for entry in trades_dict],
    'assetSold':            [entry['assetSold']['name'] for entry in trades_dict],
    'exchange':             [entry['exchange']['name'] for entry in trades_dict],
    'timestamp':            [entry['timestamp'] for entry in trades_dict],
    'method':               [entry['methodName'] for entry in trades_dict],
    'gasPrice':             [entry['gasPrice'] for entry in trades_dict],
    'gasUsed':              [entry['gasUsed'] for entry in trades_dict],
    'transactionID':        [entry['id'] for entry in trades_dict],
 }).rename_axis('executingFundID')

del data_dict
del trades_dict



###############################################################################
#  Create investments dataframe
###############################################################################

data_dict = pullInvestmentsData()
invest_dict = data_dict['data']['funds']
del data_dict

index_array = []
data_dict = {
    'fundID':[],
    'action':[],
    'amount':[],
    'timestamp':[],
    'sharePrice':[],
    'shares':[],
    'assetName':[],
    'investID':[],
    }

for invest_entry in invest_dict:
    FundName = invest_entry['name']
    FundID = invest_entry['id']
    Accounting = invest_entry['investments']
   # Test = Accounting['history']['action']
    
    for asset in Accounting:
        
        ownedAsset = asset['history']
        
        for entry in ownedAsset:
            index_array += [FundName]
            data_dict['fundID']     += [FundID]
            data_dict['action']     += [entry['action']]
            data_dict['amount']     += [int(entry['amount'])]
            data_dict['timestamp']  += [entry['timestamp']]
            data_dict['sharePrice'] += [entry['sharePrice']]
            data_dict['shares']     += [entry['shares']]
            data_dict['assetName']  += [entry['asset']['name']]
            data_dict['investID']   += [entry['id']]
    

# integreate into a dataframe
df_invest = pd.DataFrame(
    index = index_array,
    data = data_dict
    ).rename_axis('FundName')

del invest_dict
del index_array
del data_dict
del FundName
del FundID
del Accounting
del ownedAsset
del entry
del asset
del invest_entry



###############################################################################
#  Create Asset prices dataframe
###############################################################################    

data_dict = pullAssetsPrices()
token_dict = data_dict['data']['assets']
del data_dict

token_dataframe_dict = {}
for index, token in enumerate(token_dict):
    asset_name = token['name']
    price_history = token['priceHistory']
    price_list = []
    time_list = []
    for price_dict in price_history:
        price_list.append(np.float64(price_dict['price']))
        time_list.append(pd.to_datetime(price_dict['timestamp'], unit='s'))
    
    df_temp = pd.DataFrame({asset_name: price_list}, index=time_list) 
    token_dataframe_dict[index] = df_temp
    
df_prices = token_dataframe_dict[0]
for index in range(1,len(token_dataframe_dict.keys())):
    df_prices = pd.merge(df_prices, token_dataframe_dict[index], how='outer', left_index=True, right_index=True)

# remove 0 values by nan
df_prices.where(df_prices>0, inplace=True)
    
del token_dataframe_dict, token_dict
del index, token
del asset_name, price_history, price_list, time_list
del price_dict
del df_temp

    

###############################################################################
#  Create holdings dataframe
###############################################################################

data_dict = pullHoldingsData()
holdings_dict = data_dict['data']['funds']
del data_dict

index_array = []
data_dict = {
    'fundID':[],
    'ownedAsset':[],
    'ownedAmount':[],
    }

for holdings_entry in holdings_dict:
    FundName = holdings_entry['name']
    FundID = holdings_entry['id']
    holdings = holdings_entry['holdings']
   # Test = Accounting['history']['action']
    
    for hold in holdings:        
        index_array += [FundName]
        data_dict['fundID']     += [FundID]
        data_dict['ownedAsset'] += [hold['asset']['name']]
        data_dict['ownedAmount']+= [int(hold['amount'])]
        
# integreate into a dataframe
df_holdings = pd.DataFrame(
    index = index_array,
    data = data_dict
    ).rename_axis('FundName')

del data_dict
del index_array
del holdings_dict
del holdings_entry
del holdings
del hold
del FundName
del FundID



###############################################################################
#  Create investors dataframe
###############################################################################

data_dict = pullInvestorsData()
investor_dict = data_dict['data']['investors']
del data_dict

index_array = []
data_dict = {
    'investorID':[]
    }

for investor_entry in investor_dict:
    InvestorID = investor_entry['id']
    
    InvestID = investor_entry['investmentHistory']
   # Test = Accounting['history']['action']
    
    for invest in InvestID:
        
        index_array += [invest['id']]     
        data_dict['investorID']   += [InvestorID]
        
# integreate into a dataframe
df_investor = pd.DataFrame(
    index = index_array,
    data = data_dict
    ).rename_axis('InvestID')

del investor_dict
del index_array
del data_dict
del InvestorID
del InvestID
del invest
del investor_entry



###############################################################################
#  Create USD Prices dataframe
###############################################################################

#data_dict = pullExchangesData()
USDprices_dict = result['prices']

# integreate into a dataframe
time_stamp_list = []
dollar_list = []
for entry in USDprices_dict:
    time_stamp = pd.to_datetime(entry[0], unit='ms')
    price = np.float64(entry[1])
    if time_stamp not in time_stamp_list:
        time_stamp_list.append(time_stamp)
        dollar_list.append(price)
        
del entry, time_stamp, price
        
df_USD = pd.DataFrame(
    index = time_stamp_list,
    data = {  
    'Price':  dollar_list                   ,  
    }).rename_axis('Timestamp')


#del data_dict
del USDprices_dict, time_stamp_list, dollar_list



###############################################################################
#  Conversions
###############################################################################

# convert unix epoch times to timestamp
df_funds['createdAt'] = pd.to_datetime(df_funds['createdAt'], unit='s')
df_funds['shutdownAt'] = pd.to_datetime(df_funds['shutdownAt'], unit='s')
df_funds['lastCalculationsUpdate'] = pd.to_datetime(df_funds['lastCalculationsUpdate'], unit='s')

df_trades['timestamp'] = pd.to_datetime(df_trades['timestamp'], unit='s')

df_invest['timestamp'] = pd.to_datetime(df_invest['timestamp'], unit='s')
df_invest['timestampInvOnly'] = pd.to_datetime(df_invest['timestamp'], unit='s')


df_counts['date'] = pd.to_datetime(df_counts['date'], unit='s')
df_AuM['date'] = pd.to_datetime(df_AuM['date'], unit='s')

df_exchanges['createdAt'] = pd.to_datetime(df_exchanges['createdAt'], unit='s')
df_exchanges['removedFromRegistryAt'] = pd.to_datetime(df_exchanges['removedFromRegistryAt'], unit='s')

df_assets['createdAt'] = pd.to_datetime(df_assets['createdAt'], unit='s')

df_assets['removedFromRegistryAt'] = pd.to_datetime(df_assets['removedFromRegistryAt'], unit='s')





###############################################################################
#  Add columns
###############################################################################

#df create FM list
fundManagerList = list(dict.fromkeys(df_funds['manager'].tolist()))
fundManager_dict = {'Unique':fundManagerList}
df_fundManagerID = pd.DataFrame(fundManager_dict)
df_fundManagerID['Index'] = df_fundManagerID.index

# add managerID to df_funds
df_funds['ID'] = [df_fundManagerID.loc[df_fundManagerID['Unique'] == id, 'Index'].iloc[0] for id in df_funds['manager']]

del fundManager_dict


# after how many days it was shut down
df_funds['shutDownAfter'] = df_funds['shutdownAt'] - df_funds['createdAt']

# age of funds
df_funds['age'] = pd.Timestamp.now() - df_funds['createdAt']
# replace the value of the closed values by NaT
df_funds['age'] = df_funds.where(df_funds['isShutdown']==False, pd.NaT)['age']



# performanceFeePeriod in Days
df_funds['performanceFeePeriod'] = pd.to_timedelta('{}s'.format(entry) for entry in df_funds['performanceFeePeriod'])
df_funds['PerformanceFeePeriod'] = df_funds['performanceFeePeriod'].values.astype(np.int64)*1/1e9/3600/24

# how often is the 'fundID' of this fund involved in a trade
OccurencesOfTrades = Counter(df_trades.index)
df_funds['numTradesOnAllExchanges'] = [OccurencesOfTrades[id] for id in df_funds['fundID']]
del OccurencesOfTrades



# how often is the 'fundID' of this fund involved in a investment
df_invest['occurence'] = np.where(df_invest['action']=='Investment', 1, 0)
invest_pivot = pd.pivot_table(df_invest, values='occurence', index='fundID', aggfunc = np.sum)
df_funds['numInvestments'] = [invest_pivot.loc[id]['occurence'] if id in invest_pivot.index else 0 for id in df_funds['fundID']]
del invest_pivot

# how many assets does 'fundID' have
df_holdings['occurence'] = np.where(df_holdings['ownedAmount']!=0, 1, 0)
holdings_pivot = pd.pivot_table(df_holdings, values='occurence', index='fundID', aggfunc = np.sum)
df_funds['numAssets'] = [holdings_pivot.loc[id]['occurence'] if id in holdings_pivot.index else 0 for id in df_funds['fundID']]
del holdings_pivot



# add investorID to df_invest
df_invest['investorID'] = [df_investor.loc[id]['investorID'] for id in df_invest['investID']]

# add managerID to df_invest
df_invest['managerID'] = [df_funds.loc[df_funds['fundID'] == id, 'manager'].iloc[0] for id in df_invest['fundID']]

# is the investor the 'manager' of this fund and add this to fundList
df_invest['managerBool'] = np.where(df_invest['investorID']==df_invest['managerID'], 0, 1)
investor_pivot = pd.pivot_table(df_invest, values='managerBool', index='fundID', aggfunc = np.sum)
df_funds['numExternalInvestments'] = [investor_pivot.loc[id]['managerBool'] if id in investor_pivot.index else 0 for id in df_funds['fundID']]
del investor_pivot

#add price without decimals
df_assets['priceWithoutDecimals'] = df_assets['lastPrice'] / 10**18 # this is not needed: (10**df_assets['decimals']) 

# add eth value of holdings to df_holdings
df_holdings['valueInEth'] = ([df_assets.loc[id]['priceWithoutDecimals'] for id in df_holdings['ownedAsset']]) * (df_holdings['ownedAmount']) / ([10**df_assets.loc[id]['decimals'] for id in df_holdings['ownedAsset']])


# cluster exchange versions
df_exchanges['exchangeCluster'] = np.where(df_exchanges['Name']=='Oasisdex', df_exchanges['Name'], np.where(df_exchanges['Name']=='Uniswap', df_exchanges['Name'], np.where(df_exchanges['Name']=='Kyber Network', df_exchanges['Name'], np.where(df_exchanges['Name']=='Ethfinex', df_exchanges['Name'],np.where(df_exchanges['Name']=='Melon Engine (v1)', 'Melon Engine', np.where(df_exchanges['Name']=='Melon Engine (v2)', 'Melon Engine',np.where(df_exchanges['Name']=='0x (v3)', '0x',np.where(df_exchanges['Name']=='0x (v2.0)', '0x',np.where(df_exchanges['Name']=='0x (v2.1)', '0x',0)))))))))
df_trades['exchangeCluster'] = np.where(df_trades['exchange']=='Oasisdex', df_trades['exchange'], np.where(df_trades['exchange']=='Uniswap', df_trades['exchange'], np.where(df_trades['exchange']=='Kyber Network', df_trades['exchange'], np.where(df_trades['exchange']=='Ethfinex', df_trades['exchange'],np.where(df_trades['exchange']=='Melon Engine (v1)', 'Melon Engine', np.where(df_trades['exchange']=='Melon Engine (v2)', 'Melon Engine',np.where(df_trades['exchange']=='0x (v3)', '0x',np.where(df_trades['exchange']=='0x (v2.0)', '0x',np.where(df_trades['exchange']=='0x (v2.1)', '0x',0)))))))))

# add amount without Decimals of investments to df_invest
df_invest['amountWithoutDecimals'] = (df_invest['amount']) / ([10**df_assets.loc[id]['decimals'] for id in df_invest['assetName']])

# add amount without Decimals of trades to df_trades
df_trades['amountBoughtWithoutDecimals'] = (df_trades['amountBought']) / ([10**df_assets.loc[id]['decimals'] for id in df_trades['assetBought']])
df_trades['amountSoldWithoutDecimals'] = (df_trades['amountSold']) / ([10**df_assets.loc[id]['decimals'] for id in df_trades['assetSold']])

# what is the value of the assets of 'fundID'
holdings_pivot = pd.pivot_table(df_holdings, values='valueInEth', index='fundID', aggfunc = np.sum)
df_funds['valueAssets'] = [holdings_pivot.loc[id]['valueInEth'] if id in holdings_pivot.index else 0 for id in df_funds['fundID']]
del holdings_pivot

# when was the last investment
df_invest['timestampInvOnly'] = np.where(df_invest['action']=='Investment', df_invest['timestampInvOnly'] , pd.NaT)
df_invest['timestampInvOnly'] = pd.to_datetime(df_invest['timestampInvOnly'], unit='ns')
invest_pivot = pd.pivot_table(df_invest, values='timestampInvOnly', index='fundID', aggfunc = np.max)
df_funds['lastInvestment'] = [invest_pivot.loc[id]['timestampInvOnly'] if id in invest_pivot.index else pd.NaT for id in df_funds['fundID']]
del invest_pivot





trade_pivot = pd.pivot_table(df_trades, values='timestamp', index='fundId', aggfunc = np.max)
df_funds['lastTrade'] = [trade_pivot.loc[id]['timestamp'] if id in trade_pivot.index else pd.NaT for id in df_funds['fundID']]
del trade_pivot

df_funds['lastAction'] = np.where(df_funds['lastTrade']>=df_funds['lastInvestment'],df_funds['lastTrade'],df_funds['lastInvestment'])


# not acted since
df_funds['notActedSince'] = pd.Timestamp.now() - df_funds['lastAction']
# replace the value of the closed values by not acted since
df_funds['notActedSince'] = np.where(df_funds['isShutdown']==False, df_funds['notActedSince'], df_funds['shutdownAt'] - df_funds['lastAction'])

# not traded since
df_funds['notTradedSince'] = pd.Timestamp.now() - df_funds['lastTrade']
# replace the value of the closed values by not acted since
df_funds['notTradedSince'] = np.where(df_funds['isShutdown']==False, df_funds['notTradedSince'], df_funds['shutdownAt'] - df_funds['lastTrade'])




# add exchange rate at a given timestamp to df_invest
# exchange rates are stored in df_prices
timestamp_list = df_invest['timestamp']
asset_list = df_invest['assetName']
conversion_list = []
for index, asset in enumerate(asset_list):
    time_stamp = timestamp_list[index]
    # find closest timestamp in df_prices
    use_index = df_prices.index.get_loc(time_stamp, method='nearest')
    time_delta = time_stamp - df_prices.index[use_index]
    if time_delta>datetime.timedelta(seconds=1):
        # use_index points to a time before time_stamp.
        # This is what I want. Next I check that the price for this time is not
        # a Nan. There I will reduce the index. Since the use_index points already to
        # a time before, I increase it now by 1, so I get the same use_index in 
        # the while loop
        use_index += 1
    # use previous index until I have no NaN
    while True:
        # use one index before
        use_index -= 1
        asset_price = df_prices[asset].iloc[use_index]
        if not np.isnan(asset_price):
            break
    conversion_list.append(asset_price/10**18)
# add conversion from asset into 
df_invest['conversionPrice'] = conversion_list
df_invest['valueInETH'] = conversion_list*df_invest['amountWithoutDecimals']

del timestamp_list, asset_list, conversion_list
del index, asset, time_stamp, use_index, time_delta
del asset_price

# add exchange rate at a given timestamp to df_trades
# exchange rates are stored in df_prices
timestamp_list = df_trades['timestamp']
asset_list = df_trades['assetBought']
conversion_list = []
for index, asset in enumerate(asset_list):
    time_stamp = timestamp_list[index]
    # find closest timestamp in df_prices
    use_index = df_prices.index.get_loc(time_stamp, method='nearest')
    time_delta = time_stamp - df_prices.index[use_index]
    if time_delta>datetime.timedelta(seconds=1):        
        use_index += 1
    # use previous index until I have no NaN
    while True:
        # use one index before
        use_index -= 1
        asset_price = df_prices[asset].iloc[use_index]
        if not np.isnan(asset_price):
            break
    conversion_list.append(asset_price/10**18)
# add conversion from asset into 
df_trades['conversionPriceAssetBought'] = conversion_list
df_trades['valueInEthBought'] = conversion_list*df_trades['amountBoughtWithoutDecimals']

del timestamp_list, asset_list, conversion_list
del index, asset, time_stamp, use_index, time_delta
del asset_price

# add exchange rate at a given timestamp to df_trades
# exchange rates are stored in df_prices
timestamp_list = df_trades['timestamp']
asset_list = df_trades['assetSold']
conversion_list = []
for index, asset in enumerate(asset_list):
    time_stamp = timestamp_list[index]
    # find closest timestamp in df_prices
    use_index = df_prices.index.get_loc(time_stamp, method='nearest')
    time_delta = time_stamp - df_prices.index[use_index]
    if time_delta>datetime.timedelta(seconds=1):
       use_index += 1
    # use previous index until I have no NaN
    while True:
        # use one index before
        use_index -= 1
        asset_price = df_prices[asset].iloc[use_index]
        if not np.isnan(asset_price):
            break
    conversion_list.append(asset_price/10**18)
df_trades['conversionPriceAssetSold'] = conversion_list
df_trades['valueInEthSold'] = conversion_list*df_trades['amountSoldWithoutDecimals']

del timestamp_list, asset_list, conversion_list
del index, asset, time_stamp, use_index, time_delta
del asset_price



# add USD prices to df_prices
conversion_list = []
for index, time_stamp in enumerate(df_prices.index):
    # find closest timestamp in df_prices
    use_index = df_USD.index.get_loc(time_stamp, method='nearest')
    # use previous index until I have no NaN
    asset_price = df_USD['Price'].iloc[use_index]
    conversion_list.append(asset_price)
# add conversion from asset into ???
df_prices['EthUsd'] = conversion_list


del result
del conversion_list
del index, time_stamp, use_index
del asset_price



###############################################################################
#  Create Korrelation & performancedataframe
###############################################################################

df_pricesInUsd = df_prices.copy()
df_pricesInUsd['Ether'] = 1
df_pricesInUsd = df_pricesInUsd[df_pricesInUsd.columns.difference(['EthUsd'])].multiply(df_pricesInUsd['EthUsd'], axis='index')

df_pricesInUsd1 = df_pricesInUsd.drop(columns=['0x Protocol Token', 'Augur Reputation Token', 'Basic Attention Token', 'Digix Gold Token', 'Enigma Token', 'Kyber Network', 'Maker Token', 'Melon Token', 'OmiseGo', 'Sai Stable Coin', 'Tether USD', 'USD Coin', 'Wrapped BTC', 'Wrapped Ether'])
df_pricesInUsd1 = df_pricesInUsd1.dropna()

df_pricesInUsd2 = df_pricesInUsd.drop(columns=['Aragon Network Token', 'ChainLink', 'Decentraland', 'Digix Gold Token', 'Enigma Token', 'iExec Token', 'Multi-Collateral Dai', 'OmiseGo', 'Republic Project', 'Tether USD', 'Wrapped Ether'])
df_pricesInUsd2 = df_pricesInUsd2.dropna()

df_correlation3 = df_prices.copy()
#df_correlation3 = df_correlation3.dropna()
df_correlation3['Ether'] = 1
df_correlation3 = df_correlation3[df_correlation3.columns.difference(['EthUsd'])].multiply(df_correlation3['EthUsd'], axis='index')

#df_correlation = df_prices.copy()
df_correlation1 = df_prices.drop(columns=['0x Protocol Token', 'Augur Reputation Token', 'Basic Attention Token', 'Digix Gold Token', 'Enigma Token', 'Kyber Network', 'Maker Token', 'Melon Token', 'OmiseGo', 'Sai Stable Coin', 'Tether USD', 'USD Coin', 'Wrapped BTC', 'Wrapped Ether'])
df_correlation1 = df_correlation1.dropna()
df_correlation1['Ether'] = 1
df_correlation1 = df_correlation1[df_correlation1.columns.difference(['EthUsd'])].multiply(df_correlation1['EthUsd'], axis='index')


df_performance1 = df_correlation1.iloc[[0, -1]]
df_performance1 = df_performance1.transpose()
df_performance1['% performance'] = (df_performance1[df_performance1.columns[1]]-df_performance1[df_performance1.columns[0]])/df_performance1[df_performance1.columns[0]]*100

df_correlation2 = df_prices.drop(columns=['Aragon Network Token', 'ChainLink', 'Decentraland', 'Digix Gold Token', 'Enigma Token', 'iExec Token', 'Multi-Collateral Dai', 'OmiseGo', 'Republic Project', 'Tether USD', 'Wrapped Ether'])
df_correlation2 = df_correlation2.dropna()
df_correlation2['Ether'] = 1
df_correlation2 = df_correlation2[df_correlation2.columns.difference(['EthUsd'])].multiply(df_correlation2['EthUsd'], axis='index')

df_performance2 = df_correlation2.iloc[[0, -1]]
df_performance2 = df_performance2.transpose()
df_performance2['% performance'] = (df_performance2[df_performance2.columns[1]]-df_performance2[df_performance2.columns[0]])/df_performance2[df_performance2.columns[0]]*100



corrMatrix1 = df_correlation1.corr()
corrMatrix1 = corrMatrix1.round(1)
corrMatrix2 = df_correlation2.corr()
corrMatrix2 = corrMatrix2.round(1)
corrMatrix3 = df_correlation3.corr()
corrMatrix3 = corrMatrix3.round(1)



###############################################################################
# Add cluster info to df_funds from JSON 3
###############################################################################

# add clustering. This file was produced by Etherscan/EtherscanAnalyzer.py
#file_name = 'Etherscan/EtherscanScraper_20200517_052824_650network_name_dict.json'
# column 'cluserIndex': index of the cluster
# column 'clusterSize': number of manager in respective cluster
# file_name = 'Etherscan/EtherscanScraper_20200517_052824_650network_dict.json'
file_name = 'data/EtherscanAnalyzer_network_dict.json'
with open(file_name) as json_file:
    network_dict = json.load(json_file)
del network_dict['meta_data']    
    
fund_manager_list = df_funds['manager'].to_list()
cluster_list = [np.nan]*len(df_funds.index)

# level 0 clustering
level0_cluster = network_dict['level0']
for cluster_name, cluster in level0_cluster.items():
    # only use cluster with more than 1 address
    cluster_size = len(cluster)
    if len(cluster)>1:
        cluster_index = int(cluster_name)
        for address in cluster:
            fund_indices = [i for i, x in enumerate(fund_manager_list) if x == address]
            for index in fund_indices:
                cluster_list[index] = cluster_index
df_funds['L0_clusterIndex'] = cluster_list
cluster_size_list = [0]*len(df_funds.index)
for index, cluster_index in enumerate(cluster_list):
    cluster_size = np.sum([1 for x in cluster_list if x == cluster_index])
    cluster_size_list[index] = cluster_size
df_funds['L0_clusterSize'] = cluster_size_list

#check for clusters where fund managers have 2
#level 1 level 0 merge!!!

# level 1 clustering
level1_cluster = network_dict['level1']
for cluster_name, cluster in level1_cluster.items():
    # only use cluster with more than 1 address
    cluster_size = len(cluster)
    if len(cluster)>1:
        cluster_index = int(cluster_name)
        for address in cluster:
            fund_indices = [i for i, x in enumerate(fund_manager_list) if x == address]
            for index in fund_indices:
                cluster_list[index] = cluster_index
df_funds['L1_clusterIndex'] = cluster_list
cluster_size_list = [0]*len(df_funds.index)
for index, cluster_index in enumerate(cluster_list):
    cluster_size = np.sum([1 for x in cluster_list if x == cluster_index])
    cluster_size_list[index] = cluster_size
df_funds['L1_clusterSize'] = cluster_size_list

# level 2 clustering
level2_cluster = network_dict['level2']
for cluster_name, cluster in level2_cluster.items():
    # only use cluster with more than 1 address
    cluster_size = len(cluster)
    if len(cluster)>1:
        cluster_index = int(cluster_name)
        for address in cluster:
            fund_indices = [i for i, x in enumerate(fund_manager_list) if x == address]
            for index in fund_indices:
                cluster_list[index] = cluster_index
df_funds['L2_clusterIndex'] = cluster_list
cluster_size_list = [0]*len(df_funds.index)
for index, cluster_index in enumerate(cluster_list):
    cluster_size = np.sum([1 for x in cluster_list if x == cluster_index])
    cluster_size_list[index] = cluster_size
df_funds['L2_clusterSize'] = cluster_size_list

del network_dict
del file_name
del fund_manager_list
del cluster_list
del cluster_name, cluster, cluster_index
del level0_cluster, level1_cluster, level2_cluster
del cluster_size, cluster_size_list
del address
del index
del fund_indices



###############################################################################
#  df_fund_metrix
###############################################################################

columns_to_use_name = ['numTradesOnAllExchanges','numInvestments', 'numAssets', 'numExternalInvestments', 'valueAssets', 'managementFee', 'performanceFee', 'PerformanceFeePeriod']
index_list = ['avg', 'min', 'max', 'avg per active fund', 'avg. per non active fund',	'avg. per active funded fund', 'avg. per nonactive funded fund', \
                    'w avg', 'w avg per active fund', 'w avg. per non active fund',	'w avg. per active funded fund', 'w avg. per nonactive funded fund']
fund_metrix_dict = {}
for col in columns_to_use_name:
    fund_metrix_dict[col] = []
    # average
    fund_metrix_dict[col].append(np.average(df_funds[col]))
    # min
    fund_metrix_dict[col].append(np.min(df_funds[col]))
    # max
    fund_metrix_dict[col].append(np.max(df_funds[col]))
    # avg per active fund
    fund_metrix_dict[col].append(np.average(df_funds[df_funds['isShutdown']==False][col]))
    # avg. per non active fund
    fund_metrix_dict[col].append(np.average(df_funds[df_funds['isShutdown']==True][col]))
    # avg. per active funded fund, (i.e. valueAssets unequal zero)
    fund_metrix_dict[col].append(np.average(df_funds[(df_funds['valueAssets']>0) & (df_funds['isShutdown']==False)][col]))
    # avg. per nonactive funded fund, (i.e. valueAssets equal zero)
    fund_metrix_dict[col].append(np.average(df_funds[(df_funds['valueAssets']>0) & (df_funds['isShutdown']==True)][col]))  
    # weighted by value assets
    weight_array = df_funds['valueAssets'] 
    # weighted avg
    fund_metrix_dict[col].append(np.average(df_funds[col], weights=weight_array))
    # weighted avg per active fund
    fund_metrix_dict[col].append(np.average(df_funds[df_funds['isShutdown']==False][col], weights=weight_array[df_funds['isShutdown']==False]))
    # weighted avg. per non active fund
    fund_metrix_dict[col].append(np.average(df_funds[df_funds['isShutdown']==True][col], weights=weight_array[df_funds['isShutdown']==True]))
    # weighted avg. per active funded fund, (i.e. valueAssets unequal zero)
    fund_metrix_dict[col].append(np.average(df_funds[(df_funds['valueAssets']>0) & (df_funds['isShutdown']==False)][col], weights=weight_array[(df_funds['valueAssets']>0) & (df_funds['isShutdown']==False)]))
    # weighted avg. per nonactive funded fund, (i.e. valueAssets equal zero)
    fund_metrix_dict[col].append(np.average(df_funds[(df_funds['valueAssets']>0) & (df_funds['isShutdown']==True)][col], weights=weight_array[(df_funds['valueAssets']>0) & (df_funds['isShutdown']==True)]))

df_fund_metrix = pd.DataFrame(fund_metrix_dict, index=index_list)
df_fund_metrix = df_fund_metrix.round(1)

del fund_metrix_dict, columns_to_use_name, col, weight_array, index_list



###############################################################################
#  df_age 'lastInvestment' :df_funds['lastInvestment'].values.astype(np.int64), \
###############################################################################

# convert timedelta to nanoseconds
df_funds_int64 = pd.DataFrame( {'age' :df_funds['age'].values.astype(np.int64), \
                             'shutDownAfter' :df_funds['shutDownAfter'].values.astype(np.int64), \
                             'notActedSince' :df_funds['notActedSince'].values.astype(np.int64), \
                            'notTradedSince' :df_funds['notTradedSince'].values.astype(np.int64), \
                            'isShutdown' : df_funds['isShutdown']}, \
                              index = df_funds.index)
# NaT got converted negative numbers. Make them NaN. Convert to days
ns_to_days = 1/1e9/3600/24
df_funds_int64['age'] = df_funds_int64.where(df_funds_int64['age']>0)['age']*ns_to_days 
df_funds_int64['shutDownAfter'] = df_funds_int64.where(df_funds_int64['shutDownAfter']>0)['shutDownAfter']*ns_to_days
df_funds_int64['notActedSince'] = df_funds_int64.where(df_funds_int64['notActedSince']>0)['notActedSince']*ns_to_days
df_funds_int64['notTradedSince'] = df_funds_int64.where(df_funds_int64['notTradedSince']>0)['notTradedSince']*ns_to_days
df_age = df_funds_int64.groupby('isShutdown').agg(np.nanmean)[['age', 'shutDownAfter', 'notActedSince', 'notTradedSince']]
df_age['notActedLC'] = df_age['notActedSince'] / df_age['age']
df_age['notTradedLC'] = df_age['notTradedSince'] / df_age['age']
df_age['notActedLC'][1] = df_age['notActedSince'][1] / df_age['shutDownAfter'][1]
df_age['notTradedLC'][1] = df_age['notTradedSince'][1] / df_age['shutDownAfter'][1]

df_age = df_age.round(1)




del ns_to_days
del df_funds_int64



###############################################################################
#  create cluster graphs from JSON 2
###############################################################################

file_name = 'data/EtherscanExcluder_excluded_person_dict.json'


with open(file_name) as json_file:
    person_dict = json.load(json_file)
del person_dict['meta_data']



###############################################################################
#  create cluster graph for level 2
###############################################################################

import networkx as nx
import matplotlib.pyplot as plt
    
#from list
transactionSenderList = []
#to list
transactionReceiverList = []
#FM list
externalList = []

#here I create a df with managers and clusterIndex
df_ClusterIndexToPlot = df_funds[['manager','L2_clusterIndex']]
#here I define which cluster I want to display
df_ClusterIndexToPlot = df_ClusterIndexToPlot[df_ClusterIndexToPlot.L2_clusterIndex == 11]
#here I create a list of relevant managers
managerPlotList = df_ClusterIndexToPlot['manager'].tolist()


#add items from connection path to sender and receiver list
for person in person_dict:
    if person in managerPlotList:
        connection = person_dict[person]['level2']['connection_path']
        for id in range(len(connection)):
            transactionSenderList.append(person)
            transactionReceiverList.append(connection[id][0])
            transactionSenderList.append(connection[id][0])
            transactionReceiverList.append(connection[id][1])
            transactionSenderList.append(connection[id][1])
            transactionReceiverList.append(connection[id][2])
    else:
        pass
    
for person in person_dict:
    if person in managerPlotList:
        connection = person_dict[person]['level0']['connection_path']
        for id in range(len(connection)):
            transactionSenderList.append(person)
            transactionReceiverList.append(connection[id])

#add items from connection path to x and y list
for person in person_dict:
    if person in managerPlotList:
        connection = person_dict[person]['level1']['connection_path']
        for id in range(len(connection)):
            transactionSenderList.append(person)
            transactionReceiverList.append(connection[id][0])
            transactionSenderList.append(connection[id][0])
            transactionReceiverList.append(connection[id][1])
    else:
        pass

for id in range(len(transactionSenderList)):
    if transactionSenderList[id] in fundManagerList:
        pass
    else:      
        if transactionSenderList[id] in externalList:
            pass
        else:
            externalList.append(transactionSenderList[id])
    if transactionReceiverList[id] in fundManagerList:
        pass
    else:        
        if transactionReceiverList[id] in externalList:
            pass
        else:
            externalList.append(transactionReceiverList[id])

#df unique        
external_dict =     {'Unique':externalList}
df_external = pd.DataFrame(external_dict)
df_external['Index'] = df_external.index + len(fundManagerList)
del external_dict
del externalList

concatFundsAndExternal = [df_external, df_fundManagerID]

df_uniqueAdresses = pd.concat(concatFundsAndExternal)

df_uniqueAdresses['mngVsExt'] = np.where(df_uniqueAdresses['Index']>=len(fundManagerList), 'ext' , 'fm')

df_IDConversion = df_uniqueAdresses.copy()

del concatFundsAndExternal
del df_external

    
#df to plot        
transactionsToPlot_dict = {'From':transactionSenderList,'To':transactionReceiverList}



#lookup unique value, sort order from to, remove duplicates        
df_transactionsToPlot = pd.DataFrame(transactionsToPlot_dict)
df_transactionsToPlot['fromId'] = [df_uniqueAdresses.loc[df_uniqueAdresses['Unique'] == id, 'Index'].iloc[0] for id in df_transactionsToPlot['From']]
df_transactionsToPlot['toId'] = [df_uniqueAdresses.loc[df_uniqueAdresses['Unique'] == id, 'Index'].iloc[0] for id in df_transactionsToPlot['To']]
#df_transactionsToPlot_copy = df_transactionsToPlot.copy()
df_transactionsToPlot['from'] = np.where(df_transactionsToPlot['fromId']>=df_transactionsToPlot['toId'], df_transactionsToPlot['toId'] , df_transactionsToPlot['fromId'])
df_transactionsToPlot['to'] = np.where(df_transactionsToPlot['fromId']<=df_transactionsToPlot['toId'], df_transactionsToPlot['toId'] , df_transactionsToPlot['fromId'])
df_transactionsToPlot = df_transactionsToPlot.drop(columns=['From', 'To', 'fromId', 'toId'])
df_transactionsToPlot = df_transactionsToPlot.drop_duplicates()
 

carac = df_uniqueAdresses

F=nx.from_pandas_edgelist(df_transactionsToPlot, 'from', 'to', create_using=nx.Graph() )
F.nodes()
# Thus, I cannot give directly the 'fmVsExt' column to netowrkX, I need to arrange the order!


# delete external id's with only one link
count_list = nx.degree(F)
max_fm_id = len(fundManagerList)-1
IDs_to_delete_list = []
for ID, n_neighbors in count_list:
    if (ID>max_fm_id) and (n_neighbors==1):
        IDs_to_delete_list.append(ID)
    
for ID in IDs_to_delete_list:
    F.remove_node(ID)
for ID in IDs_to_delete_list:    
    carac = carac[carac['Index']!=ID]    


# Here is the tricky part: I need to reorder carac to assign the good color to each node
carac= carac.set_index('Index')
carac=carac.reindex(F.nodes())
 
# And I need to transform my categorical column in a numerical value: fm->1, nfm->2...
carac['mngVsExt']=pd.Categorical(carac['mngVsExt'])
carac['mngVsExt'].cat.codes


from matplotlib.colors import LinearSegmentedColormap


#0 defines min value (my fund manager nodes); 
#1 defines max value (my external nodes);
#0.5 is not required
cdict1 = {'red':   ((0.0, 0.0, (210/255)),
                    #(0.5, 1.0, 0.0),
                    (1.0, (30/255), 0.0)),

         'green': ((0.0, 0.0, (5/255)),
                   #(0.5, 0.0, 0.0),
                   (1.0, (165/255), 0.0)),
                   

         'blue':  ((0.0, 0.0, (55/255)),
                   #(0.5, 0.0, 0.0),
                   (1.0, (165/255), 0.0))
         }

unibas = LinearSegmentedColormap('unibas', cdict1)

plt.figure(figsize=(52,32))
nx.draw(F, with_labels=True,  node_color=carac['mngVsExt'].cat.codes, cmap=unibas, node_size=1000)
plt.savefig('plots/cluster_level2.pdf') 
del carac
del transactionSenderList
del transactionReceiverList
del person, connection, transactionsToPlot_dict, id, json_file, file_name
#del uniqueAdresses_dict


###############################################################################
#  bar plot
###############################################################################

# how many bars should be plotted
num_to_plot = 10

count_list = nx.degree(F)
id_list = []
n_neighbors_list = []
for ID, n_neighbors in count_list:
    id_list.append(ID)
    n_neighbors_list.append(n_neighbors)
df_sorted_neighbor = pd.DataFrame(data={'num_neighbors':n_neighbors_list}, index=id_list).sort_values(by=['num_neighbors'], ascending=False)
  
top_ids_list = df_sorted_neighbor.index.to_list()[:num_to_plot]
top_num_connections_list = df_sorted_neighbor.num_neighbors.to_list()[:num_to_plot]

# fund manager or extern
df_uniqueAdresses_copy = df_uniqueAdresses.set_index('Index')
bar_color = []
green = (210/255, 5/255, 55/255)
red = (30/255, 165/255, 165/255)
for id in top_ids_list:
    if df_uniqueAdresses_copy.loc[id]['mngVsExt'] == 'fm':
        bar_color.append(red)
    else:
        bar_color.append(green)
    


def cm2inch(value):
    return value/2.54

width = 13 # cm
height = 8 # cm
fig, ax = plt.subplots(figsize=(cm2inch(width),cm2inch(height)))

bar_x = np.linspace(1, num_to_plot, num_to_plot)
# replace bar_height by cluster counts
bar_height = top_num_connections_list
# replace bar_tick_label by fund name
bar_tick_label = [str(id) for id in top_ids_list]

bar_plot = plt.bar(bar_x, bar_height, tick_label=bar_tick_label, color=bar_color)

def autolabel(rects, ax_handle, vertical_offset):
    for idx,rect in enumerate(rects):
        height = rect.get_height()
        ax_handle.text(rect.get_x() + rect.get_width()/2., height-vertical_offset,
                height,
                ha='center', va='center', color='w')

autolabel(bar_plot, ax, 6)
plt.xlabel('ID')
fig.subplots_adjust(bottom=0.2)

# plt.ylim(0,20)

# remove axis
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.set_yticks([]) 
ax.tick_params(axis=u'both', which=u'both',length=0)

plt.savefig('plots/top10_level2.pdf')


if bSave:
    folder = 'dataframes/'
    df_trades.to_pickle(folder + 'df_trades.pkl')
    df_funds.to_pickle(folder + 'df_funds.pkl')
    df_exchanges.to_pickle(folder + 'df_exchanges.pkl')
    df_AuM.to_pickle(folder + 'df_AuM.pkl') 
    df_counts.to_pickle(folder + 'df_counts.pkl')



#check whether color grouping works
#del df_AuM
del df_transactionsToPlot
del cg, df_ClusterIndexToPlot, df_assets
del df_USD
del df_correlation1, df_correlation2, df_correlation3, df_counts, df_exchanges
del df_investor, df_performance1, df_performance2, df_prices
del df_pricesInUsd, df_pricesInUsd1, df_pricesInUsd2
del ax, bar_color, bar_height, bar_plot, bar_tick_label, bar_x
del fig, green, height, id, num_to_plot, red, top_ids_list
del top_num_connections_list, width
del df_holdings, df_invest, df_trades



del managerPlotList
del F
#del df_ENS



###############################################################################
#  ENS check dataframe
###############################################################################

def pullENSDomains(person):
    from graphqlclient import GraphQLClient

    client = GraphQLClient('https://api.thegraph.com/subgraphs/name/ensdomains/ens')

    result = client.execute('''
                        {{
                            account(id: "{}") {{
                                id
                                domains {{
                                  id
                                  name
                                }}
                                
                                }}
                            }}
                        '''.format(person))
    JSON = json.loads(result)
    return JSON

data_dict = {
    'userID':[],
    'ownedDomainID':[],
    'ownedDomain':[],
    }

uniqueAdresses = df_uniqueAdresses['Unique'].tolist()
for person in uniqueAdresses:

    data = pullENSDomains(person)
    ENS_dict = data['data']['account']
    
    if ENS_dict == None:
        # go to next person
        continue
    
    UserId = ENS_dict['id']
    ens = ENS_dict['domains']
         
    for en in ens:
        data_dict['userID'].append(UserId)
        data_dict['ownedDomainID'].append(en['id'])
        data_dict['ownedDomain'].append(en['name'])
            
         
# integreate into a dataframe
df_ENS = pd.DataFrame(
    data = data_dict
    ).set_index('userID')


del df_uniqueAdresses
del uniqueAdresses
del ENS_dict, UserId, data, data_dict, en, ens



###############################################################################
#  create cluster graph for level 1
###############################################################################

#from list
transactionSenderList = []
#to list
transactionReceiverList = []
#FM list
externalList = []

#here I create a df with managers and clusterIndex
df_ClusterIndexToPlot = df_funds[['manager','L1_clusterIndex']]
#here I define which cluster I want to display
df_ClusterIndexToPlot = df_ClusterIndexToPlot[df_ClusterIndexToPlot.L1_clusterIndex == 15]
#here I create a list of relevant managers
managerPlotList = df_ClusterIndexToPlot['manager'].tolist()


#add items from connection path to x and y list
for person in person_dict:
    if person in managerPlotList:
        connection = person_dict[person]['level1']['connection_path']
        for id in range(len(connection)):
            transactionSenderList.append(person)
            transactionReceiverList.append(connection[id][0])
            transactionSenderList.append(connection[id][0])
            transactionReceiverList.append(connection[id][1])
    else:
        pass
    
for person in person_dict:
    if person in managerPlotList:
        connection = person_dict[person]['level0']['connection_path']
        for id in range(len(connection)):
            transactionSenderList.append(person)
            transactionReceiverList.append(connection[id])

#sort items from x and y list into fmlist and nfmlist and create unique list
for id in range(len(transactionSenderList)):
    if transactionSenderList[id] in fundManagerList:
        pass
    else:      
        if transactionSenderList[id] in externalList:
            pass
        else:
            externalList.append(transactionSenderList[id])
    if transactionReceiverList[id] in fundManagerList:
        pass
    else:        
        if transactionReceiverList[id] in externalList:
            pass
        else:
            externalList.append(transactionReceiverList[id])

#df unique        
external_dict =     {'Unique':externalList}
df_external = pd.DataFrame(external_dict)
df_external['Index'] = df_external.index + len(fundManagerList)
del external_dict
del externalList

concatFundsAndExternal = [df_external, df_fundManagerID]

df_uniqueAdresses = pd.concat(concatFundsAndExternal)

df_uniqueAdresses['mngVsExt'] = np.where(df_uniqueAdresses['Index']>=len(fundManagerList), 'ext' , 'fm')

del concatFundsAndExternal
del df_external
    
#df to plot        
transactionsToPlot_dict = {'From':transactionSenderList,'To':transactionReceiverList}



#lookup unique value, sort order from to, remove duplicates        
df_transactionsToPlot = pd.DataFrame(transactionsToPlot_dict)
df_transactionsToPlot['fromId'] = [df_uniqueAdresses.loc[df_uniqueAdresses['Unique'] == id, 'Index'].iloc[0] for id in df_transactionsToPlot['From']]
df_transactionsToPlot['toId'] = [df_uniqueAdresses.loc[df_uniqueAdresses['Unique'] == id, 'Index'].iloc[0] for id in df_transactionsToPlot['To']]
#df_transactionsToPlot_copy = df_transactionsToPlot.copy()
df_transactionsToPlot['from'] = np.where(df_transactionsToPlot['fromId']>=df_transactionsToPlot['toId'], df_transactionsToPlot['toId'] , df_transactionsToPlot['fromId'])
df_transactionsToPlot['to'] = np.where(df_transactionsToPlot['fromId']<=df_transactionsToPlot['toId'], df_transactionsToPlot['toId'] , df_transactionsToPlot['fromId'])
df_transactionsToPlot = df_transactionsToPlot.drop(columns=['From', 'To', 'fromId', 'toId'])
df_transactionsToPlot = df_transactionsToPlot.drop_duplicates()
 

carac = df_uniqueAdresses

F=nx.from_pandas_edgelist(df_transactionsToPlot, 'from', 'to', create_using=nx.Graph() )

F.nodes()

carac= carac.set_index('Index')
carac=carac.reindex(F.nodes())
 

carac['mngVsExt']=pd.Categorical(carac['mngVsExt'])
carac['mngVsExt'].cat.codes

unibas = LinearSegmentedColormap('unibas', cdict1)

plt.figure(figsize=(52,32))
nx.draw(F, with_labels=True,  node_color=carac['mngVsExt'].cat.codes, cmap=unibas, node_size=1000)
plt.savefig('plots/cluster_level1.pdf') 
del carac
del transactionSenderList
del transactionReceiverList
del person, connection, transactionsToPlot_dict, id
#del uniqueAdresses_dict


###############################################################################
#  bar plot
###############################################################################

# how many bars should be plotted
num_to_plot = 10

count_list = nx.degree(F)
id_list = []
n_neighbors_list = []
for ID, n_neighbors in count_list:
    id_list.append(ID)
    n_neighbors_list.append(n_neighbors)
df_sorted_neighbor = pd.DataFrame(data={'num_neighbors':n_neighbors_list}, index=id_list).sort_values(by=['num_neighbors'], ascending=False)
  
top_ids_list = df_sorted_neighbor.index.to_list()[:num_to_plot]
top_num_connections_list = df_sorted_neighbor.num_neighbors.to_list()[:num_to_plot]

# fund manager or extern
df_uniqueAdresses_copy = df_uniqueAdresses.set_index('Index')
bar_color = []
green = (210/255, 5/255, 55/255)
red = (30/255, 165/255, 165/255)
for id in top_ids_list:
    if df_uniqueAdresses_copy.loc[id]['mngVsExt'] == 'fm':
        bar_color.append(red)
    else:
        bar_color.append(green)
    


def cm2inch(value):
    return value/2.54

width = 13 # cm
height = 8 # cm
fig, ax = plt.subplots(figsize=(cm2inch(width),cm2inch(height)))

bar_x = np.linspace(1, num_to_plot, num_to_plot)
# replace bar_height by cluster counts
bar_height = top_num_connections_list
# replace bar_tick_label by fund name
bar_tick_label = [str(id) for id in top_ids_list]

bar_plot = plt.bar(bar_x, bar_height, tick_label=bar_tick_label, color=bar_color)

def autolabel(rects, ax_handle, vertical_offset):
    for idx,rect in enumerate(rects):
        height = rect.get_height()
        ax_handle.text(rect.get_x() + rect.get_width()/2., height-vertical_offset,
                height,
                ha='center', va='center', color='w')

autolabel(bar_plot, ax, 1)
plt.xlabel('ID')
fig.subplots_adjust(bottom=0.2)

# plt.ylim(0,20)

# remove axis
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.set_yticks([]) 
ax.tick_params(axis=u'both', which=u'both',length=0)

plt.savefig('plots/top10_level1.pdf')



#check whether color grouping works
del df_transactionsToPlot
del df_ClusterIndexToPlot
del ax, bar_color, bar_height, bar_plot, bar_tick_label, bar_x
del df_uniqueAdresses, fig, green, height, id, num_to_plot, red, top_ids_list
del top_num_connections_list, width

del managerPlotList
del F



###############################################################################
#  create cluster graph for level 0
###############################################################################

#add items from connection path to x and y list
#from list
transactionSenderList = []
#to list
transactionReceiverList = []


#here I create a df with managers and clusterIndex
df_ClusterIndexToPlot = df_funds[['manager','L0_clusterSize']]
#here I define which cluster I want to display
df_ClusterIndexToPlot = df_ClusterIndexToPlot[df_ClusterIndexToPlot.L0_clusterSize >= 5]
#here I create a list of relevant managers
managerPlotList = df_ClusterIndexToPlot['manager'].tolist()



for person in person_dict:
    if person in managerPlotList:
        connection = person_dict[person]['level0']['connection_path']
        for id in range(len(connection)):
            transactionSenderList.append(person)
            transactionReceiverList.append(connection[id])

      

df_uniqueAdresses = df_fundManagerID.copy()

        
df_uniqueAdresses['mngVsExt'] = np.where(df_uniqueAdresses['Index']>=len(fundManagerList), 'ext' , 'fm')
      
        
transactionsToPlot_dict = {'From':transactionSenderList,'To':transactionReceiverList}
        
df_transactionsToPlot = pd.DataFrame(transactionsToPlot_dict)
df_transactionsToPlot['from'] = [df_uniqueAdresses.loc[df_uniqueAdresses['Unique'] == id, 'Index'].iloc[0] for id in df_transactionsToPlot['From']]
df_transactionsToPlot['to'] = [df_uniqueAdresses.loc[df_uniqueAdresses['Unique'] == id, 'Index'].iloc[0] for id in df_transactionsToPlot['To']]
df_transactionsToPlot = df_transactionsToPlot.drop(columns=['From', 'To'])
df_transactionsToPlot = df_transactionsToPlot.drop_duplicates()

carac = df_uniqueAdresses




        
# Build your graph
G=nx.from_pandas_edgelist(df_transactionsToPlot, 'from', 'to', create_using=nx.Graph() )

G.nodes()

carac= carac.set_index('Index')
carac=carac.reindex(G.nodes())

# And I need to transform my categorical column in a numerical value: fm->1, nfm->2...
carac['mngVsExt']=pd.Categorical(carac['mngVsExt'])
carac['mngVsExt'].cat.codes

cdict1 = {'red':   ((0.0, 0.0, (30/255)),
                    #(0.5, 1.0, 0.0),
                    (1.0, (210/255), 0.0)),

         'green': ((0.0, 0.0, (165/255)),
                   #(0.5, 0.0, 0.0),
                   (1.0, (5/255), 0.0)),
                   

         'blue':  ((0.0, 0.0, (165/255)),
                   #(0.5, 0.0, 0.0),
                   (1.0, (55/255), 0.0))
         }

unibas = LinearSegmentedColormap('unibas', cdict1)


plt.figure(figsize=(52,32))
nx.draw(G, with_labels=True,  node_color=carac['mngVsExt'].cat.codes, cmap=unibas, node_size=4000)
plt.savefig('plots/cluster_level0.pdf') 
del transactionSenderList, transactionReceiverList, person, connection, transactionsToPlot_dict
del person_dict, id
del cdict1
#del df_transactionsToPlot

###############################################################################
#  bar plot
###############################################################################

# how many bars should be plotted
num_to_plot = 10

count_list = nx.degree(G)
id_list = []
n_neighbors_list = []
for ID, n_neighbors in count_list:
    id_list.append(ID)
    n_neighbors_list.append(n_neighbors)
df_sorted_neighbor = pd.DataFrame(data={'num_neighbors':n_neighbors_list}, index=id_list).sort_values(by=['num_neighbors'], ascending=False)
  
top_ids_list = df_sorted_neighbor.index.to_list()[:num_to_plot]
top_num_connections_list = df_sorted_neighbor.num_neighbors.to_list()[:num_to_plot]

# fund manager or extern
df_uniqueAdresses_copy = df_uniqueAdresses.set_index('Index')
bar_color = []
green = (210/255, 5/255, 55/255)
red = (30/255, 165/255, 165/255)
for id in top_ids_list:
    if df_uniqueAdresses_copy.loc[id]['mngVsExt'] == 'fm':
        bar_color.append(red)
    else:
        bar_color.append(green)
    


def cm2inch(value):
    return value/2.54

width = 13 # cm
height = 8 # cm
fig, ax = plt.subplots(figsize=(cm2inch(width),cm2inch(height)))

bar_x = np.linspace(1, num_to_plot, num_to_plot)
# replace bar_height by cluster counts
bar_height = top_num_connections_list
# replace bar_tick_label by fund name
bar_tick_label = [str(id) for id in top_ids_list]

bar_plot = plt.bar(bar_x, bar_height, tick_label=bar_tick_label, color=bar_color)

def autolabel(rects, ax_handle, vertical_offset):
    for idx,rect in enumerate(rects):
        height = rect.get_height()
        ax_handle.text(rect.get_x() + rect.get_width()/2., height-vertical_offset,
                height,
                ha='center', va='center', color='w')

autolabel(bar_plot, ax, 1)
plt.xlabel('ID')
fig.subplots_adjust(bottom=0.2)

# plt.ylim(0,20)

# remove axis
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.set_yticks([]) 
ax.tick_params(axis=u'both', which=u'both',length=0)

plt.savefig('plots/top10_level0.pdf')


del G
del managerPlotList
#del uniqueAdresses
#check whether color grouping works
del df_transactionsToPlot
del df_ClusterIndexToPlot
del ax, bar_color, bar_height, bar_plot, bar_tick_label, bar_x, df_uniqueAdresses_copy
del df_uniqueAdresses, fig, green, height, id, num_to_plot, red, top_ids_list
del top_num_connections_list, width
del carac
del fundManagerList
del df_fundManagerID
del IDs_to_delete_list
del bSave
del folder
del style, plot_style
del max_fm_id, id_list, n_neighbors, n_neighbors_list, df_sorted_neighbor



print('')
print('----------- DONE --------------')