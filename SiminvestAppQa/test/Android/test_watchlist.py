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






