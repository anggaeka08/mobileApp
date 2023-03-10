from selenium.common.exceptions import InvalidElementStateException
from datetime import datetime
from SiminvestAppQa.src.data.userData import user_data
from SiminvestAppQa.src.pages.Android_pages.buy_process import BuyProcess
from SiminvestAppQa.src.pages.Android_pages.home_page import HomePage
import time
import allure
from datetime import timedelta
from datetime import date
import logging as logger
from  numerize import numerize

#loactors
fo_header = 'FastBSHeader'
fo_close = '//android.view.ViewGroup[@content-desc="FastBSClose"]/android.widget.ImageView'
fo_stock_code = 'FastBSStockCode'
fo_stock_name = 'FastBSStockName'
fo_price = 'FastBSStockPrice'
fo_pl = 'FastBSStockPL'
fo_harga_text = 'FastBSHarga'
fo_hagra_decrease  = 'FastBSHargaDecreaseImage'
fo_harga_increase = 'FastBSHargaValueIncrease'
fo_hagra_value = 'FastBSHargaValue'
fo_lot_text = 'FastBSLot'
fo_lot_decrease = 'FastBSLotDecreaseImg'
fo_lot_increase = 'FastBSLotIncreaseImg'
fo_lot_value = 'FastBSLotValue'
fo_max_buy_text = 'FastBSMaxText'
fo_limit = '//android.widget.TextView[@text = "Limit"]'
fo_limit_btn = '//android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[5]/android.widget.ImageView'
fo_cash = '//android.widget.TextView[@text = "Cash"]'
fo_cash_btn_enable = '//android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[6]/android.widget.ImageView'
fo_cash_btn_disable = '//android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[6]/android.widget.ImageView'
fo_total_beli_text = 'FastBSTotalText'
fo_total_beli_value = 'FastBSTotalValue'
fo_btn = 'FastBSButtonText'
fo_jual_semua = '//android.widget.TextView[@text = "Jual Semua"]'
#confirm page loactors for buy
fo_conf_header = 'FastBSConfHeader'
fo_saham_text  = 'FastBSConfSaham'
fo_saham_value = 'FastBSConfSahamValue'
fo_conf_lot_text = 'FastBSConfLot'
fo_conf_lot_value ='FastBSConfLotValue'
fo_conf_harga_text = 'FastBSConfHarga'
fo_conf_harga_value = 'FastBSConfHargaValue'
fo_conf_jumlah_text = 'FastBSConfJumlah'
fo_conf_jumlah_value = 'FastBSConfJumlahValue'
fo_conf_error_msg =  'FastBSConfFeeMsg'
fo_conf_batal_btn = 'FastBSConfBatal'
fo_conf_setuju = 'FastBSConfSetuju'
#confirma page locator for sell
fo_conf_lot_text_s = 'FastBSConfLot1'
fo_conf_lot_value_s ='FastBSConfLotValue1'
fo_conf_harga_text_s = 'FastBSConfHarga1'
fo_conf_harga_value_s = 'FastBSConfHargaValue1'
fo_conf_jumlah_text_S = 'FastBSConfJumlah1'
fo_conf_jumlah_value_s = 'FastBSConfJumlahValue1'
fo_pl_text = '(//android.widget.TextView[@content-desc="FastBSConfProfitLoss1"])[1]'
fo_pl_value = '(//android.widget.TextView[@content-desc="FastBSConfProfitLoss1"])[2]'
outside_halfcard = '//android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup'
saham_tab = 'Saham_tab'
transaction_type = 'transactionType_0'
stock_code_l='stockCode_0'
trading_limit = 'FastBSErrorText'
trading_limit_text = 'Nilai pembelian kamu melebihi trading limit.'
homepage_tab = '//android.widget.TextView[@text = "Home"]'
home_rdn = 'HomePageRdnValue'
home_buying_power = 'HomepagebuyPower'



class FastOrder(BuyProcess):

    @allure.step("Scroll to open fastOrder")
    def scroll_to_open_fastOrder_buy(self):
        self.sleep(2)
        self.scroll_screen(start_x=72, start_y=1656, end_x=887, end_y=1656, duration=5000)
        self.sleep(2)

    @allure.step("Scroll to open fastOrder")
    def scroll_to_open_fastOrder_sell(self):
        self.sleep(2)
        second_coordinate= self.get_attribute('HomepageWLStockPrice1', 'bounds')
        lst_1 = second_coordinate.split(',')
        fist_x = int(lst_1[0][1:])
        fist_y = int(lst_1[1][0:4])
        fist_coordinate= self.get_attribute('HomepageWLStockCode1', 'bounds')
        lst_2 = fist_coordinate.split(',')
        sec_x = int(lst_2[0][1:])
        sec_y = int(lst_2[1][0:4])
        #logger.info(f'{second_coordinate} {type(second_coordinate)} {second_coordinate[1]}')
        #logger.info(f'{fist_coordinate} {type(fist_coordinate)} {fist_coordinate[1]}')
        self.scroll_screen(start_x=fist_x, start_y=fist_y, end_x=sec_x, end_y=sec_y, duration=5000)
        self.sleep(2)

    @allure.step("Scroll to open fastOrder")
    def scroll_to_open_fastOrder_sell_without_portfolio(self):
        self.sleep(2)
        second_coordinate= self.get_attribute('HomepageWLStockPrice3', 'bounds')
        lst_1 = second_coordinate.split(',')
        fist_x = int(lst_1[0][1:])
        fist_y = int(lst_1[1][0:4])
        fist_coordinate= self.get_attribute('HomepageWLStockCode3', 'bounds')
        lst_2 = fist_coordinate.split(',')
        sec_x = int(lst_2[0][1:])
        sec_y = int(lst_2[1][0:4])
        #logger.info(f'{second_coordinate} {type(second_coordinate)} {second_coordinate[1]}')
        #logger.info(f'{fist_coordinate} {type(fist_coordinate)} {fist_coordinate[1]}')
        self.scroll_screen(start_x=fist_x, start_y=fist_y, end_x=sec_x, end_y=sec_y, duration=5000)
        self.sleep(2)

    @allure.step("Verify UI data for fastOrder buy")
    def verify_ui_data_for_fastOrder_buy(self):
        self.assert_equal(self.get_attribute(fo_header, 'text'), ' ORDER BELI')
        self.assert_equal(self.get_attribute(fo_harga_text, 'text'), 'Beli di Harga')
        self.assert_equal(self.get_attribute(fo_lot_text, 'text'), 'Jumlah Lot')
        self.assert_equal(self.get_attribute(fo_max_buy_text, 'text'), 'Max Buy')
        self.assert_equal(self.get_attribute(fo_limit, 'text'), 'Limit')
        self.assert_equal(self.get_attribute(fo_cash, 'text'), 'Cash')
        self.assert_equal(self.get_attribute(fo_total_beli_text, 'text'), 'Total Beli')
        total_beli_rp = self.get_attribute(fo_total_beli_value, 'text')
        total_beli = int((total_beli_rp[3:]).replace(',',''))
        #self.assert_equal(type(total_beli), int)
        #confirmation page validation
        code_buy= self.get_attribute(fo_stock_code, 'text')
        lot_buy= self.get_attribute(fo_lot_value, 'text')
        harga_buy= self.get_attribute(fo_hagra_value, 'text')
        jumlah_buy= (int(harga_buy.replace(',', '')))*100
        self.click(fo_btn)
        self.sleep(1)
        self.assert_equal(self.get_attribute(fo_conf_header, 'text'), 'Konfirmasi Pembelian')
        self.assert_equal(self.get_attribute(fo_saham_text, 'text'), 'Saham')
        self.assert_equal(self.get_attribute(fo_saham_value, 'text'), code_buy)
        self.assert_equal(self.get_attribute(fo_conf_lot_text, 'text'), 'Lot')
        self.assert_equal(self.get_attribute(fo_conf_lot_value, 'text'), lot_buy)
        self.assert_equal(self.get_attribute(fo_conf_harga_text, 'text'), 'Harga')
        self.assert_equal(self.get_attribute(fo_conf_harga_value, 'text'), harga_buy)
        self.assert_equal(self.get_attribute(fo_conf_jumlah_text, 'text'), 'Jumlah')
        self.assert_equal(int(self.get_attribute(fo_conf_jumlah_value, 'text').replace(',','')), jumlah_buy)
        self.assert_equal(self.get_attribute(fo_conf_error_msg, 'text'), '*Fee akan dipotong dari trading balance kamu di akhir hari bursa')
        self.assert_equal(self.is_element_visible(fo_conf_setuju), True)
        self.assert_equal(self.is_element_visible(fo_conf_batal_btn), True)

    @allure.step("Verify UI data for fastOrder sell")
    def verify_ui_data_for_fastOrder_sell(self):
        self.assert_equal(self.get_attribute(fo_header, 'text'), ' ORDER JUAL')
        self.assert_equal(self.get_attribute(fo_harga_text, 'text'), 'Jual di Harga')
        self.assert_equal(self.get_attribute(fo_lot_text, 'text'), 'Jumlah Lot')
        self.assert_equal(self.get_attribute(fo_max_buy_text, 'text'), 'Max Sell')
        self.assert_equal(self.get_attribute(fo_jual_semua, 'text'), 'Jual Semua')
        self.assert_equal(self.get_attribute(fo_total_beli_text, 'text'), 'Total Jual')
        total_jual_rp = self.get_attribute(fo_total_beli_value, 'text')
        total_jual = int((total_jual_rp[3:]).replace(',',''))
        #self.assert_equal(type(total_beli), int)
        code_buy = self.get_attribute(fo_stock_code, 'text')
        lot_buy = self.get_attribute(fo_lot_value, 'text')
        harga_buy = self.get_attribute(fo_hagra_value, 'text')
        jumlah_buy = (int(harga_buy.replace(',', ''))) * 100
        self.click(fo_btn)
        self.sleep(1)
        self.assert_equal(self.get_attribute(fo_conf_header, 'text'), 'Konfirmasi Penjualan')
        self.assert_equal(self.get_attribute(fo_saham_text, 'text'), 'Saham')
        self.assert_equal(self.get_attribute(fo_saham_value, 'text'), code_buy)
        self.assert_equal(self.get_attribute(fo_conf_lot_text_s, 'text'), 'Lot')
        self.assert_equal(self.get_attribute(fo_conf_lot_value_s, 'text'), lot_buy)
        self.assert_equal(self.get_attribute(fo_conf_harga_text_s, 'text'), 'Harga')
        self.assert_equal(self.get_attribute(fo_conf_harga_value_s, 'text'), harga_buy)
        self.assert_equal(self.get_attribute(fo_conf_jumlah_text_S, 'text'), 'Jumlah')
        self.assert_equal(self.get_attribute(fo_pl_text, 'text'), 'Profit Loss')
        self.assert_equal(self.is_element_visible(fo_pl_value), True)
        self.assert_equal(int(self.get_attribute(fo_conf_jumlah_value_s, 'text').replace(',', '')), jumlah_buy)
        self.assert_equal(self.get_attribute(fo_conf_error_msg, 'text'),'*Fee akan dipotong dari trading balance kamu di akhir hari bursa')
        self.assert_equal(self.is_element_visible(fo_conf_setuju), True)
        self.assert_equal(self.is_element_visible(fo_conf_batal_btn), True)

    @allure.step("Verify buttons for buy process on fastOrder")
    def verify_buttons_for_buy_on_fastOrder(self):
        stock_code = self.get_attribute(fo_stock_code, 'text')
        self.click(outside_halfcard)
        self.verify_home_page_reg_user_after_back_from_watchlist_new()
        self.scroll_to_open_fastOrder_buy()
        self.go_back()
        self.verify_home_page_reg_user_after_back_from_watchlist_new()
        self.scroll_to_open_fastOrder_buy()
        harga_value = self.get_attribute(fo_hagra_value, 'text')
        self.click(fo_harga_increase)
        self.click(fo_hagra_decrease)
        self.assert_equal(self.get_attribute(fo_hagra_value, 'text'), harga_value)
        lot_value= self.get_attribute(fo_lot_value, 'text')
        self.click(fo_lot_increase)
        self.click(fo_lot_decrease)
        self.assert_equal(self.get_attribute(fo_lot_value, 'text'), lot_value)
        self.click(fo_limit_btn)
        lot_value = self.get_attribute(fo_lot_value, 'text')
        self.click(fo_lot_increase)
        self.assert_equal(self.get_attribute(fo_lot_value, 'text'), lot_value)
        self.click(fo_cash_btn_enable)
        lot_value = self.get_attribute(fo_lot_value, 'text')
        self.click(fo_lot_increase)
        self.assert_equal(self.get_attribute(fo_lot_value, 'text'), lot_value)
        self.click(fo_cash_btn_disable)
        self.clear_text(fo_lot_value)
        self.set_text(fo_lot_value, '1')
        self.assert_equal(self.get_attribute(fo_lot_value, 'text'), '1')
        self.scroll_to_close_halfCard()
        self.assert_equal(self.is_element_visible(fo_header), True)
        self.click(fo_btn)
        self.sleep(2)
        self.go_back()
        self.click(fo_conf_batal_btn)
        self.verify_home_page_reg_user_after_back_from_watchlist_new()
        self.scroll_to_open_fastOrder_buy()
        self.click(fo_btn)
        self.click(fo_conf_setuju)
        self.sleep(5)
        self.assert_equal(self.is_element_visible(saham_tab), True)
        self.assert_equal(self.get_attribute(transaction_type, 'text'), 'BELI')
        self.assert_equal(self.get_attribute(stock_code_l, 'text'), stock_code)


    @allure.step("Scroll to close halfCard")
    def scroll_to_close_halfCard(self):
        self.sleep(2)
        second_coordinate= self.get_attribute(fo_header, 'bounds')
        lst_1 = second_coordinate.split(',')
        fist_x = int(lst_1[0][1:])
        fist_y = int(lst_1[1][0:4])
        fist_coordinate= self.get_attribute(fo_total_beli_text, 'bounds')
        lst_2 = fist_coordinate.split(',')
        sec_x = int(lst_2[0][1:])
        sec_y = int(lst_2[1][0:3])
        #logger.info(f'{second_coordinate} {type(second_coordinate)} {second_coordinate[1]}')
        #logger.info(f'{fist_coordinate} {type(fist_coordinate)} {fist_coordinate[1]}')
        self.scroll_screen(start_x=fist_x, start_y=fist_y, end_x=sec_x, end_y=sec_y, duration=5000)

    @allure.step("Verify buttons for sell process on fastOrder")
    def verify_buttons_for_sell_on_fastOrder(self):
        stock_code = self.get_attribute(fo_stock_code, 'text')
        self.click(outside_halfcard)
        self.verify_home_page_reg_user_after_back_from_watchlist_new()
        self.scroll_to_open_fastOrder_sell()
        self.go_back()
        self.verify_home_page_reg_user_after_back_from_watchlist_new()
        self.scroll_to_open_fastOrder_sell()
        harga_value = self.get_attribute(fo_hagra_value, 'text')
        self.click(fo_harga_increase)
        self.click(fo_hagra_decrease)
        self.assert_equal(self.get_attribute(fo_hagra_value, 'text'), harga_value)
        lot_value= self.get_attribute(fo_lot_value, 'text')
        self.click(fo_lot_increase)
        self.click(fo_lot_decrease)
        self.assert_equal(self.get_attribute(fo_lot_value, 'text'), lot_value)
        self.clear_text(fo_lot_value)
        self.set_text(fo_lot_value, '1')
        self.scroll_to_close_halfCard()
        self.assert_equal(self.is_element_visible(fo_header), True)
        self.click(fo_btn)
        self.sleep(2)
        self.go_back()
        self.click(fo_conf_batal_btn)
        self.verify_home_page_reg_user_after_back_from_watchlist_new()
        self.scroll_to_open_fastOrder_sell()
        self.click(fo_btn)
        self.click(fo_conf_setuju)
        self.sleep(5)
        self.assert_equal(self.is_element_visible(saham_tab), True)
        self.assert_equal(self.get_attribute(transaction_type, 'text'), 'JUAL')
        self.assert_equal(self.get_attribute(stock_code_l, 'text'), stock_code)

    @allure.step("Validate trading limit and buy process")
    def validate_trading_limit_and_buy_process(self):
        self.assert_equal(self.get_attribute(fo_header, 'text'), ' ORDER BELI')
        self.clear_text(fo_hagra_value)
        self.set_text(fo_hagra_value, '100000000000000')
        self.assert_equal(self.get_attribute(trading_limit, 'text'), trading_limit_text)
        self.click(fo_close)
        self.scroll_to_open_fastOrder_buy()
        self.sleep(1)
        stock_code = self.get_attribute(fo_stock_code, 'text')
        self.click(fo_btn)
        self.click(fo_conf_setuju)
        self.sleep(5)
        self.assert_equal(self.is_element_visible(saham_tab), True)
        self.assert_equal(self.get_attribute(transaction_type, 'text'), 'BELI')
        self.assert_equal(self.get_attribute(stock_code_l, 'text'), stock_code)
        self.click(homepage_tab)
        self.sleep(2)
        self.scroll_up()
        self.scroll_to_open_fastOrder_buy()
        stock_code = self.get_attribute(fo_stock_code, 'text')
        self.click(fo_cash_btn_disable)
        self.click(fo_btn)
        self.click(fo_conf_setuju)
        self.sleep(5)
        self.assert_equal(self.is_element_visible(saham_tab), True)
        self.assert_equal(self.get_attribute(transaction_type, 'text'), 'BELI')
        self.assert_equal(self.get_attribute(stock_code_l, 'text'), stock_code)
        self.click(homepage_tab)
        self.sleep(2)
        self.scroll_up()
        self.scroll_to_open_fastOrder_buy()
        stock_code = self.get_attribute(fo_stock_code, 'text')
        self.click(fo_limit_btn)
        self.click(fo_btn)
        self.click(fo_conf_setuju)
        self.sleep(5)
        self.assert_equal(self.is_element_visible(saham_tab), True)
        self.assert_equal(self.get_attribute(transaction_type, 'text'), 'BELI')
        self.assert_equal(self.get_attribute(stock_code_l, 'text'), stock_code)


    @allure.step("Validate max sell and sell process")
    def validate_max_sell_and_sell_process(self):
        self.assert_equal(self.get_attribute(fo_header, 'text'), ' ORDER JUAL')
        self.sleep(1)
        stock_code = self.get_attribute(fo_stock_code, 'text')
        self.click(fo_btn)
        self.click(fo_conf_setuju)
        self.sleep(5)
        self.assert_equal(self.is_element_visible(saham_tab), True)
        self.assert_equal(self.get_attribute(transaction_type, 'text'), 'JUAL')
        self.assert_equal(self.get_attribute(stock_code_l, 'text'), stock_code)
        self.click(homepage_tab)
        self.sleep(2)
        self.scroll_up()
        self.scroll_to_open_fastOrder_sell()
        stock_code = self.get_attribute(fo_stock_code, 'text')
        self.click(fo_max_buy_text)
        self.click(fo_btn)
        self.click(fo_conf_setuju)
        self.sleep(5)
        self.assert_equal(self.is_element_visible(saham_tab), True)
        self.assert_equal(self.get_attribute(transaction_type, 'text'), 'JUAL')
        self.assert_equal(self.get_attribute(stock_code_l, 'text'), stock_code)
        self.click(homepage_tab)
        self.sleep(2)
        self.scroll_up()
        self.scroll_to_open_fastOrder_sell_without_portfolio()
        self.assert_equal(self.is_element_visible(fo_header, 'text'), False)

    @allure.step("Functional validation in fast order")
    def function_validation_in_fast_order(self):
        rdn_with_rp = self.get_attribute(home_rdn, 'text')
        rdn_balance = int((rdn_with_rp[3:]).replace(',', ''))
        buy_power_with_text = self.get_attribute(home_buying_power, 'text')
        buying_power = int((buy_power_with_text[13:]).replace(',', ''))
        self.scroll_up()
        stock_price_h = self.get_attribute('HomepageWLStockPrice2', 'text')
        response_price_h = self.get_attribute('HomepageWLStockPL2', 'text')
        self.scroll_to_open_fastOrder_with_specific_stock_for_buy()
        self.sleep(2)
        lot_value_default = self.get_attribute(fo_lot_value, 'text')
        harga_default_value = (self.get_attribute(fo_hagra_value, 'text')).replace(',','')
        self.assert_equal(harga_default_value,stock_price_h.replace(',',''))
        stock_price_fo = self.get_attribute(fo_price, 'text')
        stock_response_price_fo = self.get_attribute(fo_pl, 'text')
        self.assert_equal(stock_price_fo, stock_price_h)
        self.assert_equal(stock_response_price_fo, response_price_h)
        self.click(fo_hagra_value)
        self.verify_keyboard_on_off(True)
        self.clear_text(fo_hagra_value)
        self.update_text(fo_hagra_value, '10000000000')
        self.assert_equal(self.is_element_visible(trading_limit), True)
        self.click(fo_btn)
        self.assert_equal(self.is_element_visible(fo_header), True)
        self.clear_text(fo_hagra_value)
        self.update_text(fo_hagra_value, harga_default_value)
        self.assert_equal(self.is_element_visible(trading_limit), False)
        self.assert_equal(self.is_element_visible(fo_limit_btn), True)
        self.assert_equal(self.is_element_visible(fo_cash_btn_enable), True)
        self.click(fo_cash_btn_enable)
        self.assert_equal(self.is_element_visible(fo_limit_btn), True)
        harga_value = self.get_attribute(fo_hagra_value, 'text')
        self.click(fo_harga_increase)
        self.click(fo_hagra_decrease)
        self.assert_equal(self.get_attribute(fo_hagra_value, 'text'), harga_value)
        lot_value_after_cash = self.get_attribute(fo_lot_value, 'text')
        self.assert_not_equal(lot_value_after_cash, lot_value_default)
        total_beli_amount_text = self.get_attribute(fo_total_beli_value, 'text')
        total_beli_amount = int((total_beli_amount_text[3:]).replace(',', ''))
        self.assertGreater(buying_power, total_beli_amount)
        self.click(fo_limit_btn)
        self.assert_equal(self.is_element_visible(fo_cash_btn_disable), True)
        lot_value_after_limit = self.get_attribute(fo_lot_value, 'text')
        self.assert_not_equal(lot_value_after_cash, lot_value_after_limit)
        total_beli_amount_text = self.get_attribute(fo_total_beli_value, 'text')
        total_beli_amount = int((total_beli_amount_text[3:]).replace(',', ''))
        self.assertGreater(buying_power, total_beli_amount)
        self.click(fo_lot_value)
        self.verify_keyboard_on_off(True)


    @allure.step("Scroll to open fastOrder with specific stock for buy")
    def scroll_to_open_fastOrder_with_specific_stock_for_buy(self):
        self.sleep(2)
        second_coordinate= self.get_attribute('HomepageWLStockPrice2', 'bounds')
        lst_1 = second_coordinate.split(',')
        fist_x = int(lst_1[0][1:])
        fist_y = int(lst_1[1][0:4])
        fist_coordinate= self.get_attribute('HomepageWLStockCode2', 'bounds')
        lst_2 = fist_coordinate.split(',')
        sec_x = int(lst_2[0][1:])
        sec_y = int(lst_2[1][0:4])
        #logger.info(f'{second_coordinate} {type(second_coordinate)} {second_coordinate[1]}')
        #logger.info(f'{fist_coordinate} {type(fist_coordinate)} {fist_coordinate[1]}')
        self.scroll_screen(start_x=sec_x, start_y=sec_y, end_x=fist_x, end_y=fist_y, duration=5000)
        self.sleep(2)

    @allure.step("validate fast order with non kyc user")
    def validate_fast_order_with_non_kyc_user(self):
        self.scroll_to_open_fastOrder_with_specific_stock_for_buy()
        self.sleep(5)
        self.verify_sdp_page()
        self.go_back()
        self.sleep(3)
        self.scroll_up()
        self.scroll_to_open_fastOrder_sell()
        self.sleep(5)
        #self.verify_sdp_page()





