import pytest
from SiminvestAppQa.src.data.userData import user_data
from SiminvestAppQa.src.pages.Android_pages.transaction import Transaction


@pytest.mark.usefixtures("_unittest_setUpClass_fixture_Transaction_test")
class Transaction_test(Transaction):

    # Cover all 5 test cases in single test
    @pytest.mark.T_SMMA_001_to_005
    @pytest.mark.Android
    @pytest.mark.transaction
    def test_validate_transaction_btn_redirection_saham_reksadana_tab(self):
        self.open_trans_page_with_reg_user(user_data['reg_no'])
        self.verify_last_transaction_orderlist()

    @pytest.mark.T_SMMA_008
    @pytest.mark.Android
    @pytest.mark.transaction
    def test_GTC_tab_contain_gtc_transactions(self):
        self.open_trans_page_with_reg_user(user_data['reg_no'])
        self.click_on_gtc_tab()
        self.verify_GTC_tab_entries()

    @pytest.mark.T_SMMA_010_to_017
    @pytest.mark.Android
    @pytest.mark.transaction
    def test_verify_all_type_btn_feature(self):
        self.open_trans_page_with_reg_user(user_data['reg_no'])
        self.verify_search_bar()
        self.click_to_reksadana()
        self.verify_reksadana_tab()
        self.click_to_saham()
        self.verify_saham_tab()
        self.click_to_all_types()
        self.go_back()
        self.verify_saham_tab()
        self.click_to_all_types()
        self.verify_all_types_values()
        self.click_on_buy_all()
        self.verify_transaction_page_for_buy_all()
        self.click_to_all_types()
        self.click_on_sell_all()
        self.verify_transaction_page_for_sell_all()

    @pytest.mark.T_SMMA_019_to_026
    @pytest.mark.Android
    @pytest.mark.transaction
    def test_verify_reksadana_transactions(self):
        self.open_trans_page_with_reg_user(user_data['mf_user'])
        self.click_to_reksadana()
        self.verify_all_types_and_all_status_btn()
        self.verify_orderlist_and_riwayat_tab()
        self.click_on_all_status_btn()
        self.verify_option_in_all_status_btn()
        self.click_on_in_progress()
        self.verify_status_after_sorting_by_inprogress()
        #self.click_on_all_status_btn()
        #self.click_on_awaiting_payment()
        #self.verify_status_after_sorting_by_awaitning_payemnt()
        self.scroll_up()
        self.scroll_down()
        self.click_to_saham()
        self.sleep(3)
        self.scroll_down()
        self.scroll_up()

    @pytest.mark.T_SMMA_028_29_30_34
    @pytest.mark.Android
    @pytest.mark.transaction
    def test_verify_left_right_swipe_and_search_options(self):
        self.open_trans_page_with_reg_user(user_data['reg_no'])
        self.swipe_right()
        self.verify_all_types_btn_for_trade_list()
        self.swipe_right()
        self.verify_all_type_btn_for_history_list()
        self.swipe_right()
        self.verify_all_type_btn_for_gtc_list()
        self.swipe_left()
        self.swipe_left()
        self.swipe_left()
        self.verify_all_types_btn_for_order_list()
        self.enter_value_in_search_box('TEST')
        self.verify_enteries_after_enter_null_or_space_in_search_option()
        self.enter_value_in_search_box(' ')
        self.verify_enteries_after_enter_null_or_space_in_search_option()
        self.click_on_gtc_tab()
        self.click_on_gtc_first_entry()
        self.click_on_batal()
        self.click_on_YA()
        self.click_on_ok()
        self.verify_status_of_first_entry()

    @pytest.mark.T_SMMA_039_040
    @pytest.mark.Android
    @pytest.mark.transaction
    def test_verify_gtc_order_page_and_help_option(self):
        self.open_trans_page_with_reg_user(user_data['reg_no'])
        self.click_on_gtc_tab()
        self.click_on_gtc_first_entry()
        self.verify_details_available_on_gtc_order_details_page()
        self.click_on_customer_btn()
        self.sleep(3)
        self.verify_redirection_after_click_on_customer_support()


    @pytest.mark.T_SMMA_035
    @pytest.mark.Android
    @pytest.mark.transaction
    def test_verify_gtc_order_page_redirection(self):
        self.open_trans_page_with_reg_user(user_data['reg_no'])
        self.click_on_gtc_tab()
        self.click_on_gtc_first_entry()
        self.go_back()
        self.verify_gtc_first_entry_available()


















