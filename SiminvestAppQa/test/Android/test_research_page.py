import allure
import pytest
from SiminvestAppQa.src.data.userData import user_data
from SiminvestAppQa.src.pages.Android_pages.research_page import Research

class Research_test(Research):

    @pytest.mark.RE_001_to_012
    @pytest.mark.Android
    @pytest.mark.Research
    @pytest.mark.Revamp
    @allure.story("F-4:Research Feature")
    def test_validate_research_page_redirection_and_search_option(self):
        self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
        self.verify_research_tab_on_homepage()
        self.click_on_research_btn()
        self.verify_header_of_research_page()
        self.Verify_search_btn_on_research_page()
        self.click_on_search_btn()
        self.verify_redirection_on_search_page()
        self.Validate_place_holder_in_search_option()
        self.Verify_availability_for_last_report_and_news_on_search_option()
        self.enter_and_verify_some_value_in_search_option()
        self.Click_to_new_and_verify_entry()
        self.click_to_lastreport_and_verify_entry()

    @pytest.mark.RE_014_to_019
    @pytest.mark.Android
    @pytest.mark.Research
    @pytest.mark.Revamp
    @allure.story("F-4:Research Feature")
    def test_validate_redirection_for_news_and_media_and_search_option(self):
        self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
        self.click_on_research_btn()
        self.verify_tabs_on_research_page()
        self.click_on_news_research_tab_and_verify_entry()
        self.click_on_media_tab_and_verify_entry()
        self.click_on_search_btn()
        self.enter_some_value_in_search_option_verify_entry()

    @pytest.mark.RE_022_to_039
    @pytest.mark.Android
    @pytest.mark.Research
    @pytest.mark.Revamp
    @allure.story("F-4:Research Feature")
    def test_validate_red_dots_on_stock_signal(self):
        self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
        self.click_on_research_btn()
        self.verify_10_entries_on_news_section()
        #self.click_to_lastreport_and_verify_entry()
        self.click_to_daily_search_verify_redirection()
        self.go_back()
        self.click_on_stock_signal()
        self.verify_red_dont_on_one_entry()
        self.Click_on_entry_and_verify_red_dot_remove_from_entry()
        self.close()
        self.launch_app_again()
        self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
        self.click_on_research_btn()
        self.verify_red_dont_on_one_entry_after_read()
        self.click_to_signal_tadai_and_verify_red_dots()
        self.go_back()
        self.go_back()
        self.Verify_exit_from_app_on_research_page()





