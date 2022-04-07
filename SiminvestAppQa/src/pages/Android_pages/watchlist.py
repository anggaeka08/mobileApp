from SiminvestAppQa.src.pages.Android_pages.home_page import HomePage
from SiminvestAppQa.src.data.userData import user_data
import allure
import logging as logger

default = '//*[@text="Default"]'
plus_btn = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.widget.ImageView'
watchlist_name_edit = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.EditText'
watchlist_entry_2 = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[1]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]'
watchlist_name_2 = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[1]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView'
edit_btn = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[1]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.widget.ImageView'
delete_btn = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[1]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.widget.ImageView'
select_delete_btn = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[1]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[3]/android.widget.ImageView'
name_edit = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.EditText'
simpan = '//*[@text="Simpan"]'
Hapus = '//*[@text="HAPUS"]'
Batal = '//*[@text="BATAL"]'
pop_msg = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[2]'
pop_ok_btn = '//*[@text="OK"]'
cross_btn = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.widget.ImageView'
Tambah_saham = "//*[@text='Tambah saham']"
test = "//*[@text='test']"
default_watchlist = "//*[@text='Default']"
ARTO = '//*[@text="ARTO"]'
BBCA = '//*[@text="BBCA"]'
BBRI = '//*[@text="BBRI"]'
BMRI = '//*[@text="BMRI"]'
TLKM = '//*[@text="TLKM"]'
top_gainer = '//*[@text="Top gainers"]'
top_frequency = '//*[@text="Top frequency"]'
top_gainers_prese = '//*[@text="Top gainers %"]'
top_value = '//*[@text="Top value"]'
top_volume = '//*[@text="Top Volume"]'
top_losers = '//*[@text="Top losers"]'
top_losers_prese = '//*[@text="Top losers %"]'
search_btn = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[4]/android.widget.EditText'
stock_name = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.TextView[1]'
stock_1_add = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ImageView'
stock_2_add = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ImageView'
stock_3_add = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ImageView'
watchlist_stock_entry_1 = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[5]/android.view.ViewGroup[13]/android.view.ViewGroup[2]/android.view.ViewGroup'
watchlist_stock_entry_1_homepage='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[13]/android.view.ViewGroup[2]/android.view.ViewGroup'
harga_decrease = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[2]/android.widget.ImageView'
harga_increase = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[1]/android.widget.ImageView'
lot_increase = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[4]'
lot_decrease = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup[1]'
beli_btn ='//*[@text="Beli"]'
jual_btn ='//*[@text="Jual"]'
cancel_btn = '//*[@text="CANCEL"]'
confirm_btn = '//*[@text="CONFIRM"]'
confirm_sell_btn = '//*[@text="SETUJU"]'
harga_value = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.EditText'
lot_value = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[4]/android.widget.EditText'
#market_close_message_lct_watch = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView[1]'
market_close_message_lct_watch = '//*[@text="Silahkan kembali"]'
order_jual = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[1]"
max_sell = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[5]/android.widget.ImageView'
max_sell_after_click = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[5]/android.view.ViewGroup/android.widget.ImageView'

class Watchlist(HomePage):

    @allure.step("Go to watchlist option")
    def go_to_watchlist_option_after_login(self, number):
        self.click_mulai_sekarang()
        self.type_mobile_no(number)
        self.click_selanjutnya()
        self.enter_otp(user_data['valid_otp'])
        self.enter_pin()
        self.close_home_page_banner()
        self.scroll_up()

    @allure.step("Click on plus btn")
    def click_on_plus_btn(self):
        self.click(plus_btn)

    @allure.step("Click on default btn")
    def click_on_defaults_btn(self):
        self.click(default)

    @allure.step("Click on test")
    def click_on_test(self):
        self.click(test)

    @allure.step("Enter watchlist name")
    def enter_watchlist_name(self, name):
        self.update_text(watchlist_name_edit, name)
        self.tap_by_coordinates(x=1060, y=2100)

    @allure.step("Validate watchlist Entry")
    def validate_watchlist_entry(self, name):
        self.assert_equal(self.is_element_visible(watchlist_entry_2), True)
        self.assert_equal(self.get_attribute(watchlist_name_2, "text"), name)

    @allure.step("Click to edit watchlist name")
    def click_on_edit_btn(self):
        self.click(edit_btn)

    @allure.step("Click to edit watchlist stock")
    def click_on_edit_for_stock(self):
        self.click('//*[@text="Edit"]')

    @allure.step("Edit watchlist name")
    def edit_watchlist_name(self):
        self.set_text(name_edit, 'test')

    @allure.step("Click on Simpan")
    def click_on_simpan(self):
        self.click(simpan)

    @allure.step("Click on Hapus")
    def click_on_Hapus(self):
        self.click(Hapus)

    @allure.step("Click on Batal")
    def click_on_Batal(self):
        self.click(Batal)

    @allure.step("Click on delete")
    def click_on_delete(self):
        self.click(delete_btn)

    @allure.step("Click on selected watchlist delete")
    def click_on_selected_watchlist(self):
        self.click(select_delete_btn)

    @allure.step("Delete the created watchlist")
    def Cancel_delete_and_delete_watchlist(self):
        self.click(delete_btn)
        self.click_on_Batal()
        self.assert_equal(self.is_element_visible(watchlist_entry_2), True)
        self.click(delete_btn)
        self.click_on_Hapus()
        self.assert_equal(self.is_element_visible(watchlist_entry_2), False)

    @allure.step("Validate pop msg")
    def validate_pop_message(self):
        self.assert_equal(self.is_element_visible(pop_msg), True)
        self.click(pop_ok_btn)

    @allure.step("Click on cross btn")
    def click_on_cross_btn(self):
        self.click(cross_btn)

    @allure.step("Click on watchlist entry 2")
    def click_on_watchlist_entry_2(self):
        self.click(watchlist_entry_2)

    @allure.step("Validate empty msg in watchlist")
    def empty_watchlist_msg(self):
        self.assert_equal(self.get_attribute(Tambah_saham, "text"), "Tambah saham")

    @allure.step("Click on Tambah saham")
    def click_on_tambah_saham(self):
        self.click(Tambah_saham)

    @allure.step("small scroll up")
    def scroll_ups(self):
        self.sleep(2)
        self.scroll_screen(start_x=374, start_y=2057, end_x=435, end_y=1729, duration=10000)

    @allure.step("Validate default watchlist")
    def validate_default_watchlist(self):
        self.assert_equal(self.is_element_visible(default_watchlist), True)

    @allure.step("Verify top gainer")
    def verify_top_gainer_presence(self):
        self.assert_equal(self.is_element_visible(top_gainer), True)

    @allure.step("click on top gainer")
    def click_on_top_gainer(self):
        self.click(top_gainer)

    @allure.step("Verify tambahkan page")
    def verify_stock_type_selection(self):
        self.assert_equal(self.is_element_visible(top_frequency), True)
        self.assert_equal(self.is_element_visible(top_gainers_prese), True)
        self.assert_equal(self.is_element_visible(top_value), True)
        self.assert_equal(self.is_element_visible(top_volume), True)
        self.assert_equal(self.is_element_visible(top_losers), True)
        self.assert_equal(self.is_element_visible(top_losers_prese), True)

    @allure.step("Availability check Stock list in default watchlist")
    def validate_avail_check_for_stock_on_watchlist(self):
        self.assert_equal(self.is_element_visible(ARTO), True)
        self.assert_equal(self.is_element_visible(BBCA), True)
        self.assert_equal(self.is_element_visible(BBRI), True)
        self.assert_equal(self.is_element_visible(BMRI), True)
        self.assert_equal(self.is_element_visible(TLKM), True)

    @allure.step("Search stock")
    def search_stock(self, Value):
        self.update_text(search_btn, Value)
        self.sleep(3)

    @allure.step("Verify Stock Search")
    def verify_stock_search_by_full_code(self):
        self.assert_equal(self.get_attribute(stock_name, "text"), "ARGO")

    @allure.step("Verify stock after search by single character")
    def verify_stock_list_after_single_character_search(self):
        self.assert_equal(self.is_element_visible(stock_1_add), True)
        self.assert_equal(self.is_element_visible(stock_2_add), True)
        self.assert_equal(self.is_element_visible(stock_3_add), True)

    @allure.step("Click to add or remove")
    def click_to_add_remove(self):
        self.click(stock_1_add)

    @allure.step("Verify stock available in watchlist")
    def verify_stock_available(self, Value):
        self.assert_equal(self.is_element_visible(f"//*[@text='{Value}']"), True)

    @allure.step("Click_on_ok_btn")
    def click_on_ok(self):
        self.click("//*[@text='OK']")

    @allure.step("Stock list available on page")
    def stock_list_available_on_page(self):
        elements = self.find_elements(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView")
        logger.info(elements)

    @allure.step("Verify delete btn")
    def verify_delete_btn(self):
        self.assert_equal(self.is_element_visible(delete_btn), False)

    @allure.step("Verify watchlist entry")
    def verify_watchlist_entry(self):
        self.assert_equal(self.is_element_visible(watchlist_stock_entry_1), True)

    @allure.step("Click on watchlist stock")
    def click_on_stock_code_in_watclist(self):
        self.click(watchlist_stock_entry_1_homepage)
        self.sleep(2)

    @allure.step("swipe right")
    def swipe_right(self):
        self.sleep(1)
        self.scroll_screen(start_x=248, start_y=1897, end_x=733, end_y=1900, duration=10000)

    @allure.step("swipe left for without buy")
    def swipe_left_without_buy(self):
        self.sleep(1)
        self.scroll_screen(start_x=733, start_y=1900, end_x=248, end_y=1897, duration=10000)

    @allure.step("swipe left for without buy")
    def swipe_left_with_buy(self):
        self.sleep(1)
        self.scroll_screen(start_x=782, start_y=1572, end_x=244, end_y=1710, duration=10000)

    @allure.step("harga increase")
    def harga_increase(self):
        self.click(harga_increase)

    @allure.step("Harga value")
    def harga_value(self):
        return self.get_attribute(harga_value, "text")


    @allure.step("lot value")
    def lot_value(self):
        return self.get_attribute(lot_value, "text")

    @allure.step("change lot value")
    def change_lot_value(self):
        self.click(lot_value)
        self.tap_by_coordinates(x=1060, y=2000)

    @allure.step("harga decrease")
    def harga_decrease(self):
        self.click(harga_decrease)

    @allure.step("lot increase")
    def lot_increase(self):
        self.click(lot_increase)

    @allure.step("lot decrease")
    def lot_decrease(self):
        self.click(lot_decrease)

    @allure.step("Click on beli")
    def click_on_beli(self):
        self.click(beli_btn)

    @allure.step("Click on jual")
    def click_on_jual(self):
        self.click(jual_btn)

    @allure.step("Click on confirm")
    def click_on_confirm_btn(self):
        self.click(confirm_btn)

    @allure.step("verify trasaction page or market close message")
    def verify_trasaction_page_or_market_close(self):
        message = self.is_element_visible(market_close_message_lct_watch)
        logger.info(message)
        if (self.is_element_visible(market_close_message_lct_watch)) == True:
            self.click_on_ok()
        else :
            self.verify_transaction_page()

    @allure.step("Verify half card for sell")
    def verify_half_card_for_sell(self):
        self.assert_equal(self.is_element_visible(order_jual), True)

    @allure.step("Click on max sell")
    def click_on_max_sell(self):
        self.click(max_sell)

    @allure.step("Click on max sell after click")
    def unclick_on_max_sell(self):
        self.click(max_sell_after_click)

    @allure.step("Click on max sell after click")
    def click_on_confirm_sell(self):
        self.click(confirm_sell_btn)


