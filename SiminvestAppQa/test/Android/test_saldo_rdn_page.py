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