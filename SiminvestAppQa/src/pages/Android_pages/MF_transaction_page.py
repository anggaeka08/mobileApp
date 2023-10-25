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
mf_entry_1_date = 'ReksadanaEnrty0Date'
mf_entry_1 = 'ReksadanaEnrty0'
mf_entry_2 = 'ReksadanaEnrty1'
mf_order_details_header = 'MFOderDetailsHeader'
back_btn_order_details_page = '//android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.ImageView'
order_details_status = 'ReksadanaEnrtyundefinedStatus0'
order_id_order_details = 'MFOderDetailsOderIDValue'
date_order_d = 'MFOderDetailsTanggalValue'
od_product_details = 'MFOderDetailsProdukValue'
od_unit_value = 'MFOderDetailsUnitValue'
od_total_value = 'android.view.ViewGroup/android.widget.TextView[20]'
trans_od_header = '(//android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.TextView)[1]'
value_of_mf_confirm = '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]/android.widget.TextView[3]'
bank_account_confirm = '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView[2]'
bank_name_confirm = '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView[3]'
jumlah_yang_value_confirm = '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.TextView[2]'
mf_value_confirm = '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]/android.widget.TextView[3]'
mf_nav_value_confirm = '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]/android.widget.TextView[5]'
mf_buy_date_confirm = '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]/android.widget.TextView[6]'
mf_processing_fee_confirm = '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]/android.widget.TextView[8]'
mf_total_value_confirm = '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]/android.widget.TextView[12]'
arrow_on_confirm = '//android.view.ViewGroup[4]/android.view.ViewGroup[1]/android.widget.ImageView'
confirm_permission_reminder =  'knfirmasi_pmesnan_text_reminder'
confirm_check_status = 'knfirmasi_pmesnan_btn_status_bayar'
confirm_kembali = 'knfirmasi_pmesnan_btn_back_beranda'

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

    @allure.step("validate redirection for jual entry")
    def validate_redirection_for_jual_entry(self):
        order_status = self.get_attribute(mf_entry_1_status, 'text')
        unit_tran = self.get_attribute(mf_entry_1_unit_value,'text')
        value_tran = self.get_attribute(mf_entry_1_total_value,'text')
        date_tran = self.get_attribute(mf_entry_1_date,'text')
        self.click(mf_entry_1)
        self.sleep(1)
        self.assert_equal(self.is_element_visible(mf_order_details_header), True)
        self.assert_equal(self.get_attribute(order_details_status,'text'), order_status)
        date_order_details = self.get_attribute(date_order_d, 'text')
        unit_order_details = self.get_attribute(od_unit_value, 'text')
        value_order_details = self.get_attribute(od_total_value, 'text')
        for i in range(14,21,2):
            self.assert_not_equal(self.get_attribute(f'//android.view.ViewGroup/android.widget.TextView[{i}]','text'),'-')
        order_id_1 = self.get_attribute(order_id_order_details,'text')
        self.assert_equal(date_order_details, date_tran)
        self.assert_equal(unit_tran, unit_order_details)
        self.assert_equal(value_tran, value_order_details)
        self.click(back_btn_order_details_page)
        self.sleep(1)
        self.assert_equal(self.is_element_visible(mf_entry_1), True)
        self.click(mf_entry_1)
        self.sleep(1)
        self.assert_equal(self.is_element_visible(mf_order_details_header), True)
        self.go_back()
        self.sleep(1)
        self.assert_equal(self.is_element_visible(mf_entry_1), True)
        self.click(mf_entry_2)
        self.sleep(1)
        order_id_2 = self.get_attribute(order_id_order_details, 'text')
        self.assert_not_equal(order_id_2, order_id_1)
        self.go_back()
        self.sleep(1)

    @allure.step("Validate orderDetails for without payment proof transaction")
    def validate_orderDetails_for_without_payment_proof_transaction(self):
        self.click(mf_entry_1)
        self.assert_equal(self.is_element_visible(all_Status), True)
        self.click(process_btn)
        self.assert_equal(self.is_element_visible(trans_od_header),True)
        self.assert_equal(self.is_element_visible(value_of_mf_confirm), True)
        self.assert_equal(self.is_element_visible(bank_account_confirm), True)
        self.assert_equal(self.is_element_visible(bank_name_confirm), True)
        self.assert_equal(self.is_element_visible(jumlah_yang_value_confirm), True)
        self.assert_equal(self.is_element_visible(mf_value_confirm), True)
        self.assert_equal(self.is_element_visible(mf_nav_value_confirm), True)
        self.assert_equal(self.is_element_visible(mf_buy_date_confirm), True)
        self.assert_equal(self.is_element_visible(mf_processing_fee_confirm), True)
        self.assert_equal(self.is_element_visible(mf_total_value_confirm), True)
        self.assert_equal(self.is_element_visible(confirm_permission_reminder), True)
        self.click(arrow_on_confirm)
        self.assert_equal(self.is_element_visible(value_of_mf_confirm), False)
        self.click(arrow_on_confirm)
        self.assert_equal(self.is_element_visible(value_of_mf_confirm), True)
        self.click(confirm_check_status)
        self.sleep(2)
        self.assert_equal(self.is_element_visible(all_Status), True)
        self.click(process_btn)
        self.assert_equal(self.is_element_visible(trans_od_header),True)
        self.scroll_up()
        self.sleep(1)
        self.click(confirm_kembali)
        self.sleep(2)
        self.assert_equal(self.is_element_visible(reksadana_list_1), True)

    @allure.step("validate payment upload proof")
    def validate_payment_proof_upload_option_validation(self):
        self.click(process_btn)
        self.sleep(1)
        self.assert_equal(self.is_element_visible(order_details_page_header), True)
        self.click(upload_bukti_bayar)
        self.sleep(1)
        self.click('//android.widget.TextView[@text="Cancel"]')
        self.sleep(2)
        self.assert_equal(self.is_element_visible(upload_bukti_bayar), True)
        self.click(upload_bukti_bayar)
        self.sleep(1)
        self.go_back()
        self.sleep(2)
        self.assert_equal(self.is_element_visible(upload_bukti_bayar), True)
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
        self.go_back()
        self.sleep(2)
        self.assert_equal(self.is_element_visible(upload_bukti_bayar), True)
       # self.click('//android.widget.TextView[@text="Unggah Gambar"]')
        #self.sleep(4)

