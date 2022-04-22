from SiminvestAppQa.src.data.userData import user_data
import time
import allure
import logging as logger
from SiminvestAppQa.src.pages.Android_pages.watchlist import Watchlist

star_without_click = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ImageView'
search_btn = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.widget.ImageView'
search_box = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.EditText'
searched_stock = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup'
stock = '//*[@text="ACES"]'
watchlist ='//*[@text="Default"]'

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