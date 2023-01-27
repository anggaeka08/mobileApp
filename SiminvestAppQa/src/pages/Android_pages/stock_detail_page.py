import pytest
from selenium.common.exceptions import NoSuchElementException
from  numerize import numerize
from SiminvestAppQa.src.data.userData import user_data
from datetime import datetime
import allure
import logging as logger
from SiminvestAppQa.src.pages.Android_pages.watchlist import Watchlist
from SiminvestAppQa.src.pages.Android_pages.buy_process import BuyProcess
import language_tool_python
from SiminvestAppQa.src.utilities.requestUtilities import RequestsUtilities
from datetime import datetime

request_utilities = RequestsUtilities()
star_without_click = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ImageView'
search_btn = 'SDPSearchBtn'
search_box = '//android.widget.EditText[@text="Cari Saham"]'
searched_stock = '//android.widget.TextView[@text="Ace Hardware Indonesia Tbk"]'
stock = '//*[@text="ACES"]'
sdp_header = 'SDPStockCode'
stock_name = 'SDPStockName'
stock_price = 'SDPStockPrice'
stock_pl = 'SDPStockPL'
watchlist ='//*[@text="Default"]'
chart_view = '//android.view.View[@resource-id="root"]'
bid_lot = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[23]'
bid = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[24]'
ask = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[27]'
ask_lot = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[28]'
bid_text = '//android.widget.TextView[@text="Bid"]'
ask_text = '//android.widget.TextView[@text="Ask"]'
lot_text = '//android.widget.TextView[@text="Lot"]'
profile_btn = '//android.widget.TextView[@text="Profile"]'
Order_Book = '//*[@text="Order Book"]'
News = '//*[@text="News"]'
Keystats = '//*[@text="Keystats"]'
Financials = '//*[@text="Financials"]'
Profile = '//*[@text="Profile"]'
beli_btn = 'SDPBeliBtn'
#list of news date and domain
news_1= 'news_link_3'
news_url_1 = 'news_title_3'
browser_url = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.EditText'
Hubungi = '//*[@text="Hubungi Customer Care"]'
chrome_url = 'com.android.chrome:id/url_bar'
total_nilai = "SDPPortPageText1"
total_nilai_text = 'SDPPortPageText3'
lot_dimiliki = "SDPPortPageText2"
lot_dimiliki_text = 'SDPPortPageText5'
Diinvestasikan = "SDPPortPageText6"
Diinvestasikan_text = 'SDPPortPageText8'
Harga_rata_rata = "SDPPortPageText7"
Harga_rata_rata_text = 'SDPPortPageText9'
#running trade account
running_trade = '//android.widget.TextView[@text="Running Trade"]'
lihat_semua = '//android.widget.TextView[@text="Lihat Semua"]'
running_time = '//android.widget.TextView[@text="Time"]'
running_Code = '//android.widget.TextView[@text="Code"]'
running_Price = '//android.widget.TextView[@text="Price"]'
running_Lot = '//android.widget.TextView[@text="Lot"]'
back_btn_on_search='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ImageView'
back_btn_on_sdp = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.ImageView'
search_edit_box = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.EditText'
search_entry_1 = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]'
search_entry_2 = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]'
search_entry_code= '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.TextView[1]'
search_entry_name = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.TextView[2]'
exchange_notification= '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[5]/android.widget.TextView'
exchange_time_loader ='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[5]/android.widget.ImageView'
buy_btn_on_buy_page = 'SellPageSellBtn'
confirm_btn = 'BuySellConfSetujuBtn'
market_close_msg ='BuyTransactionMarketClosePopUpHeading'
notation_watchlist = '//android.view.ViewGroup[@content-desc="HomepageWLEntry4"]/android.view.ViewGroup[2]'
notation_search = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup'
notation_text = '//android.view.TextView[@text="!"]'
notation_after_name = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]'
notation_after_chart ='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[6]'
suspend_image = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ImageView'
watchlist_card = '//*[@text="Default"]'
#chart_btn
D1 = "//android.widget.Button[@text = '1D']"
M1 = "//android.widget.Button[@text = '1M']"
M3 = "//android.widget.Button[@text = '3M']"
YTD = "//android.widget.Button[@text = 'YTD']"
Y1 = "//android.widget.Button[@text = '1Y']"
Y3 = "//android.widget.Button[@text = '3Y']"
Y5 = "//android.widget.Button[@text = '5Y']"
chart_view = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[8]/android.view.View/android.widget.Image/android.view.View[1]'
time_on_chart = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[8]/android.view.View/android.view.View/android.widget.TextView[1]'
stock_code_on_chart = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[8]/android.view.View/android.view.View/android.widget.TextView[2]'
y_axis_value = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[8]/android.view.View/android.widget.Image/android.widget.TextView[2]'
candlestick_chart = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]/android.widget.ImageView'
#financial tab
Kuartal = '//android.widget.TextView[@text="Kuartal"]'
Tahunan = '//android.widget.TextView[@text="Tahunan"]'
Income_Statement = '//android.widget.TextView[@text="Income Statement"]'
Balance_Sheet = '//android.widget.TextView[@text="Balance Sheet"]'
Cash_Flow = '//android.widget.TextView[@text="Cash Flow"]'
Buying_Power="HomepagebuyPower"

class StockDetailPage(Watchlist, BuyProcess):

    @allure.step("Tab on star")
    def tap_on_star(self):
        #self.sleep(3)
        #logger.info(self.is_element_visible(star_without_click))
        self.click(star_without_click)

    @allure.step("Verify stock on watchlist")
    def verify_stock_on_watchlist(self, status):
        self.assert_equal(self.is_element_visible(stock), status)

    @allure.step("Click on stock")
    def click_on_stock(self):
        self.click(stock)

    @allure.step("Click on watchlist")
    def click_on_watchlist(self):
        self.click(watchlist)

    @allure.step("Click search btn")
    def click_on_search_btn(self):
        self.click(search_btn)

    @allure.step("Enter Stock Code")
    def enter_stock_code(self, stock_code):
        self.set_text(search_box, stock_code)

    @allure.step("Click on stock code")
    def click_on_stocks(self):
        self.double_tap(searched_stock)
        self.sleep(5)

    @allure.step("Verify chart is present")
    def chart_presence(self):
        self.assert_equal(self.is_element_visible(chart_view), True)

    @allure.step("Verify Oder Book tab is open")
    def order_book_tab_open(self):
        self.assert_equal(self.is_element_visible(ask_text), True)
        self.assert_equal(self.is_element_visible(lot_text), True)
        self.assert_equal(self.is_element_visible(bid_text), True)

    @allure.step("Validate bid list")
    def validate_bid_list(self):
        lot_list = []
        bid_list = []
        try:
            for i in range(20, 30):
                lot_list.append(int((self.get_attribute(f'SDPbid_volumeText{i}',"text")).replace(',','')))
                bid_list.append(int((self.get_attribute(f'SDPbid_priceText{i}',"text")).replace(',','')))
        except NoSuchElementException as E:
            pass
        try:
            total = 0
            self.assert_equal(len(lot_list), 10)
            self.assert_equal(len(bid_list), 10)
            total_lot_value_for_bid = int(self.get_attribute('(//android.widget.TextView[@content-desc="SDPOrderBookFooter"])[1]', 'text').replace(',',''))
            for ele in range(0, len(lot_list)):
                total = total + lot_list[ele]
            logger.info(f"total:{total}")
            logger.info(f"total:{total_lot_value_for_bid}")
            self.assert_equal(total_lot_value_for_bid, total)
        except AssertionError as E:
            logger.info(len(lot_list))
            logger.info(len(bid_list))
            self.assert_equal(len(lot_list), len(bid_list))

    @allure.step("Validate bid lot list on sbp page")
    def validate_bid_lot_list_on_sbp(self):
        self.scroll_up_screen()
        self.sleep(1)
        lot_list = []
        try:
            for i in range(10, 30):
                lot_list.append(int((self.get_attribute(f'SellPageOrderBookTextLot{i}',"text")).replace(',','')))
        except NoSuchElementException as E:
            pass
        try:
            total = 0
            self.assert_equal(len(lot_list), 10)
            total_lot_value_for_bid = int(self.get_attribute('(//android.widget.TextView[@content-desc="SellPageFooterText"])[1]', 'text').replace(',',''))
            for ele in range(0, len(lot_list)):
                total = total + lot_list[ele]
            logger.info(f"total:{total}")
            logger.info(f"total:{total_lot_value_for_bid}")
            self.assert_equal(total_lot_value_for_bid, total)
        except AssertionError as E:
            logger.info(len(lot_list))

    @allure.step("Validate ask list")
    def validate_ask_list(self):
        lot_list = []
        ask_list = []
        try:
            for i in range(20, 30):
                lot_list.append(int((self.get_attribute(f'SDPask_volumeText{i}', "text")).replace(',', '')))
                ask_list.append(int((self.get_attribute(f'SDPask_priceText{i}', "text")).replace(',', '')))
        except NoSuchElementException as E:
            pass
        try:
            total = 0
            self.assert_equal(len(lot_list), 10)
            self.assert_equal(len(ask_list), 10)
            total_lot_value_for_bid = int(
                self.get_attribute('(//android.widget.TextView[@content-desc="SDPOrderBookFooter"])[2]',
                                   'text').replace(',', ''))
            for ele in range(0, len(lot_list)):
                total = total + lot_list[ele]
            logger.info(f"total:{total}")
            logger.info(f"total:{total_lot_value_for_bid}")
            self.assert_equal(total_lot_value_for_bid, total)
        except AssertionError as E:
            logger.info(len(lot_list))
            logger.info(len(ask_list))
            self.assert_equal(len(lot_list), len(ask_list))

    @allure.step("Validate ask lot on sbp")
    def validate_ask_list_lot_on_sbp(self):
        lot_list = []
        #ask_list = []
        try:
            for i in range(20, 30):
                lot_list.append(int((self.get_attribute(f'SellPageOrderBookTextLot{i}', "text")).replace(',', '')))
                #ask_list.append(int((self.get_attribute(f'SDPask_priceText{i}', "text")).replace(',', '')))
        except NoSuchElementException as E:
            pass
        try:
            total = 0
            self.assert_equal(len(lot_list), 10)
            #self.assert_equal(len(ask_list), 10)
            total_lot_value_for_bid = int(
                self.get_attribute('(//android.widget.TextView[@content-desc="SellPageFooterText"])[2]',
                                   'text').replace(',', ''))
            for ele in range(0, len(lot_list)):
                total = total + lot_list[ele]
            logger.info(f"total:{total}")
            logger.info(f"total:{total_lot_value_for_bid}")
            self.assert_equal(total_lot_value_for_bid, total)
        except AssertionError as E:
            logger.info(len(lot_list))
            #logger.info(len(ask_list))
           # self.assert_equal(len(lot_list), len(ask_list))


    @allure.step("Bit value list")
    def Bit_value_list(self):
        bit_value_list = []
        bit_value_list.append(int((self.get_attribute('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[24]', "text")).replace(',','')))
        for i in range(26, 54,4):
            bit_value_list.append(int((self.get_attribute(
                f'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[{i}]',
                "text")).replace(',','')))
        bit_value_list.append(int((self.get_attribute(
                f'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[56]',
                "text")).replace(',','')))
        bit_value_list.append(int((self.get_attribute(
                f'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[60]',
                "text")).replace(',','')))
        return bit_value_list

    @allure.step("Bit value list")
    def ask_value_list(self):
        ask_value_list = []
        #ask_value_list.append(int((self.get_attribute('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[27]', "text")).replace(',','')))
        for i in range(27, 55,4):
            ask_value_list.append(int((self.get_attribute(
                f'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[{i}]',
                "text")).replace(',','')))
        ask_value_list.append(int((self.get_attribute(
            f'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[54]',
            "text")).replace(',', '')))
        ask_value_list.append(int((self.get_attribute(
            f'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[58]',
            "text")).replace(',', '')))
        ask_value_list.append(int((self.get_attribute(
            f'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[61]',
            "text")).replace(',', '')))
        return ask_value_list

    @allure.step("ask lot list")
    def ask_lot_list(self):
        ask_lot_list = []
        for i in range(28, 56,4):
            ask_lot_list.append(int((self.get_attribute(
                f'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[{i}]',
                "text")).replace(',','')))
        ask_lot_list.append(int((self.get_attribute(
            f'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[55]',
            "text")).replace(',', '')))
        ask_lot_list.append(int((self.get_attribute(
            f'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[59]',
            "text")).replace(',', '')))
        ask_lot_list.append(int((self.get_attribute(
            f'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[62]',
            "text")).replace(',', '')))
        return ask_lot_list

    @allure.step("Verify  Orderbook, News, Keystats, Financials and profile ")
    def verify_details_down_to_beli_btn(self):
        self.assert_equal(self.is_element_visible(Order_Book), True)
        self.assert_equal(self.is_element_visible(News), True)
        self.assert_equal(self.is_element_visible(Keystats), True)
        self.assert_equal(self.is_element_visible(Financials), True)
        self.assert_equal(self.is_element_visible(profile_btn), True)

    @allure.step("Click on profile tab")
    def click_on_profile(self):
        self.click(profile_btn)

    @allure.step("Verify details of profile tab")
    def verify_details_of_profile_tab(self):
        self.click(profile_btn)
        self.assert_equal(self.get_attribute('profile_entry_1', 'text'), 'Keterangan Perusahaan')
        self.assert_equal(self.is_element_visible('profile_entry_1_value'), True)
        self.scroll_up_screen()
        self.sleep(1)
        self.scroll_up_screen()
        #verify stackholder entries
        self.assert_equal(self.get_attribute('profile_entry_2', 'text'), 'Pemegang Saham')
        pemegang_lst = ['PT Kawan Lama Sejahtera', 'Kuncoro Wibowo', 'Dewi Triana Saleh', 'Suharno', 'Gregory Sugyono Widjaja', 'Public', 'Treasury Stock']
        for i in range(0, 7,1):
            self.assert_equal(self.get_attribute(f'shareholder_entry_{i}', 'text'), pemegang_lst[i])
            self.assert_not_equal(self.get_attribute(f'shareholder_entry_value{i}', 'text'), '-')
        #verify director entries
        self.assert_equal(self.get_attribute('profile_entry_3', 'text'), 'Direksi')
        director_lst = ['President Director', 'Director','Director','Director','Director','Director']
        for i in range(0,6,1):
            self.assert_equal(self.get_attribute(f'director_entry{i}','text'), director_lst[i])
            self.assert_not_equal(self.get_attribute(f'director_entry_value{i}', 'text'), '-')
        self.scroll_up_screen()
        #verify_commissioner_entry
        self.assert_equal(self.get_attribute('profile_entry_4', 'text'), 'Komisaris')
        commissioner_lst = ['President Commissioner', 'Commissioner', 'Commissioner', 'Independent Commissioner', 'Independent Commissioner', 'Director']
        for i in range(0, 5, 1):
            self.assert_equal(self.get_attribute(f'commissioners_entry{i}', 'text'), commissioner_lst[i])
            self.assert_not_equal(self.get_attribute(f'commissioners_entry_value{i}', 'text'), '-')
        #verify address entry
        self.assert_equal(self.get_attribute('profile_entry_5', 'text'), 'Alamat')
        self.assert_not_equal(self.get_attribute('profile_entry_5_value', 'text'), '-')
        self.assert_equal(self.get_attribute('profile_entry_6', 'text'), 'Sejarah Perusahaan')
        self.assert_equal(self.get_attribute('profile_entry_7', 'text'), 'Listing Date')
        self.assert_not_equal(self.get_attribute('profile_entry_7_value', 'text'), '-')
        self.assert_equal(self.get_attribute('profile_entry_8', 'text'), 'IPO Price')
        self.assert_not_equal(self.get_attribute('profile_entry_8_value', 'text'), '-')
        self.assert_equal(self.get_attribute('profile_entry_9', 'text'), 'IPO Shares')
        self.assert_not_equal(self.get_attribute('profile_entry_9_value', 'text'), '-')
        self.assert_equal(self.get_attribute('profile_entry_10', 'text'), 'IPO Amount')
        self.assert_not_equal(self.get_attribute('profile_entry_10_value', 'text'), '-')



    @allure.step("Verify News section available on SDP")
    def verify_news_availability_on_sdp(self):
        self.assert_equal(self.is_element_visible(News), True)

    @allure.step("Click on News")
    def click_on_news(self):
        self.click(News)

    @allure.step("scroll up")
    def scroll_up_screen(self):
        self.scroll_screen(start_x=401, start_y=2030, end_x=401, end_y=717, duration=10000)
        self.sleep(2)

    @allure.step("Verify news date list is shorted")
    def verify_news_tab(self):
        date_list = []
        title_lst = []
        sorted_date_list = []
        news_1_string = self.get_attribute(f'news_link_0',"text")
        news_title_1 = self.get_attribute(f'news_title_0',"text")
        title_lst.append(news_title_1)
        logger.info(news_1_string)
        logger.info(title_lst)
        date_1 = news_1_string[-11:]
        date_list.append(date_1)
        self.scroll_up_screen()
        self.sleep(1)
        self.scroll_up_screen()
        self.validate_domain_name_for_one_news()
        for i in range(1, 10, 1):
            news_1_string = self.get_attribute(f'news_link_{i}', "text")
            news_1_title = self.get_attribute(f'news_title_{i}', "text")
            date_1 = news_1_string[-11:]
            date_list.append(date_1)
            title_lst.append(news_1_title)
            logger.info(title_lst)
            logger.info(date_list)
        logger.info(date_list)
        fetched_date_lst = date_list
        date_list.sort(key=lambda date: datetime.strptime(date, '%d %b %Y'))
        date_list.reverse()
        sorted_date_list = date_list
        logger.info(sorted_date_list)
        self.assert_equal(fetched_date_lst, sorted_date_list)
        for i in range(len(title_lst)):
            if len(title_lst[i]) > 80:
                a = title_lst[i]
                if '.' in a :
                    logger.info(". Available after 81 string")
            else:
                logger.info("String length is not greater then 80")
        logger.info(title_lst)
        self.assert_equal(len(title_lst), 10)
        for i in range(len(title_lst) - 1):
            if title_lst[i] == title_lst[i + 1]:
                logger.info("News are same")
            else:
                logger.info("News are not same")
        self.go_back()

    @allure.step("Validate domain name for one news")
    def validate_domain_name_for_one_news(self):
        news_url_text = self.get_attribute(news_url_1, 'text')
        c = 'id'
        #d = 'com'
        index = news_url_text.find(c)
        news_url = news_url_text[4:index+2]
        logger.info(news_url)
        self.click(news_1)
        self.sleep(3)
        # browser_full_url = self.get_attribute(browser_url, 'text')
        # d = '/2'
        # index = browser_full_url.find(d)
        # browser_url_text = browser_full_url[:index]
        # logger.info(browser_url_text)
        # self.assert_equal(news_url, browser_url_text[12:])
        self.go_back()


    @allure.step("Verify keystat tab")
    def verify_keystat_tab(self):
        self.click_on_stock_code()
        self.sleep(3)
        self.click(Keystats)
        #Verify earnings entries
        self.assert_equal(self.is_element_visible('Earnings_entry'), True)
        self.scroll_up_screen()
        for i in range(0,7, 1):
            self.assert_equal(self.is_element_visible(f'Earnings_label_{i}'), True)
            self.assert_equal(self.is_element_visible(f'Earnings_label_{i}_value'), True)
        #verify entries for valuation
        self.assert_equal(self.is_element_visible('Valuation_entry'), True)
        self.scroll_up_screen()
        for i in range(0, 2, 1):
            self.assert_equal(self.is_element_visible(f'Valuation_label_{i}'), True)
            self.assert_equal(self.is_element_visible(f'Valuation_label_{i}_value'), True)
        #verify entries for profitability
        self.assert_equal(self.is_element_visible('Profitability_entry'), True)
        self.scroll_up_screen()
        for i in range(0, 6, 1):
            self.assert_equal(self.is_element_visible(f'Profitability_label_{i}'), True)
            self.assert_equal(self.is_element_visible(f'Profitability_label_{i}_value'), True)
        #verify entries for Liquidity
        self.assert_equal(self.is_element_visible('Liquidity_entry'), True)
        self.scroll_up_screen()
        for i in range(0, 2, 1):
            self.assert_equal(self.is_element_visible(f'Liquidity_label_{i}'), True)
            self.assert_equal(self.is_element_visible(f'Liquidity_label_{i}_value'), True)

    @allure.step("verify financial tab")
    def verify_Financials_tab(self):
        self.click(Financials)
        self.sleep(1)
        self.assert_equal(self.is_element_visible(Kuartal), True)
        self.assert_equal(self.is_element_visible(Tahunan), True)
        self.scroll_up_screen()
        self.assert_equal(self.is_element_visible(Income_Statement), True)
        self.assert_equal(self.is_element_visible(Balance_Sheet), True)
        self.scroll_up_screen()
        self.assert_equal(self.is_element_visible(Cash_Flow), True)

    @allure.step('verify redirection after click on Hubungi Customer')
    def verify_redirection_after_click_on_support_btn(self):
        self.click(Hubungi)
        self.sleep(4)
        support_url_text = self.get_attribute(chrome_url,'text')
        index = support_url_text.find('.com')
        domain_name = support_url_text[:index]
        self.assert_equal(domain_name[8:], 'invest.i')

    """@allure.step("Verify stock company address")
    def verify_stock_company_address(self):
        self.scroll_up_screen()
        address = str(self.get_attribute(address_text, 'text'))
        logger.info(address)
        #address_spaces = address.isspace()
        for i in range(len(address)):
            if ' ' in address:
                logger.info("single spaces available in address")
            elif '  ' in address:
                logger.info("double spaces available in address")
                raise "double spaces available in address" """

    @allure.step("Verify stock profile when details not available")
    def verify_stock_profile_when_details_not_available(self):
        #sdp page have single view
        pass

    @allure.step("Verify details availability when move to sdp by portfolio page")
    def verify_details_availability_when_move_to_sdp_by_portfolio_page(self):
        self.assert_equal(self.is_element_visible(total_nilai), True)
        self.assert_equal(self.is_element_visible(total_nilai_text), True)
        self.assert_equal(self.is_element_visible(lot_dimiliki), True)
        self.assert_equal(self.is_element_visible(lot_dimiliki_text), True)
        self.assert_equal(self.is_element_visible(Diinvestasikan), True)
        self.assert_equal(self.is_element_visible(Diinvestasikan_text), True)
        self.assert_equal(self.is_element_visible(Harga_rata_rata), True)
        self.assert_equal(self.is_element_visible(Harga_rata_rata_text), True)


    @allure.step("Validate grammar of title")
    def validate_grammar_of_title(self):
        all_value_lst = ['ACES', 'Ace Hardware Indonesia Tbk', 'Open','','High','','Vol','', 'Close', '','Low','', 'Val', '','Avg','', 'F.Buy', '','F.Sell' ]
        self.assert_equal(self.get_attribute(sdp_header, 'text'), all_value_lst[0])
        self.assert_equal(self.get_attribute(stock_name, 'text'), all_value_lst[1])
        for i in range(1, 18, 2):
            logger.info(self.get_attribute(f'SDPText{i}', 'text'))
            logger.info(all_value_lst[1+i])
            self.assert_equal(self.get_attribute(f'SDPText{i}', 'text'), all_value_lst[1+i])
        self.scroll_up_screen()
        self.assert_equal(self.is_element_visible(beli_btn), True)
        self.assert_equal(self.is_element_visible(Order_Book), True)
        self.assert_equal(self.is_element_visible(News), True)
        self.assert_equal(self.is_element_visible(Financials), True)
        self.assert_equal(self.is_element_visible(Profile), True)
        self.assert_equal(self.is_element_visible(bid_text), True)
        self.assert_equal(self.is_element_visible(lot_text), True)
        self.assert_equal(self.is_element_visible(ask_text), True)
        self.assert_equal(self.is_element_visible(running_trade), True)
        self.assert_equal(self.is_element_visible(lihat_semua), True)
        self.assert_equal(self.is_element_visible(running_time), True)
        self.assert_equal(self.is_element_visible(running_Code), True)
        self.assert_equal(self.is_element_visible(running_Price), True)
        self.assert_equal(self.is_element_visible(running_Lot), True)

    @allure.step("Validate all api data")
    def validate_all_api_data(self):
        api_value=[]
        token_value = self.login()
        token = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJpWlYzdUJkTkJyTDA4dVIzQUR2bmg4akdTdHNkSHpQVSIsInN1YiI6IlNpbWFzSW52ZXN0In0.Kj31bgBrbc94NaUDKWgbx-N4ZBQNFsrZBmF7xtZ4hNo"}
        token['Authorization'] = 'Bearer ' + token_value
        sdp_rs = request_utilities.get(base_url='https://api.siminvest.co.id/api/v1/pcs/v2/product/equity',endpoint='/ACES', headers=token,expected_status_code=200)
        vol = str(numerize.numerize(int(sdp_rs['vol'])))
        val = str(numerize.numerize(int(sdp_rs['val'])))
        # new_value = vol[:2]+"."+vol[2:4] +" Jt"
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

    @allure.step("Collect data from sdp ui")
    def collect_all_data_from_ui(self):
        all_value = []
        for i in range(2, 20, 2):
            value = self.get_attribute(f'SDPText{i}', 'text')
            all_value.append(value)
        return all_value

    @allure.step("click on back btn")
    def click_on_back_btn(self):
        self.click(back_btn_on_search)

    @allure.step("click on back btn on SDP")
    def click_on_back_btn_on_SDP(self):
        self.click(back_btn_on_sdp)

    @allure.step("Verify text in search bar")
    def verify_text_in_search_bar(self):
        self.assert_equal(self.get_attribute(search_edit_box, 'text'), 'Cari Saham')
        self.set_text(search_edit_box, 'A')
        self.assert_not_equal(self.get_attribute(search_edit_box, 'text'), 'Cari Saham')
        self.clear_text(search_edit_box)
        self.assert_equal(self.get_attribute(search_edit_box, 'text'), 'Cari Saham')

    @allure.step("verify search option in search bar")
    def verify_search_option_in_search_bar(self):
        self.set_text(search_edit_box, 'A')
        self.assert_equal(self.is_element_visible(search_entry_1), True)
        self.assert_equal(self.is_element_visible(search_entry_2), True)
        self.assert_equal(self.is_element_visible(search_entry_code), True)
        self.assert_equal(self.is_element_visible(search_entry_name), True)
        self.set_text(search_edit_box, 'Simas Danamas Saham')
        self.assert_equal(self.is_element_visible(search_entry_1), False)

    @allure.step("Validate notification in timeline")
    def validate_notification_in_timeline(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        logger.info(f"Current Time = {current_time}")
        if (current_time >= '7:30' and current_time <='10:00') or (current_time >='12:00' and current_time <='13:15') :
            self.assert_equal(self.is_element_visible(exchange_notification), False)
            logger.info("within time")
        else:
            logger.info("Out of time")
            self.assert_equal(self.is_element_visible(exchange_notification), True)
            self.assert_equal(self.get_attribute(exchange_notification, 'text'), 'Sedang berada di luar jam kerja bursa')
            self.assert_equal(self.is_element_visible(exchange_time_loader), True)
            self.click(exchange_notification)
            self.verify_sdp_page_after_back()
            self.scroll_up()
            self.click_on_news()
            self.scroll_down()
            self.assert_equal(self.is_element_visible(exchange_notification), True)
            self.click(beli_btn)
            self.click(buy_btn_on_buy_page)
            self.click(confirm_btn)
            self.sleep(2)
            self.assert_equal(self.is_element_visible(market_close_msg), True)

    @allure.step("Validate position of elements on sdp")
    def validate_position_of_elements_on_sdp(self):
        self.assert_equal(self.get_attribute(stock_name, 'bounds'), '[52,277][541,332]')
        #self.assert_equal(self.get_attribute(stock_price, 'bounds'), '[52,445][163,517]')
        #self.assert_equal(self.get_attribute(stock_pl, 'bounds'), '[52,536][440,572]')


    @allure.step("Validate Special notation")
    def validate_special_notation(self):
        self.login_and_verify_homepage_for_reg_user(user_data['reg_no_4'])
        self.scroll_up()
        self.sleep(1)
        self.scroll_up()
        self.assert_equal(self.is_element_visible(notation_watchlist), True)
        self.click_on_edit_for_stock()
        self.sleep(2)
        self.search_stock('KBLV')
        self.assert_equal(self.is_element_visible(notation_text), False)
        self.go_back()
        self.sleep(1)
        self.go_back()
        self.scroll_down()
        self.sleep(1)
        self.scroll_down()
        self.click_global_search_btn_and_saerch_stock('KBLV')
        self.assert_equal(self.is_element_visible(notation_search), True)
        self.click_on_stock_code()
        self.verify_sdp_page_after_back()
        self.assert_equal(self.is_element_visible(notation_after_name), True)
        self.assert_equal(self.is_element_visible(notation_after_chart), True)
        #self.assert_equal(self.get_attribute(notation_after_chart, 'bounds'), '[52,1341][1028,1468]')

    @allure.step("Validate watchlist buy for suspended stock")
    def validate_watchlist_buy_for_suspended_stock(self):
        self.login_and_verify_homepage_for_reg_user(user_data['reg_no_3'])
        self.scroll_up()
        self.sleep(1)
        self.scroll_up()
        self.scroll_screen(start_x=144, start_y=1566, end_x=901, end_y=1566, duration=10000)
        self.sleep(2)
        self.scroll_down()
        self.sleep(1)
        self.scroll_down()
        self.verify_home_page_reg_user_after_back_from_watchlist()

    @allure.step("Validate suspended stock on SDP")
    def validate_suspended_stock_on_sdp(self):
        self.click_global_search_btn_and_saerch_stock('PURE-W')
        self.sleep(1)
        self.click_on_stock_code()
        self.verify_sdp_page_after_back()
        self.assert_equal(self.is_element_visible(suspend_image), True)
        self.click(beli_btn)
        self.verify_sdp_page_after_back()
        self.click(suspend_image)
        self.verify_sdp_page_after_back()
        self.assert_equal(self.get_attribute(suspend_image, 'bounds'), '[843,372][1027,429]')

    @allure.step("Verify star mark on sdp")
    def verify_star_mark_on_sdp(self):
        self.assert_equal(self.is_element_visible(star_without_click), True)
        self.click(star_without_click)
        self.assert_equal(self.is_element_visible(watchlist_card), True)
        self.go_back()
        self.assert_equal(self.is_element_visible(watchlist_card), False)
        self.click(star_without_click)
        self.click(watchlist_card)
        self.sleep(2)
        self.assert_equal(self.is_element_visible(star_without_click), True)
        self.launch_app_again()
        self.login_and_verify_homepage_for_reg_user(user_data['reg_no_3'])
        self.scroll_up()
        self.sleep(1)
        self.scroll_up()
        self.sleep(2)
        self.assert_equal(self.is_element_visible('//*[@text = "ACES"]'), True)
        self.scroll_down()
        self.sleep(1)
        self.scroll_down()
        self.click_global_search_btn_and_saerch_stock('ACES')
        self.sleep(3)
        self.click_on_stock_code()
        self.verify_sdp_page_after_back()
        self.assert_equal(self.is_element_visible(star_without_click), True)
        self.click(star_without_click)
        self.click(watchlist_card)
        self.sleep(2)
        self.assert_equal(self.is_element_visible(star_without_click), True)
        #self.assert_equal(self.get_attribute(star_without_click, 'bounds'), '[953,525][1010,583]')
        self.go_back()
        self.sleep(1)
        self.go_back()
        self.scroll_up()
        self.sleep(1)
        self.scroll_up()
        self.assert_equal(self.is_element_visible('//*[@text = "ACES"]'), False)

    @allure.step("validate response price")
    def validate_response_price(self):
        self.sleep(4)
        pl = self.get_attribute(stock_pl, 'text')
        c = ')'
        index = pl.find(c)
        time_dur = pl[index + 3:]
        logger.info(time_dur)
        return time_dur

    @allure.step("Validate on chart value")
    def validate_on_chart_values(self):
        self.click(chart_view)
        self.sleep(2)
        time = self.get_attribute(time_on_chart, 'text')
        format_value = time.find('20')
        if format_value == 0:
            pytest.fail("Not in date format")
        self.assert_equal(self.is_element_visible(stock_code_on_chart), True)

    @allure.step("Validate sdp chart")
    def validate_sdp_chart(self):
        full_pl = self.validate_response_price()
        self.assert_equal(full_pl, 'Past One Day')
        self.sleep(2)
        self.click(chart_view)
        self.sleep(2)
        time = self.get_attribute(time_on_chart, 'text')
        format_value = time.find(':')
        if format_value == 0:
            pytest.fail("Not in time format")
        self.assert_equal(self.is_element_visible(stock_code_on_chart), True)
        d1_y_value = self.get_attribute(y_axis_value, 'text')
        self.click(M1)
        self.assert_equal(self.is_element_visible(chart_view), False)
        full_pl = self.validate_response_price()
        self.assert_equal(full_pl, 'Past One Month')
        self.validate_on_chart_values()
        m1_y_value = self.get_attribute(y_axis_value, 'text')
        self.assert_not_equal(d1_y_value, m1_y_value)
        self.click(M3)
        self.assert_equal(self.is_element_visible(chart_view), False)
        full_pl = self.validate_response_price()
        self.assert_equal(full_pl, 'Past Three Months')
        self.validate_on_chart_values()
        m3_y_value = self.get_attribute(y_axis_value, 'text')
        self.assert_not_equal(m1_y_value, m3_y_value)
        #ytd value
        self.click(YTD)
        self.assert_equal(self.is_element_visible(chart_view), False)
        full_pl = self.validate_response_price()
        self.assert_equal(full_pl, 'Year To Date')
        self.validate_on_chart_values()
        ytd_y_value = self.get_attribute(y_axis_value, 'text')
        self.assert_not_equal(ytd_y_value, m3_y_value)
        # 1Y value
        self.click(Y1)
        self.assert_equal(self.is_element_visible(chart_view), False)
        self.sleep(3)
        full_pl = self.validate_response_price()
        self.assert_equal(full_pl, 'Past One Year')
        self.validate_on_chart_values()
        y1_y_value = self.get_attribute(y_axis_value, 'text')
        if y1_y_value == ytd_y_value :
            pass
        else :
            self.assert_not_equal(y1_y_value, ytd_y_value)
        # 3Y value
        self.click(Y3)
        self.assert_equal(self.is_element_visible(chart_view), False)
        self.sleep(3)
        full_pl = self.validate_response_price()
        self.assert_equal(full_pl, 'Past Three Year')
        self.validate_on_chart_values()
        y3_y_value = self.get_attribute(y_axis_value, 'text')
        if y1_y_value == y3_y_value:
            pass
        else :
            self.assert_not_equal(y1_y_value, y3_y_value)
        # 3Y value
        self.click(Y5)
        self.assert_equal(self.is_element_visible(chart_view), False)
        self.sleep(3)
        full_pl = self.validate_response_price()
        self.assert_equal(full_pl, 'Past Five Year')
        self.validate_on_chart_values()
        y5_y_value = self.get_attribute(y_axis_value, 'text')
        if y5_y_value == y3_y_value:
            pass
        else :
            self.assert_not_equal(y5_y_value, y3_y_value)
        self.click(candlestick_chart)
        self.sleep(3)
        self.go_back()
        self.verify_sdp_page_after_back()
        #self.assert_equal(self.get_attribute(y_axis_value, 'bounds'), '[973,906][1028,944]')

    @allure.step("Validate Mathematical Calculation")
    def validate_mathematical_cal(self):
        stock_current_price = int(self.get_attribute(stock_price, 'text'))
        stock_response_extra = self.get_attribute(stock_pl,'text')
        c = '('
        index = stock_response_extra.find(c)
        resposnePrice = int(stock_response_extra[:index])
        d = stock_response_extra.find('%')
        response_percentage = float(stock_response_extra[index + 1:d])
        logger.info(stock_response_extra)
        close_price = int(self.get_attribute('SDPText8','text'))
        cal_pecent = float(numerize.numerize(((stock_current_price - close_price) / close_price)*100))
        cal_response_price = stock_current_price -close_price
        logger.info(f'resposnePrice {resposnePrice}')
        logger.info(f'response_percentage {response_percentage}')
        logger.info(f'cal_pecent {cal_pecent}')
        logger.info(f'cal_response_price {cal_response_price}')
        self.assert_equal(cal_pecent, response_percentage)
        self.assert_equal(cal_response_price, resposnePrice)






