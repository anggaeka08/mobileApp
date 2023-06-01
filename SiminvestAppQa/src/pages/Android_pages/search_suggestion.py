from SiminvestAppQa.src.data.userData import user_data
from SiminvestAppQa.src.utilities.requestUtilities import RequestsUtilities
from SiminvestAppQa.src.pages.Android_pages.stock_detail_page import StockDetailPage
import allure
import logging as logger

#locators
homePage_search_btn = 'Browser_Stack'
search_field= 'StockSearch'
stock_search_entries = '(//android.widget.TextView[@content-desc="StockSearchCode"])'
MF_entries = '//android.widget.TextView'
reksadana_tab = '//android.view.ViewGroup[2]/android.widget.TextView[@text = "Reksadana"]'
saham_tab = '//android.widget.TextView[@text = "Saham"]'
search_delete='search_delete'
acceleration_board_btn = 'acceleration_board_btn'
mover_tab='MoverPageHeader'
mover_option = 'Mover'
empty_search_history_msg = '//android.view.ViewGroup[3]/android.widget.HorizontalScrollView[1]/android.view.ViewGroup/android.widget.TextView'
hapus_btn='hapus_btn'

class SearchSuggestion(StockDetailPage):

    @allure.step("click search btn on homepage")
    def click_on_search_btn_on_homepage(self):
        self.click(homePage_search_btn)
        self.sleep(1)

    @allure.step("Switch to reksadana tab")
    def switch_to_reksadana_tab(self):
        self.double_tap(reksadana_tab)
        self.sleep(1)

    @allure.step("Switch to Sahanm tab")
    def switch_to_Saham_tab(self):
        self.double_tap(saham_tab)
        self.sleep(1)

    @allure.step("clear search box")
    def clear_search_box(self):
        self.tap(search_delete)
        self.sleep(1)

    @allure.step("verify text disappear after type word in search_box")
    def verify_text_disappear_after_type_word_in_search_box(self):
        self.assert_equal(self.get_attribute(search_field, 'text'), 'Cari saham atau reksadana')
        self.assert_equal(self.get_attribute(empty_search_history_msg, 'text'), 'Riwayat pencarianmu masih kosong')
        self.update_text(search_field, 'A')
        self.assert_equal(self.get_attribute(search_field, 'text'), 'A')
        self.assert_not_equal(self.get_attribute(search_field, 'text'), 'Cari saham atau reksadana')
        entries_list_saham = self.find_elements(stock_search_entries)
        for i in range(1,len(entries_list_saham)):
            stock_code = self.get_attribute(f'(//android.widget.TextView[@content-desc="StockSearchCode"])[{i}]', 'text')
            self.assert_equal(self.is_element_visible(f'(//android.widget.TextView[@content-desc="StockSearchName"])[{i}]'), True)
            self.assertIn('A',stock_code)
        #self.go_back()
        self.sleep(2)
        self.switch_to_reksadana_tab()
        entries_list_MF = self.find_elements(MF_entries)
        for i in range(1,(len(entries_list_MF)-4)):
            mf_name = self.get_attribute(f'//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[{i}]/android.widget.TextView', 'text')
            self.assertIn('a', mf_name)

    @allure.step("validate selection of tab before search")
    def validate_selection_of_tab_before_search(self):
        self.clear_search_box()
        self.switch_to_Saham_tab()
        self.update_text(search_field, 'A')
        for i in range(1,3):
            self.assert_equal(self.is_element_visible(f'(//android.widget.TextView[@content-desc="StockSearchName"])[{i}]'), True)
        self.clear_search_box()
        self.switch_to_reksadana_tab()
        self.update_text(search_field, 'A')
        for i in range(1,3):
            self.assert_equal(self.is_element_visible(f'//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[{i}]/android.widget.TextView'), True)

    @allure.step("click on acceleration board")
    def click_on_acceleration_board(self):
        self.click(acceleration_board_btn)
        self.sleep(2)

    @allure.step("Validate keyboard option on search box")
    def validate_keyboard_option_on_search_box(self):
        self.click(search_field)
        self.assert_equal(self.check_keyboard_shown(), True)
        self.click(reksadana_tab)
        self.assert_equal(self.check_keyboard_shown(), False)

    @allure.step("validate last 4 search stock function")
    def validate_last_4_search_stock_function(self):
        self.switch_to_Saham_tab()
        stock_list_for_search = ['ASMI', 'APLN', 'AYLS', 'ABDA']
        for i in range(len(stock_list_for_search)):
            self.update_text(search_field, stock_list_for_search[i])
            self.sleep(1)
            self.tap(stock_search_entries)
            self.sleep(3)
            self.go_back()
        self.clear_search_box()
        self.sleep(2)
        for i in range(1, 5):
            self.assertIn(self.get_attribute(f'last_search_entry_{i}_name', 'text'), stock_list_for_search)
            self.assert_equal(self.is_element_visible(f'last_search_entry_{i}_icon'), True)
            #test for popular stock presence
            self.assert_equal(self.is_element_visible(f'popular_entry_{i}_name'), True)
            self.assert_equal(self.is_element_visible(f'popular_entry_{i}_icon'), True)
        self.click_on_acceleration_board()
        self.assert_equal(self.is_element_visible(mover_tab), True)
        self.assert_equal(self.is_element_visible(mover_option), True)
        self.go_back()
        self.sleep(2)

    @allure.step("Verify search suggestion after reopen app for kyc user")
    def verify_search_suggestion_after_reopen_app_user_for_kyc_user(self):
        self.launch_app_again()
        self.login_and_verify_homepage_for_reg_user(user_data['reg_no_2'])
        self.click(homePage_search_btn)
        self.sleep(2)
        # for i in range(1, 5):
        #     self.assertIn(self.get_attribute(f'last_search_entry_{i}_name', 'text'), stock_list_for_search)
        #     self.assert_equal(self.is_element_visible(f'last_search_entry_{i}_icon'), True)
        # self.click(hapus_btn)
        # self.sleep(1)
        # self.assert_equal(self.get_attribute(empty_search_history_msg, 'text'), 'Riwayat pencarianmu masih kosong')

    @allure.step("Verify search suggestion after reopen app for non kyc user")
    def verify_search_suggestion_after_reopen_app_user_for_non_kyc_user(self):
        self.launch_app_again()
        self.login_and_verify_homepage_for_non_kyc_user(user_data['unkyc_reg_no_2'])
        self.click(homePage_search_btn)
        self.sleep(2)
        # for i in range(1, 5):
        #     self.assertIn(self.get_attribute(f'last_search_entry_{i}_name', 'text'), stock_list_for_search)
        #     self.assert_equal(self.is_element_visible(f'last_search_entry_{i}_icon'), True)
        # self.click(hapus_btn)
        # self.sleep(1)
        # self.assert_equal(self.get_attribute(empty_search_history_msg, 'text'), 'Riwayat pencarianmu masih kosong')
