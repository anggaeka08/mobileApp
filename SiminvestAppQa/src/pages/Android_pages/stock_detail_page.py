from SiminvestAppQa.src.data.userData import user_data
from datetime import datetime
import allure
import logging as logger
from SiminvestAppQa.src.pages.Android_pages.watchlist import Watchlist
import language_tool_python

star_without_click = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ImageView'
search_btn = 'SDPSearchBtn'
search_box = '//android.widget.EditText[@text="Cari Saham"]'
searched_stock = '//android.widget.TextView[@text="Ace Hardware Indonesia Tbk."]'
stock = '//*[@text="ACES"]'
sdp_header = 'SDPStockCode'
stock_name = 'SDPStockName'
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
pemegang = '//android.widget.TextView[@text="Pemegang Saham"]'
direksi = '//android.widget.TextView[@text="Direksi"]'
komisaris = '//android.widget.TextView[@text="Komisaris"]'
alamat = '//android.widget.TextView[@text="Alamat"]'
share_holder_1 = '//android.widget.TextView[@index="1"]'
share_holder_1_details = '//android.widget.TextView[@index="2"]'
share_holder_2 = '//android.widget.TextView[@index="3"]'
share_holder_2_details = '//android.widget.TextView[@index="4"]'
director_1 = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.HorizontalScrollView[2]/android.view.ViewGroup/android.widget.TextView[17]'
director_1_name = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.HorizontalScrollView[2]/android.view.ViewGroup/android.widget.TextView[18]'
director_2 = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.HorizontalScrollView[2]/android.view.ViewGroup/android.widget.TextView[19]'
director_2_name = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.HorizontalScrollView[2]/android.view.ViewGroup/android.widget.TextView[20]'
Commissioner_1 = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.HorizontalScrollView/android.view.ViewGroup/android.widget.TextView[19]'
Commissioner_1_name = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.HorizontalScrollView/android.view.ViewGroup/android.widget.TextView[20]'
Commissioner_2 = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.HorizontalScrollView/android.view.ViewGroup/android.widget.TextView[21]'
Commissioner_2_name = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.HorizontalScrollView/android.view.ViewGroup/android.widget.TextView[21]'
address = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.HorizontalScrollView/android.view.ViewGroup/android.widget.TextView[27]'
#address_text = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[39]'
address_text = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.HorizontalScrollView/android.view.ViewGroup/android.widget.TextView[28]'
Order_Book = '//*[@text="Order Book"]'
News = '//*[@text="News"]'
Keystats = '//*[@text="Keystats"]'
Financials = '//*[@text="Financials"]'
Profile = '//*[@text="Profile"]'
beli_btn = 'SDPBeliBtn'
#list of news date and domain
news_1= '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[13]/android.widget.TextView[2]'
news_url_1 = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[13]/android.widget.TextView[1]'
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


class StockDetailPage(Watchlist):

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

    @allure.step("Lot value list")
    def lot_bit_list(self):
        lot_bit_list = []
        lot_bit_list.append(int((self.get_attribute('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[23]', "text")).replace(',','')))
        for i in range(25, 61,4):
            lot_bit_list.append(int((self.get_attribute(
                f'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[{i}]',
                "text")).replace(',','')))
        return lot_bit_list

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
        self.assert_equal(self.is_element_visible(pemegang), True)
        self.assert_equal(self.is_element_visible(direksi), True)
        self.assert_equal(self.is_element_visible(share_holder_1), True)
        self.assert_equal(self.is_element_visible(share_holder_1_details), True)
        self.assert_equal(self.is_element_visible(share_holder_2), True)
        self.assert_equal(self.is_element_visible(share_holder_2_details), True)
        self.assert_equal(self.is_element_visible(director_1), True)
        self.assert_equal(self.is_element_visible(director_1_name), True)
        self.assert_equal(self.is_element_visible(director_2), True)
        self.assert_equal(self.is_element_visible(director_2_name), True)
        self.assert_equal(self.is_element_visible(Commissioner_1), True)
        self.assert_equal(self.is_element_visible(Commissioner_1_name), True)
        self.assert_equal(self.is_element_visible(Commissioner_2), True)
        self.assert_equal(self.is_element_visible(Commissioner_2_name), True)
        self.scroll_up_screen()
        self.assert_equal(self.is_element_visible(komisaris), True)
        self.assert_equal(self.is_element_visible(alamat), True)

    @allure.step("Verify profile details")
    def verify_details_of_profile(self):
        self.assert_not_equal(self.get_attribute(pemegang, 'text'), '-')
        self.assert_not_equal(self.get_attribute(direksi, 'text'), '-')
        self.assert_not_equal(self.get_attribute(share_holder_1, 'text'), '-')
        self.assert_not_equal(self.get_attribute(share_holder_1_details, 'text'), '-')
        self.assert_not_equal(self.get_attribute(share_holder_2, 'text'), '-')
        self.assert_not_equal(self.get_attribute(share_holder_2_details, 'text'), '-')
        self.assert_not_equal(self.get_attribute(director_1, 'text'), '-')
        self.assert_not_equal(self.get_attribute(director_1_name, 'text'), '-')
        self.assert_not_equal(self.get_attribute(director_2, 'text'), '-')
        self.assert_not_equal(self.get_attribute(director_2_name, 'text'), '-')
        self.assert_not_equal(self.get_attribute(Commissioner_1, 'text'), '-')
        self.assert_not_equal(self.get_attribute(Commissioner_1_name, 'text'), '-')
        self.assert_not_equal(self.get_attribute(Commissioner_2, 'text'), '-')
        self.assert_not_equal(self.get_attribute(Commissioner_2_name, 'text'), '-')
        self.scroll_up_screen()
        self.assert_not_equal(self.get_attribute(komisaris, 'text'), '-')
        self.assert_not_equal(self.get_attribute(alamat, 'text'), '-')

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
    def verify_news_dates_list(self):
        date_list = []
        sorted_date_list = []
        news_1_string = self.get_attribute(f'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.HorizontalScrollView[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.TextView[1]',"text")
        date_1 = news_1_string[-11:]
        date_list.append(date_1)
        self.scroll_up_screen()
        for i in range(3, 20, 2):
            news_1_string = self.get_attribute(f'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[{i}]/android.widget.TextView[1]', "text")
            date_1 = news_1_string[-11:]
            date_list.append(date_1)
        logger.info(date_list)
        fetched_date_lst = date_list
        date_list.sort(key=lambda date: datetime.strptime(date, '%d %b %Y'))
        date_list.reverse()
        sorted_date_list = date_list
        logger.info(sorted_date_list)
        self.assert_equal(fetched_date_lst, sorted_date_list)

    @allure.step("Verify news title")
    def verify_news_title(self):
        title_lst = []
        for i in range(3, 20, 2):
            news_title = self.get_attribute(
                f'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[{i}]/android.widget.TextView[2]',
                "text")
            title_lst.append(news_title)
        for i in range(len(title_lst)):
            if len(title_lst[i]) > 80:
                a = title_lst[i]
                if '.' in a :
                    logger.info(". Available after 81 string")
            else:
                logger.info("String length is not greater then 80")
        logger.info(title_lst)

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
        browser_full_url = self.get_attribute(browser_url, 'text')
        d = '/2'
        index = browser_full_url.find(d)
        browser_url_text = browser_full_url[:index]
        logger.info(browser_url_text)
        self.assert_equal(news_url, browser_url_text[12:])

    @allure.step("Validate maximum available news")
    def validate_maximum_available_news(self):
        try:
            date_list = []
            news_1_string = self.get_attribute(
                f'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.HorizontalScrollView[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.TextView[1]',
                "text")
            date_1 = news_1_string[-11:]
            date_list.append(date_1)
            self.scroll_up_screen()
            for i in range(3, 23, 2):
                news_1_string = self.get_attribute(
                    f'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[{i}]/android.widget.TextView[1]',
                    "text")
                date_1 = news_1_string[-11:]
                date_list.append(date_1)
            logger.info(date_list)
        except:
            logger.info("News not available more then 10")
            self.scroll_down()
            date_list = []
            news_1_string = self.get_attribute(
                f'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.HorizontalScrollView[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.TextView[1]',
                "text")
            date_1 = news_1_string[-11:]
            date_list.append(date_1)
            self.scroll_up_screen()
            for i in range(3, 20, 2):
                news_1_string = self.get_attribute(
                    f'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[{i}]/android.widget.TextView[1]',
                    "text")
                date_1 = news_1_string[-11:]
                date_list.append(date_1)
            self.assert_equal(len(date_list), 10)


    @allure.step("Validate all news are separated")
    def validate_all_news_are_separated(self):
        self.scroll_up_screen()
        title_lst = []
        for i in range(3, 20, 2):

            news_title = self.get_attribute(
                f'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[{i}]/android.widget.TextView[2]',
                "text")
            title_lst.append(news_title)
        for i in range(len(title_lst) - 1):
            if title_lst[i] == title_lst[i + 1]:
                logger.info("News are same")
            else:
                logger.info("News are not same")


    @allure.step('verify redirection after click on Hubungi Customer')
    def verify_redirection_after_click_on_support_btn(self):
        self.click(Hubungi)
        self.sleep(4)
        support_url_text = self.get_attribute(chrome_url,'text')
        index = support_url_text.find('.com')
        domain_name = support_url_text[:index]
        self.assert_equal(domain_name[8:], 'sinarmassekuritas.zendesk')

    @allure.step("Verify stock company address")
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
                raise "double spaces available in address"

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

        """self.scroll_up_screen()      
        title_lst = []
        my_tool = language_tool_python.LanguageTool('Eng US')
        for i in range(1, 20, 2):
            news_title = self.get_attribute(
                f'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[{i}]/android.widget.TextView[2]',
                "text")
            title_lst.append(news_title)
        for i in range(len(title_lst)):
            my_matches = my_tool.check(title_lst[i])
            logger.info(my_matches)"""



