import pytest
from SiminvestAppQa.src.pages.Android_pages.portfolio_page import Portfolio
from SiminvestAppQa.src.pages.Android_pages.stock_detail_page import StockDetailPage
from SiminvestAppQa.src.pages.Android_pages.sell_process import SellProcess
from SiminvestAppQa.src.pages.Android_pages.gamification import Gamification
from SiminvestAppQa.src.data.userData import user_data
import allure
from selenium.common.exceptions import NoSuchElementException


class Gamification_test(Portfolio, SellProcess,StockDetailPage,Gamification):

    @pytest.mark.functional_response_validation_of_gamification_homepage
    @pytest.mark.Android
    @pytest.mark.Gamification
    @allure.story("F-17:Gamification")
    def test_functional_response_validation_of_gamification_homepage(self):
        try:
            self.execute_script('lambda-name=test_functional_response_validation_of_gamification_homepage')
            self.open_gamification_page(user_data['reg_no_3'])
            self.validate_mission_status()
            self.validate_mission_message()
            #self.validate_swipe_functionality()
            self.validate_subtabs_visiblity()
            self.validate_cara_kerja()
            self.validate_swipe_functionality_on_cara_kerja_webpage()
            self.validate_back_button_functionality_on_cara_kerja_webpage()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_functional_response_validation_of_gamification_homepage', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_functional_response_validation_of_gamification_homepage', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    @pytest.mark.button_response_validation_of_gamification_homepage
    @pytest.mark.Android
    @pytest.mark.Gamification
    @allure.story("F-17:Gamification")
    def test_button_response_validation_of_gamification_homepage(self):
        try:
            self.execute_script('lambda-name=test_button_response_validation_of_gamification_homepage')
            self.open_gamification_page(user_data['reg_no_4'])
            self.validate_level_button_functionality()
            self.validate_riwayat_button_functionality()
            self.validate_info_button_functionality()
            self.validate_lihat_semua_functionality()
            self.validate_menu_button_functionality()
            self.validate_back_button_functionality()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_button_response_validation_of_gamification_homepage',
                                 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_button_response_validation_of_gamification_homepage',
                                 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)