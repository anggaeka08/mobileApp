from SiminvestAppQa.src.pages.Android_pages.home_page import HomePage
from SiminvestAppQa.src.data.userData import user_data
import allure

default = '//*[@text="Default"]'
plus_btn = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.widget.ImageView'
watchlist_name_edit = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.EditText'
watchlist_entry_2 = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[1]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]'
watchlist_name_2 = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[1]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView'
edit_btn = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[1]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.widget.ImageView'
name_edit = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.EditText'
simpan = '//*[@text="Simpan"]'
Hapus = '//*[@text="HAPUS"]'
delete_btn = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[1]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.widget.ImageView'
Batal = '//*[@text="BATAL"]'
pop_msg = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[2]'
pop_ok_btn = '//*[@text="OK"]'
cross_btn = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.widget.ImageView'

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



