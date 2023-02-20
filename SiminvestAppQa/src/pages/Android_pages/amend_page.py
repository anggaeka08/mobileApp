from SiminvestAppQa.src.data.userData import user_data
from SiminvestAppQa.src.pages.Android_pages.buy_process import BuyProcess
import time
import allure
import logging as logger

trans_entry_1 = 'OrderListEntry0'
order_status = 'AmendPageStatusValue'
order_id = 'AmendPageOderID'
amend_btn = '//android.widget.TextView[@text="AMEND"]'
cancel_btn = 'AmendPageBatakan'
amend_btn_on_buy_page = 'SellPageSellBtn'
buy_page_header = 'SellPageHeader'
lot_count = 'SellPageLotValue'
price_plus_btn = 'SellPageHargaPlus'
price_minus_btn = 'SellPageHargaMinus'
price_space = 'SellPageHargaValue'
bit_price_on_buy_page = '//android.view.ViewGroup[@content-desc="SellPageOrderBookTextBid0"]/android.widget.TextView'
ask_price_on_buy_page = '//android.view.ViewGroup[@content-desc="SellPageOrderBookTextAsk0"]/android.widget.TextView'
lot_on_status_page = 'AmendPageLotDipesanValue'
harga_on_status_page = 'AmendPageHargaValue'
Auto_rejection_popup = '//android.widget.TextView[@text="Can not increase quantity"]'
Auto_rejection_ok = '//android.widget.TextView[@text="OK"]'
price_on_trans_for_entry_1 = 'OrderListEntry0Price'
lot_on_trans_for_entry_1 = 'OrderListEntry0Lot'
hubungi_customer_care = 'AmendPageHelpBtn'
chrome_xpath = '//android.view.View[@content-desc="Halaman beranda Pusat Bantuan Sinarmas Sekuritas"]/android.widget.Image'
click_browser=  '//*[@text="Browser"]'
click_accept = '//*[@text="AGREE & CONTINUE"]'
class AmendProcess(BuyProcess):

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
        self.click(trans_entry_1)

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
        self.click_on_ok_btn()
        self.verify_transaction_page()
        transaction_page_price = self.get_attribute(price_on_trans_for_entry_1, "text")
        self.assert_equal(self.add_thousand_seprator(int(increased_price)), transaction_page_price)

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
       # self.click(click_browser)
        self.sleep(2)

    @allure.step("Verify redirection after click on customer support")
    def verify_redirection_after_click_on_customer_support(self):
        self.assert_equal(self.is_element_visible(chrome_xpath), True)
