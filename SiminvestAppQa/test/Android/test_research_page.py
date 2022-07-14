import pytest
from SiminvestAppQa.src.data.userData import user_data
from SiminvestAppQa.src.pages.Android_pages.research_page import Research

@pytest.mark.usefixtures("_unittest_setUpClass_fixture_Research_test")
class Research_test(Research):

    @pytest.mark.RE_001_to_012
    @pytest.mark.Android
    @pytest.mark.Research
    def test_validate_research_page_redirection_and_search_option(self):
        self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
        self.verify_research_tab_on_homepage()
        self.click_on_research_btn()
        self.verify_header_of_research_page()
        self.Verify_search_btn_on_research_page()
        self.click_on_search_btn()
        self.verify_redirection_on_search_page()
        self.Verify_availability_for_last_report_and_news_on_search_option()
        self.enter_and_verify_some_value_in_search_option()
        self.Click_to_new_and_verify_entry()
        self.click_to_lastreport_and_verify_entry()

    @pytest.mark.RE_014_to_019
    @pytest.mark.Android
    @pytest.mark.Research
    def test_validate_redirection_for_news_and_media_and_search_option(self):
        self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
        self.click_on_research_btn()
        self.verify_tabs_on_research_page()
        self.click_on_news_research_tab_and_verify_entry()
        self.click_on_media_tab_and_verify_entry()
        self.click_on_search_btn()
        self.enter_some_value_in_search_option_verify_entry()




