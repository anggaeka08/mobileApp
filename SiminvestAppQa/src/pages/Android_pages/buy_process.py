from selenium.common.exceptions import InvalidElementStateException
from SiminvestAppQa.src.utilities.requestUtilities import RequestsUtilities
from datetime import datetime
request_utilities = RequestsUtilities()
from SiminvestAppQa.src.data.userData import user_data
from SiminvestAppQa.src.pages.Android_pages.login_page import LoginPage
from SiminvestAppQa.src.pages.Android_pages.home_page import HomePage
import time
import allure
from datetime import timedelta
from datetime import date
import logging as logger
from  numerize import numerize

#buy process locators
sell_btn = 'SDPPageSellBtn'
buy_btn_with_sell='SDPPageBuyBtn'
buy_btn_without_sell='SDPBeliBtn'
stock_name_buy_page= 'SellPageStockName'
#refferal page locators
refferal_page_heading = '//android.widget.TextView[@index="1"]'
refferal_page_heading_valstock_name_buy_pageue = 'Punya Kode Referral?\nBanyak teman semakin untung!?'
refferal_code_edit_box = '//android.widget.EditText[@text="Kode Referral"]'
selanjutnya = '//android.widget.TextView[@text="Selanjutnya"]'
#buy page locators
buy_page_header = 'SellPageHeader'
buy_btn_on_buy_page = 'SellPageSellBtn'
disable_buy_btn = '//android.widget.TextView[@text="Beli"]'
gtc_area = 'SellPageGTCText'
lot_area = 'SellPageLotValue'
cancel_btn = 'BuySellConfBetalBtn'
gtc_on_off_btn = 'SellPageGTCEnableBtn'
date_option = 'BuyPageGTCCalender'
date_value = '//android.view.ViewGroup[@content-desc="BuyPageGTCCalender"]/android.view.ViewGroup/android.widget.TextView'
date_selection = '30 June 2022'
ok_btn_on_calender = "//*[@text='OK']"
cancel_btn_on_calender = "//*[@text='CANCEL']"
next_arrow = '//android.widget.ImageButton[@content-desc="Next month"]'
provious_arrow = '//android.widget.ImageButton[@content-desc="Previous month"]'
#year_selection = "//android.widget.TextView[@resource-id='android:id/date_picker_header_year']"
year_selection = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.DatePicker/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[1]"
year_list = "//*[@text='2026']"
date_pick="//*[@resource-id='android:id/date_picker_header_date']"
confirm_btn = 'BuySellConfSetujuBtn'
ok_btn = 'BuyTransactionMarketOpenButton'
ok_btn_close = 'BuyTransactionMarketCloseButton'
lot_count = 'SellPageLotValue'
lot_increase_btn = 'SellPageLotPlus'
lot_decrease_btn = 'SellPageLotMinus'
cari_btn_after_click ='StockSearch'
market_close_message_lct = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView[1]'
market_close_message = 'Bursa Tidak Beroperasi'
price_minus_btn = 'SellPageHargaMinus'
price_plus_btn = 'SellPageHargaPlus'
price_space = 'SellPageHargaValue'
buy_power_exceed_msg = '//android.widget.TextView[@text="Nilai pembelian kamu melebihi trading limit."]'
total_beli_amount = '//android.view.ViewGroup[2]/android.widget.TextView[6]'
status_on_trasction_page = 'status_label_0'
lot_count_on_buy_conf_page = 'BuyConfLotValue'
hagra_on_buy_conf_page = 'BuyConfHargaValue'
jumlah_on_buy_conf_page = 'BuyConfJumlahValue'
date_on_buy_conf_page = 'BuyConfGoodTillDate'
gtc_date_on_buy_page = '//android.view.ViewGroup[@content-desc="BuyPageGTCCalender"]/android.view.ViewGroup/android.widget.TextView'
Buying_Power_homepage='HomepagebuyPower'
buying_power_buy_page = '//android.view.ViewGroup[2]/android.widget.TextView[4]'
bid_amount = '//android.view.ViewGroup[@content-desc="SellPageOrderBookTextBid0"]/android.widget.TextView'
ask_amount = '//android.view.ViewGroup[@content-desc="SellPageOrderBookTextAsk0"]/android.widget.TextView'
confirmation_page_header = 'Konfirmasi PembelianHeader'
confirmation_page_sell_header = 'Konfirmasi PenjualanHeader'
stock_code_on_buy = 'SellPageStockCode'
stock_code_on_cnf = 'BuySellConfSahamValue'
stock_code_text = 'BuySellConfSahamText'
lot_text = 'BuyConfLotText'
harga_text = 'BuyConfHargaText'
jumlah_text = 'BuyConfJumlahText'
fee_msg = 'FeeDeductionMsgText'
fee_msg_text = '*Fee akan dipotong dari trading balance kamu di akhir hari bursa'
total_jumlah_sell = 'SellPageTotalJualValue'
sell_pl = 'SellPagePLValue'
lot_value_sell_cnf= 'SellConfLotValue'
harga_value_sell_cnf ='SellConfHargaValue'
jumlah_value_sell_cnf = 'SellConfJumlahValue'
pl_on_cnf = 'SellConfPLTextValue'
gtc_sell_cnf = 'SellConfGoodTillDate'
fee_msg_sell_cnf = 'SellFeeDeductionMsgText'
Buying_Power="HomepagebuyPower"
stock_price_ele = 'SellPageStockPrice'
stock_code_l='stockCode_0'
exchange_notification= '//android.widget.TextView[contains(@text, "Bursa Tidak Beroperasi")]'
saham_tab = 'Saham_tab'
transaction_type_tran = 'transactionType_0'
stock_code_on_portfolio = 'PortPageEntry0Code'
transaction_entry ='order_list_entry_0'
transaction_entry_2 ='order_list_entry_1'
stock_code_oder = "//android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.TextView[1][@index='0']"
stock_name_oder = "//android.view.ViewGroup[3]/android.widget.TextView[2][@index='1']"
harga_order = "//android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[9][@index='13']"
lot_order = "//android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[11][@index='15']"
order_id = "//android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[3][@index='6']"

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
        self.sleep(4)
        self.click_on_stock_code()
        #self.verify_sdp_page()

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
        #self.assert_equal(refferal_page_heading_text, refferal_page_heading_value)
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
       # gtc_area_present = self.is_element_visible(gtc_area)
       # assert gtc_area_present == True, f"gtc_area Should be present"
        lot_area_present = self.is_element_visible(lot_area)
        assert lot_area_present == True, f"lot_area Should be present"

    @allure.step("Verify buy page after disable buy btn")
    def verify_buy_page_after_disable_buy_btn(self):
        buy_page_header_present = self.is_element_visible(buy_page_header)
        assert buy_page_header_present == True, f"buy_page_header Should be present"
        #gtc_area_present = self.is_element_visible(gtc_area)
        #assert gtc_area_present == True, f"gtc_area Should be present"
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

    @allure.step("click on ok after market close")
    def click_on_ok_btn_after_market_close(self):
        self.click(ok_btn_close)
        self.sleep(2)

    @allure.step("verify current date")
    def verify_current_date(self):
        current_date = time.strftime("%d %b %Y")
        date_option_text = self.get_attribute(date_value, "text")
        self.assert_equal(date_option_text, current_date)

    @allure.step("verify date changes reflection")
    def verify_date_changes_reflects(self):
        date_option_text = self.get_attribute(date_value, "text")
        self.assert_equal(date_option_text, "30 Jun 2022")

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
        assert buy_power_exceed_msg_presence == True, f"price_exceed_msg_presence visible "
        buy_power_exceed_msg_text = self.get_attribute(buy_power_exceed_msg, "text")
        self.assert_equal(buy_power_exceed_msg_text, "Nilai pembelian kamu melebihi trading limit.")
        self.click_disabled_buy_btn()
        buy_page_header_present = self.is_element_visible(buy_page_header)
        assert buy_page_header_present == True, f"buy_page_header Should be present"


    def add_thousand_seprator(self, number):
        sep_number = f"{number :,}"
        return sep_number

    @allure.step("verify total beli amount")
    def verify_total_beli_amount(self):
        current_price = int((self.get_attribute(price_space, "text")).replace(',', ''))*100
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
        hagra_value_on_buy_pg = (self.get_attribute(price_space, "text")).replace(',','')
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
        beli_da_hagra = (self.get_attribute(price_space, "text")).replace(',', '')
        ask_amount_text = self.get_attribute(ask_amount, "text")
        self.assert_equal(self.add_thousand_seprator(int(beli_da_hagra)), ask_amount_text)

    @allure.step("Verify ask value reflect in beli de harga")
    def verify_ask_value_reflect_in_beli_de_harga(self):
        ask_amount_text = self.get_attribute(ask_amount, "text")
        self.click(ask_amount)
        beli_da_hagra = self.get_attribute(price_space, "text")
        self.assert_equal(self.add_thousand_seprator(int(beli_da_hagra)), ask_amount_text)

    @allure.step("message after buy again stock on same price")
    def message_after_buy_again_on_same_price(self):
        pass

    @allure.step("click disabled buy btn")
    def click_disabled_buy_btn(self):
        self.click(disable_buy_btn)

    @allure.step("Verify redirection to confirmation page")
    def verify_redirection_to_confirmation_page(self):
        self.assert_equal(self.is_element_visible(confirmation_page_header), True)

    @allure.step("Scroll right to left")
    def scroll_right_to_left(self):
        self.scroll_screen(start_x=870, start_y=1114, end_x=203, end_y=1114, duration=10000)
        self.sleep(2)

    @allure.step("Scroll left to right")
    def scroll_left_to_right(self):
        self.scroll_screen(start_x=203, start_y=1114, end_x=870, end_y=1114, duration=10000)
        self.sleep(2)


    @allure.step("verify default date after tap on gtc option")
    def verify_default_date_after_tap_on_gtc_option(self):
        today = date.today()
        d4_locator = today.strftime("%d %B %Y")
        d4 = today.strftime("%d %b %Y")
        date_on_gtc = self.get_attribute(date_value, 'text')
        self.assert_equal(date_on_gtc, d4)
        self.click(date_value)
        self.sleep(1)
        self.assert_equal(self.is_element_visible(d4_locator), True)
        self.click(next_arrow)
        self.sleep(2)
        self.assert_equal(self.is_element_visible(d4_locator), False)
        self.click(provious_arrow)
        self.sleep(2)
        self.assert_equal(self.is_element_visible(d4_locator), True)
        self.click(year_selection)
        self.sleep(1)
        self.assert_equal(self.is_element_visible(year_list), True)
        self.click(cancel_btn_on_calender)
        self.sleep(1)
        self.verify_buy_page()
        self.click(date_value)
        self.sleep(1)
        self.click(year_selection)
        self.sleep(1)
        self.click(ok_btn_on_calender)
        self.sleep(1)
        self.verify_buy_page()
        self.click(date_value)
        self.sleep(1)
        self.click(year_selection)
        self.sleep(1)
        self.click("//*[@text='2027']")
        self.sleep(1)
        d5 = today.strftime("%d %b 2027")
        print(d5)
        d5_locator = today.strftime("%d %B 2027")
        self.click(ok_btn_on_calender)
        self.sleep(1)
        date_on_gtc_2 = self.get_attribute(date_value, 'text')
        self.assert_equal(date_on_gtc_2, d5)
        self.click(date_value)
        self.sleep(1)
        self.click(cancel_btn_on_calender)
        self.sleep(1)
        self.verify_buy_page()
        self.click(date_value)
        self.scroll_right_to_left()
        self.scroll_left_to_right()
        self.assert_equal(self.is_element_visible(d5_locator), True)
        yesterday = today - timedelta(days=1)
        yesterday_date = yesterday.strftime("%d %B 2027")
        self.click(yesterday_date)
        self.assert_equal(self.is_element_visible(date_value), False)
        try:
            #self.tap_by_coordinates(x=635, y=1860)
            self.click("//*[@text='OK']")
        except InvalidElementStateException as E:
            pass
        self.sleep(2)
        #self.assert_equal(self.is_element_visible(date_value), True)

    @allure.step("Validate order confirmation page for buy")
    def validate_order_confirmation_page_for_buy(self):
        stock_code_buy = self.get_attribute(stock_code_on_buy, 'text')
        harga_value_buy = self.get_attribute(price_space, 'text')
        lot_value_buy = self.get_attribute(lot_area, 'text')
        amount_with_rp = self.get_attribute(total_beli_amount, "text")
        amount_without_rp_buy = amount_with_rp[3:]
       # self.click(gtc_on_off_btn)
        #gtc_date_buy = self.get_attribute(gtc_date_on_buy_page, 'text')
        self.click(buy_btn_on_buy_page)
        self.sleep(1)
        self.assert_equal(self.is_element_visible(confirmation_page_header), True)
        stock_code_cnf = self.get_attribute(stock_code_on_cnf, 'text')
        lot_cnf = self.get_attribute(lot_count_on_buy_conf_page, 'text')
        harga_cnf = self.get_attribute(hagra_on_buy_conf_page, 'text')
        jumlah_conf_page = self.get_attribute(jumlah_on_buy_conf_page, 'text')
        #gtc_on_cnf = self.get_attribute(date_on_buy_conf_page, 'text')
        self.assert_equal(stock_code_buy, stock_code_cnf)
        self.assert_equal(harga_value_buy, harga_cnf)
        self.assert_equal(lot_value_buy, lot_cnf)
        self.assert_equal(amount_without_rp_buy, jumlah_conf_page)
        self.assert_equal(self.is_element_visible(stock_code_text), True)
        self.assert_equal(self.is_element_visible(lot_text), True)
        self.assert_equal(self.is_element_visible(harga_text), True)
        self.assert_equal(self.is_element_visible(jumlah_text), True)
        self.assert_equal(self.get_attribute(fee_msg, 'text'), fee_msg_text)
        #self.assert_equal(gtc_on_cnf, gtc_date_buy)
        self.click(cancel_btn)
        self.verify_buy_page()
        #self.click(gtc_on_off_btn)
        self.click(buy_btn_on_buy_page)
        try:
            self.tap_by_coordinates(x=635, y=1860)
        except InvalidElementStateException as E:
            pass
        self.sleep(2)
        self.assert_equal(self.is_element_visible(stock_code_text), True)
        self.click(confirm_btn)
        self.sleep(5)
        if self.is_element_visible(ok_btn_close) == True:
            self.go_back()
        else :
            self.assert_equal(self.is_element_visible(ok_btn), True)
            self.go_back()
        self.sleep(2)
        self.verify_buy_page()
        #self.go_back()
        self.sleep(2)
        self.go_back()
        # self.click(sell_btn)

    @allure.step("Validate order confirmation page for sell")
    def validate_order_confirmation_page_for_sell(self):
        self.click(sell_btn)
        stock_code_buy = self.get_attribute(stock_code_on_buy, 'text')
        harga_value_buy = self.get_attribute(price_space, 'text')
        lot_value_buy = self.get_attribute(lot_area, 'text')
        total_jumlah_value_Sell_with_rp = self.get_attribute(total_jumlah_sell, "text")
        total_jumlah_value_Sell=total_jumlah_value_Sell_with_rp[3:]
        pl_value_sell = self.get_attribute(sell_pl, 'text')
        #self.click(gtc_on_off_btn)
       # gtc_date_buy = self.get_attribute(gtc_date_on_buy_page, 'text')
        self.click(buy_btn_on_buy_page)
        self.sleep(1)
        self.assert_equal(self.is_element_visible(confirmation_page_sell_header), True)
        stock_code_cnf = self.get_attribute(stock_code_on_cnf, 'text')
        lot_cnf = self.get_attribute(lot_value_sell_cnf, 'text')
        harga_cnf = self.get_attribute(harga_value_sell_cnf, 'text')
        jumlah_conf_page = self.get_attribute(jumlah_value_sell_cnf, 'text')
        #gtc_on_cnf = self.get_attribute(gtc_sell_cnf, 'text')
        pl_value_cnf = self.get_attribute(pl_on_cnf, 'text')
        self.assert_equal(stock_code_buy, stock_code_cnf)
        self.assert_equal(harga_value_buy, harga_cnf)
        self.assert_equal(lot_value_buy, lot_cnf)
        self.assert_equal(pl_value_cnf, pl_value_sell)
        self.assert_equal(total_jumlah_value_Sell, jumlah_conf_page)
        self.assert_equal(self.is_element_visible(stock_code_text), True)
        self.assert_equal(self.get_attribute(fee_msg_sell_cnf, 'text'), fee_msg_text)
        #self.assert_equal(gtc_on_cnf, gtc_date_buy)
        self.click(cancel_btn)
        #self.click(gtc_on_off_btn)
        self.click(buy_btn_on_buy_page)
        try:
            self.tap_by_coordinates(x=635, y=1860)
        except InvalidElementStateException as E:
            pass
        self.sleep(2)
        self.assert_equal(self.is_element_visible(stock_code_text), True)
        self.click(confirm_btn)
        self.sleep(5)
        #self.assert_equal(self.is_element_visible('//*[@text="OK"]'), True)
        if self.is_element_visible(ok_btn_close) == True:
            pass
        else :
            self.assert_equal(self.is_element_visible(ok_btn), True)

    @allure.step("Validate all api data")
    def validate_all_api_data(self):
        api_value=[]
        token_value = self.login()
        token = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJpWlYzdUJkTkJyTDA4dVIzQUR2bmg4akdTdHNkSHpQVSIsInN1YiI6IlNpbWFzSW52ZXN0In0.Kj31bgBrbc94NaUDKWgbx-N4ZBQNFsrZBmF7xtZ4hNo"}
        token['Authorization'] = 'Bearer ' + token_value
        sdp_rs = request_utilities.get(base_url='https://api.siminvest.co.id/api/v1/pcs/v2/product/equity',endpoint='/ACES', headers=token,expected_status_code=200)
        vol = str(numerize.numerize(int(sdp_rs['vol'])))
        val = str(numerize.numerize(int(sdp_rs['val'])))
        #new_value = vol[:2]+"."+vol[2:4] +" Jt"
        new_value = vol.replace('M', ' Jt')
        logger.info(new_value)
        new_value_val = vol.replace('M', ' Jt')
        logger.info(new_value_val)
        api_value.append(sdp_rs['open'])
        api_value.append(sdp_rs['high'])
        api_value.append(new_value)
        api_value.append(sdp_rs['close'])
        api_value.append(sdp_rs['low'])
        api_value.append(new_value_val)
        api_value.append(sdp_rs['avg'])
        api_value.append(sdp_rs['buy_f_vol'])
        api_value.append(sdp_rs['sell_f_vol'])
        return api_value

    @allure.step("Verify default lot value stock code and name on sbp page")
    def verify_default_lot_value_stock_code_and_name_on_sbp(self):
        lot_value_buy = self.get_attribute(lot_area, 'text')
        self.assert_equal(int(lot_value_buy), 1)
        self.assert_equal(self.is_element_visible(stock_code_on_buy), True)
        self.assert_equal(self.is_element_visible(stock_name_buy_page), True)


    @allure.step("Verify sbp numerical and mathematical values")
    def verify_sbp_numerical_and_mathematical_values(self):
        # buying_power_with_buy = self.get_attribute(Buying_Power, 'text')
        # buying_power = (buying_power_with_buy[16:]).replace(',', '')
        self.click_global_search_btn_and_saerch_stock('ACES')
        self.sleep(3)
        self.click_on_stock_code()
        self.click_on_buy_btn()
        stock_price = self.get_attribute(stock_price_ele, 'text')
        price_beli = self.get_attribute(price_space, 'text')
        self.assert_equal(stock_price, price_beli)
        #buying_power_on_buy_page = (self.buy_power_on_buy_page()).replace(',','')
        # self.assert_equal(buying_power, buying_power_on_buy_page)
        lot_value_buy = self.get_attribute(lot_area, 'text')
        self.assert_equal(int(lot_value_buy), 1)
        self.verify_total_beli_amount()
        """value_on_sbp = []
        for i in range(2,20,2):
            value = self.get_attribute(f'SDPPageText{i}', 'text')
            value_on_sbp.append(value)
        API_data = self.validate_all_api_data()
        for i in range(9):
            self.assert_equal(value_on_sbp[i], str(API_data[i]))"""

    @allure.step("Verify market timing")
    def verify_market_timing(self, stock_code, transaction_type):
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        logger.info(f"Current Time = {current_time}")
        if (current_time >= '7:30' or current_time <= '15:15'):
            self.assert_equal(self.is_element_visible(exchange_notification), False)
            logger.info("within time")
            self.click_on_ok_btn()
            self.assert_equal(self.is_element_visible(saham_tab), True)
            self.assert_equal(self.get_attribute(transaction_type_tran, 'text'), transaction_type)
            self.assert_equal(self.get_attribute(stock_code_l, 'text'), stock_code)
        else:
            logger.info("Out of time")
            self.assert_equal(self.is_element_visible(exchange_notification), True)
            self.click_on_ok_btn_after_market_close()

    @allure.step("Redirection from portfolio to sdp")
    def redirection_from_portfolio_to_sdp(self):
        self.click(f'PortPageEntry0')
        self.sleep(2)
        self.verify_sdp_page()

    @allure.step("Click on sell btn")
    def click_on_sell_btn(self):
        self.click(sell_btn)
        self.sleep(1)

    @allure.step("Get Stock code on portfolio page")
    def get_stock_code_on_portfolio_page(self):
        return self.get_attribute(stock_code_on_portfolio, 'text')

    @allure.step("Data comparison between buy page and OrderDP")
    def data_comparison_between_buy_page_and_OrderDP(self, stock_code):
        stock_code_b = self.get_attribute(stock_code_on_buy, 'text')
        stock_full_name_b = self.get_attribute(stock_name_buy_page, 'text')
        harga_b = self.get_attribute(price_space, 'text')
        lot_value_b = self.get_attribute(lot_area, 'text')
        self.click_on_buy_btn_on_buy_page()
        self.click_on_confirm_btn()
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        logger.info(f"Current Time = {current_time}")
        if (current_time >= '7:30'  or current_time <= '15:15'):
            self.assert_equal(self.is_element_visible(exchange_notification), False)
            logger.info("within time")
            self.click_on_ok_btn()
            self.assert_equal(self.is_element_visible(saham_tab), True)
            self.assert_equal(self.get_attribute(transaction_type_tran, 'text'), 'BELI')
            self.assert_equal(self.get_attribute(stock_code_l, 'text'), stock_code)
            self.click(transaction_entry)
            self.sleep(3)
            stock_code_o = self.get_attribute(stock_code_oder, 'text')
            stock_full_name_o = self.get_attribute(stock_name_oder, 'text')
            harga_o = self.get_attribute(harga_order, 'text')
            harga_without_rp = harga_o[3:]
            lot_value_o = self.get_attribute(lot_order, 'text')
            self.assert_equal(stock_code_b, stock_code_o)
            self.assert_equal(stock_full_name_b, stock_full_name_o)
            self.assert_equal(harga_b, harga_without_rp)
            self.assert_equal(lot_value_b, lot_value_o)
        else:
            logger.info("Out of time")
            self.assert_equal(self.is_element_visible(exchange_notification), True)
            self.click_on_ok_btn_after_market_close()

    @allure.step("verify lot limit in buy process")
    def verify_lot_limit_in_buy_process(self):
        self.update_text(lot_count, '5000000')
        self.sleep(2)
        lot_value = self.get_attribute(lot_count, 'text')
        self.assert_equal(lot_value, '50,000')
        self.update_text(lot_count, '1')

    @allure.step("API data comparison")
    def api_data_comparison(self):
        self.verify_buy_page()
        stock_code_b = self.get_attribute(stock_code_on_buy, 'text')
        harga_b = self.get_attribute(price_space, 'text')
        lot_value_b = self.get_attribute(lot_area, 'text')
        beli_with_rp = self.get_attribute(total_beli_amount, "text")
        beli_without_rp = beli_with_rp[3:]
        self.click_on_buy_btn_on_buy_page()
        self.click_on_confirm_btn()
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        logger.info(f"Current Time = {current_time}")
        if (current_time >= '7:30' and current_time <= '10:00') or (
                current_time >= '12:00' and current_time <= '15:00'):
            self.assert_equal(self.is_element_visible(exchange_notification), False)
            logger.info("within time")
            self.click_on_ok_btn()
            self.assert_equal(self.is_element_visible(saham_tab), True)
            self.assert_equal(self.get_attribute(transaction_type_tran, 'text'), 'BELI')
            self.assert_equal(self.get_attribute(stock_code_l, 'text'), stock_code_b)
            self.click(transaction_entry)
            self.sleep(3)
            token_value = self.login()
            token = {
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJpWlYzdUJkTkJyTDA4dVIzQUR2bmg4akdTdHNkSHpQVSIsInN1YiI6IlNpbWFzSW52ZXN0In0.Kj31bgBrbc94NaUDKWgbx-N4ZBQNFsrZBmF7xtZ4hNo"}
            token['Authorization'] = 'Bearer ' + token_value
            order_details_rs = request_utilities.get(base_url='https://stg-api.siminvest.co.id/',endpoint='api/v1/oms/equities/orders/53615', headers=token, expected_status_code=200)
            self.assert_equal(stock_code_b, order_details_rs['data'][0]['code'])
            self.assert_equal(harga_b, str(order_details_rs['data'][0]['price']))
            self.assert_equal(lot_value_b, str(order_details_rs['data'][0]['order_lot']))
            self.assert_equal(beli_without_rp.replace(',',''), str(order_details_rs['data'][0]['order_amount']))
        else:
            logger.info("Out of time")
            self.assert_equal(self.is_element_visible(exchange_notification), True)
            self.click_on_ok_btn_after_market_close()

    @allure.step("Order Id comparison with different orders")
    def order_id_comparison_with_different_orders(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        logger.info(f"Current Time = {current_time}")
        if (current_time >= '7:30' or current_time <= '15:15'):
            self.assert_equal(self.is_element_visible(exchange_notification), False)
            logger.info("within time")
            self.click_on_ok_btn()
            self.click(transaction_entry)
            order_id_1 = self.get_attribute(order_id, 'text')
            self.go_back()
            self.sleep(2)
            self.click(transaction_entry_2)
            order_id_2 = self.get_attribute(order_id, 'text')
            self.assert_not_equal(order_id_1, order_id_2)
        else:
            logger.info("Out of time")
            self.assert_equal(self.is_element_visible(exchange_notification), True)
            self.click_on_ok_btn_after_market_close()

    @allure.step("price value decrease")
    def price_value_decrease(self):
        self.click(price_minus_btn)