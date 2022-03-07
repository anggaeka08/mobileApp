from SiminvestAppQa.src.data.userData import user_data
from SiminvestAppQa.src.pages.Android_pages.login_page import LoginPage
from SiminvestAppQa.src.pages.Android_pages.home_page import HomePage
import time
import allure
import logging as logger

#buy process locators
sell_btn = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[6]'
buy_btn_with_sell='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[5]'
buy_btn_without_sell='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]'
#refferal page locators
refferal_page_heading = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView'
refferal_page_heading_value = 'Masukkan Kode Referral Teman Kamu?'
refferal_code_edit_box = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.widget.EditText'
selanjutnya = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]'
#buy page locators
buy_page_header = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.TextView'
buy_btn_on_buy_page = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]'
gtc_area = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]'
lot_area = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]'
cancel_btn = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.TextView'
gtc_on_off_btn = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.Switch'
date_option = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView'
date_selection = '//android.view.View[@content-desc="30 March 2022"]'
ok_btn_on_calender = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button[2]'
confirm_btn = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView'
ok_btn = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.TextView'
lot_count = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.widget.EditText'
lot_increase_btn = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ImageView'
lot_decrease_btn = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.widget.ImageView'
cari_btn_after_click ='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.EditText'
market_close_message_lct = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView[1]'
market_close_message = 'Bursa Tidak Beroperasi'
price_minus_btn = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.ImageView'
price_plus_btn = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.widget.ImageView'
price_space = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.widget.EditText'
buy_power_exceed_msg = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.widget.TextView'
total_beli_amount = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView[6]'
status_on_trasction_page = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[5]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[2]'
lot_count_on_buy_conf_page = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[5]'
hagra_on_buy_conf_page = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[7]'
jumlah_on_buy_conf_page = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[9]'
date_on_buy_conf_page = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[11]'
gtc_date_on_buy_page = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView'
Buying_Power_homepage='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[6]/android.widget.TextView[4]'
buying_power_buy_page = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView[4]'
bid_amount = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]/android.widget.TextView'
class BuyProcess(HomePage):

    @allure.step("open sdp page with kyc user")
    def open_sdp_page_with_kyc_user(self, number, stock_code):
        self.click_mulai_sekarang()
        self.type_mobile_no(number)
        self.click_selanjutnya()
        self.enter_otp(user_data['valid_otp'])
        self.enter_pin()
        self.close_home_page_banner()
        self.verify_home_page_reg_user()
        self.click_global_search_btn_and_saerch_stock(stock_code)
        self.sleep(3)
        self.click_on_stock_code()
        self.verify_sdp_page()

    @allure.step("open sdp page with non-kyc user")
    def open_sdp_page_with_non_kyc_user(self, number, stock_code):
        self.click_mulai_sekarang()
        self.type_mobile_no(number)
        self.click_selanjutnya()
        self.enter_otp(user_data['valid_otp'])
        self.enter_pin()
        self.close_home_page_banner()
        self.verify_home_page()
        self.click_global_search_btn_and_saerch_stock(stock_code)
        self.sleep(3)
        self.click_on_stock_code()

    @allure.step("open sdp page from portfolio page with kyc user")
    def open_sdp_by_portfolio_with_kyc_user(self, number):
        self.click_mulai_sekarang()
        self.type_mobile_no(number)
        self.click_selanjutnya()
        self.enter_otp(user_data['valid_otp'])
        self.enter_pin()
        self.close_home_page_banner()
        self.verify_home_page_reg_user()
        self.click_on_portfolio_btn()
        self.click_on_portfolio_entry_2()

    @allure.step("Check sell btn on sdp page")
    def check_for_sell_btn(self):
        sell_btn_present = self.is_element_visible(sell_btn)
        assert sell_btn_present == True, f"sell Btn Should be present"

    @allure.step("Check buy btn on sdp page")
    def check_for_buy_btn(self):
        buy_btn_with_sell_present = self.is_element_visible(buy_btn_with_sell)
        if buy_btn_with_sell_present == True:
            assert buy_btn_with_sell_present == True, f"buy Btn Should be present"
        else :
            buy_btn_without_sell_present = self.is_element_visible(buy_btn_without_sell)
            assert buy_btn_without_sell_present == True, f"buy Btn Should be present"

    @allure.step("Click on buy btn")
    def click_on_buy_btn(self):
        buy_with_sell = self.is_element_visible(buy_btn_with_sell)
        if buy_with_sell == True :
            self.click(buy_btn_with_sell)
            self.sleep(2)
        else :
            self.click(buy_btn_without_sell)
            self.sleep(2)

    @allure.step("Verif referral page")
    def verify_refferal_page(self):
        refferal_page_heading_text = self.get_attribute(refferal_page_heading, "text")
        self.assert_equal(refferal_page_heading_text, refferal_page_heading_value)
        refferal_code_edit_box_present = self.is_element_visible(refferal_code_edit_box)
        assert refferal_code_edit_box_present == True, f"refferal_code_edit_box Should be present"
        selanjutnya_present = self.is_element_visible(selanjutnya)
        assert selanjutnya_present == True, f"selanjutnya Should be present"

    @allure.step("Verify buy page")
    def verify_buy_page(self):
        buy_page_header_present = self.is_element_visible(buy_page_header)
        assert buy_page_header_present == True, f"buy_page_header Should be present"
        buy_btn_on_buy_page_present = self.is_element_visible(buy_btn_on_buy_page)
        assert buy_btn_on_buy_page_present == True, f"buy_btn_on_buy_page Should be present"
        gtc_area_present = self.is_element_visible(gtc_area)
        assert gtc_area_present == True, f"gtc_area Should be present"
        lot_area_present = self.is_element_visible(lot_area)
        assert lot_area_present == True, f"lot_area Should be present"

    @allure.step("Click on buy btn on buy page")
    def click_on_buy_btn_on_buy_page(self):
        self.click(buy_btn_on_buy_page)
        self.sleep(2)

    @allure.step("Click on cancel btn")
    def click_on_cancel_btn(self):
        self.click(cancel_btn)
        self.sleep(2)

    @allure.step("Click on gtc option")
    def tap_on_gtc_option(self):
        self.click(gtc_on_off_btn)

    @allure.step("Click on date")
    def click_on_date(self):
        self.click(date_option)
        self.sleep(1)

    @allure.step("select date")
    def select_date(self):
        self.click(date_selection)
        self.click(ok_btn_on_calender)

    @allure.step("click on confirm btn")
    def click_on_confirm_btn(self):
        self.click(confirm_btn)
        self.sleep(1)

    @allure.step("click on ok")
    def click_on_ok_btn(self):
        self.click(ok_btn)
        self.sleep(2)

    @allure.step("verify current date")
    def verify_current_date(self):
        current_date = time.strftime("%d %b %Y")
        date_option_text = self.get_attribute(date_option, "text")
        self.assert_equal(date_option_text, current_date)

    @allure.step("verify date changes reflection")
    def verify_date_changes_reflects(self):
        date_option_text = self.get_attribute(date_option, "text")
        self.assert_equal(date_option_text, "28 Feb 2022")

    @allure.step("verify lot count")
    def verify_lot_count(self, count):
        lot_count_text = self.get_attribute(lot_count, "text")
        self.assert_equal(lot_count_text, count)

    @allure.step("click on lot increase btn")
    def click_on_lot_increase_no(self):
        self.click(lot_increase_btn)
        self.sleep(1)

    @allure.step("Click on lot decrease btn")
    def click_on_lot_decrease_btn(self):
        self.click(lot_decrease_btn)
        self.sleep(1)

    @allure.step("verify search bar")
    def verify_search_bar(self):
        cari_btn_after_click_presence = self.is_element_visible(cari_btn_after_click)
        assert cari_btn_after_click_presence == True , f"Cari option not visible "

    @allure.step("Verify error message after exchange hour")
    def verify_error_message_after_exchange_market(self):
        error_message_text = self.get_attribute(market_close_message_lct, "text")
        self.assert_equal(error_message_text, market_close_message)

    @allure.step("verify beli plus minus btn")
    def verify_plus_minus_btn_beli(self):
        current_price = self.get_attribute(price_space, "text")
        self.click(price_plus_btn)
        self.click(price_minus_btn)
        price_after_plus_minus = self.get_attribute(price_space, "text")
        self.assert_equal(current_price, price_after_plus_minus, msg="Price is not same after plus minus")

    @allure.step("verify buying power exceed message")
    def verify_buying_power_exceed_msg(self):
        self.set_text(price_space, '1299090988')
        buy_power_exceed_msg_presence = self.is_element_visible(buy_power_exceed_msg)
        assert buy_power_exceed_msg_presence == True, f"price_exceed_msg_presence not visible "
        buy_power_exceed_msg_text = self.get_attribute(buy_power_exceed_msg, "text")
        self.assert_equal(buy_power_exceed_msg_text, "Nilai pembelian kamu melebihi trading limit.")

    def add_thousand_seprator(self, number):
        sep_number = f"{number :,}"
        return sep_number

    @allure.step("verify total beli amount")
    def verify_total_beli_amount(self):
        current_price = int((self.get_attribute(price_space, "text")))*100
        self.click_on_lot_increase_no()
        lot_value = self.get_attribute(lot_count, "text")
        beli_amount_without_sep = int(lot_value) * current_price
        beli_amount_with_sep = self.add_thousand_seprator(beli_amount_without_sep)
        amount_with_rp = self.get_attribute(total_beli_amount, "text")
        amount_without_rp = amount_with_rp[3:]
        self.assert_equal(str(beli_amount_with_sep), amount_without_rp)

    @allure.step("verify status on transaction page")
    def verify_status_on_transaction_page(self):
        status_text = self.get_attribute(status_on_trasction_page, "text")
        self.assert_equal(status_text, "SENDING")

    @allure.step("Take status from transaction page")
    def status_on_trans_page(self):
        return self.get_attribute(status_on_trasction_page, "text")

    @allure.step("verify lot harga jumlah values")
    def verify_lot_harga_jumlah_value(self):
        hagra_value_on_buy_pg = self.get_attribute(price_space, "text")
        lot_value = self.get_attribute(lot_count, "text")
        beli_with_rp = self.get_attribute(total_beli_amount, "text")
        beli_without_rp = beli_with_rp[3:]
        self.click(buy_btn_on_buy_page)
        self.assert_equal(self.add_thousand_seprator(int(hagra_value_on_buy_pg)), self.get_attribute(hagra_on_buy_conf_page, "text"))
        self.assert_equal(lot_value, self.get_attribute(lot_count_on_buy_conf_page, "text"))
        self.assert_equal(beli_without_rp, self.get_attribute(jumlah_on_buy_conf_page, "text"))

    @allure.step("verify gtc on ocp page")
    def verify_gtc_date_on_ocp(self):
        date_on_buy_page = self.get_attribute(gtc_date_on_buy_page, "text")
        self.click_on_buy_btn_on_buy_page()
        date_on_ocp_page = self.get_attribute(date_on_buy_conf_page, "text")
        self.assert_equal(date_on_buy_page, date_on_ocp_page)

    @allure.step("buy power on homepage")
    def buy_power_on_homepage(self):
        buying_power_home_page = self.get_attribute(Buying_Power_homepage, "text")
        return buying_power_home_page[13:]

    @allure.step("buy power on buy page")
    def buy_power_on_buy_page(self):
        buying_power_buy_page_text = self.get_attribute(buying_power_buy_page, "text")
        return buying_power_buy_page_text[3:]

    @allure.step("verify bit amount with beli di harga")
    def verify_bit_amount_with_beli_di_harga(self):
        beli_da_hagra = self.get_attribute(price_space, "text")
        bid_amount_text = self.get_attribute(bid_amount, "text")
        self.assert_equal(self.add_thousand_seprator(int(beli_da_hagra)), bid_amount_text)

    @allure.step("message after buy again stock on same price")
    def message_after_buy_again_on_same_price(self):
        pass










