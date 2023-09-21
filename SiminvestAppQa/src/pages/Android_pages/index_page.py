import pytest
from selenium.common.exceptions import NoSuchElementException
from SiminvestAppQa.src.data.userData import user_data
import allure
import logging as logger
from SiminvestAppQa.src.pages.Android_pages.stock_detail_page import StockDetailPage
from SiminvestAppQa.src.utilities.requestUtilities import RequestsUtilities
from datetime import datetime
request_utilities = RequestsUtilities()

#locators
index_page_header = 'IndeksPageHeader'
search_field= 'StockSearch'
search_btn_index = 'IndeksPageSearchBtn'
search_type = 'StockSearchType'
index_entry_1 = 'IndeksPageEntry0'
price_entry_1 = 'IndeksEntryLastPrice0'
search_entry_stock_code = '(//android.widget.TextView[@content-desc="StockSearchCode"])[1]'
search_entry_stock_name = '(//android.widget.TextView[@content-desc="StockSearchName"])[1]'
search_entry_reksadana = '//android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]'
search_close_btn = '//android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]'
special_notation = '//android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup'
last_entry_index='IndeksPageEntry49'

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
        # self.update_text(search_field, 'Danamas')
        # self.assert_equal(self.get_attribute(search_type, 'text'), 'REKSADANA')
        # self.assert_equal(self.is_element_visible(search_entry_reksadana), True)
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
        # self.update_text(search_field, 'Danamas')
        # self.sleep(2)
        # self.click(search_entry_reksadana)
        # self.go_back()
        # self.assert_equal(self.is_element_visible(search_entry_reksadana), True)
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

    @allure.step("Validate scroll up and down on index page")
    def validate_scroll_up_and_down_on_index_page(self):
        self.scroll_up()
        self.assert_equal(self.is_element_visible(index_entry_1), False)
       # self.assert_equal(self.is_element_visible(last_entry_index), True)
        self.scroll_down()
        self.assert_equal(self.is_element_visible(index_entry_1), True)

    @allure.step("Validate thousand separator and name in index entry")
    def validate_thousand_separator_and_name_in_index_entry(self):
        self.assert_equal(self.get_attribute(index_page_header, 'text'), 'Indeks')
        for i in range(5):
            self.assert_not_in(' ', self.get_attribute(f'IndeksEntryName{i}', 'text'))
            price_value = self.get_attribute(f'IndeksEntryLastPrice{i}', 'text')
            if len(price_value) >= 5:
                self.assert_in(',', price_value)

    @allure.step("validate the data with api and app ui")
    def validate_data_with_api_and_ui(self):
        ui_index_name = []
        api_index_name = []
        for i in range(11):
            ui_index_name.append(self.get_attribute(f'IndeksEntryName{i}', 'text'))
        token_value = self.login()
        token = {
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJpWlYzdUJkTkJyTDA4dVIzQUR2bmg4akdTdHNkSHpQVSIsInN1YiI6IlNpbWFzSW52ZXN0In0.Kj31bgBrbc94NaUDKWgbx-N4ZBQNFsrZBmF7xtZ4hNo"}
        token['Authorization'] = 'Bearer ' + token_value
        index_api = request_utilities.get(base_url='https://stg-api.siminvest.co.id/', endpoint='emerson/v1/index', headers=token, expected_status_code=200)
        for i in range(len(index_api['data'])):
            api_index_name.append(index_api['data'][i]['name'])
        logger.info(ui_index_name)
        logger.info(api_index_name)
        for i in range(len(ui_index_name)):
            self.assert_in(ui_index_name[i], api_index_name)

