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

    @pytest.mark.validate_button_responce_gamification_mission_list_page
    @pytest.mark.Android
    @pytest.mark.Gamification
    @allure.story("F-17:Gamification")
    def test_validate_button_responce_gamification_mission_list_page(self):
        try:
            self.execute_script('lambda-name=test_validate_button_responce_gamification_mission_list_page')
            self.open_gamification_page(user_data['reg_no_3'])
            self.button_response_validation_on_mission_list_page()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_validate_button_responce_gamification_mission_list_page',
                                 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_validate_button_responce_gamification_mission_list_page',
                                 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    @pytest.mark.functional_validation_gamification_mission_list_page
    @pytest.mark.Android
    @pytest.mark.Gamification
    @allure.story("F-17:Gamification")
    def test_functional_validation_gamification_mission_list_page(self):
        try:
            self.execute_script('lambda-name=test_functional_validation_gamification_mission_list_page')
            self.open_gamification_page(user_data['reg_no_4'])
            self.open_onboarding_lihat_semua()
            self.open_transaction_lihat_semua()
            self.open_frequency_lihat_semua()
            self.open_refferal_lihat_semua()
            self.validate_redirection_of_jalankan_misi()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_functional_validation_gamification_mission_list_page',
                                 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_functional_validation_gamification_mission_list_page',
                                 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    @pytest.mark.validate_mission_list_filtered_api_ui_data
    @pytest.mark.Android
    @pytest.mark.Gamification
    @allure.story("F-17:Gamification")
    def test_validate_mission_list_filtered_api_ui_data(self):
        try:
            self.execute_script('lambda-name=test_validate_mission_list_filtered_api_ui_data')
            self.open_gamification_page(user_data['reg_no'])
            ob_label_ui, ob_xp_ui, trans_label_ui, trans_xp_ui, freq_label_ui, freq_xp_ui, refer_label_ui, refer_xp_ui = self.collect_mission_list_filtered_Ui_data()
            ob_label_api, ob_xp_api, trans_label_api, trans_xp_api, freq_label_api, freq_xp_api, refer_label_api, refer_xp_api =self.collect_mission_list_filtered_api_data()
            self.assert_true(set(ob_label_ui).issubset(ob_label_api))
            self.assert_true(set(ob_xp_ui).issubset(ob_xp_api))
            self.assert_true(set(trans_label_ui).issubset(trans_label_api))
            self.assert_true(set(freq_label_ui).issubset(freq_label_api))
            self.assert_true(set(freq_xp_ui).issubset(freq_xp_api))
            self.assert_true(set(refer_label_ui).issubset(refer_label_api))
            self.assert_true(set(refer_xp_ui).issubset(refer_xp_api))
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_validate_mission_list_filtered_api_ui_data', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_validate_mission_list_filtered_api_ui_data', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)


    @pytest.mark.ui_and_grammer_gamification_xp_history_page
    @pytest.mark.Android
    @pytest.mark.Gamification
    @allure.story("F-17:Gamification")
    def test_ui_and_grammer_gamification_xp_history_page(self):
        try:
            self.execute_script('lambda-name=test_ui_and_grammer_gamification_xp_history_page')
            self.open_gamification_page(user_data['reg_no_2'])
            self.open_riwayat_page()
            self.validate_active_xp_expired_xp_back_button_until_date_xp_value_visibility()
            self.validate_empty_state_page()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_ui_and_grammer_gamification_xp_history_page',
                                 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_ui_and_grammer_gamification_xp_history_page',
                                 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    @pytest.mark.button_responce_gamification_xp_history_page
    @pytest.mark.Android
    @pytest.mark.Gamification
    @allure.story("F-17:Gamification")
    def test_button_responce_gamification_xp_history_page(self):
        try:
            self.execute_script('lambda-name=test_button_responce_gamification_xp_history_page')
            self.open_gamification_page(user_data['reg_no_3'])
            self.open_riwayat_page()
            self.validate_empty_state_page()
            self.validate_swipe_functionality_in_riwayat_subtabs()
            self.click_back_button_on_gamification_history_page()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_button_responce_gamification_xp_history_page',
                                 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_button_responce_gamification_xp_history_page',
                                 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    @pytest.mark.functional_validation_gamification_XP_History_Page
    @pytest.mark.Android
    @pytest.mark.Gamification
    @allure.story("F-17:Gamification")
    def test_functional_validation_gamification_XP_History_Page(self):
        try:
            self.execute_script('lambda-name=test_functional_validation_gamification_XP_History_Page')
            self.open_gamification_page(user_data['reg_no_4'])
            self.validate_riwayat_button_is_visible_on_gamification_homepage()
            self.open_riwayat_page()
            self.validate_active_xp_expired_xp_back_button_until_date_xp_value_visibility()
            self.validate_until_date_and_time_format()
            self.validate_empty_state_page()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_functional_validation_gamification_XP_History_Page',
                                 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_functional_validation_gamification_XP_History_Page',
                                 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    @pytest.mark.validate_gamification_history_api_ui_data
    @pytest.mark.Android
    @pytest.mark.Gamification
    @allure.story("F-17:Gamification")
    def test_validate_gamification_history_api_ui_data(self):
        try:
            self.execute_script('lambda-name=test_validate_gamification_history_api_ui_data')
            self.open_gamification_page(user_data['reg_no'])
            label_ui, credit_ui = self.collect_ui_data_for_gamification_history()
            label_api, credit_api= self.collect_api_data_for_gamification_history()
            self.assert_true(set(label_ui).issubset(label_api))
            self.assert_true(set(credit_ui).issubset(credit_api))
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_validate_gamification_history_api_ui_data',
                                 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_validate_gamification_history_api_ui_data',
                                 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)