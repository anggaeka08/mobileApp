import allure
import pytest
from SiminvestAppQa.src.pages.Android_pages.index_page import IndexPage
from SiminvestAppQa.src.data.userData import user_data
import logging as logger
from selenium.common.exceptions import NoSuchElementException

class Index_test(IndexPage):


    @pytest.mark.index_functional_feature
    @pytest.mark.Android
    @pytest.mark.index
    @allure.story("F-18 :Index Page")
    def test_validate_functional_feature_for_index_page(self):
        try:
            self.execute_script('lambda-name=test_validate_functional_feature_for_index_page')
            self.open_index_page(user_data['reg_no_3'])
            self.scroll_up()
            self.validate_header_movement()
            self.open_search_on_index_page()
            self.verify_redirection_for_search_option()
            self.Verify_search_saham_reksadana_from_search_box()
            self.search_close()
            self.validate_header_movement()
            self.open_search_on_index_page()
            self.verify_redirection_for_search_option()
            self.go_back()
            self.validate_header_movement()
            self.click_verification_on_index_entry()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_validate_functional_feature_for_index_page', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_validate_functional_feature_for_index_page', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)


    @pytest.mark.ui_and_grammar_validation
    @pytest.mark.Android
    @pytest.mark.index
    @allure.story("F-18 :Index Page")
    def test_validate_ui_and_grammar_for_index_page(self):
        try:
            self.execute_script('lambda-name=test_validate_ui_and_grammar_for_index_page')
            self.open_index_page(user_data['reg_no_4'])
            self.go_back()
            self.verify_home_page_reg_user()
            self.click_on_indeks_btn()
            self.sleep(2)
            self.verify_indeks_page()
            self.validate_scroll_up_and_down_on_index_page()
            self.validate_thousand_separator_and_name_in_index_entry()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_validate_ui_and_grammar_for_index_page', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_validate_ui_and_grammar_for_index_page', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

