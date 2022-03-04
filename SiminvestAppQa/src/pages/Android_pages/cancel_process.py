from SiminvestAppQa.src.data.userData import user_data
from SiminvestAppQa.src.pages.Android_pages.amend_page import AmendProcess
import time
import allure
import logging as logger

cancel_confirmation ='//*[@text="Ya"]'
Cancel_btn_Confirmation_pop = '//*[@text="Tidak"]'
trans_entry_1 = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[5]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup'
status_on_trasction_page = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[5]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[2]'
order_id = '//*[@text="Order ID"]'
tanggal = '//*[@text="Tanggal Pembelian"]'
produk ='//*[@text="Produk"]'
harga = '//*[@text="Harga"]'
Lot = '//*[@text="Lot Dipesan"]'
Lot_s = '//*[@text="Lot Selesai"]'
jumlah = '//*[@text="Jumlah Selesai"]'
Biaya = '//*[@text="Biaya"]'


class CancelProcess(AmendProcess):

    @allure.step("Click on ok btn")
    def click_on_cancel_confirmation_btn(self):
        self.click(cancel_confirmation)

    @allure.step("Verify transaction on transaction page after cancel")
    def verify_transaction_on_transaction_page_after_cancel(self):
        trans_entry_1_presence = self.is_element_visible(trans_entry_1)
        assert trans_entry_1_presence == True, f"trans_entry_1  available on transaction page"
        self.assert_equal(self.get_attribute(status_on_trasction_page, "text"), 'WITHDRAW')

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
