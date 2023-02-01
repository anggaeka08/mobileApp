import allure
import pytest
from selenium.common.exceptions import NoSuchElementException
from SiminvestAppQa.src.data.userData import user_data
from SiminvestAppQa.src.pages.Android_pages.fast_order_process import FastOrder


@pytest.mark.usefixtures("_unittest_setUpClass_fixture_FastOrder_test")
class FastOrder_test(FastOrder):

    # BuyProcess UI  validation
    @pytest.mark.buyProcess_UI
    @pytest.mark.Android
    @pytest.mark.fastOrder
    @allure.story("F-9:FastOrderProcess")
    def test_ui_for_buy_process(self):
        try:
            self.execute_script('lambda-name=test_ui_for_buy_process')
            self.open_trans_page_with_reg_user(user_data['reg_no'])
            self.verify_common_details_for_all_tabs()
            self.verify_entries_details_on_transaction_tab()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_ui_for_buy_process', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_ui_for_buy_process', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)
