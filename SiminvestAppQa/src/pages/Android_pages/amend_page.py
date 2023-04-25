from datetime import datetime

from SiminvestAppQa.src.data.userData import user_data
from SiminvestAppQa.src.pages.Android_pages.buy_process import BuyProcess
from SiminvestAppQa.src.pages.Android_pages.stock_detail_page import StockDetailPage
from SiminvestAppQa.src.pages.Android_pages.sell_process import SellProcess
import time
import allure
import logging as logger

trans_entry_1 = 'order_list_entry_0'
order_status = "//android.view.ViewGroup[4]/android.widget.TextView[@index = '0']"
order_id = "//android.view.ViewGroup/android.widget.TextView[3][@index='6']"
amend_btn = '//android.widget.TextView[@text="AMEND"]'
cancel_btn = '//android.widget.TextView[@text="BATALKAN"]'
amend_btn_on_buy_page = 'SellPageSellBtn'
buy_page_header = 'SellPageHeader'
lot_count = 'SellPageLotValue'
price_plus_btn = 'SellPageHargaPlus'
price_minus_btn = 'SellPageHargaMinus'
price_space = 'SellPageHargaValue'
bit_price_on_buy_page = '//android.view.ViewGroup[@content-desc="SellPageOrderBookTextBid0"]/android.widget.TextView'
ask_price_on_buy_page = '//android.view.ViewGroup[@content-desc="SellPageOrderBookTextAsk0"]/android.widget.TextView'
lot_on_status_page = "//android.view.ViewGroup/android.widget.TextView[11][@index = '15']"
harga_on_status_page = "//android.view.ViewGroup/android.widget.TextView[9][@index = '13']"
Auto_rejection_popup = '//android.widget.TextView[@text="Can not increase quantity"]'
Auto_rejection_ok = '//android.widget.TextView[@text="OK"]'
price_on_trans_for_entry_1 = 'price_0'
lot_on_trans_for_entry_1 = 'lot_0'
hubungi_customer_care = 'SellPageHelpLink'
chrome_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.view.View"
click_browser=  '//*[@text="Browser"]'
click_accept = '//*[@text="AGREE & CONTINUE"]'
exchange_notification= '//android.widget.TextView[contains(@text, "Bursa Tidak Beroperasi")]'
stock_price = 'SellPageStockPrice'
sdp_page_open = "(//android.view.ViewGroup/android.view.ViewGroup[3][@index = '2'])[1]"
stock_res_p_sdp = 'SDPStockPL'
srp_amend_page = 'SellPageStockPL'
buying_power = '//android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView[4]'
total_lot_value = 'SellPageTotalLotValue'
stock_code_amend = 'SellPageStockCode'
stock_com_name = 'SellPageStockName'
buy_power_exceed_msg = '//android.widget.TextView[@text="Nilai pembelian kamu melebihi trading limit."]'
stock_price_sdp = 'SDPStockPrice'
stock_pl_sdp = 'SDPStockPL'
total_beli = '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView[6]'
class AmendProcess(StockDetailPage,SellProcess ):

    @allure.step('Open transaction page with register user ')
    def open_trans_page_with_reg_user(self, phone_number):
        self.click_mulai_sekarang()
        self.type_mobile_no(phone_number)
        self.click_selanjutnya()
        self.enter_otp(user_data['valid_otp'])
        self.enter_pin()
        self.close_home_page_banner()
        self.verify_home_page_reg_user()
        self.click_on_transaction_btn()
        #self.verify_transaction_page()

    @allure.step("Open status page of buy order")
    def open_status_page_of_buy_order(self):
        #self.click(trans_entry_1)
        self.click('(//android.widget.TextView[contains(@text, "BELI")])[1]')

    @allure.step("Open status page of sell order")
    def open_status_page_of_sell_order(self):
        #self.click(trans_entry_1)
        self.click('(//android.widget.TextView[contains(@text, "JUAL")])[1]')

    @allure.step("Verify order status page")
    def verify_order_status_page(self):
        status_text_presence = self.is_element_visible(order_status)
        self.assert_equal(status_text_presence, True)
        self.assert_equal(self.get_attribute(order_status, "Text"), "SENDING")
        self.assert_equal(self.is_element_visible(order_id), True)
        self.assert_equal(self.is_element_visible(amend_btn), True)
        self.assert_equal(self.is_element_visible(cancel_btn), True)

    @allure.step("Verify amend page")
    def verify_amend_purchase_page(self):
        self.sleep(2)
        buy_page_header_present = self.is_element_visible(buy_page_header)
        assert buy_page_header_present == True, f"buy_page_header Should be present"
        amend_btn_on_buy_page_present = self.is_element_visible(amend_btn_on_buy_page)
        assert amend_btn_on_buy_page_present == True, f"amend_btn_on_buy_page Should be present"
        lot_area_present = self.is_element_visible(lot_count)
        assert lot_area_present == True, f"lot_area Should be present"

    @allure.step("click on amend btn")
    def click_on_amend_btn(self):
        self.sleep(3)
        self.click(amend_btn)

    @allure.step("click on cancel btn on status page")
    def click_on_cancel_btn_on_status_page(self):
        self.click(cancel_btn)

    @allure.step("Click to increase price")
    def click_on_price_increase(self):
        self.click(price_plus_btn)

    @allure.step("Click to decrease price")
    def click_on_price_decrease(self):
        self.click(price_minus_btn)

    @allure.step("Click on amend btn on amend page")
    def click_amend_btn_amend_page(self):
        self.click(amend_btn_on_buy_page)

    @allure.step("Verify user able to set ask or bid value in harga")
    def verify_user_able_to_set_ask_bid_value_in_harga(self):
        self.click(bit_price_on_buy_page)
        self.sleep(2)
        self.assert_equal(self.add_thousand_seprator(int((self.get_attribute(price_space, "text")).replace(',', ''))), self.get_attribute(bit_price_on_buy_page, "text"))
        self.click(ask_price_on_buy_page)
        self.sleep(3)
        self.assert_equal(self.add_thousand_seprator(int((self.get_attribute(price_space, "text")).replace(',', ''))), self.get_attribute(ask_price_on_buy_page, "text"))

    @allure.step("Verify lot and harga on order status and purchased page")
    def verify_lot_harga_on_two_pages(self):
        harga_value = self.get_attribute(harga_on_status_page, "text")
        lot_value = self.get_attribute(lot_on_status_page, "text")
        self.click_on_amend_btn()
        self.assert_equal(harga_value[3:],self.add_thousand_seprator(int((self.get_attribute(price_space, "text")).replace(',', ''))))
        self.assert_equal(lot_value,self.get_attribute(lot_count, "text"))

    @allure.step("Verify Auto rejection pop message")
    def verify_auto_rejection_pop_message(self):
        self.assert_equal(self.get_attribute(Auto_rejection_popup, "text"), "Can not increase quantity")

    @allure.step("click on ok btn on auto rejection")
    def click_on_ok_btn_on_auto_rejection(self):
        self.click(Auto_rejection_ok)

    @allure.step("Verify transaction presence of amend on transaction page")
    def verify_transaction_presence_after_amend_success(self):
        self.click_on_price_increase()
        increased_price = self.get_attribute(price_space, "text")
        self.click_amend_btn_amend_page()
        self.click_on_confirm_btn()
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        logger.info(f"Current Time = {current_time}")
        if (current_time >= '7:30') or ( current_time <= '15:00'):
            self.assert_equal(self.is_element_visible(exchange_notification), False)
            logger.info("within time")
            self.click_on_ok_btn()
            self.verify_transaction_page()
            #transaction_page_price = self.get_attribute(price_on_trans_for_entry_1, "text")
            #transaction_page_price = int(transaction_page_price[7:])
            # self.assert_equal(self.add_thousand_seprator(int(increased_price)), transaction_page_price)
        else:
            logger.info("Out of time")
            self.assert_equal(self.is_element_visible(exchange_notification), True)
            self.click_on_ok_btn_after_market_close()

    @allure.step("Verify lot and price value on transaction page and amend/cancel page")
    def verify_lot_price_value_on_trans_page_and_amend_or_cancel_page(self):
        transaction_page_price = self.get_attribute(price_on_trans_for_entry_1, "text")
        transaction_page_lot = self.get_attribute(lot_on_trans_for_entry_1, "text")
        self.open_status_page_of_buy_order()
        harga_value = self.get_attribute(harga_on_status_page, "text")
        lot_value = self.get_attribute(lot_on_status_page, "text")
        self.assert_equal(transaction_page_price, harga_value[3:])
        self.assert_equal(transaction_page_lot, lot_value)

    @allure.step("Click on Customer care support link")
    def click_on_customer_support_link(self):
        self.click(hubungi_customer_care)
        #self.click(click_accept)
        self.sleep(2)

    @allure.step("Verify redirection after click on customer support")
    def verify_redirection_after_click_on_customer_support(self):
        self.assert_equal(self.is_element_visible(hubungi_customer_care), False)

    @allure.step('Open transaction page with nonKYC user ')
    def open_trans_page_with_nonKYC_user(self, phone_number):
        self.click_mulai_sekarang()
        self.type_mobile_no(phone_number)
        self.click_selanjutnya()
        self.enter_otp(user_data['valid_otp'])
        self.enter_pin()
        self.verify_home_page()
        self.click_on_transaction_btn()

    @allure.step("Verify amend process by subtract in harga")
    def verify_amend_process_by_subtract_in_harga(self):
        self.click_on_price_decrease()
        decreased_price = self.get_attribute(price_space, "text")
        self.click_amend_btn_amend_page()
        self.click_on_confirm_btn()
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        logger.info(f"Current Time = {current_time}")
        if (current_time >= '7:30') or (current_time <= '15:100'):
            self.assert_equal(self.is_element_visible(exchange_notification), False)
            logger.info("within time")
            self.click_on_ok_btn()
            self.verify_transaction_page()
            transaction_page_price = self.get_attribute(price_on_trans_for_entry_1, "text")
            #transaction_page_price = int(transaction_page_price[7:])
            # self.assert_equal(self.add_thousand_seprator(int(decreased_price)), transaction_page_price)
        else:
            logger.info("Out of time")
            self.assert_equal(self.is_element_visible(exchange_notification), True)
            self.click_on_ok_btn_after_market_close()

    @allure.step("Verify amend process by add lot value after add harga")
    def Verify_amend_process_by_add_lot_value_after_add_harga(self):
        self.click_on_price_increase()
        increased_price = self.get_attribute(price_space, "text")
        self.click_on_lot_increase_no()
        increased_lot = self.get_attribute(lot_count, "text")
        self.click_amend_btn_amend_page()
        self.click_on_confirm_btn()
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        logger.info(f"Current Time = {current_time}")
        if (current_time >= '7:30') or (current_time <= '15:00'):
            self.assert_equal(self.is_element_visible(exchange_notification), False)
            logger.info("within time")
            self.click_on_ok_btn()
            self.verify_transaction_page()
            transaction_page_price = self.get_attribute(price_on_trans_for_entry_1, "text")
            transaction_page_lot = self.get_attribute(lot_on_trans_for_entry_1, "text")
           # transaction_page_lot = transaction_page_lot[5:]
          #  transaction_page_price = int(transaction_page_price[7:])
            # self.assert_equal(self.add_thousand_seprator(int(increased_price)), transaction_page_price)
            # self.assert_equal(self.add_thousand_seprator(int(increased_lot)), transaction_page_lot)
        else:
            logger.info("Out of time")
            self.assert_equal(self.is_element_visible(exchange_notification), True)
            self.click_on_ok_btn_after_market_close()

    @allure.step("Verify amend process by subtract lot value after add harga")
    def Verify_amend_process_by_subtract_lot_value_after_add_harga(self):
        self.click_on_price_increase()
        increased_price = self.get_attribute(price_space, "text")
        self.click_on_lot_decrease_btn()
        decreased_lot = self.get_attribute(lot_count, "text")
        self.click_amend_btn_amend_page()
        self.click_on_confirm_btn()
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        logger.info(f"Current Time = {current_time}")
        if (current_time >= '7:30') or (current_time <= '15:00'):
            self.assert_equal(self.is_element_visible(exchange_notification), False)
            logger.info("within time")
            self.click_on_ok_btn()
            self.verify_transaction_page()
            transaction_page_price = self.get_attribute(price_on_trans_for_entry_1, "text")
            transaction_page_lot = self.get_attribute(lot_on_trans_for_entry_1, "text")
           # transaction_page_lot = transaction_page_lot[5:]
           # transaction_page_price = int(transaction_page_price[7:])
            # self.assert_equal(self.add_thousand_seprator(int(increased_price)), transaction_page_price)
            # self.assert_equal(self.add_thousand_seprator(int(decreased_lot)), transaction_page_lot)
        else:
            logger.info("Out of time")
            self.assert_equal(self.is_element_visible(exchange_notification), True)
            self.click_on_ok_btn_after_market_close()

    @allure.step("verify auto rejection due to Lot increase")
    def verify_auto_rejection_due_to_lot_increase(self):
        self.click_on_lot_increase_no()
        self.click_amend_btn_amend_page()
        self.click_on_confirm_btn()
        self.verify_auto_rejection_pop_message()

    @allure.step("Verify stock price and other things on amend page for buy")
    def verify_stock_price_and_other_fields_on_amend_page(self):
        self.go_back()
        self.sleep(2)
        self.click(sdp_page_open)
        self.sleep(2)
        full_d_SRP_ON_SDP = self.Response_price()
        self.go_back()
        self.verify_order_status_page()
        self.click_on_amend_btn()
        SRP_amend = self.get_attribute(srp_amend_page, 'text')
        self.assert_equal(full_d_SRP_ON_SDP, SRP_amend)
        self.assert_equal(self.is_element_visible(stock_price), True)
        self.assert_equal(self.is_element_visible(buying_power), True)
        self.update_text(lot_count, '500000')
        self.assert_equal(self.get_attribute(lot_count, 'text'), '50,000')
        self.update_text(lot_count, '2')
        self.click_on_lot_decrease_btn()
        self.assert_equal(self.get_attribute(lot_count, 'text'), '1')

    @allure.step("Verify stock price and other things on amend page for sell")
    def verify_stock_price_and_other_fields_on_amend_page_for_sell(self):
        self.go_back()
        self.sleep(2)
        self.click(sdp_page_open)
        self.sleep(2)
        full_d_SRP_ON_SDP = self.Response_price()
        self.go_back()
        self.verify_order_status_page()
        self.click_on_amend_btn()
        SRP_amend = self.get_attribute(srp_amend_page, 'text')
        self.assert_equal(full_d_SRP_ON_SDP, SRP_amend)
        self.assert_equal(self.is_element_visible(stock_price), True)
        self.assert_equal(self.is_element_visible(buying_power), True)
        self.update_text(lot_count, '500000')
        self.assert_equal(self.get_attribute(lot_count, 'text'), self.get_attribute(total_lot_value, 'text'))
        self.update_text(lot_count, '2')
        self.click_on_lot_decrease_btn()
        self.assert_equal(self.get_attribute(lot_count, 'text'), '1')

    @allure.step("Lot plus subtract feature")
    def lot_plus_subtract_feature(self):
        default_lot = int(self.get_attribute(lot_count, "text"))
        self.click_on_lot_increase_no()
        increased_lot = int(self.get_attribute(lot_count, "text"))
        self.assert_equal(default_lot+1, increased_lot)
        self.click_on_lot_decrease_btn()
        decreased_lot = int(self.get_attribute(lot_count, "text"))
        self.assert_equal(default_lot, decreased_lot)

    @allure.step("Functional validation for amend")
    def functional_validation_for_amend(self):
        self.assert_equal(self.is_element_visible(buy_page_header), True)
        self.assert_equal(self.is_element_visible(stock_code_amend), True)
        self.assert_equal(self.is_element_visible(stock_com_name), True)
        self.assert_equal(self.get_attribute(lot_count, 'text'), '2')
        self.scroll_up()
        self.assert_equal(self.is_element_visible(hubungi_customer_care) , True)
        self.scroll_down()
        self.assert_equal(self.is_element_visible(stock_code_amend), True)
        self.set_text(price_space, '1299090988')
        buy_power_exceed_msg_presence = self.is_element_visible(buy_power_exceed_msg)
        assert buy_power_exceed_msg_presence == True, f"price_exceed_msg_presence visible "
        buy_power_exceed_msg_text = self.get_attribute(buy_power_exceed_msg, "text")
        self.assert_equal(buy_power_exceed_msg_text, "Nilai pembelian kamu melebihi trading limit.")
        self.assert_equal(self.is_element_visible(amend_btn_on_buy_page), False)

    @allure.step("Validate numeric and mathematical values on amend page")
    def validate_numeric_and_mathematical_values_on_amend_page(self):
        transaction_page_price = self.get_attribute(price_on_trans_for_entry_1, "text")
        transaction_page_lot = self.get_attribute(lot_on_trans_for_entry_1, "text")
        self.open_status_page_of_buy_order()
        self.click(sdp_page_open)
        self.sleep(3)
        stock_current_price_sdp = int((self.get_attribute(stock_price_sdp, 'text')).replace(',',''))
        stock_response_price_sdp = self.get_attribute(stock_pl_sdp, 'text')
        c = '('
        index = stock_response_price_sdp.find(c)
        reponsePrice_sdp = int(stock_response_price_sdp[:index])
        d = stock_response_price_sdp.find('%')
        response_percentage_sdp = float(stock_response_price_sdp[index + 1:d])
        self.go_back()
        self.sleep(3)
        self.click_on_amend_btn()
        stock_price_amend = int((self.get_attribute(stock_price, 'text')).replace(',',''))
        stock_response_price_amend = self.get_attribute(srp_amend_page, 'text')
        c = '('
        index = stock_response_price_amend.find(c)
        reponsePrice_amend = int(stock_response_price_amend[:index])
        d = stock_response_price_amend.find('%')
        response_percentage_amend = float(stock_response_price_amend[index + 1:d])
        lot_amend = self.get_attribute(lot_count, 'text')
        beli_harga_amend = self.get_attribute(price_space, 'text')
        self.assert_equal(transaction_page_price[8:] , beli_harga_amend)
        self.assert_equal(transaction_page_lot[6:] , lot_amend)
        self.assert_equal(stock_current_price_sdp ,stock_price_amend)
        self.assert_equal(response_percentage_amend , response_percentage_sdp)
        self.assert_equal(reponsePrice_amend , reponsePrice_sdp)
        total_beli_amount_txt = self.get_attribute(total_beli, 'text')
        total_beli_amount = int((total_beli_amount_txt[3:]).replace(",", ""))
        self.assert_equal(total_beli_amount, (int(beli_harga_amend)) * 100)
        self.click_on_price_decrease()
        total_beli_amount_txt = self.get_attribute(total_beli, 'text')
        total_beli_amount = int((total_beli_amount_txt[3:]).replace(",", ""))
        beli_harga_amend = self.get_attribute(price_space, 'text')
        self.assert_equal(total_beli_amount, (int(beli_harga_amend)) * 100)
        self.click_on_lot_increase_no()
        beli_harga_amend = self.get_attribute(price_space, 'text')
        total_beli_amount_txt = self.get_attribute(total_beli, 'text')
        total_beli_amount = int((total_beli_amount_txt[3:]).replace(",", ""))
        lot_amend = int(self.get_attribute(lot_count, 'text'))
        self.assert_equal(total_beli_amount, ((int(beli_harga_amend)) * 100)*lot_amend)




