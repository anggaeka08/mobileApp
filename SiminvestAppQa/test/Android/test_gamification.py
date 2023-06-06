import pytest
from SiminvestAppQa.src.pages.Android_pages.portfolio_page import Portfolio
from SiminvestAppQa.src.pages.Android_pages.stock_detail_page import StockDetailPage
from SiminvestAppQa.src.pages.Android_pages.sell_process import SellProcess
from SiminvestAppQa.src.pages.Android_pages.gamification import Gamification
from SiminvestAppQa.src.data.userData import user_data
import allure
from selenium.common.exceptions import NoSuchElementException
import logging


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

    @pytest.mark.validate_gamification_api_ui_data
    @pytest.mark.Android
    @pytest.mark.Gamification
    @allure.story("F-17:Gamification")
    def test_validate_gamification_api_ui_data(self):
        try:
            self.execute_script('lambda-name=test_validate_gamification_api_ui_data')
            self.open_gamification_page(user_data['reg_no'])
            xp_value  = self.get_mission_xp()
            code_api, xp_value_api, success_api, message_api = self.collect_api_data_for_gamification()
            ids_api, lables_api,xps_api= self.collect_mission_list_api_data()
            labels_ui,XPs_Ui= self.collect_ui_data_for_gamification()
            self.assert_true(set(labels_ui).issubset(lables_api))
            self.assert_equal((len(ids_api) == len(set(ids_api))),True)
            self.assert_true(set(XPs_Ui).issubset(xps_api))
            self.assert_equal(xp_value, xp_value_api)
            self.assert_equal(code_api, 2)
            self.assert_equal(success_api, True)
            self.assert_equal(message_api, "data found")
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_validate_gamification_api_ui_data', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_validate_gamification_api_ui_data', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    @pytest.mark.button_response_validation_of_level_benifit_page
    @pytest.mark.Android
    @pytest.mark.Gamification
    @allure.story("F-17:Gamification")
    def test_button_response_validation_of_level_benifit_page(self):
        try:
            self.execute_script('lambda-name=test_button_response_validation_of_level_benifit_page')
            self.open_gamification_page(user_data['reg_no_4'])
            self.validate_level_button_functionality()
            self.validate_default_level_name()
            self.functional_validation_for_level_forward_and_backward_button()
            self.validate_level_entry_are_not_clickable()
            self.validate_level_back_button_is_not_scrollable()
            self.validate_refresh_functionality_for_level_page()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_button_response_validation_of_level_benifit_page',
                                 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_button_response_validation_of_level_benifit_page',
                                 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    @pytest.mark.validate_all_lavels_on_level_benefit_page
    @pytest.mark.Android
    @pytest.mark.Gamification
    @allure.story("F-17:Gamification")
    def test_validate_all_lavels_on_level_benefit_page(self):
        try:
            self.execute_script('lambda-name=test_validate_all_lavels_on_level_benefit_page')
            self.open_gamification_page(user_data['reg_no_4'])
            self.open_level_benefit_page()
            self.validate_pemimpi_level()
            self.validate_juragan_level()
            self.validate_tajir_konglo_sultan_level()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_validate_all_lavels_on_level_benefit_page',
                                 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_validate_all_lavels_on_level_benefit_page',
                                 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    @pytest.mark.validate_level_api_ui_data
    @pytest.mark.Android
    @pytest.mark.Gamification
    @allure.story("F-17:Gamification")
    def test_validate_level_api_ui_data(self):
        try:
            self.execute_script('lambda-name=test_validate_level_api_ui_data')
            self.open_gamification_page(user_data['reg_no'])
            level_xp_ui= self.collect_level_ui_data()
            level_xp_api= self.collect_level_api_data()
            self.assert_equal(level_xp_ui, level_xp_api)
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_validate_level_api_ui_data', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_validate_level_api_ui_data', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)