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

    @pytest.mark.mf_transaction_awaiting_order_buy
    @pytest.mark.Android
    @pytest.mark.MF_Transaction
    @allure.story("F-21(A):MF Transaction Page")
    def test_mf_transaction_awaiting_order_buy(self):
        try:
            self.execute_script('lambda-name=test_mf_transaction_awaiting_order_buy')
            self.open_reksadana_page(user_data['reg_no_7'])
            self.Validate_text_reksadana()
            self.open_mf_from_homepage()
            p_value , nav_value = self.topup_process_from_homepage()
            self.validate_payment_status_on_transaction_page()
            trans_unit , trans_value = self.sorting_validation_by_date()
           # self.assertAlmostEqual(int(p_value.replace(',','')), int(trans_value.replace(',','')))
            self.assert_equal(nav_value, trans_unit)
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_mf_transaction_awaiting_order_buy', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_mf_transaction_awaiting_order_buy', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    @pytest.mark.order_details_page_validation_for_jual
    @pytest.mark.Android
    @pytest.mark.MF_Transaction
    @allure.story("F-21(A):MF Transaction Page")
    def test_order_details_page_validation_for_jual(self):
        try:
            self.execute_script('lambda-name=test_order_details_page_validation_for_jual')
            self.login_and_verify_homepage_for_reg_user(user_data['reg_no_7'])
            self.click_on_portfolio_btn()
            self.click_on_reksadana_tab_on_portfolio_page()
            self.jual_process_for_transaction_page()
            self.validate_redirection_for_jual_entry()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_order_details_page_validation_for_jual', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_order_details_page_validation_for_jual', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    @pytest.mark.order_details_page_validation_buy_without_payment_proof
    @pytest.mark.Android
    @pytest.mark.MF_Transaction
    @allure.story("F-21(A):MF Transaction Page")
    def test_order_details_page_validation_buy_without_payment_proof(self):
        try:
            self.execute_script('lambda-name=test_order_details_page_validation_buy_without_payment_proof')
            self.open_reksadana_page(user_data['reg_no_6'])
            self.Validate_text_reksadana()
            self.open_mf_from_homepage()
            self.topup_process_from_homepage()
            self.validate_orderDetails_for_without_payment_proof_transaction()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_order_details_page_validation_buy_without_payment_proof', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_order_details_page_validation_buy_without_payment_proof', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    @pytest.mark.validate_payment_proof_upload_pop_for_mf
    @pytest.mark.Android
    @pytest.mark.MF_Transaction
    @allure.story("F-21(A):MF Transaction Page")
    def test_validate_payment_proof_upload_pop_for_mf(self):
        try:
            self.execute_script('lambda-name=test_validate_payment_proof_upload_pop_for_mf')
            self.open_reksadana_page(user_data['reg_no_6'])
            self.Validate_text_reksadana()
            self.open_mf_from_homepage()
            self.topup_process_from_homepage()
            self.validate_payment_proof_upload_option_validation()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_validate_payment_proof_upload_pop_for_mf', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_validate_payment_proof_upload_pop_for_mf', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    @pytest.mark.validate_order_details_page_for_mf
    @pytest.mark.Android
    @pytest.mark.MF_Transaction
    @allure.story("F-21(A):MF Transaction Page")
    def test_validate_order_details_page_for_mf(self):
        try:
            self.execute_script('lambda-name=test_validate_order_details_page_for_mf')
            self.open_reksadana_page(user_data['reg_no_7'])
            self.Validate_text_reksadana()
            self.open_mf_from_homepage()
            self.topup_process_from_homepage()
            self.validate_payment_proof_upload_option_validation()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_validate_order_details_page_for_mf', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_validate_order_details_page_for_mf', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)