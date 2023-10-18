import datetime
from datetime import datetime,date,timedelta
from SiminvestAppQa.src.pages.Android_pages.amend_page import AmendProcess
from SiminvestAppQa.src.pages.Android_pages.reksadana_page import ReksadanaPage
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
reksadana_list_1 = 'Top_reksadana_box1'
process_btn = '//android.view.ViewGroup[@content-desc="ReksadanaEnrty0"]/android.view.ViewGroup[5]'
order_details_page_header = '//android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.TextView'
close_konfirmasi_page = '//android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup'
upload_bukti_bayar = 'knfirmasi_pmesnan_btn_upload'
mf_entry_1_status = 'ReksadanaEnrty0Status0'
mf_entry_1_unit_value = 'ReksadanaEnrty0UnitValue'
mf_entry_1_total_value = 'ReksadanaEnrty0TotalValue'


class MF_Transaction(AmendProcess, ReksadanaPage):

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

    @allure.step("Open MF from homepage")
    def open_mf_from_homepage(self):
        self.click(reksadana_list_1)
        self.sleep(2)

    @allure.step("Validate redirection for order details page of MF")
    def validate_upload_payment_proof_for_order_details_page_of_MF(self):
        self.click(process_btn)
        self.sleep(1)
        self.assert_equal(self.is_element_visible(order_details_page_header), True)
        self.click(upload_bukti_bayar)
        self.sleep(1)
        self.click('//android.widget.TextView[@text="Camera"]')
        self.sleep(2)
       # self.click('//android.widget.TextView[@text="Allow only while using the app"]')
        self.sleep(2)
        self.click('Take photo')
        self.sleep(2)
        self.click('Done')
        self.sleep(2)
        self.click('//android.widget.TextView[@text="Unggah Gambar"]')
        self.sleep(4)
        self.assert_equal(self.is_element_visible(process_btn), False)
        self.click(close_konfirmasi_page)
        self.sleep(1)


    @allure.step("validate mf payment status")
    def validate_payment_status_on_transaction_page(self):
        status_mf= self.get_attribute(mf_entry_1_status,'text')
        self.validate_upload_payment_proof_for_order_details_page_of_MF()
        self.click(reksadana_tab)
        self.sleep(1)
        self.assert_not_equal(status_mf, self.get_attribute(mf_entry_1_status,'text'))
        self.assert_equal(self.is_element_visible(process_btn), False)
        self.assert_in(',', self.get_attribute(mf_entry_1_total_value,'text'))
        self.assert_in(',', self.get_attribute(mf_entry_1_unit_value,'text'))

    @allure.step("Sorting validation by date")
    def sorting_validation_by_date(self):
        unit = self.get_attribute(mf_entry_1_unit_value,'text')
        total_value = self.get_attribute(mf_entry_1_total_value,'text')
        date_list = []
        for i in range(4):
            date_list.append(self.get_attribute(f'ReksadanaEnrty{i}Date', 'text'))
        logger.info(date_list)
        self.assertGreater(date_list[0], date_list[1])
        return unit, total_value[3:]







