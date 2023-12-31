import allure
import pytest
from selenium.common.exceptions import NoSuchElementException
from SiminvestAppQa.src.pages.Android_pages.login_page import LoginPage
from SiminvestAppQa.src.pages.Android_pages.home_page import HomePage
from SiminvestAppQa.src.utilities.genericUtilities import generate_random_integer
from SiminvestAppQa.src.data.userData import user_data
import time
import logging as logger


class homePage_test(HomePage,LoginPage):

    # Validate global search bar.
    @pytest.mark.GlobalSaerchOption
    @pytest.mark.Homepage
    @pytest.mark.Android
    @pytest.mark.Revamp
    @allure.story("F-5:HomePage Feature")
    def test_validate_global_search_for_stock(self):
        try:
            self.execute_script('lambda-name=test_validate_global_search_for_stock')
            self.login_and_verify_homepage_for_reg_user(user_data['reg_no_4'])
            self.validate_text_in_global_search_before_click()
            self.click_global_search_btn()
            self.Validate_text_and_keyboard_on_after_click_in_global_search()
            self.validate_search_entry_for_invalid_stock_and_saham_text()
            self.go_back()
            self.go_back()
            self.validate_text_in_global_search_before_click()
            self.click_global_search_btn_and_saerch_stock('ACES')
            self.sleep(2)
            self.validate_header_saham_and_stock_code_and_name('ACES')
            self.click_on_stock_code()
            self.verify_sdp_page()
            self.go_back()
            self.sleep(2)
            self.validate_header_saham_and_stock_code_and_name('ACES')
            #self.global_search_stock('A')
            self.sleep(3)
            #self.validate_header_saham_and_stock_code_and_name('A')
            self.global_search_stock_mf('Simas Saham Bertumbuh')
            self.sleep(3)
            self.validate_MF_search_in_global_search_and_Redirection_after_click()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_validate_all_buttons_on_homepage', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_validate_all_buttons_on_homepage', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    # Validate all buttons on homepage.
    @pytest.mark.AllButtons
    @pytest.mark.Homepage
    @pytest.mark.Android
    @pytest.mark.Revamp
    @allure.story("F-5:HomePage Feature")
    def test_validate_all_buttons_on_homepage(self):
        try:
            self.execute_script('lambda-name=test_validate_all_buttons_on_homepage')
            self.login_and_verify_homepage_for_reg_user(user_data['reg_no_4'])
            self.click_to_soldo_rdn()
            self.verify_rdn_balance_page()
            self.click_on_top_up_btn()
            self.verify_topup_page()
            self.go_back()
            self.click_on_tarik_dana_btn()
            self.verify_tarik_dana_page()
            self.go_back()
            self.click_on_riwayat_btn()
            self.verify_riwayat_page()
            self.go_back()
            self.go_back()
            self.verify_star_point_btn()
            self.go_back()
            self.verify_Reksadana_page()
            self.click_top_up_from_homepage()
            self.verify_topup_page()
            self.go_back()
            self.click_on_indeks_btn()
            self.verify_indeks_page()
            self.go_back()
            self.click_on_sector_button()
            self.verify_sector_page()
            self.go_back()
            self.click_on_event_btn()
            self.verify_event_page()
            self.go_back()
            self.sleep(2)
            self.scroll_up()
            self.click_on_eipo_btn()
            self.verify_eipo_page()
            #self.verify_eipo_entry()
            self.go_back()
            self.verify_top_frequency_presention()
           # self.verify_stock_presence_in_top_frequency()
            self.click_on_TF_down_arrow()
            self.verify_half_card_page()
            self.go_back()
            self.verify_home_page_reg_user_after_back_from_watchlist_new()
            self.click_on_see_more_btn()
            #self.verify_mover_page()
            self.go_back()
            #self.verify_home_page_reg_user_after_back_from_watchlist_new()
            self.scroll_up()
            self.click_on_default_btn()
            self.verify_watchlist_card()
            self.verify_watchlist_details()
            self.go_back()
            self.verify_home_page_reg_user_after_back_from_watchlist_new()
           # self.click_stock_1_from_top_frequency_list()
            #self.sleep(3)
            #self.verify_sdp_page_from_top_freqency_list()
            self.go_back()
            #self.verify_home_page_reg_user_after_back_from_watchlist_new()
            #self.click_on_default_watchlist_entry_1()
            ##self.verify_sdp_page_from_top_freqency_list()
           ## self.go_back()
            #self.verify_home_page_reg_user_after_back_from_watchlist_new()
            self.verify_edit_btn()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_validate_all_buttons_on_homepage', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_validate_all_buttons_on_homepage', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    # Validate api data with homepage data.
    @pytest.mark.DataValidation
    @pytest.mark.Homepage
    @pytest.mark.Android
    @pytest.mark.Revamp
    @allure.story("F-5:HomePage Feature")
    def test_validate_api_data_with_homepage_data(self):
        try:
            self.execute_script('lambda-name=test_validate_api_data_with_homepage_data')
            self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
            self.verify_data_with_api()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_validate_api_data_with_homepage_data', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_validate_api_data_with_homepage_data', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)
        except ValueError as E:
            self.save_screenshot('test_validate_api_data_with_homepage_data', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    # Functional Validation on homepage data.
    @pytest.mark.FunctionalValidation
    @pytest.mark.Homepage
    @pytest.mark.Android
    @pytest.mark.Revamp
    @allure.story("F-5:HomePage Feature")
    def test_functional_with_homepage_data(self):
        try:
            self.execute_script('lambda-name=test_functional_with_homepage_data')
            self.login_and_verify_homepage_for_reg_user(user_data['reg_no_3'])
            self.scroll_up()
            self.validate_default_btn_available_after_scroll_up()
            self.scroll_down()
            self.verify_username_on_homepage()
            self.verify_spelling_on_homepage()
            self.go_back()
            self.verify_username_on_homepage()
            self.go_back()
            self.go_back()
            self.go_back()
            #self.verify_username_on_homepage_after_close()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_functional_with_homepage_data', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_functional_with_homepage_data', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

     #  Hide RDN and shield tracker implimentation on the homepage
    @pytest.mark.HideRDN_and_ShieldTracker
    @pytest.mark.Homepage
    @pytest.mark.Android
    @pytest.mark.Revamp
    @allure.story("F-5:HomePage Feature")
    def test_hideRDN_homepage(self):
        try:
            self.execute_script('lambda-name=test_hideRDN_homepage')
            self.login_and_verify_homepage_for_reg_user_shield_tracker(user_data['reg_no_6'])
            self.verify_sheild_tracker_tidak()
            self.scroll_up_on_sheild()
            self.scroll_down_on_sheild()
            self.verify_sheild_tracker_setuju()
            self.verify_eye_defaultmode()
            self.Validate_kill_app()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_hideRDN_homepage', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_hideRDN_homepage', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)












