import pytest
from SiminvestAppQa.src.pages.Android_pages.watchlist import Watchlist
from SiminvestAppQa.src.utilities.genericUtilities import generate_random_string
from SiminvestAppQa.src.data.userData import user_data

@pytest.mark.usefixtures("unittest_setUpClass_fixture_Watchlist_test")
class Watchlist_test(Watchlist):

    #Cover all 5 test cases in single test
    @pytest.mark.Wat_SMMA_001_004
    @pytest.mark.Android
    @pytest.mark.watchlist
    def test_validate_user_able_create_rename_deleteCancel_delete_watchlist(self):
        self.go_to_watchlist_option_after_login(user_data['reg_no'])
        self.click_on_defaults_btn()
        self.click_on_plus_btn()
        self.enter_watchlist_name('test')
        self.validate_watchlist_entry('test')
        self.click_on_edit_btn()
        self.edit_watchlist_name()
        self.click_on_simpan()
        self.validate_watchlist_entry('testtest')
        self.Cancel_delete_and_delete_watchlist()

    #SMMA-005 Validate user will able to have maximum 10 watchlists.
    @pytest.mark.Wat_SMMA_005
    @pytest.mark.Android
    @pytest.mark.watchlist
    def test_validate_user_able_to_add_maximum_10_watchlist(self):
        self.go_to_watchlist_option_after_login(user_data['reg_no'])
        self.click_on_defaults_btn()
        for i in range(10):
            self.click_on_plus_btn()
            self.enter_watchlist_name(f'test{i}')
        self.validate_pop_message()
        self.click_on_cross_btn()
        for i in range(9):
            self.click_on_delete()
            self.click_on_Hapus()
            self.sleep(1)

    # Validate If there is no stock inside watchlist, please show empty stock with button tamnah saham.
    @pytest.mark.Wat_SMMA_007
    @pytest.mark.Android
    @pytest.mark.watchlist
    def test_validate_msg_when_watchlist_empty(self):
        self.go_to_watchlist_option_after_login(user_data['reg_no'])
        self.click_on_defaults_btn()
        self.click_on_plus_btn()
        self.enter_watchlist_name('test')
        self.validate_watchlist_entry('test')
        self.click_on_watchlist_entry_2()
        self.scroll_ups()
        self.empty_watchlist_msg()
        self.click_on_test()
        self.click_on_selected_watchlist()
        self.click_on_Hapus()

    #Validate only new Siminvest’s will have default watchlis
    @pytest.mark.Wat_SMMA_008
    @pytest.mark.Android
    @pytest.mark.watchlist
    def test_validate_default_watchlist_for_new_user(self):
        self.go_to_watchlist_option_after_login(user_data['unkyc_reg_no'])
        self.validate_default_watchlist()

    # Validate stocks for default watchlist are BBCA, BBRI, TLKM, BMRI, ARTO
    @pytest.mark.Wat_SMMA_009
    @pytest.mark.Android
    @pytest.mark.watchlist
    def test_validate_stock_list_in_default_watchlist(self):
        self.go_to_watchlist_option_after_login(user_data['unkyc_reg_no'])
        self.validate_avail_check_f0r_stock_on_watchlist()

    #Validate watchlist name will have maximum 60 characters.
    @pytest.mark.Wat_SMMA_010
    @pytest.mark.Android
    @pytest.mark.watchlist
    def test_validate_watchlist_name_max_60_character(self):
        self.go_to_watchlist_option_after_login(user_data['reg_no'])
        self.click_on_defaults_btn()
        self.click_on_plus_btn()
        name = generate_random_string(65)
        self.enter_watchlist_name(name)
        self.validate_watchlist_entry(name[:60])
        self.click_on_delete()
        self.click_on_Hapus()

    #Validate as default show top gainer at the time of adding stock.
    @pytest.mark.Wat_SMMA_012_013
    @pytest.mark.Android
    @pytest.mark.watchlist
    def test_validate_default_show_top_gainer(self):
        self.go_to_watchlist_option_after_login(user_data['reg_no'])
        self.click_on_defaults_btn()
        self.click_on_plus_btn()
        self.enter_watchlist_name('test')
        self.validate_watchlist_entry('test')
        self.click_on_watchlist_entry_2()
        self.scroll_ups()
        self.empty_watchlist_msg()
        self.click_on_tambah_saham()
        self.verify_top_gainer_presence()
        self.click_on_top_gainer()
        self.verify_stock_type_selection()
        self.go_back()
        self.go_back()
        self.click_on_test()
        self.click_on_selected_watchlist()
        self.click_on_Hapus()

   #Validate test cases from count 014 to 018.
    @pytest.mark.Wat_SMMA_014_018
    @pytest.mark.Android
    @pytest.mark.watchlist
    def test_validate_test_case_smma_014_to_smma_018(self):
        self.go_to_watchlist_option_after_login(user_data['reg_no'])
        self.click_on_edit_for_stock()
        self.search_stock('A')
        self.verify_stock_list_after_single_character_search()
        self.search_stock('ARGO')
        self.verify_stock_search_by_full_code()
        self.click_to_add_remove()
        self.sleep(3)
        self.click_to_add_remove()
        self.click_on_ok()

    #Validate test cases from count 019 to 020.
    @pytest.mark.Wat_SMMA_019_020
    @pytest.mark.Android
    @pytest.mark.watchlist
    def test_validate_stcok_sorting_and_delete_disble_for_single_watchlist(self):
        self.go_to_watchlist_option_after_login(user_data['unkyc_reg_no'])
        self.click_on_edit_for_stock()
        self.validate_avail_check_for_stock_on_watchlist()
        self.go_back()
        self.go_back()
        self.click_on_defaults_btn()
        self.verify_delete_btn()

    #Validate user able to create duplicate name watchlist and able to add stock
    @pytest.mark.Wat_SMMA_021_022
    @pytest.mark.Android
    @pytest.mark.watchlist
    def test_user_able_to_create_duplicate_name_watchlist_and_able_to_add_stock(self):
        self.go_to_watchlist_option_after_login(user_data['reg_no'])
        self.click_on_defaults_btn()
        self.click_on_plus_btn()
        self.enter_watchlist_name('Default')
        self.validate_watchlist_entry('Default')
        self.click_on_watchlist_entry_2()
        self.scroll_ups()
        self.empty_watchlist_msg()
        self.click_on_tambah_saham()
        self.search_stock('ARGO')
        self.click_to_add_remove()
        self.go_back()
        self.scroll_ups()
        self.verify_watchlist_entry()
        self.click_on_defaults_btn()
        self.click_on_selected_watchlist()
        self.click_on_Hapus()

    @pytest.mark.Wat_SMMA_024_028
    @pytest.mark.Android
    @pytest.mark.watchlist
    def test_validate_selected_watchlist_visible_after_reopen_app_and_sdp_open_after_click_stock(self):
        self.go_to_watchlist_option_after_login(user_data['reg_no'])
        self.click_on_defaults_btn()
        self.click_on_plus_btn()
        self.enter_watchlist_name('test')
        self.validate_watchlist_entry('test')
        self.click_on_watchlist_entry_2()
        self.app_in_background(20)
        self.scroll_ups()
        self.click_on_test()
        self.click_on_selected_watchlist()
        self.click_on_Hapus()
        self.go_back()
        self.click_on_stock_code_in_watclist()
        self.verify_sdp_page()










