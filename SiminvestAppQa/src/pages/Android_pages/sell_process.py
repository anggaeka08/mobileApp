from SiminvestAppQa.src.data.userData import user_data
from SiminvestAppQa.src.pages.Android_pages.buy_process import BuyProcess
import allure
import logging as logger

jaul_btn = 'SDPPageSellBtn'
jaul_btn_on_sell = 'SellPageSellBtn'
Setuju_btn = 'BuySellConfSetujuBtn'
Batal_btn = 'BuySellConfBetalBtn'
bs_on_trans = 'OrderlistEntry0BS'
bs_on_gtc = 'GTCListEntry0BS'
GTC_list_tab = 'TransactionPageSahamHeader3'
status_on_gtc_page = 'GTCListEntry0BS'
lot_count = 'SellPageLotValue'
lot_decrease_btn = 'SellPageLotMinus'
available_lot = 'SellPageTotalLotValue'
bit_amount = '//android.view.ViewGroup[@content-desc="SellPageOrderBookTextBid0"]/android.widget.TextView'
ask_amount = '//android.view.ViewGroup[@content-desc="SellPageOrderBookTextAsk0"]/android.widget.TextView'
price_space = 'SellPageHargaValue'
total_beli_amount = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView[6]'
total_jual_amount = 'SellPageTotalJualValue'
buy_btn_on_buy_page = 'SellPageSellBtn'
hagra_on_sell_conf_page = 'SellConfHargaValue'
lot_count_on_sell_conf_page= 'SellConfLotValue'
jumlah_on_sell_conf_page = 'SellConfJumlahValue'
sell_page_header= "SellPageHeader"
sell_page_stock_code= "SellPageStockCode"
transaction_entry ='order_list_entry_0'
od_stock_code = '//android.view.ViewGroup[3]/android.widget.TextView[1]'
od_harga_text = "//android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[9]"
od_lotDip_text ="//android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[11]"
od_status_text ='//android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[4]/android.widget.TextView'


class SellProcess(BuyProcess):

    @allure.step("ope and verify portfolio page")
    def open_and_verify_portfolio(self, number):
        self.click_mulai_sekarang()
        self.type_mobile_no(number)
        self.click_selanjutnya()
        self.enter_otp(user_data['valid_otp'])
        self.enter_pin()
        self.close_home_page_banner()
        self.verify_home_page_reg_user()
        self.click_on_portfolio_btn()
        self.verify_portfolio_for_kyc_user()

    @allure.step("Click on jual button on sdp page")
    def click_on_jual_btn(self):
        self.click(jaul_btn)

    @allure.step("Click on jual button on sell page")
    def click_on_jual_btn_on_sell_page(self):
        self.click(jaul_btn_on_sell)

    @allure.step("click on setuju btn")
    def click_on_setuju(self):
        self.click(Setuju_btn)

    @allure.step("click on batal btn")
    def click_on_batal(self):
        self.click(Batal_btn)

    @allure.step("Verify transaction for sell")
    def verify_transaction_page_for_sell(self):
        self.sleep(4)
        self.assert_equal(self.get_attribute(bs_on_trans, "text"), 'SELL')

    @allure.step("Verify transaction for sell on gtc page")
    def verify_transaction_page_for_sell_on_gtc_page(self):
        self.assert_equal(self.get_attribute(bs_on_gtc, "text"), 'SELL')

    @allure.step("Go too GTC tab")
    def go_to_gtc_tab_on_trans_page(self):
        self.click(GTC_list_tab)

    @allure.step("Check initial value of lot")
    def check_initial_value_of_lot(self, value):
        self.assert_equal(self.get_attribute(lot_count, "text"), value)

    @allure.step("Verify lot value change default when change it overlimit")
    def verify_lot_value_change_default(self):
        available_lot_value = self.get_attribute(available_lot, "text")
        enter_new_value = int(available_lot_value) + 5
        self.set_text(lot_count, enter_new_value)
        self.sleep(3)
        self.assert_equal(self.get_attribute(lot_count, "text"), available_lot_value)

    @allure.step("Verify error message for sell stock exceed limit")
    def verify_error_message_for_sell_stock_exceed_limit(self):
        pass

    @allure.step("Verify value change in harga accord. to click")
    def verify_value_change_in_harga_accord_to_click(self):
        self.click(bit_amount)
        self.sleep(2)
        self.assert_equal(self.add_thousand_seprator(int((self.get_attribute(price_space, "text").replace(',','')))), self.get_attribute(bit_amount, "text"))
        self.click(ask_amount)
        self.sleep(2)
        self.assert_equal(self.add_thousand_seprator(int((self.get_attribute(price_space, "text").replace(',','')))), self.get_attribute(ask_amount, "text"))

    @allure.step("verify lot harga jumlah values")
    def verify_lot_harga_jumlah_value_sell(self):
        hagra_value_on_buy_pg = (self.get_attribute(price_space, "text")).replace(',','')
        lot_value = self.get_attribute(lot_count, "text")
        beli_with_rp = self.get_attribute(total_beli_amount, "text")
        beli_without_rp = beli_with_rp[3:]
        self.click(buy_btn_on_buy_page)
        self.assert_equal(self.add_thousand_seprator(int(hagra_value_on_buy_pg)), self.get_attribute(hagra_on_sell_conf_page, "text"))
        self.assert_equal(lot_value, self.get_attribute(lot_count_on_sell_conf_page, "text"))
        self.assert_equal(beli_without_rp, self.get_attribute(jumlah_on_sell_conf_page, "text"))

    @allure.step("Verify positive flow of sell and data compare from odp")
    def verify_positive_flow_of_sell_and_data_compare_from_odp(self):
        self.click_on_portfolio_btn()
        stock_code = self.get_stock_code_on_portfolio_page()
        self.redirection_from_portfolio_to_sdp()
        self.check_for_sell_btn()
        self.check_for_buy_btn()
        self.click_on_sell_btn()
        self.sleep(2)
        stock_code_sell_page = self.get_attribute(sell_page_stock_code, 'text')
        hargavalue_sell_page = self.get_attribute( price_space, 'text')
        lot_value_sell_page = self.get_attribute( lot_count, 'text')
        assert self.is_element_visible(sell_page_header) == True, f"sell_page_header Should be present"
        assert self.is_element_visible(jaul_btn_on_sell) == True, f"jual_btn_on_sell_page Should be present"
        self.verify_lot_value_change_default()
        self.update_text(lot_count, "1")
        self.click_on_jual_btn_on_sell_page()
        self.click_on_setuju()
        self.verify_market_timing(stock_code, 'JUAL')
        self.sleep(2)
        self.click(transaction_entry)
        stock_code_odp= self.get_attribute(od_stock_code, 'text')
        harga_odp = self.get_attribute(od_harga_text, 'text')
        harga_without_rp = harga_odp[3:]
        lot_value_odp = self.get_attribute(od_lotDip_text, 'text')
        status= self.get_attribute(od_status_text,'text')
        self.assert_equal(stock_code_sell_page, stock_code_odp)
        self.assert_equal(hargavalue_sell_page, harga_without_rp)
        self.assert_equal(lot_value_sell_page, lot_value_odp)
        self.assert_equal(status, "SENDING")