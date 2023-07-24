import allure
import pytest
from SiminvestAppQa.src.pages.Android_pages.event_page import EventPage
from SiminvestAppQa.src.data.userData import user_data
import logging as logger
from selenium.common.exceptions import NoSuchElementException

class Event_test(EventPage):


    @pytest.mark.event_functional_feature
    @pytest.mark.Android
    @pytest.mark.Event
    @allure.story("F-19 :Event Page")
    def test_validate_functional_feature_for_event_page(self):
        try:
            self.execute_script('lambda-name=test_validate_functional_feature_for_event_page')
            self.login_and_verify_homepage_for_reg_user(user_data['reg_no_2'])
            self.click_on_event_btn()
            self.verify_event_page()
            self.go_back()
            self.verify_home_page_reg_user()
            self.click_on_event_btn()
            self.verify_event_page()
            self.verify_all_tab_available()
            self.click_on_back_btn_on_event()
            self.verify_home_page_reg_user()
            self.click_on_event_btn()
            self.verify_event_page()
            self.verify_today_tab()
            self.validate_dividend_tab()
            self.validate_right_issue()
            self.validate_warrant_tab()
            self.validate_bonus_tab()
            self.validate_rups_tab()
            self.validate_public_expose_tab()
            self.validate_IPO_tab()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_validate_functional_feature_for_event_page', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_validate_functional_feature_for_event_page', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    @pytest.mark.API_data_validation_event
    @pytest.mark.Android
    @pytest.mark.Event
    @allure.story("F-19 :Event Page")
    def test_validate_API_data_validation_event_page(self):
        try:
            self.execute_script('lambda-name=test_validate_API_data_validation_event_page')
            self.login_and_verify_homepage_for_reg_user(user_data['reg_no_2'])
            self.click_on_event_btn()
            self.api_data_validation_for_event_page()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_validate_API_data_validation_event_page', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_validate_API_data_validation_event_page', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)


    @pytest.mark.event_ui_and_grammar_validation
    @pytest.mark.Android
    @pytest.mark.Event
    @allure.story("F-19 :Event Page")
    def test_validate_event_ui_and_grammar_validation(self):
        try:
            self.execute_script('lambda-name=test_validate_event_ui_and_grammar_validation')
            self.login_and_verify_homepage_for_reg_user(user_data['reg_no_2'])
            self.click_on_event_btn()
            self.verify_event_page()
            self.validate_sunday_to_saturday()
            self.validate_format_date_devidend()
            self.validate_format_date_StockSlipt()
            self.validate_format_date_Right()
            self.validate_format_date_Warrant()
            self.validate_format_date_Bonus()
            self.validate_IPO_tab()
            self.validate_format_date_and_time_Public()
            self.click_on_back_btn_on_event()
            self.click_on_event_btn()
            self.verify_event_page()
            self.validate_scroll_up_and_down_on_Event_page()
            self.validate_week_on_calender()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_validate_event_ui_and_grammar_validation', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_validate_event_ui_and_grammar_validation', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)
