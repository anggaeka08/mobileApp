import allure
import pytest
from selenium.common.exceptions import NoSuchElementException
from SiminvestAppQa.src.data.userData import user_data
from SiminvestAppQa.src.pages.Android_pages.saldo_rdn_page import SaldoRdn


@pytest.mark.usefixtures("_unittest_setUpClass_fixture_saldoRdn_test")
class saldoRdn_test(SaldoRdn):

    #all btns related test case
    @pytest.mark.All_btn_functinality
    @pytest.mark.Android
    @pytest.mark.saldoRdn
    @allure.story("F-10:SaldoRdnPage")
    def test_validate_btn_functionality_on_saldo_rdn(self):
        try:
            self.execute_script('lambda-name=test_validate_btn_functionality_on_saldo_rdn')
            self.login_and_verify_homepage_for_reg_user(user_data['reg_no_3'])
            self.click_on_saldo_rdn_btn()
            self.validate_all_btn_on_rdn_balance_page()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_validate_btn_functionality_on_saldo_rdn', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_validate_btn_functionality_on_saldo_rdn', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    #all btns related test case
    @pytest.mark.Functional_validation_rdn_page
    @pytest.mark.Android
    @pytest.mark.saldoRdn
    @allure.story("F-10:SaldoRdnPage")
    def test_Functional_validation_rdn_page(self):
        try:
            self.execute_script('lambda-name=test_Functional_validation_rdn_page')
            self.login_and_verify_homepage_for_reg_user(user_data['reg_no_3'])
            self.click_on_saldo_rdn_btn()
            self.functional_validation_of_rdn_page()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_Functional_validation_rdn_page', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_Functional_validation_rdn_page', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    #UI Validation test case
    @pytest.mark.ui_validation_RDN_page
    @pytest.mark.Android
    @pytest.mark.saldoRdn
    @allure.story("F-10:SaldoRdnPage")
    def test_ui_validation_RDN_page(self):
        try:
            self.execute_script('lambda-name=test_ui_validation_RDN_page')
            self.login_and_verify_homepage_for_reg_user(user_data['reg_no_4'])
            self.click_on_saldo_rdn_btn()
            self.ui_validation_for_rdn_page()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_ui_validation_RDN_page', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_ui_validation_RDN_page', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    #data comparision test case
    @pytest.mark.data_comparison_on_rdn_page
    @pytest.mark.Android
    @pytest.mark.saldoRdn
    @allure.story("F-10:SaldoRdnPage")
    def test_data_comparison_on_rdn_page(self):
        try:
            self.execute_script('lambda-name=test_data_comparision_on_rdn_page')
            self.login_and_verify_homepage_for_reg_user(user_data['reg_no_3'])
            self.data_comparison_btw_homepage_profile_and_rdn_page()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_data_comparision_on_rdn_page', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_data_comparision_on_rdn_page', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    #UI functionality of Withdrawal page.
    @pytest.mark.ui_functionality_of_withdrawal_page
    @pytest.mark.Android
    @pytest.mark.saldoRdn
    @allure.story("F-10:SaldoRdnPage")
    def test_ui_functionality_of_withdrawal_page(self):
        try:
            self.execute_script('lambda-name=ui_functionality_of_withdrawal_page')
            self.login_and_verify_homepage_for_reg_user(user_data['reg_no_4'])
            self.click_on_saldo_rdn_btn()
            self.click_on_tarik_dana_btn()
            self.validate_ui_for_tarikDana_page()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('ui_functionality_of_withdrawal_page', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('ui_functionality_of_withdrawal_page', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    #UI functionality of Withdrawal page.
    @pytest.mark.functional_feature_of_withdrawal_page
    @pytest.mark.Android
    @pytest.mark.saldoRdn
    @allure.story("F-10:SaldoRdnPage")
    def test_functional_feature_of_withdrawal_page(self):
        try:
            self.execute_script('lambda-name=test_functional_feature_of_withdrawal_page')
            self.login_and_verify_homepage_for_reg_user(user_data['reg_no_2'])
            self.click_on_saldo_rdn_btn()
            self.validate_functional_feature_of_tarikDana_page()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_functional_feature_of_withdrawal_page', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_functional_feature_of_withdrawal_page', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)