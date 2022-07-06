from SiminvestAppQa.src.pages.Android_pages.amend_page import AmendProcess
from SiminvestAppQa.src.data.userData import user_data
import allure
import logging as logger
from datetime import date


GTC_list ='TransactionPageSahamHeader3'
search_oderlist = 'TransactionSahamOrderListSearchBox'
date_last_trans='AmendPageTanggalValue'
rekshadana_tab ='(//android.widget.TextView[@content-desc="TranasactionPageSahamText"])[2]'
order_kamu = '//android.widget.TextView[@text="Order kamu kosong"]'
saham_tab = '(//android.widget.TextView[@content-desc="TransactionPageReksadanaText"])[1]'
All_types = 'TransactionSahamOrderListDropDown'
buy_all = '//android.widget.CheckedTextView[@text="Buy"]'
sell_all ='//android.widget.CheckedTextView[@text="Sell"]'
BS = 'OrderListEntry0BS'
all_status_reks = 'ReksadanaAllStatus'
all_types_reks = 'ReksadanaAllTypes'
orderlist_rek = '(//android.widget.TextView[@content-desc="ReksadanaOrderlistText"])[1]'
riwayat = '(//android.widget.TextView[@content-desc="ReksadanaOrderlistText"])[2]'
entry_status = 'ReksadanaEnrty0Status0'
all_status_choice = '//android.widget.CheckedTextView[@text="All Status"]'
inprogress = '//android.widget.CheckedTextView[@text="In Progress"]'
awaiting_payment = '//android.widget.CheckedTextView[@text="Awaiting Payment"]'

today = date.today()

class Transaction(AmendProcess):

    @allure.step("Verify last transaction in orderlist")
    def verify_last_transaction_orderlist(self):
        self.open_status_page_of_buy_order()
        date_trans = self.get_attribute(date_last_trans, 'text')
        c = ','
        index = date_trans.find(c)
        d1 = date_trans[:index]
        d2 = today.strftime("%d %B, %Y")
        c = ','
        index = d2.find(c)
        d3 = d2[1:index-1]
        self.assert_equal(d1, d3)

    @allure.step("Click on GTC tab")
    def click_on_gtc_tab(self):
        self.click(GTC_list)

    @allure.step("Verify GTC tab entries")
    def verify_GTC_tab_entries(self):
        self.sleep(3)
        for i in range(0,9):
            self.is_element_visible(f'GTCListEntry{i}Date')

    @allure.step("Verify search bar")
    def verify_search_bar(self):
        self.set_text(search_oderlist, 'REAL')
        self.assert_equal(self.get_attribute(search_oderlist,'text'), 'REAL')

    @allure.step("Click to reksadana")
    def click_to_reksadana(self):
        self.click(rekshadana_tab)

    @allure.step("Verify Reksadana tab")
    def verify_reksadana_tab(self):
        self.sleep(3)
        self.assert_equal(self.is_element_visible(order_kamu), True)

    @allure.step("Click to saham")
    def click_to_saham(self):
        self.click(saham_tab)

    @allure.step("Verify Saham tab")
    def verify_saham_tab(self):
        self.sleep(3)
        self.assert_equal(self.is_element_visible(All_types), True)

    @allure.step("Click to All types")
    def click_to_all_types(self):
        self.click(All_types)

    @allure.step("Verify all types values")
    def verify_all_types_values(self):
        self.sleep(3)
        self.assert_equal(self.is_element_visible(buy_all), True)
        self.assert_equal(self.is_element_visible(sell_all), True)

    @allure.step("Click on buy")
    def click_on_buy_all(self):
        self.click(buy_all)

    @allure.step("Click on sell")
    def click_on_sell_all(self):
        self.click(sell_all)

    @allure.step("Verify transaction page for buy all")
    def verify_transaction_page_for_buy_all(self):
        self.sleep(3)
        for i in range(0,9):
            self.assert_equal(self.get_attribute(f'OrderListEntry{i}BS', 'text'), 'BUY')

    @allure.step("Verify transaction page for sell")
    def verify_transaction_page_for_sell_all(self):
        self.sleep(3)
        for i in range(0,9):
            self.assert_equal(self.get_attribute(f'OrderListEntry{i}BS', 'text'), 'SELL')

    @allure.step("Verify all types and all status btn")
    def verify_all_types_and_all_status_btn(self):
        self.sleep(3)
        self.assert_equal(self.is_element_visible(all_status_reks), True)
        self.assert_equal(self.is_element_visible(all_types_reks), True)

    @allure.step("Verify orderlist and riwayat tab")
    def verify_orderlist_and_riwayat_tab(self):
        self.assert_equal(self.is_element_visible(orderlist_rek), True)
        self.assert_equal(self.is_element_visible(riwayat), True)

    @allure.step("Verify status available in entries")
    def verify_status_available_in_entries(self):
        self.assert_equal(self.is_element_visible(entry_status), True)

    @allure.step("Click on all status btn")
    def click_on_all_status_btn(self):
        self.click(all_status_reks)

    @allure.step("Verify option in all status btn")
    def verify_option_in_all_status_btn(self):
        self.sleep(2)
        self.assert_equal(self.is_element_visible(all_status_choice), True)
        self.assert_equal(self.is_element_visible(inprogress), True)
        self.assert_equal(self.is_element_visible(awaiting_payment), True)

    @allure.step("Click on In Progress")
    def click_on_in_progress(self):
        self.click(inprogress)

    @allure.step("Verify status after sorting by inprogress")
    def verify_status_after_sorting_by_inprogress(self):
        self.sleep(2)
        self.assert_equal(self.get_attribute(entry_status, 'text'), 'IN PROGRESS')

    @allure.step("Verify status after sorting by awaitning payemnt")
    def verify_status_after_sorting_by_awaitning_payemnt(self):
        self.sleep(2)
        self.assert_equal(self.get_attribute(entry_status, 'text'), 'Awaiting Payment')


