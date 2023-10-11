import allure
import pytest
from SiminvestAppQa.src.data.userData import user_data
from SiminvestAppQa.src.pages.Android_pages.research_page import Research
from selenium.common.exceptions import NoSuchElementException

class Research_test(Research):

    @pytest.mark.RE_001_to_012
    @pytest.mark.Android
    @pytest.mark.Research
    @pytest.mark.Revamp
    @allure.story("F-4:Research Feature")
    def test_validate_research_page_redirection_and_search_option(self):
        try:
            self.execute_script('lambda-name=test_validate_research_page_redirection_and_search_option')
            self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
            self.verify_research_tab_on_homepage()
            self.click_on_research_btn()
            self.verify_header_of_research_page()
            self.Verify_search_btn_on_research_page()
            #self.click_on_search_btn()
            #self.verify_redirection_on_search_page()
            self.Validate_place_holder_in_search_option()
            self.Verify_availability_for_last_report_and_news_on_search_option()
            self.enter_and_verify_some_value_in_search_option()
            self.Click_to_new_and_verify_entry()
            #self.click_to_lastreport_and_verify_entry()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_validate_research_page_redirection_and_search_option', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_validate_research_page_redirection_and_search_option', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)


    @pytest.mark.RE_014_to_019
    @pytest.mark.Android
    @pytest.mark.Research
    @pytest.mark.Revamp
    @allure.story("F-4:Research Feature")
    def test_validate_redirection_for_news_and_media_and_search_option(self):
        try:
            self.execute_script('lambda-name=test_validate_redirection_for_news_and_media_and_search_option')
            self.login_and_verify_homepage_for_non_kyc_user(user_data['unkyc_reg_no'])
            self.click_on_research_btn()
            self.verify_tabs_on_research_page()
            self.click_on_news_research_tab_and_verify_entry()
            self.click_on_media_tab_and_verify_entry()
            self.click_on_search_btn()
            self.enter_some_value_in_search_option_verify_entry()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_validate_research_page_redirection_and_search_option', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_validate_research_page_redirection_and_search_option', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    @pytest.mark.RE_022_to_039
    @pytest.mark.Android
    @pytest.mark.Research
    @pytest.mark.Revamp
    @allure.story("F-4:Research Feature")
    def test_validate_red_dots_on_stock_signal(self):
        try:
            self.execute_script('lambda-name=test_validate_red_dots_on_stock_signal')
            self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
            self.click_on_research_btn()
            self.verify_10_entries_on_news_section()
            self.click_to_lastreport_and_verify_entry()
            self.click_to_daily_search_verify_redirection()
            self.go_back()
            self.click_on_stock_signal()
            #self.verify_red_dont_on_one_entry()
            #self.Click_on_entry_and_verify_red_dot_remove_from_entry()
            #self.close()
            #self.launch_app_again()
            #self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
            #self.click_on_research_btn()
            #self.verify_red_dont_on_one_entry_after_read()
            #self.click_to_signal_tadai_and_verify_red_dots()
            self.go_back()
            self.go_back()
            self.Verify_exit_from_app_on_research_page()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_validate_red_dots_on_stock_signal', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_validate_red_dots_on_stock_signal', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)


    @pytest.mark.functional_validation_stock_signal_research_page
    @pytest.mark.Android
    @pytest.mark.Research
    @pytest.mark.Revamp
    @allure.story("F-4:Research Feature")
    def test_functional_validation_stock_signal_research_page(self):
        try:
            self.execute_script('lambda-name=test_functional_validation_stock_signal_research_page')
            self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
            self.verify_research_tab_on_homepage()
            self.click_on_research_btn()
            self.verify_header_of_research_page()
            self.verify_tabs_on_research_page()
            self.verify_title_date_card()
            self.verify_header_of_all_tab()
            self.validate_refresh_functionality_for_level_page()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_functional_validation_stock_signal_research_page', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_functional_validation_stock_signal_research_page', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    @pytest.mark.functional_validation_stock_signal_research_page_non_kyc
    @pytest.mark.Android
    @pytest.mark.Research
    @pytest.mark.Revamp
    @allure.story("F-4:Research Feature")
    def test_validate_stock_signal_research_page_non_kyc(self):
        try:
            self.execute_script('lambda-name=test_validate_stock_signal_research_page_non_kyc')
            self.login_and_verify_homepage_for_non_kyc_user(user_data['unkyc_reg_no_2'])
            self.verify_research_tab_on_homepage()
            self.click_on_research_btn()
            self.verify_header_of_research_page()
            self.verify_tabs_on_research_page()
            self.verify_title_date_card()
            self.verify_header_of_all_tab()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_validate_stock_signal_research_page_non_kyc', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_validate_stock_signal_research_page_non_kyc', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    @pytest.mark.functional_validation_stock_signal_stock_breakdown 
    @pytest.mark.Android
    @pytest.mark.Research
    @pytest.mark.Revamp
    @allure.story("F-4:Research Feature")
    def test_functional_validation_stock_signal_stock_breakdown(self):
        try:
            self.execute_script('lambda-name=test_functional_validation_stock_signal_stock_breakdown')
            self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
            self.click_on_research_btn()
            self.verify_header_of_research_page()
            self.verify_stock_breakdown_page()
            self.click_on_lihat_stock_btn()
            self.verify_on_sdp_page()
            self.verify_on_image()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_functional_validation_stock_signal_stock_breakdown', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_functional_validation_stock_signal_stock_breakdown', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    @pytest.mark.functional_validation_stock_signal_stock_breakdown_non_kyc
    @pytest.mark.Android
    @pytest.mark.Research
    @pytest.mark.Revamp
    @allure.story("F-4:Research Feature")
    def test_functional_validation_stock_signal_stock_breakdown_non_kyc(self):
        try:
            self.execute_script('lambda-name=test_functional_validation_stock_signal_stock_breakdown_non_kyc')
            self.login_and_verify_homepage_for_non_kyc_user(user_data['unkyc_reg_no_2'])
            self.click_on_research_btn()
            self.verify_header_of_research_page()
            self.verify_stock_breakdown_page()
            self.click_on_lihat_stock_btn()
            self.verify_on_sdp_page()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_functional_validation_stock_signal_stock_breakdown_non_kyc', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_functional_validation_stock_signal_stock_breakdown_non_kyc', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

