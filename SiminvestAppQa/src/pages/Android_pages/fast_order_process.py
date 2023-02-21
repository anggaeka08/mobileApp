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
fo_cash = '//android.widget.TextView[@text = "Cash"]'
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
        logger.info(f'{second_coordinate} {type(second_coordinate)} {second_coordinate[1]}')
        logger.info(f'{fist_coordinate} {type(fist_coordinate)} {fist_coordinate[1]}')
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







