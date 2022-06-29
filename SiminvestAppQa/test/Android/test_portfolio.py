import pytest
from SiminvestAppQa.src.pages.Android_pages.portfolio_page import Portfolio
from SiminvestAppQa.src.pages.Android_pages.stock_detail_page import StockDetailPage
from SiminvestAppQa.src.pages.Android_pages.sell_process import SellProcess
from SiminvestAppQa.src.utilities.genericUtilities import generate_random_string
from SiminvestAppQa.src.data.userData import user_data
import logging as logger

@pytest.mark.usefixtures("unittest_setUpClass_fixture_Portfolio_test")
class Portfolio_test(Portfolio, SellProcess,StockDetailPage):

    # Cover all 5 test cases in single test
    @pytest.mark.Port_SMMA_001_to_005
    @pytest.mark.Android
    @pytest.mark.portfolio
    def test_validate_portfolio_btn_position_clickable_redirection_rakshdana_saham_btn_clickable(self):
        self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
        self.verify_portfolio_on_homepage()
        self.click_on_portfolio_btn()
        self.verify_portfolio_for_kyc_user()
        self.verify_saham_tab_clickable()
        self.verify_reksadhana_tab_clickable()

    # Cover all 3 test cases in single test
    @pytest.mark.Port_SMMA_006_007_008
    @pytest.mark.Android
    @pytest.mark.portfolio
    def test_validate_presence_of_values_and_stock_in_portfolio(self):
        self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
        self.click_on_portfolio_btn()
        self.verify_portfolio_for_kyc_user()
        self.verify_buypower_and_other_values_presence()
        self.verify_presence_of_Code_Lot_Avg_Last_PL_IDR_PL_percentage_invested_value()
        self.validate_stock_row_availability_in_portfolio()

    # Cover all 4 test cases in single test
    @pytest.mark.Port_SMMA_009_to_012
    @pytest.mark.Android
    @pytest.mark.portfolio
    def test_validate_values_on_two_different_pages(self):
        self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
        self.click_on_portfolio_btn()
        self.click_on_portfolio_entry_2()
        self.verify_jual_btn_on_home_page()
        self.go_back()
        self.comparing_the_value_between_portfolio_page_and_sdp()


    # Cover all 2 test cases in single test
    @pytest.mark.Port_SMMA_014_to_015
    @pytest.mark.Android
    @pytest.mark.portfolio
    def test_validate_redirection_and_buy_sell_after_tab_on_portfolio_stock(self):
        self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
        self.click_on_portfolio_btn()
        self.validate_redirection_from_portfolio_to_sdp()
        self.click_on_buy_btn()
        self.verify_buy_page()
        self.click_on_buy_btn_on_buy_page()
        self.click_on_confirm_btn()
        self.click_on_ok_btn()
        self.verify_transaction_page()
        self.go_back()
        self.click_on_jual_btn()
        self.verify_buy_page()
        self.click_on_jual_btn()
        self.click_on_setuju()
        self.click_on_ok_btn()
        self.verify_transaction_page()
        self.verify_transaction_page_for_sell()

    # Cover all 2 test cases in single test
    @pytest.mark.Port_SMMA_016_017
    @pytest.mark.Android
    @pytest.mark.portfolio
    def test_validate_redirection_after_click_reksadana(self):
        self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
        self.click_on_portfolio_btn()
        self.click_on_reksadhana_tab()
        self.verify_tab_on_reksadhana()
        self.verify_redirection_reksadhana_tab()


    # Cover all 4 test cases in single test
    @pytest.mark.Port_SMMA_018_to_21
    @pytest.mark.Android
    @pytest.mark.portfolio
    def test_right_left_swipe_on_portfolio_and_customer_care(self):
        self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
        self.click_on_portfolio_btn()
        self.right_swipe_on_portfolio()
        self.sleep(2)
        self.verify_half_card_page_buy()
        self.go_back()
        self.left_swipe_on_portfolio()
        self.verify_half_card_for_sell()
        self.go_back()
        self.verify_redirection_after_click_on_support_btn()

    # Cover all 3 test cases in single test
    @pytest.mark.Port_SMMA_025_26_29a
    @pytest.mark.Android
    @pytest.mark.portfolio
    def test_validate_portfolio_value_buying_power_PL_value_with_portfolio_page_value(self):
        self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
        self.Compare_values_between_homepage_and_portfolio()

# Cover all 3 test cases in single test
    @pytest.mark.Port_SMMA_034_035_037
    @pytest.mark.Android
    @pytest.mark.portfolio
    def test_back_btn_non_kyc_reksadana_help_btn(self):
        self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
        self.click_on_portfolio_btn()
        self.go_back()
        self.verify_portfolio_for_kyc_user()
        self.click_on_reksadhana_tab()
        self.sleep(2)
        self.verify_redirection_reksadhana_tab()
        self.click_to_help_btn()
        self.verify_redirection_after_click_on_customer_support()

# Cover all 2 test cases in single test
    @pytest.mark.Port_SMMA_039_040
    @pytest.mark.Android
    @pytest.mark.portfolio
    def test_validate_PL_and_PL_per_value(self):
        self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
        self.click_on_portfolio_btn()
        self.verify_pl_value()
        self.verify_pl_percentage()









