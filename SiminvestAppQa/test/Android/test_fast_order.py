import allure
import pytest
from selenium.common.exceptions import NoSuchElementException
from SiminvestAppQa.src.data.userData import user_data
from SiminvestAppQa.src.pages.Android_pages.fast_order_process import FastOrder


@pytest.mark.usefixtures("_unittest_setUpClass_fixture_FastOrder_test")
class FastOrder_test(FastOrder):

    #BuyProcess UI  validation
    @pytest.mark.UI_buy_fo_Verification
    @pytest.mark.Android
    @pytest.mark.fastOrder
    @allure.story("F-9:FastOrderProcess")
    def test_verify_displayed_ui_for_buy_fastorder(self):
        try:
            self.execute_script('lambda-name=test_ui_for_buy_process')
            self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
            self.scroll_up()
            self.scroll_to_open_fastOrder_buy()
            self.sleep(1)
            self.verify_ui_data_for_fastOrder_buy()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_ui_for_buy_process', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_ui_for_buy_process', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    # BuyProcess UI  validation
    @pytest.mark.UI_sell_fo_Verification
    @pytest.mark.Android
    @pytest.mark.fastOrder
    @allure.story("F-9:FastOrderProcess")
    def test_verify_displayed_ui_for_sell_fastorder(self):
        try:
            self.execute_script('lambda-name=test_verify_displayed_ui_for_sell_fastorder')
            self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
            self.scroll_up()
            self.scroll_to_open_fastOrder_sell()
            self.sleep(1)
            self.verify_ui_data_for_fastOrder_sell()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_verify_displayed_ui_for_sell_fastorder', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_verify_displayed_ui_for_sell_fastorder', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    # BuyProcess buttons  validation
    @pytest.mark.fo_btn_on_buy
    @pytest.mark.Android
    @pytest.mark.fastOrder
    @allure.story("F-9:FastOrderProcess")
    def test_validate_btn_for_buy_in_fastOrder(self):
        try:
            self.execute_script('lambda-name=test_validate_btn_for_buy_in_fastOrder')
            self.login_and_verify_homepage_for_reg_user(user_data['reg_no_3'])
            self.scroll_up()
            self.scroll_to_open_fastOrder_buy()
            self.verify_buttons_for_buy_on_fastOrder()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_validate_btn_for_buy_in_fastOrder', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_validate_btn_for_buy_in_fastOrder', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    # BuyProcess buttons  validation
    @pytest.mark.fo_btn_on_sell
    @pytest.mark.Android
    @pytest.mark.fastOrder
    @allure.story("F-9:FastOrderProcess")
    def test_validate_btn_for_sell_in_fastOrder(self):
        try:
            self.execute_script('lambda-name=test_validate_btn_for_sell_in_fastOrder')
            self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
            self.scroll_up()
            self.scroll_to_open_fastOrder_sell()
            self.sleep(1)
            self.verify_buttons_for_sell_on_fastOrder()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_validate_btn_for_sell_in_fastOrder', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_validate_btn_for_sell_in_fastOrder', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    # BuyProcess functionality test cases
    @pytest.mark.fo_buy_functionality
    @pytest.mark.Android
    @pytest.mark.fastOrder
    @allure.story("F-9:FastOrderProcess")
    def test_validate_buy_functionality_in_fo(self):
        try:
            self.execute_script('lambda-name=test_validate_buy_functionality_in_fo')
            self.login_and_verify_homepage_for_reg_user(user_data['reg_no_4'])
            self.scroll_up()
            self.scroll_to_open_fastOrder_buy()
            self.sleep(1)
            self.validate_trading_limit_and_buy_process()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_validate_buy_functionality_in_fo', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_validate_buy_functionality_in_fo', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    # SellProcess functionality test cases
    @pytest.mark.fo_sell_functionality
    @pytest.mark.Android
    @pytest.mark.fastOrder
    @allure.story("F-9:FastOrderProcess")
    def test_validate_sell_functionality_in_fo(self):
        try:
            self.execute_script('lambda-name=test_validate_sell_functionality_in_fo')
            self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
            self.scroll_up()
            self.scroll_to_open_fastOrder_sell()
            self.sleep(1)
            self.validate_max_sell_and_sell_process()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_validate_sell_functionality_in_fo', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_validate_sell_functionality_in_fo', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    # FastOrder functionality test cases
    @pytest.mark.fo_functional_feature
    @pytest.mark.Android
    @pytest.mark.fastOrder
    @allure.story("F-9:FastOrderProcess")
    def test_validate_functional_feature_of_fast_order(self):
        try:
            self.execute_script('lambda-name=test_validate_functional_feature_of_fast_order')
            self.login_and_verify_homepage_for_reg_user(user_data['reg_no_4'])
            self.function_validation_in_fast_order()
            self.self.scroll_to_open_fastOrder_with_specific_stock_for_buy()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_validate_functional_feature_of_fast_order',
                                 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_validate_functional_feature_of_fast_order',
                                 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    # FastOrder test cases for non kyc user
    @pytest.mark.fo_non_kyc_user
    @pytest.mark.Android
    @pytest.mark.fastOrder
    @allure.story("F-9:FastOrderProcess")
    def test_validate_fast_order_for_non_kyc_user(self):
        try:
            self.execute_script('lambda-name=test_validate_fast_order_for_non_kyc_user')
            self.login_and_verify_homepage_for_non_kyc_user((user_data['unkyc_reg_no']))
            self.scroll_up()
            self.validate_fast_order_with_non_kyc_user()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_validate_fast_order_for_non_kyc_user','SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_validate_fast_order_for_non_kyc_user','SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    # FastOrder test cases for functionality of confirmation page
    @pytest.mark.fo_confirm_page
    @pytest.mark.Android
    @pytest.mark.fastOrder
    @allure.story("F-9:FastOrderProcess")
    def test_validate_functionality_of_confirmation_page_for_fastOrder(self):
        try:
            self.execute_script('lambda-name=test_validate_functionality_of_confirmation_page_for_fastOrder')
            self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
            self.scroll_up()
            self.scroll_to_open_fastOrder_with_specific_stock_for_buy()
            self.validate_confirmation_page_functionality()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_validate_functionality_of_confirmation_page_for_fastOrder','SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_validate_functionality_of_confirmation_page_for_fastOrder','SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)


# Test cases of fastOrder from portfolio page

    @pytest.mark.UI_buy_sell_fo_Verification_portfolio
    @pytest.mark.Android
    @pytest.mark.fastOrder
    @allure.story("F-9:FastOrderProcess")
    def test_verify_displayed_ui_for_buy_sell_fastOrder_portfolio(self):
        try:
            self.execute_script('lambda-name=test_verify_displayed_ui_for_buy_sell_fastorder_portfolio')
            self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
            self.open_portfolio_page()
            self.scroll_for_open_fastOrder_buy_from_portfolio()
            self.sleep(1)
            self.verify_ui_data_for_fastOrder_buy()
            self.click_on_batal_btn()
            self.scroll_for_open_fastOrder_sell_from_portfolio()
            self.sleep(1)
            self.verify_ui_data_for_fastOrder_sell()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_verify_displayed_ui_for_buy_sell_fastorder_portfolio', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_verify_displayed_ui_for_buy_sell_fastorder_portfolio', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

   # BuyProcess buttons validation from portfolio
    @pytest.mark.fo_btn_on_buy_sell_from_portfolio
    @pytest.mark.Android
    @pytest.mark.fastOrder
    @allure.story("F-9:FastOrderProcess")
    def test_validate_btn_for_buy_sell_in_fastOrder_from_portfolio(self):
        try:
            self.execute_script('lambda-name=test_validate_btn_for_buy_sell_in_fastOrder_from_portfolio')
            self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
            self.open_portfolio_page()
            self.scroll_for_open_fastOrder_buy_from_portfolio()
            self.sleep(1)
            self.verify_buttons_for_buy_on_fastOrder_from_portfolio()
            self.open_portfolio_page()
            self.scroll_for_open_fastOrder_sell_from_portfolio()
            self.sleep(2)
            self.verify_buttons_for_sell_on_fastOrder_from_portfolio()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_validate_btn_for_buy_sell_in_fastOrder_from_portfolio', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_validate_btn_for_buy_sell_in_fastOrder_from_portfolio', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

