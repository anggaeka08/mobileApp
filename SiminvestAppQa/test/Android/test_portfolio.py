import pytest
from SiminvestAppQa.src.pages.Android_pages.portfolio_page import Portfolio
from SiminvestAppQa.src.pages.Android_pages.stock_detail_page import StockDetailPage
from SiminvestAppQa.src.pages.Android_pages.sell_process import SellProcess
from SiminvestAppQa.src.utilities.genericUtilities import generate_random_string
from SiminvestAppQa.src.data.userData import user_data
import logging as logger
import allure
from selenium.common.exceptions import NoSuchElementException


class Portfolio_test(Portfolio, SellProcess,StockDetailPage):

    @pytest.mark.functional_feature_of_portfolio
    @pytest.mark.Android
    @pytest.mark.Portfolio
    @allure.story("F-15:Portfolio Page")
    def test_functional_feature_of_portfolio(self):
        try:
            self.execute_script('lambda-name=test_functional_feature_of_portfolio')
            self.login_and_verify_homepage_for_reg_user(user_data['reg_no_3'])
            self.click_on_portfolio_btn()
            self.redirection_from_portfolio_to_sdp()
            self.click_on_sell_btn()
            self.sleep(2)
            self.click_on_jual_btn_on_sell_page()
            self.click_on_setuju()
            self.verify_buy_sell_success()
            self.click_on_portfolio_btn()
            self.redirection_from_portfolio_to_sdp()
            self.click_on_buy_btn()
            self.price_value_decrease()
            self.click_on_buy_btn_on_buy_page()
            self.click_on_confirm_btn()
            self.verify_buy_sell_success()
            self.click_on_home_page()
            self.Compare_values_between_homepage_and_portfolio()
            self.verify_buypower_and_other_values_presence()
            self.comparing_the_value_between_portfolio_page_and_sdp()
            self.go_back()
            #reached on portfolio page
            self.go_back()
            self.go_back()
            self.verify_app_closed()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_functional_feature_of_portfolio', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_functional_feature_of_portfolio', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    @pytest.mark.functional_feature_of_portfolio_for_non_kyc_user
    @pytest.mark.Android
    @pytest.mark.Portfolio
    @allure.story("F-15:Portfolio Page")
    def test_functional_feature_of_portfolio_for_non_kyc_user(self):
        try:
            self.execute_script('lambda-name=test_functional_feature_of_portfolio_for_non_kyc_user')
            self.login_and_verify_homepage_for_non_kyc_user(user_data['unkyc_reg_no'])
            self.click_on_portfolio_btn()
            self.validate_portfolio_for_non_kyc_user()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_functional_feature_of_portfolio_for_non_kyc_user', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_functional_feature_of_portfolio_for_non_kyc_user', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    @pytest.mark.ui_feature_of_portfolio_tab
    @pytest.mark.Android
    @pytest.mark.Portfolio
    @allure.story("F-15:Portfolio Page")
    def test_ui_feature_of_portfolio_tab(self):
        try:
            self.execute_script('lambda-name=test_ui_feature_of_portfolio_tab')
            self.login_and_verify_homepage_for_reg_user(user_data['reg_no_2'])
            self.verify_ui_feature_for_portfolio()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_ui_feature_of_portfolio_tab','SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_ui_feature_of_portfolio_tab','SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    @pytest.mark.mathematical_validation_of_portfolio_tab
    @pytest.mark.Android
    @pytest.mark.Portfolio
    @allure.story("F-15:Portfolio Page")
    def test_mathematical_validation_of_portfolio_tab(self):
        try:
            self.execute_script('lambda-name=test_mathematical_validation_of_portfolio_tab')
            self.login_and_verify_homepage_for_reg_user(user_data['reg_no_4'])
            self.click_on_portfolio_btn()
            self.verify_pl_value()
            self.verify_pl_percentage()
            self.verify_pl_percentage_for_stock()
            self.verify_pl_value_for_stock()
            self.verify_portfolio_value()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_mathematical_validation_of_portfolio_tab', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_mathematical_validation_of_portfolio_tab', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    @pytest.mark.validate_portfoilo_api_ui_data
    @pytest.mark.Android
    @pytest.mark.Portfolio
    @allure.story("F-15:Portfolio Page")
    def test_validate_portfoilo_api_ui_data(self):
        try:
            self.execute_script('lambda-name=test_validate_portfoilo_api_ui_data')
            self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
            rdn_balance_ui, trading_balance_ui, buying_power_ui, buyopen_ui, cash_balance_ui, earnings_ui, market_value_ui, return_ui, sellopen_ui, total_investment_ui = self.collect_ui_data_for_portfolio()
            rdn_balance_api, trading_balance_api, buying_power_api, buyopen_api,cash_balance_api,earnings_api,market_value_api,return_api,sellopen_api,total_investment_api = self.collect_api_data_for_portfolio()
            self.assert_equal(rdn_balance_ui,rdn_balance_api)
            self.assert_equal(trading_balance_ui,trading_balance_ui)
            self.assert_equal(buying_power_ui, buying_power_api)
            self.assert_equal(buyopen_ui, buyopen_api)
            self.assert_equal(cash_balance_ui, cash_balance_api)
            self.assert_equal(earnings_ui, earnings_api)
            self.assert_equal(market_value_ui, market_value_api)
            self.assert_equal(return_ui, return_api)
            self.assert_equal(sellopen_ui, sellopen_api)
            self.assert_equal(total_investment_ui,total_investment_api)
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_validate_portfoilo_api_ui_data', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_validate_portfoilo_api_ui_data', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)



    # Cover all 5 test cases in single test
    @pytest.mark.Port_SMMA_001_to_005
    @pytest.mark.Android
    @pytest.mark.portfolio_old
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
    @pytest.mark.portfolio_old
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
    @pytest.mark.portfolio_old
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
    @pytest.mark.portfolio_old
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
    @pytest.mark.portfolio_old
    def test_validate_redirection_after_click_reksadana(self):
        self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
        self.click_on_portfolio_btn()
        self.click_on_reksadhana_tab()
        self.verify_tab_on_reksadhana()
        self.verify_redirection_reksadhana_tab()


    # Cover all 4 test cases in single test
    @pytest.mark.Port_SMMA_018_to_21
    @pytest.mark.Android
    @pytest.mark.portfolio_old
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
    @pytest.mark.portfolio_old
    def test_validate_portfolio_value_buying_power_PL_value_with_portfolio_page_value(self):
        self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
        self.Compare_values_between_homepage_and_portfolio()

# Cover all 3 test cases in single test
    @pytest.mark.Port_SMMA_034_035_037
    @pytest.mark.Android
    @pytest.mark.portfolio_old
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
    @pytest.mark.portfolio_old
    def test_validate_PL_and_PL_per_value(self):
        self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
        self.click_on_portfolio_btn()
        self.verify_pl_value()
        self.verify_pl_percentage()








