from SiminvestAppQa.src.data.userData import user_data
from SiminvestAppQa.src.pages.Android_pages.stock_detail_page import StockDetailPage
import allure
from SiminvestAppQa.src.utilities.requestUtilities import RequestsUtilities
import logging as logger
request_utilities = RequestsUtilities()
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
first_mf_entry_search = '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.TextView'
#mf_header = '//android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView'
mf_header = "//android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[@index = '1']"
mf_last_search_entry = '//android.view.ViewGroup[@content-desc="last_search_entry_1"]/android.widget.TextView'
popular_entry_1 = '//android.view.ViewGroup[@content-desc="popular_entry_1"]/android.widget.TextView'
mf_last_search_empty_msg = '//android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[2]'
last_search_text = 'last_search_text'
popular_text = 'popular_text'
acceleration_text = '//android.view.ViewGroup[@content-desc="acceleration_board_btn"]/android.widget.TextView'
popular_stock_entry_4 = 'popular_entry_4_name'
search_close_btn = 'search_close'
homepage_locator= '//android.widget.TextView[@text="Top Up"]'
popular_mf_list =['Danamas Stabil', 'Danamas Rupiah Plus', 'Simas Syariah Pendapatan Tetap', 'Danamas Pasti']

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

    @allure.step("Verify search suggestion for MF")
    def verify_search_suggestion_for_mf_redirection_after_search(self):
        MF_list = ['Simas Saham Bertumbuh', 'Simas Danamas Shama', 'Danamas Pasti', 'Danamas Rupiah Plus']
        self.switch_to_reksadana_tab()
        self.update_text(search_field, 'Dana')
        self.click(first_mf_entry_search)
        #self.sleep(6)
        mf_name_mf_page = self.get_attribute(mf_header, 'text', timeout=10)
        self.go_back()
        self.sleep(2)
        self.clear_search_box()
        mf_name = self.get_attribute(mf_last_search_entry, 'text')
        self.assert_equal(mf_name_mf_page, mf_name)
        for i in range(1, 5):
            self.assert_equal(self.is_element_visible(f'popular_entry_{i}'), True)
        self.assert_equal(self.is_element_visible(hapus_btn), True)
        self.click(mf_last_search_entry)
        self.sleep(4)
        mf_name_mf_page = self.get_attribute(mf_header, 'text')
        self.assert_equal(mf_name_mf_page, mf_name)
        self.go_back()
        self.sleep(2)
        popular_mf_name_1_search_entry = self.get_attribute(popular_entry_1, 'text')
        self.click(popular_entry_1)
        self.sleep(4)
        mf_name_mf_page = self.get_attribute(mf_header, 'text')
        self.assert_equal(popular_mf_name_1_search_entry, mf_name_mf_page)
        self.go_back()
        self.sleep(2)
        self.clear_search_box()
        self.click(hapus_btn)
        self.assert_equal(self.get_attribute(mf_last_search_empty_msg, 'text'), 'Riwayat pencarianmu masih kosong')
        # self.app_in_background(30)
        # self.sleep(10)
        # self.login_and_verify_homepage_for_non_kyc_user(user_data['unkyc_reg_no_2'])
        # self.click(homePage_search_btn)
        # self.switch_to_reksadana_tab()
        # mf_name_after_login = self.get_attribute(mf_last_search_entry, 'text')
        # self.assert_equal(mf_name_after_login, mf_name)
        # for i in range(5):
        #     self.update_text(search_field, MF_list[i])
        #     self.click(first_mf_entry_search)
        #     self.sleep(4)
        #     self.go_back()
        #     self.sleep(2)
        # mf_first_entry_name = self.get_attribute(mf_last_search_entry, 'text')
        # self.assert_equal(mf_first_entry_name,MF_list[4])
        # self.click(hapus_btn)
        # self.assert_equal(self.get_attribute(mf_last_search_empty_msg, 'text'), 'Riwayat pencarianmu masih kosong')
        # self.launch_app_again()
        # self.login_and_verify_homepage_for_non_kyc_user(user_data['unkyc_reg_no_2'])
        # self.click(homePage_search_btn)
        # self.switch_to_reksadana_tab()
        # self.assert_equal(self.get_attribute(mf_last_search_empty_msg, 'text'), 'Riwayat pencarianmu masih kosong')

    @allure.step("Validate grammar for search suggestions")
    def Validate_grammar_for_search_suggestions(self):
        self.assert_equal(self.get_attribute(last_search_text, 'text'), 'Pencarian Terakhir')
        self.assert_equal(self.get_attribute(popular_text, 'text'), 'Pencarian Populer')
        self.assert_equal(self.get_attribute(acceleration_text, 'text'), 'Papan Akselerasi')
       # self.scroll_vertical(loc_1='popular_entry_1_icon' , loc_2=popular_stock_entry_4)
        self.assert_equal(self.is_element_visible(popular_stock_entry_4), True)
        self.click(search_field)
        self.assert_equal(self.check_keyboard_shown(), True)
        self.update_text(search_field, '*')
        self.assert_equal(self.is_element_visible(stock_search_entries), True)
        self.update_text(search_field, '123')
        self.assert_equal(self.is_element_visible(stock_search_entries), False)
        self.click(search_close_btn)
        self.sleep(3)
        self.assert_equal(self.is_element_visible(homepage_locator), True)
        self.click_on_search_btn_on_homepage()
        self.update_text(search_field, 'A')
        stock_list = []
        self.sleep(2)
        for i in range(1, 4):
            stock_list.append(self.get_attribute(f'(//android.widget.TextView[@content-desc="StockSearchCode"])[{i}]', 'text'))
        stock_list_after_small = []
        self.update_text(search_field, 'a')
        self.sleep(3)
        for i in range(1, 4):
            stock_list_after_small.append(self.get_attribute(f'(//android.widget.TextView[@content-desc="StockSearchCode"])[{i}]', 'text'))
            self.assert_equal(self.is_element_visible(f'(//android.widget.TextView[@content-desc="StockSearchCode"])[{i}]'), True)
            self.assert_equal(self.is_element_visible(f'(//android.widget.TextView[@content-desc="StockSearchName"])[{i}]'), True)
        self.assert_equal(stock_list, stock_list_after_small)


    @allure.step("Scroll vertical on screen")
    def scroll_vertical(self, loc_1, loc_2):
        self.sleep(2)
        second_coordinate= self.get_attribute(loc_1, 'bounds')
        lst_1 = second_coordinate.split(',')
        fist_x = int(lst_1[0][1:])
        fist_y = int(lst_1[1][0:4])
        fist_coordinate= self.get_attribute(loc_2, 'bounds')
        lst_2 = fist_coordinate.split(',')
        sec_x = int(lst_2[0][1:])
        sec_y = int(lst_2[1][0:4])
        #logger.info(f'{second_coordinate} {type(second_coordinate)} {second_coordinate[1]}')
        #logger.info(f'{fist_coordinate} {type(fist_coordinate)} {fist_coordinate[1]}')
        self.scroll_screen(start_x=sec_x, start_y=sec_y, end_x=fist_x, end_y=fist_y, duration=5000)
        self.sleep(2)

    @allure.step("Validate grammar for search suggestions for MF")
    def Validate_grammar_for_search_suggestions_mf(self):
        self.assert_equal(self.get_attribute(last_search_text, 'text'), 'Pencarian Terakhir')
        self.assert_equal(self.get_attribute(popular_text, 'text'), 'Pencarian Populer')
        self.assert_equal(self.get_attribute(mf_last_search_empty_msg, 'text'), 'Riwayat pencarianmu masih kosong')
        self.switch_to_Saham_tab()
        self.assert_equal(self.get_attribute(acceleration_text, 'text'), 'Papan Akselerasi')
        self.switch_to_reksadana_tab()
        self.update_text(search_field, 'Danamas')
        for i in range(1,3):
            self.assert_equal(self.is_element_visible(f'//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[{i}]/android.widget.TextView'), True)
            self.assert_equal(self.is_element_visible(f'(//android.widget.TextView[@content-desc="StockSearchCode"])[{i}]'), False)
        self.click(first_mf_entry_search)
        self.sleep(1)
        self.assert_equal(self.is_element_visible(mf_header), True)
        self.go_back()
        self.sleep(2)
        self.assert_equal(self.is_element_visible(first_mf_entry_search), True)

    @allure.step("validate api data for stock and MF on search suggestion")
    def validate_api_data_for_stock_and_mf_on_search_suggestion(self, number):
        stock_list_popular_ui = []
        MF_popular_ui = []
        api_stock_list_popular = []
        for i in range(1, 5):
            stock_list_popular_ui.append(self.get_attribute(f'popular_entry_{i}_name', 'text'))
        self.switch_to_reksadana_tab()
        for i in range(1, 5):
            MF_popular_ui.append(self.get_attribute(f'//android.view.ViewGroup[@content-desc="popular_entry_{i}"]/android.widget.TextView', 'text'))
        self.assert_equal(MF_popular_ui, popular_mf_list)
        token_value = self.login_with_a_number(number)
        token = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJpWlYzdUJkTkJyTDA4dVIzQUR2bmg4akdTdHNkSHpQVSIsInN1YiI6IlNpbWFzSW52ZXN0In0.Kj31bgBrbc94NaUDKWgbx-N4ZBQNFsrZBmF7xtZ4hNo"}
        token['Authorization'] = 'Bearer ' + token_value
        portfolio_equity_rs = request_utilities.get(base_url='https://stg-api.siminvest.co.id/',endpoint='api/mds/v1/stock/category/top-gainer-volume', headers=token,expected_status_code=200)
        for i in range(0, 4):
            api_stock_list_popular.append(portfolio_equity_rs[i]['code'])
        self.assert_equal(stock_list_popular_ui, api_stock_list_popular)