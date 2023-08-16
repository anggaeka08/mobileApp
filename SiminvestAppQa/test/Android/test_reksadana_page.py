import allure
import pytest
from selenium.common.exceptions import NoSuchElementException
from SiminvestAppQa.src.pages.Android_pages.reksadana_page import ReksadanaPage
from SiminvestAppQa.src.utilities.genericUtilities import generate_random_integer
from SiminvestAppQa.src.data.userData import user_data
import time
import logging as logger


class Reksadana_HomePage_test(ReksadanaPage):

    @pytest.mark.functional_response_validation_of_reksadana_homepage
    @pytest.mark.Reksadana
    @pytest.mark.Android
    @allure.story("F-21 :Reksadana Homepage")
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
            
            #next tiket
            #self.validate_pendapatan_tetap_page()
            #self.validate_saham_page()
            #self.validate_campuran_page()
            #self.validate_half_card()
            #self.validate_list_mutual_fund()
            #self.validate_return_mutual_fund()
            #self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_functional_response_validation_of_reksadana_homepage', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_functional_response_validation_of_reksadana_homepage', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)
            