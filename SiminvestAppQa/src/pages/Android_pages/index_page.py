import pytest
from selenium.common.exceptions import NoSuchElementException
from SiminvestAppQa.src.data.userData import user_data
import allure
import logging as logger
from SiminvestAppQa.src.pages.Android_pages.stock_detail_page import StockDetailPage
from SiminvestAppQa.src.utilities.requestUtilities import RequestsUtilities
from datetime import datetime

#locators
search_field= 'StockSearch'
search_btn_index = 'IndeksPageSearchBtn'
search_type = 'StockSearchType'
search_entry_stock_code = '(//android.widget.TextView[@content-desc="StockSearchCode"])[1]'
search_entry_stock_name = '(//android.widget.TextView[@content-desc="StockSearchName"])[1]'
search_entry_reksadana = '//android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]'
search_close_btn = '//android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]'
special_notation = '//android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup'


class IndexPage(StockDetailPage):

    @allure.step("Open index page")
    def open_index_page(self, number):
        self.login_and_verify_homepage_for_reg_user(number)
        self.click_on_indeks_btn()
        self.sleep(2)
        self.verify_indeks_page()

    @allure.step("Validate header movement")
    def validate_header_movement(self):
        self.verify_indeks_page()

    @allure.step("Open search on index page")
    def open_search_on_index_page(self):
        self.click(search_btn_index)
        self.sleep(2)

    @allure.step("verify redirection for search option")
    def verify_redirection_for_search_option(self):
        self.assert_equal(self.get_attribute(search_field, 'text'), 'Cari saham atau reksadana')
        self.verify_keyboard_on_off(True)
        self.tap_by_coordinates(x=744, y=901)
        self.verify_keyboard_on_off(False)

    @allure.step("Verify search saham & reksadana from search box")
    def Verify_search_saham_reksadana_from_search_box(self):
        self.update_text(search_field, 'A')
        self.sleep(2)
        self.assert_equal(self.get_attribute(search_type, 'text'), 'SAHAM')
        self.assert_equal(self.is_element_visible(search_entry_stock_code), True)
        self.assert_equal(self.is_element_visible(search_entry_stock_name), True)
        self.update_text(search_field, 'Danamas')
        self.assert_equal(self.get_attribute(search_type, 'text'), 'REKSADANA')
        self.assert_equal(self.is_element_visible(search_entry_reksadana), True)
        self.update_text(search_field, 'DEFI')
        self.assert_equal(self.is_element_visible(special_notation), True)
        self.update_text(search_field, 'A')
        self.click(search_entry_stock_code)
        self.sleep(3)
        self.verify_sdp_page()
        self.click_on_back_btn()
        self.assert_equal(self.is_element_visible(search_entry_stock_code), True)
        self.click(search_entry_stock_code)
        self.sleep(3)
        #self.verify_sdp_page()
        self.go_back()
        self.sleep(2)
        self.assert_equal(self.is_element_visible(search_entry_stock_code), True)
        self.update_text(search_field, 'Danamas')
        self.sleep(2)
        self.click(search_entry_reksadana)
        self.go_back()
        self.assert_equal(self.is_element_visible(search_entry_reksadana), True)
        self.update_text(search_field, 'A')
        self.scroll_up()
        self.assert_equal(self.is_element_visible(search_field), True)
        self.sleep(2)


    @allure.step("search close")
    def search_close(self):
        #self.click(search_close_btn)
        self.go_back()
        self.sleep(2)

    @allure.step("click verification on index entry")
    def click_verification_on_index_entry(self):
        self.scroll_down()
        self.click('IndeksPageEntry0')
        self.validate_header_movement()