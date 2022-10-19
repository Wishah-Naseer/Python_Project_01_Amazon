import api_call_offers
from GoogleSheet import GoogleSheet
import api_call_stock_est

class MainFile(object):
    def __init__(self):
        self.columns = []
        self.offers_data = []
        self.stock_est_data = []
        self.columns = api_call_offers.COLUMN_NAMES
        self.google_sheet_object =GoogleSheet("./resources/client_secret.json",
                                              api_call_offers.GOOGLE_SHEET_LINK)
        self.ASIN_list, self.data = api_call_offers.api_calling_offers()
        self.offer_id,self.price, self.seller_name, self.seller_id, self.ASI_number = api_call_offers.do_extraction( self.ASIN_list, self.data)
        print("Offers extracted")
        print("Offer length:  ",len(self.offer_id))
        self.google_sheet_object.create_tabs(self.google_sheet_object, api_call_offers.WORKSHEET_NAME)
        print("Worksheet checked")
        self.google_sheet_object.read_data(self.google_sheet_object, api_call_offers.WORKSHEET_NAME)
        print("Data Read and Cleared")
        self.offers_data.append(self.ASI_number)
        self.offers_data.append(self.price)
        self.offers_data.append(self.seller_name)
        self.offers_data.append(self.seller_id)
        self.offers_data.append(self.offer_id)
        for i in range(0, len(self.offers_data)):
            column = i + 1
            self.google_sheet_object.write_data(self.offers_data[i], self.google_sheet_object,
                                                api_call_offers.WORKSHEET_NAME, column, self.columns[i])
        print("Offers Data Written")
        self.stock_estimation_data = api_call_stock_est.stock_estimation(self.offer_id,self.ASI_number)
        self.stock_level, self.min_quantity, self.availability_message, self.is_prime, self.in_stock, self.has_stock_estimation = api_call_stock_est.SE_data_extraction(self.stock_estimation_data)
        print("Stock Estimation Extracted")
        print("length of stock estimation", len(self.stock_estimation_data))
        self.stock_est_data.append(self.stock_level)
        self.stock_est_data.append(self.min_quantity)
        self.stock_est_data.append(self.availability_message)
        self.stock_est_data.append(self.is_prime)
        self.stock_est_data.append(self.in_stock)
        self.stock_est_data.append(self.has_stock_estimation)
        index_SE = 0
        for i in range(len(self.offers_data), (len(self.stock_est_data)+len(self.offers_data))):
            column = i + 1
            self.google_sheet_object.write_data(self.stock_est_data[index_SE],self.google_sheet_object,
                                                api_call_offers.WORKSHEET_NAME,column,self.columns[i])
            index_SE +=1
        print("Stock Estimation Data Written")

mainfile = MainFile()
