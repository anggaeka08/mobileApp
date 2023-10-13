import allure
import pytest
from selenium.common.exceptions import NoSuchElementException
import logging as logger
from SiminvestAppQa.src.data.userData import user_data
from SiminvestAppQa.src.pages.Android_pages.MF_transaction_page import MF_Transaction



class MF_Transaction_test(MF_Transaction):


    @pytest.mark.mf_transaction_functional_1
    @pytest.mark.Android
    @pytest.mark.MF_Transaction
    @allure.story("F-21(A):MF Transaction Page")
    def test_mf_transaction_functional_1(self):
        try:
            self.execute_script('lambda-name=test_mf_transaction_functional_1')
            self.open_trans_page_with_reg_user(user_data['reg_no_6'])
            self.verify_default_redirection_when_user_land_on_transaction_page()
            self.validate_scroll_down_reset_the_filter_option()
            self.validate_switch_the_tab_reset_the_filter_option()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_mf_transaction_functional_1', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_mf_transaction_functional_1', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    @pytest.mark.mf_transaction_riwayat_filter
    @pytest.mark.Android
    @pytest.mark.MF_Transaction
    @allure.story("F-21(A):MF Transaction Page")
    def test_mf_transaction_riwayat_filter(self):
        try:
            self.execute_script('lambda-name=test_mf_transaction_riwayat_filter')
            self.open_trans_page_with_reg_user(user_data['reg_no_6'])
            self.validate_filter_option_on_riwayat_tab()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_mf_transaction_riwayat_filter', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_mf_transaction_riwayat_filter', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)
