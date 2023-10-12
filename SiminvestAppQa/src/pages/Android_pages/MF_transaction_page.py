import datetime
from datetime import datetime,date,timedelta
from SiminvestAppQa.src.pages.Android_pages.amend_page import AmendProcess
from  numerize import numerize
from SiminvestAppQa.src.data.userData import user_data
import allure
import logging as logger
import time
from SiminvestAppQa.src.utilities.requestUtilities import RequestsUtilities
request_utilities = RequestsUtilities()

#locator of transaction page
saham_tab = 'Saham_tab'
reksadana_tab = 'Reksadana_tab'
default_orderlist_selected = '(//android.view.ViewGroup[@content-desc="ReksadanaOrderlist"])[1]'
default_orderlist_riwayat = '(//android.view.ViewGroup[@content-desc="ReksadanaOrderlist"])[2]'
riwayat_selected_orderlist = '(//android.view.ViewGroup[@content-desc="ReksadanaRiwayat"])[1]'
riwayat_selected_riwayat = '(//android.view.ViewGroup[@content-desc="ReksadanaRiwayat"])[2]'
all_types = '//android.widget.TextView[@text="All Types"]'
all_Status = '//android.widget.TextView[@text="All Status"]'
all_type_click_sign = '//android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ImageView'
buy_Status = '//android.widget.TextView[@text="Buy"]'
Sell_Status = '//android.widget.TextView[@text="Sell"]'
Switching_Status = '//android.widget.TextView[@text="Switching"]'
InProgress_Status = '//android.widget.TextView[@text="In Progress"]'
awaiting_payement_Status = '//android.widget.TextView[@text="Awaiting Payment"]'
Rejetced_Status = '//android.widget.TextView[@text="Rejected"]'
completed_Status = '//android.widget.TextView[@text="Completed"]'
class MF_Transaction(AmendProcess):

    @allure.step("Verify default redirection when user land on transaction page")
    def verify_default_redirection_when_user_land_on_transaction_page(self):
        self.click(reksadana_tab)
        self.sleep(2)
        self.assert_equal(self.is_element_visible(default_orderlist_selected), True)
        self.assert_equal(self.is_element_visible(default_orderlist_riwayat), True)
        self.assert_equal(self.is_element_visible(all_types), True)
        self.assert_equal(self.is_element_visible(all_Status), True)
        self.click(default_orderlist_riwayat)
        self.assert_equal(self.is_element_visible(riwayat_selected_orderlist), True)
        self.assert_equal(self.is_element_visible(riwayat_selected_riwayat), True)
        self.assert_equal(self.is_element_visible(all_types), True)
        self.assert_equal(self.is_element_visible(all_Status), True)
        self.click(saham_tab)
        self.sleep(1)
        self.click(reksadana_tab)
        self.assert_equal(self.is_element_visible(default_orderlist_selected), True)
        self.assert_equal(self.is_element_visible(default_orderlist_riwayat), True)
        self.click(all_types)
        self.assert_equal(self.is_element_visible(default_orderlist_selected), False)
        self.assert_equal(self.is_element_visible(all_type_click_sign), True)
        self.go_back()
        self.click(all_Status)
        self.assert_equal(self.is_element_visible(default_orderlist_selected), False)
        self.assert_equal(self.is_element_visible(all_type_click_sign), True)
        self.go_back()
        self.click(all_types)
        self.click(buy_Status)
        for i in range(3):
            self.assert_equal(self.get_attribute(f'ReksadanaEnrty{i}BeliJual','text'), 'BELI')
        self.click('//android.widget.TextView[@text="Buy"]')
        self.click(Sell_Status)
        for i in range(3):
            self.assert_equal(self.get_attribute(f'ReksadanaEnrty{i}BeliJual','text'), 'JUAL')
        self.click('//android.widget.TextView[@text="Sell"]')
        self.click(Switching_Status)
        for i in range(3):
            self.assert_equal(self.get_attribute(f'ReksadanaEnrty{i}BeliJual', 'text'), 'Tukar Produk')
        self.click(saham_tab)
        self.sleep(2)
        self.click(reksadana_tab)
        self.sleep(1)
        self.click(all_Status)
        self.click(InProgress_Status)
        for i in range(3):
            self.assert_equal(self.get_attribute(f'ReksadanaEnrty{i}Status0', 'text'), 'IN PROGRESS')
        self.click('//android.widget.TextView[@text="In Progress"]')
        self.click(awaiting_payement_Status)
        self.assert_equal(self.is_element_visible('//android.widget.TextView[@text="Order kamu kosong"]'), True)

    @allure.step("Validate scroll down reset the filter option")
    def validate_scroll_down_reset_the_filter_option(self):
        #self.scroll_down()
        self.scroll_screen(start_x=686, start_y=785, end_x=675, end_y=2152, duration=5000)
        self.sleep(2)
        self.assert_equal(self.is_element_visible(all_types), True)
        self.assert_equal(self.is_element_visible(all_Status), True)

    @allure.step("Validate switch the tab reset the filter option")
    def validate_switch_the_tab_reset_the_filter_option(self):
        self.click(all_Status)
        self.click(InProgress_Status)
        for i in range(3):
            self.assert_equal(self.get_attribute(f'ReksadanaEnrty{i}Status0', 'text'), 'IN PROGRESS')
        self.click('//android.widget.TextView[@text="In Progress"]')
        self.click(default_orderlist_riwayat)
        self.assert_equal(self.is_element_visible(all_types), True)
        self.assert_equal(self.is_element_visible(all_Status), True)

    @allure.step("validate filter option on riwayat tab")
    def validate_filter_option_on_riwayat_tab(self):
        self.click(reksadana_tab)
        self.sleep(2)
        self.click(default_orderlist_riwayat)
        self.click(all_types)
        self.assert_equal(self.is_element_visible(default_orderlist_selected), False)
        self.assert_equal(self.is_element_visible(all_type_click_sign), True)
        self.go_back()
        self.click(all_Status)
        self.assert_equal(self.is_element_visible(default_orderlist_selected), False)
        self.assert_equal(self.is_element_visible(all_type_click_sign), True)
        self.go_back()
        self.click(all_types)
        self.click(buy_Status)
        for i in range(3):
            self.assert_equal(self.get_attribute(f'ReksadanaEnrty{i}BeliJual','text'), 'BELI')
        self.click('//android.widget.TextView[@text="Buy"]')
        self.click(Sell_Status)
        for i in range(3):
            self.assert_equal(self.get_attribute(f'ReksadanaEnrty{i}BeliJual','text'), 'JUAL')
        self.click('//android.widget.TextView[@text="Sell"]')
        self.click(Switching_Status)
        for i in range(3):
            self.assert_equal(self.get_attribute(f'ReksadanaEnrty{i}BeliJual', 'text'), 'Tukar Produk')
        self.click(saham_tab)
        self.sleep(2)
        self.click(reksadana_tab)
        self.sleep(1)
        self.click(default_orderlist_riwayat)
        self.sleep(1)
        self.click(all_Status)
        self.click(completed_Status)
        for i in range(3):
            self.assert_equal(self.get_attribute(f'ReksadanaEnrty{i}Status0', 'text'), 'COMPLETED')
        self.click('//android.widget.TextView[@text="Completed"]')
        self.click(Rejetced_Status)
        for i in range(3):
            self.assert_equal(self.get_attribute(f'ReksadanaEnrty{i}Status0', 'text'), 'REJECTED')