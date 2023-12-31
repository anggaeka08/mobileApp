import allure
import pytest
from selenium.common.exceptions import NoSuchElementException
import logging as logger
from SiminvestAppQa.src.data.userData import user_data
from SiminvestAppQa.src.pages.Android_pages.mf_buy_process import buy_process
from SiminvestAppQa.src.pages.Android_pages.login_page import LoginPage
from SiminvestAppQa.src.pages.Android_pages.home_page import HomePage
from SiminvestAppQa.src.pages.Android_pages.reksadana_page import ReksadanaPage
from SiminvestAppQa.src.utilities.genericUtilities import generate_random_integer



class MfBuyProcess(buy_process,ReksadanaPage):
    
    @pytest.mark.test_non_functional_mf_buy_process
    @pytest.mark.MfBuyProcess
    @pytest.mark.Android
    @allure.story("F-21(B):MF Buy Process")
    def test_non_functional_mf_buy_process(self):
        try:
            self.execute_script('lambda-name=test_non_functional_mf_buy_process')
            self.open_reksadana_page(user_data['reg_no_7'])
            self.Validate_text_reksadana()
            self.Validate_buttomsheet_kamu()
            self.Validate_popup_resiko()
        
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_non_functional_mf_buy_process', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_non_functional_mf_buy_process', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    @pytest.mark.test_non_functional_mf_buy_process_part_2
    @pytest.mark.MfBuyProcess
    @pytest.mark.Android
    @allure.story("F-21(B):MF Buy Process")
    def test_non_functional_mf_buy_process_part2(self):
        try:
            self.execute_script('lambda-name=test_non_functional_mf_buy_process_part2')
            self.open_reksadana_page(user_data['reg_no_7'])
            self.Validate_text_reksadana()
            self.Validate_bottomsheet_kamu()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_non_functional_mf_buy_process_part2', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_non_functional_mf_buy_process_part2', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)


    @pytest.mark.test_non_functional_mf_buy_process_part_3
    @pytest.mark.MfBuyProcess
    @pytest.mark.Android
    @allure.story("F-21(B):MF Buy Process")
    def test_non_functional_mf_buy_process_part3(self):
        try:
            self.execute_script('lambda-name=test_non_functional_mf_buy_process_part3')
            self.open_reksadana_page(user_data['reg_no_7'])
            self.Validate_text_reksadana()
            self.Validate_konfirmasi_page()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_non_functional_mf_buy_process_part3', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_non_functional_mf_buy_process_part3', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)
   
   
    @pytest.mark.test_non_functional_mf_buy_process_part_4
    @pytest.mark.MfBuyProcess
    @pytest.mark.Android
    @allure.story("F-21(B):MF Buy Process")
    def test_non_functional_mf_buy_process_part4(self):
        try:
            self.execute_script('lambda-name=test_non_functional_mf_buy_process_part4')
            self.open_reksadana_page(user_data['reg_no_7'])
            self.Validate_text_reksadana()
            self.verify_top_up_page()
            self.Validate_konfirmasi_pesanan()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_non_functional_mf_buy_process_part4', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_non_functional_mf_buy_process_part4', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)         
            
            
    @pytest.mark.test_non_functional_mf_buy_process_part_5
    @pytest.mark.MfBuyProcess
    @pytest.mark.Android
    @allure.story("F-21(B):MF Buy Process")
    def test_non_functional_mf_buy_process_part5(self):
        try:
            self.execute_script('lambda-name=test_non_functional_mf_buy_process_part5')
            self.open_reksadana_page(user_data['reg_no_7'])
            self.Validate_text_reksadana()
            self.Verify_order_detail()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_non_functional_mf_buy_process_part5', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_non_functional_mf_buy_process_part5', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)  
            
                           