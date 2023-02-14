import allure
import pytest
from selenium.common.exceptions import NoSuchElementException
from SiminvestAppQa.src.data.userData import user_data
from SiminvestAppQa.src.pages.Android_pages.fast_order_process import FastOrder


@pytest.mark.usefixtures("_unittest_setUpClass_fixture_FastOrder_test")
class FastOrder_test(FastOrder):

    # BuyProcess UI  validation
    @pytest.mark.UI_buy_fo_Verification
    @pytest.mark.Android
    @pytest.mark.fastOrder
    @allure.story("F-9:FastOrderProcess")
    def test_verify_displayed_ui_for_buy_fastorder(self):
        try:
            self.execute_script('lambda-name=test_ui_for_buy_process')
            self.login_and_verify_homepage_for_reg_user(user_data['reg_no_2'])
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
