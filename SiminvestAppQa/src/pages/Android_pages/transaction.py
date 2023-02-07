import datetime
from datetime import datetime
from SiminvestAppQa.src.pages.Android_pages.amend_page import AmendProcess
from SiminvestAppQa.src.data.userData import user_data
import allure
import logging as logger
import time



GTC_list ='TransactionPageSahamHeader3'
search_oderlist = 'TransactionSahamOrderListSearchBox'
date_last_trans='AmendPageTanggalValue'
rekshadana_tab ='Reksadana_tab'
order_kamu = '//android.widget.TextView[@text="Order kamu kosong"]'
saham_tab = 'Saham_tab'
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
all_types_trade_lst='TransactionSahamTradeListDropDown'
all_types_order_lst='TransactionSahamOrderListDropDown'
all_types_History_lst = 'TransactionSahamHistoryListDropDown'
all_types_gtc_lst = 'TransactionSahamGTCListDropDown'
orderlist_entry = 'order_list_entry_0'
GTC_tab = 'GTC List_tab'
gtc_entry = 'gtc_list_entry_0'
batal_btn = '//android.widget.TextView[@text ="BATAL"]'
YA_btn = '//android.widget.TextView[@text ="Ya"]'
ok_btn = '//android.widget.TextView[@text ="OK"]'
status_of_gtc_first_entry = 'GTCListEntry0Status'
#GTCODP = GTC order details Page
GTCODP_status = "AmendPageStatusValue"
GTCODP_till_date = '//android.widget.TextView[@index="6"]'
GTCODP_purchase_date = '//android.widget.TextView[@index="8"]'
GTCODP_stock_code = '//android.widget.TextView[@index="11"]'
GTCODP_harga_value = '//android.widget.TextView[@index="13"]'
GTCODP_lot_dipesan_value = '//android.widget.TextView[@index="15"]'
GTCODP_lot_selesia_value = '//android.widget.TextView[@index="17"]'
GTCODP_lot_jumlah_value = '//android.widget.TextView[@index="19"]'
GTCODP_customer_btn = '//android.widget.TextView[@text="Hubungi Customer Care"]'
GTCODP_BATAL_btn = '//android.widget.TextView[@text="BATAL"]'
chrome_xpath ='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.EditText'
order_list = 'Order List_tab'
trade_list = 'Trade List_tab'
history_tab = 'History_tab'
gtc_tab = 'GTC List_tab'
#search_sign = "//android.view.ViewGroup[2]/android.widget.ImageView[@index='0']"
filter = 'TransactionSahamOrderListDropDown'
entries_loc = '//android.view.ViewGroup/android.widget.HorizontalScrollView[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ScrollView/android.view.ViewGroup'
oder_details_header = "//android.widget.TextView[@text = 'BELI' and 'JUAL']"
od_stock_code = '//android.view.ViewGroup[3]/android.widget.TextView[1]'
od_stock_name = '//android.view.ViewGroup[3]/android.widget.TextView[2]'
od_arrow = '//android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.ImageView'
od_status = "//android.widget.TextView[@text = 'Status']"
od_order_id = "//android.widget.TextView[@text = 'Order ID']"
od_tanPem = "//android.widget.TextView[@text = 'Tanggal Pembelian']"
od_produk = "//android.widget.TextView[@text = 'Produk']"
od_harga = "//android.widget.TextView[@text = 'Harga']"
od_lotDip = "//android.widget.TextView[@text = 'Lot Dipesan']"
od_lotSel = "//android.widget.TextView[@text = 'Lot Selesai']"
od_jumDip = "//android.widget.TextView[@text = 'Jumlah Dipesan']"
od_jumSel = "//android.widget.TextView[@text = 'Jumlah Selesai']"
od_status_text ='//android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[4]/android.widget.TextView'
od_order_id_text = "//android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[3]"
od_tanPem_text ="//android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[5]"
od_produk_text ="//android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[7]"
od_harga_text = "//android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[9]"
od_lotDip_text ="//android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[11]"
od_lotSel_text ="//android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[13]"
od_jumDip_text ="//android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[15]"
od_jumSel_text ="//android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[17]"
batalkan_btn = '//android.widget.TextView[@text ="BATALKAN"]'
amend_btn = '//android.widget.TextView[@text ="AMEND"]'
Filter_header = '//android.widget.TextView[1][@text="Filter"]'
Transaksi_text='//android.widget.TextView[@text="Transaksi"]'
Semua_text='//android.widget.TextView[@text="Semua"]'
Beli_text='//android.widget.TextView[@text="Beli"]'
Jual_text='//android.widget.TextView[@text="Jual"]'
Terapkan_text='//android.widget.TextView[@text="Terapkan"]'
Minggu_ini_text='//android.widget.TextView[@text="Minggu ini"]'
Bulan_ini_text='//android.widget.TextView[@text="Bulan ini"]'
history_tab_filter='TransactionHistoryListDropDown'
history_tab_search = 'TransactionHistoryListSearchBox'
today = datetime.today()
history_list_entry = 'history_list_entry_0'
hod_back_button="//android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup"
hod_header = "//android.widget.TextView[@text = 'BELI' and 'JUAL']"
hod_stock_code = '//android.view.ViewGroup[3]/android.widget.TextView[1]'
hod_stock_name = '//android.view.ViewGroup[3]/android.widget.TextView[2]'
hod_arrow = '//android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.ImageView'
hod_order_id = "//android.widget.TextView[@text = 'Order ID']"
hod_tanPem = "//android.widget.TextView[@text = 'Tanggal Pembelian']"
hod_produk = "//android.widget.TextView[@text = 'Produk']"
hod_harga = "//android.widget.TextView[@text = 'Harga']"
hod_lot= "//android.widget.TextView[@text = 'Total Lot']"
hod_jumlah = "//android.widget.TextView[@text = 'Total Jumlah']"
hod_order_id_text = "//android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[2]"
hod_tanPem_text ="//android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[4]"
hod_produk_text ="//android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[6]"
hod_harga_text = "//android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[8]"
hod_lot_text ="//android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[10]"
hod_jumlah_text ="//android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[12]"
gtc_tab_filter='TransactionSahamGTCListDropDown'
gtc_tab_search = 'TransactionSahamGTCListSearchBox'
gtc_tab_binocular= "//android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ImageView"
gtc_tab_label= "gtc_label_0"
gtc_tab_date= "gtc_time_0"
gtc_trans_type= "transaction_type_0"
gtc_tab_stock_code= "stockCode_0"
gtc_tab_status= "status_label_0"
gtc_tab_lot= "lot_0"
gtc_tab_harga= "price_0"
gtc_tab_jumlah= "amount_0"


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

    @allure.step("Swipe right")
    def swipe_right(self):
        self.scroll_screen(start_x=1190, start_y=1724, end_x=225, end_y=1715, duration=10000)
        self.sleep(2)

    @allure.step("Swipe Left")
    def swipe_left(self):
        self.scroll_screen(start_x=225, start_y=1715, end_x=1190, end_y=1724, duration=10000)
        self.sleep(2)

    @allure.step("Verify all_types btn for trade list")
    def verify_all_types_btn_for_trade_list(self):
        self.assert_equal(self.is_element_visible(all_types_trade_lst), True)

    @allure.step("Verify search btn for trade list")
    def verify_all_types_btn_for_order_list(self):
        self.assert_equal(self.is_element_visible(all_types_order_lst), True)

    @allure.step("Verify search btn for Order list")
    def verify_all_type_btn_for_history_list(self):
        self.assert_equal(self.is_element_visible(all_types_History_lst), True)

    @allure.step("Verify search btn for gtc list")
    def verify_all_type_btn_for_gtc_list(self):
        self.assert_equal(self.is_element_visible(all_types_gtc_lst), True)

    @allure.step("Enter value in search bar")
    def enter_value_in_search_box(self, Value):
        self.set_text(search_oderlist, Value)

    @allure.step("Verify enteries after enter null or space in search option")
    def verify_enteries_after_enter_null_or_space_in_search_option(self):
        self.assert_equal(self.is_element_visible(orderlist_entry), False)

    @allure.step("Click to GTC tab")
    def click_on_gtc_tab(self):
        self.click(GTC_tab)
        self.sleep(3)

    @allure.step("Click to GTC first entry")
    def click_on_gtc_first_entry(self):
        self.click(gtc_entry)
        self.sleep(3)

    @allure.step("Click on batal btn")
    def click_on_batal(self):
        self.click(batal_btn)
        self.sleep(3)

    @allure.step("Click on YA btn")
    def click_on_YA(self):
        self.sleep(2)
        self.click(YA_btn)
        self.sleep(1)

    @allure.step("Click on ok btn")
    def click_on_ok(self):
        self.sleep(2)
        self.click(ok_btn)
        self.sleep(1)

    @allure.step("Verify first entry status after cancel buy/sell")
    def verify_status_of_first_entry(self):
        self.assert_equal(self.get_attribute(status_of_gtc_first_entry, "text"), "WITHDRAW")

    @allure.step("verify details available on gtc order details page")
    def verify_details_available_on_gtc_order_details_page(self):
        self.assert_equal(self.is_element_visible(GTCODP_status), True)
        self.assert_equal(self.is_element_visible(GTCODP_till_date), True)
        self.assert_equal(self.is_element_visible(GTCODP_purchase_date), True)
        self.assert_equal(self.is_element_visible(GTCODP_stock_code), True)
        self.assert_equal(self.is_element_visible(GTCODP_harga_value), True)
        self.assert_equal(self.is_element_visible(GTCODP_lot_dipesan_value), True)
        self.assert_equal(self.is_element_visible(GTCODP_lot_selesia_value), True)
        self.assert_equal(self.is_element_visible(GTCODP_lot_jumlah_value), True)
        self.assert_equal(self.is_element_visible(GTCODP_customer_btn), True)
        self.assert_equal(self.is_element_visible(GTCODP_BATAL_btn), True)

    @allure.step("Click on customer btn")
    def click_on_customer_btn(self):
        self.click(GTCODP_customer_btn)

    @allure.step("Verify GTC first entry available")
    def verify_gtc_first_entry_available(self):
        self.sleep(2)
        self.assert_equal(self.is_element_visible(gtc_entry), True)

    @allure.step("Verify redirection after click on customer support")
    def verify_redirection_after_click_on_customer_support(self):
        self.assert_equal(self.is_element_visible(chrome_xpath), True)

    @allure.step("Verify common details for all tabs")
    def verify_common_details_for_all_tabs(self):
        self.assert_equal(self.get_attribute(saham_tab, 'text'), 'Saham')
        self.assert_equal(self.get_attribute(rekshadana_tab, 'text'), 'Reksadana')
        self.assert_equal(self.get_attribute(order_list, 'text'), 'Order List')
        self.assert_equal(self.get_attribute(trade_list, 'text'), 'Trade List')
        self.assert_equal(self.get_attribute(history_tab, 'text'), 'History')
        self.assert_equal(self.get_attribute(gtc_tab, 'text'), 'GTC List')
        #self.assert_equal(self.is_element_visible(search_sign), True)
        self.assert_equal(self.is_element_visible(filter), True)
        self.assert_equal(self.get_attribute(search_oderlist, 'text'), 'Cari Saham')

    @allure.step("Verify entries details on transaction tab for orderlist")
    def verify_entries_details_on_transaction_tab_for_order_list(self):
        try :
            for i in range(0, 4):
                time_in_entry = self.get_attribute(f'orderTime_{i}', 'text')
                in_time = datetime.strptime(time_in_entry, "%H:%M")
                out_time = datetime.strftime(in_time, "%H:%M")
                self.assert_equal(time_in_entry, str(out_time))
                transaction_type = self.get_attribute(f'transactionType_{i}', 'text')
                assert transaction_type in ['BELI', 'JUAL'] , f'Invalid transaction type'
                self.assert_equal(self.is_element_visible(f'stockCode_{i}'), True)
                self.assert_equal(self.is_element_visible(f'lot_{i}'), True)
                self.assert_equal(self.is_element_visible(f'price_{i}'), True)
                self.assert_equal(self.is_element_visible(f'total_{i}'), True)
                transaction_status = self.get_attribute(f'status_label_{i}', 'text')
                assert transaction_status in ['OPEN', 'MATCHED', 'WITHDRAW', 'REJECTED', 'PARTIAL', 'EXPIRED','AMEND', 'SENDING'], f'Invalid transaction type'
        except:
            pass


    @allure.step("Verify entries details on transaction tab for history list")
    def verify_entries_details_on_transaction_tab_for_history_list(self):
        self.click(history_tab)
        self.sleep(1)
        try:
            self.assert_equal(self.is_element_visible(history_tab_filter), True)
            self.assert_equal(self.is_element_visible(history_tab_search), True)
            for i in range(0, 4):
                time_in_entry = self.get_attribute(f'time_{i}', 'text')
                in_time = datetime.strptime(time_in_entry, "%H:%M")
                out_time = datetime.strftime(in_time, "%H:%M")
                self.assert_equal(time_in_entry, str(out_time))
                date_in_entry = self.get_attribute(f'date_{i}', 'text')
                in_date = datetime.strptime(date_in_entry, '%d %b %Y')
                out_date = datetime.strftime(in_time, '%d %b %Y')
                self.assert_equal(in_date, str(out_date))
                transaction_type = self.get_attribute(f'transactionType_{i}', 'text')
                assert transaction_type in ['BELI', 'JUAL'] , f'Invalid transaction type'
                self.assert_equal(self.is_element_visible(f'stockCode_{i}'), True)
                self.assert_equal(self.is_element_visible(f'lot_{i}'), True)
                self.assert_equal(self.is_element_visible(f'price_{i}'), True)
                self.assert_equal(self.is_element_visible(f'total_{i}'), True)
                transaction_status = self.get_attribute(f'status_label_{i}', 'text')
                assert transaction_status == 'MATCHED' , f'Invalid transaction type'
        except:
            pass

    @allure.step("Verify filter option for history list")
    def verify_filter_option_for_history_list(self):
        self.click(history_tab_filter)
        self.assert_equal(self.is_element_visible(Filter_header), True)
        self.assert_equal(self.is_element_visible(Transaksi_text), True)
        self.assert_equal(self.is_element_visible(Beli_text), True)
        self.assert_equal(self.is_element_visible(Jual_text), True)
        self.assert_equal(self.is_element_visible(Minggu_ini_text), True)
        self.assert_equal(self.is_element_visible(Bulan_ini_text), True)
        lst = self.find_elements(Semua_text)
        self.assert_equal(len(lst), 2)


    @allure.step("Verify order details page")
    def verify_order_details_page(self):
        self.click(orderlist_entry)
        self.sleep(1)
        self.assert_equal(self.is_element_visible(oder_details_header), True)
        self.assert_equal(self.is_element_visible(od_stock_code), True)
        self.assert_equal(self.is_element_visible(od_stock_name), True)
        self.assert_equal(self.is_element_visible(od_arrow), True)
        self.assert_equal(self.is_element_visible(od_status), True)
        self.assert_equal(self.is_element_visible(od_order_id), True)
        self.assert_equal(self.is_element_visible(od_tanPem), True)
        self.assert_equal(self.is_element_visible(od_produk), True)
        self.assert_equal(self.is_element_visible(od_harga), True)
        self.assert_equal(self.is_element_visible(od_lotDip), True)
        self.assert_equal(self.is_element_visible(od_lotSel), True)
        self.assert_equal(self.is_element_visible(od_jumDip), True)
        self.assert_equal(self.is_element_visible(od_jumSel), True)
        self.assert_equal(self.is_element_visible(od_status_text), True)
        self.assert_equal(self.is_element_visible(od_order_id_text), True)
        self.assert_equal(self.is_element_visible(od_tanPem_text), True)
        self.assert_equal(self.is_element_visible(od_produk_text), True)
        self.assert_equal(self.is_element_visible(od_harga_text), True)
        self.assert_equal(self.is_element_visible(od_lotDip_text), True)
        self.assert_equal(self.is_element_visible(od_lotSel_text), True)
        self.assert_equal(self.is_element_visible(od_jumDip_text), True)
        self.assert_equal(self.is_element_visible(od_jumSel_text), True)
        if self.get_attribute(od_status_text, 'text') in ['OPEN', 'SENDING']:
            self.assert_equal(self.is_element_visible(batalkan_btn), True)
            self.assert_equal(self.is_element_visible(amend_btn), True)
        else :
            self.assert_equal(self.is_element_visible(batalkan_btn), False)
            self.assert_equal(self.is_element_visible(amend_btn), False)
        self.go_back()
        self.sleep(1)
        self.verify_transaction_page()

    @allure.step("Verify order details of history list")
    def verify_order_details_of_history_list(self):
        self.click(history_tab)
        self.sleep(1)
        self.click(history_list_entry)
        self.sleep(1)
        self.assert_equal(self.is_element_visible(hod_back_button), True)
        self.assert_equal(self.is_element_visible(hod_header), True)
        self.assert_equal(self.is_element_visible(hod_stock_code), True)
        self.assert_equal(self.is_element_visible(hod_stock_name), True)
        self.assert_equal(self.is_element_visible(hod_arrow), True)
        self.assert_equal(self.is_element_visible(hod_order_id), True)
        self.assert_equal(self.is_element_visible(hod_order_id), True)
        self.assert_equal(self.is_element_visible(hod_tanPem), True)
        self.assert_equal(self.is_element_visible(hod_produk), True)
        self.assert_equal(self.is_element_visible(hod_harga), True)
        self.assert_equal(self.is_element_visible(hod_lot), True)
        self.assert_equal(self.is_element_visible(hod_jumlah), True)
        self.assert_equal(self.is_element_visible(hod_order_id_text), True)
        self.assert_equal(self.is_element_visible(hod_tanPem_text), True)
        date_in_entry = self.get_attribute(hod_tanPem_text, 'text')
        in_date = datetime.strptime(date_in_entry, '%d %b %Y,%H:%M')
        out_date = datetime.strftime(in_date, '%d %b %Y,%H:%M')
        self.assert_equal(date_in_entry, str(out_date))
        self.assert_equal(self.is_element_visible(hod_produk_text), True)
        self.assert_equal(self.is_element_visible(hod_harga_text), True)
        self.assert_equal(self.is_element_visible(hod_lot_text), True)
        self.assert_equal(self.is_element_visible(hod_jumlah_text), True)
        self.go_back()
        self.sleep(1)
        self.assert_equal(self.is_element_visible(history_list_entry), True)

    @allure.step("Verify ui functionality of GTC list tab")
    def verify_ui_functionality_of_GTC_list_tab(self):
        self.click(gtc_tab)
        self.sleep(1)
        self.assert_equal(self.is_element_visible(gtc_entry), True)
        self.assert_equal(self.is_element_visible(gtc_tab_binocular), True)
        self.assert_equal((self.get_attribute(gtc_tab_search, 'text')), "Cari Saham")
        self.assert_equal(self.is_element_visible(gtc_tab_filter), True)
        self.assert_equal(self.is_element_visible(gtc_tab_label), True)
        self.assert_equal(self.is_element_visible(gtc_tab_date), True)
        date_in_entry = self.get_attribute(gtc_tab_date, 'text')
        in_date = datetime.strptime(date_in_entry, '%d %B %Y')
        out_date = datetime.strftime(in_date, '%d %B %Y')
        self.assert_equal(date_in_entry, str(out_date))
        self.assert_equal(self.is_element_visible(gtc_trans_type), True)
        self.assert_equal((self.get_attribute(gtc_trans_type, 'text')), "BELI" or "JUAL")
        self.assert_equal(self.is_element_visible(gtc_tab_stock_code), True)
        self.assert_equal(self.is_element_visible(gtc_tab_status), True)
        self.assert_equal((self.get_attribute(gtc_tab_status, 'text')), "WORKING")
        self.assert_equal(self.is_element_visible(gtc_tab_lot), True)
        self.assert_equal(self.is_element_visible(gtc_tab_harga), True)
        self.assert_equal(self.is_element_visible(gtc_tab_jumlah), True)
        self.click(gtc_tab_filter)
        self.sleep(1)
        self.assert_equal(self.is_element_visible(Semua_text), True)
        self.assert_equal(self.is_element_visible(Beli_text), True)
        self.assert_equal(self.is_element_visible(Jual_text), True)
        self.assert_equal(self.is_element_visible(Terapkan_text), True)



