import requests
import json

# set up the request parameters
def api_call_offer(ASIN_Numbers):
  params = {
    'api_key': '86E4DDAC37A940799F93131032482B7D',
    'type': 'offers',
    'amazon_domain': 'amazon.com',
    'asin': ASIN_Numbers,
    'max_page': '5'
  }
  return params

# make the http GET request to Rainforest API
def api_calling_offers():
  ASIN_list = ['B00070KH5Q', 'B073JYC4XM', 'B0007VM8UC', 'B000IG20RC', 'B000OH56ZS']
  data = []
  for i in range(0,len(ASIN_list)):
    params = api_call_offer(ASIN_list[i])
    api_result = requests.get('https://api.rainforestapi.com/request', params)
    # print the JSON response from Rainforest API
    api_result_data = api_result.json()
    data.append(api_result_data)
  return ASIN_list, data

COLUMN_NAMES = ["ASIN","PRICE","SELLER NAME","SELLER ID","OFFER ID","STOCK_LEVEL",
                "MIN_QUANTITY","AVAILABILITY_MESSAGE","IS_PRIME","IN_STOCK",
                "HAS_STOCK_ESTIMATION"]
#WORKSHEET_NAME = str(input("Enter Tab Name : "))
WORKSHEET_NAME = 'DC6'
GOOGLE_SHEET_LINK = "13FBd7CwO0IRKGdWE6ei9LSWblYfDNX8YsK0xHCXPbS8"

offer_id = []
price = []
seller_name = []
seller_id = []
ASI_number = []
offers = []

def do_extraction(ASIN_list,data):
  for i in range(0,len(data)):
    offers.append(data[i]['offers'])
  length = len(offers)
  for i in range(0, length):
    len_new = len(offers[i])
    for index in range(0,len_new):
      ASI_number.append(ASIN_list[i])
      offer_ID = offers[i][index]['offer_id']
      offer_id.append(offer_ID)
      price_value = offers[i][index]['price']['value']
      price.append(price_value)
      seller = offers[i][index]['seller']['name']
      seller_name.append(seller)
      if 'id' in offers[i][index]['seller']:
        seller_ID = offers[i][index]['seller']['id']
        seller_id.append(seller_ID)
      else:
        seller_id.append('No Seller ID')
  return offer_id,price,seller_name,seller_id,ASI_number