import allure
import pytest
from selenium.common.exceptions import NoSuchElementException
from SiminvestAppQa.src.pages.Android_pages.reksadana_page import ReksadanaPage
from SiminvestAppQa.src.utilities.genericUtilities import generate_random_integer
from SiminvestAppQa.src.data.userData import user_data
import time
import logging as logger


class Reksadana_Feature(ReksadanaPage):

    @pytest.mark.functional_response_validation_of_reksadana_homepage
    @pytest.mark.Reksadana
    @pytest.mark.Android
    @allure.story("F-21 :Reksadana Feature")
    def test_functional_response_validation_of_reksadana_homepage(self):
        try:
            self.execute_script('lambda-name=test_functional_response_validation_of_reksadana_homepage')
            self.open_reksadana_page(user_data['reg_no_7'])
            self.Validate_text_reksadana()
            self.validate_amount()
            self.validate_refresh_functionality_for_reksadana_page()
            self.validate_text_today()
            self.Validate_Reopen_showing_saham_page()
            self.validate_refresh_for_reksadana_page_when_tab_other()
            self.validate_pasar_uang_page()
            self.click_list_product_mf1()
            self.sleep(3)
            self.validate_RDP()
            self.validate_pendapatan_tetap_page()
            self.validate_saham_page()
            self.validate_campuran_page()
            self.validate_half_card()
            self.validate_list_mutual_fund()
            self.validate_return_mutual_fund()
            self.click_list_product_mf2()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_functional_response_validation_of_reksadana_homepage', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_functional_response_validation_of_reksadana_homepage', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)


    @pytest.mark.mathematical_validation_on_homepage
    @pytest.mark.Reksadana
    @pytest.mark.Android
    @allure.story("F-21 :Reksadana Feature")
    def test_mathematical_validation_on_homepage(self):
        try:
            self.execute_script('lambda-name=test_mathematical_validation_on_homepage')
            self.open_reksadana_page(user_data['reg_no_7'])
            self.mathematical_validation_on_homepage()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_mathematical_validation_on_homepage', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_mathematical_validation_on_homepage', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)      
            

    @pytest.mark.API_data_validation_reksadana_homepage
    @pytest.mark.Reksadana
    @pytest.mark.Android
    @allure.story("F-21 :Reksadana Feature")
    def test_ui_and_api_data_validation_reksadana_homepage(self):
        try:
            self.execute_script('lambda-name=test_ui_and_api_data_validation')
            self.open_reksadana_page(user_data['reg_no_7'])
            self.validate_data_with_api_and_ui()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_ui_and_api_data_validation_reksadana_homepage', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_ui_and_api_data_validation_reksadana_homepage', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)                


    @pytest.mark.functional_response_validation_of_reksadana_rdp
    @pytest.mark.Reksadana
    @pytest.mark.Android
    @allure.story("F-21 :Reksadana Feature")
    def test_functional_response_validation_of_reksadana_rdp(self):
        try:
            self.execute_script('lambda-name=test_functional_response_validation_of_reksadana_rdp')
            self.open_reksadana_page(user_data['reg_no_7'])
            self.Validate_title_rdp()
            self.validate_ringkasan_tab()
            self.validate_half_card_rdp()
            self.validate_button_on_rdp()
            
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_functional_response_validation_of_reksadana_rdp', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_functional_response_validation_of_reksadana_rdp', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)  
            
    @pytest.mark.functional_feature_of_reksadana_rdp_for_non_kyc_user
    @pytest.mark.Reksadana
    @pytest.mark.Android
    @allure.story("F-21 :Reksadana Feature")
    def test_functional_feature_of_reksadana_rdp_for_non_kyc_user(self):
        try:
            self.execute_script('lambda-name=test_functional_feature_of_reksadana_rdp_for_non_kyc_user')
            self.login_and_verify_homepage_for_non_kyc_user(user_data['unkyc_reg_no_2'])
            self.validate_button_buka_account_reksadana()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_functional_feature_of_reksadana_rdp_for_non_kyc_user', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_functional_feature_of_reksadana_rdp_for_non_kyc_user', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)
                   