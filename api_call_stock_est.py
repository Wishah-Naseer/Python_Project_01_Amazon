import requests
import json
import api_call_offers

# set up the request parameters
def api_call_SE(ASIN_SE, OFFERID):
  params = {
  'api_key': '86E4DDAC37A940799F93131032482B7D',
    'type': 'stock_estimation',
    'amazon_domain': 'amazon.com',
    'asin': ASIN_SE,
    'offer_id': OFFERID
  }
  return params
stock_level = []
min_quantity = []
availability_message = []
price_SE = []
is_prime = []
in_stock = []
ASIN_SE = []
has_stock_estimation = []
stock_estimation_data = []
ASINSE = ""
OFFERS_ID = ""

def stock_estimation(OFFERID,ASIN_SE):
  for i in range(0,len(OFFERID)):
    ASINSE = ASIN_SE[i]
    OFFERS_ID = OFFERID[i]
    params = api_call_SE(ASINSE, OFFERS_ID)
    api_result = requests.get('https://api.rainforestapi.com/request', params)
    data_se = api_result.json()
    stock_estimation_data.append(data_se)
  return stock_estimation_data

def SE_data_extraction(stock_estimation_data):
  stock_estimation = []
  for i in range(0,len(stock_estimation_data)):
    if 'stock_estimation' in stock_estimation_data[i]:
      stock_estimation.append(stock_estimation_data[i]['stock_estimation'])
    else:
      stock_estimation.append(stock_estimation_data[i])
  for i in range(0,len(stock_estimation)):
    if 'stock_level' in stock_estimation[i]:
      stock_level.append(stock_estimation[i]['stock_level'])
    else:
      stock_level.append('No Stock Level')
    if 'min_quantity' in stock_estimation[i]:
      min_quantity.append(stock_estimation[i]['min_quantity'])
    else:
      min_quantity.append('No Stock')
    if 'availability_message' in stock_estimation[i]:
      availability_message.append(stock_estimation[i]['availability_message'])
    elif 'message' in stock_estimation[i]:
      availability_message.append(stock_estimation[i]['message'])
    else:
      availability_message.append('No Stock')
    # is_prime.append(stock_estimation[i]['is_prime'])
    # in_stock.append(stock_estimation[i]['in_stock'])
    # has_stock_estimation.append(stock_estimation[i]['has_stock_estimation'])
  return stock_level, min_quantity, availability_message, is_prime, in_stock , has_stock_estimation
