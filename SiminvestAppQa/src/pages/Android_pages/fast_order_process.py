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

class FastOrder(BuyProcess):

    @allure.step("Scroll to open fastOrder")
    def scroll_to_open_fastOrder_buy(self):
        self.sleep(2)
        self.scroll_screen(start_x=72, start_y=1656, end_x=887, end_y=1656, duration=5000)
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





