from SiminvestAppQa.src.data.userData import user_data
from SiminvestAppQa.src.pages.Android_pages.amend_page import AmendProcess
import time
import allure
import logging as logger

cancel_confirmation ='//*[@text="Ya"]'
Cancel_btn_Confirmation_pop = '//*[@text="Tidak"]'
trans_entry_1 = 'status_label_0'
status_on_trasction_page = 'status_label_0'
order_id = '//*[@text="Order ID"]'
tanggal = '//*[@text="Tanggal Pembelian"]'
produk ='//*[@text="Produk"]'
harga = '//*[@text="Harga"]'
Lot = '//*[@text="Lot Dipesan"]'
Lot_s = '//*[@text="Lot Selesai"]'
jumlah = '//*[@text="Jumlah Selesai"]'
Biaya = '//*[@text="Biaya"]'
market_close_message_lct = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView[1]'
market_close_message = 'Bursa Tidak Beroperasi'
ok_btn_close = '//*[@text="OK"]'
order_update_pop_text = '//android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView[1]'
cancel_confirmation_pop = '//android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[2]'
class CancelProcess(AmendProcess):

    @allure.step("Click on ok btn")
    def click_on_cancel_confirmation_btn(self):
        self.sleep(1)
        self.click(cancel_confirmation)

    @allure.step("validate place order success text")
    def validate_place_order_success_text(self):
        self.assert_equal(self.get_attribute(order_update_pop_text, 'Text'), 'Pembatalan Order Terkirim')

    @allure.step("validate place order success text")
    def validate_place_order_confirmation_pop_up(self):
        self.assert_equal(self.get_attribute(cancel_confirmation_pop, 'Text'), 'Apakah kamu ingin membatalkan order ini?')

    @allure.step("Verify transaction on transaction page after cancel")
    def verify_transaction_on_transaction_page_after_cancel(self):
        self.sleep(2)
        trans_entry_1_presence = self.is_element_visible(trans_entry_1)
        assert trans_entry_1_presence == True, f"trans_entry_1  available on transaction page"
        #self.assert_equal(self.get_attribute(status_on_trasction_page, "text"), 'WITHDRAW')

    @allure.step("Verify grammatical error on order status page")
    def verify_grammatical_error_on_order_status_page(self):
        self.assert_equal(self.get_attribute(order_id, "text"), 'Order ID')
        self.assert_equal(self.get_attribute(tanggal, "text"), 'Tanggal Pembelian')
        self.assert_equal(self.get_attribute(produk, "text"), 'Produk')
        self.assert_equal(self.get_attribute(harga, "text"), 'Harga')
        self.assert_equal(self.get_attribute(Lot, "text"), 'Lot Dipesan')
        self.assert_equal(self.get_attribute(Lot_s, "text"), 'Lot Selesai')
        self.assert_equal(self.get_attribute(jumlah, "text"), 'Jumlah Selesai')
        self.assert_equal(self.get_attribute(Biaya, "text"), 'Biaya')

    @allure.step("Click on cancel btn at confirmation pop up")
    def click_on_click_cancel_btn_at_confirmation_pop_up(self):
        self.click(Cancel_btn_Confirmation_pop)

    @allure.step("Verify error message after exchange hour")
    def verify_error_message_after_exchange_market(self):
        error_message_text = self.get_attribute(market_close_message_lct, "text")
        self.assert_equal(error_message_text, market_close_message)

    @allure.step("click on ok after market close")
    def click_on_ok_btn_after_market_close(self):
        self.click(ok_btn_close)
        self.sleep(2)

    @allure.step("click on ok")
    def click_on_ok_btn(self):
        self.click(ok_btn_close)
        self.sleep(2)
