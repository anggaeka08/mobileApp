from SiminvestAppQa.src.pages.Android_pages.amend_page import AmendProcess
from SiminvestAppQa.src.data.userData import user_data
import allure
import logging as logger
from datetime import date

'''
transaction_tab = "//android.widget.TextView[@text='Transaction']"
saham_tab = '(//android.view.ViewGroup[@content-desc="TranasactionPageSaham"])[1]'
rekshadana_tab ='(//android.view.ViewGroup[@content-desc="TranasactionPageSaham"])[2]'
order_list='TransactionPageSahamHeader0'
trade_list = 'TransactionPageSahamHeader1'
history = 'TransactionPageSahamHeader2'
GTC_list ='TransactionPageSahamHeader3'
today_transaction =''
'''
date_last_trans='AmendPageTanggalValue'
today = date.today()

class Transaction(AmendProcess):

    @allure.step("Verify last transaction in orderlist")
    def verify_last_transaction_orderlist(self):
        self.open_status_page_of_buy_order()
        date_trans = self.get_attribute(date_last_trans, 'text')
        c = ','
        index = date_trans.find(c)
        d1 = date_trans[:index]
        d2 = today.strftime("%d %B, %Y")
        c = ','
        index = d2.find(c)
        d3 = d2[:index-1]
        self.assert_equal(d1, d3)

