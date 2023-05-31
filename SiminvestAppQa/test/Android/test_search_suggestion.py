import allure
import pytest
from selenium.common.exceptions import NoSuchElementException
from SiminvestAppQa.src.data.userData import user_data
from SiminvestAppQa.src.pages.Android_pages.search_suggestion import SearchSuggestion

class searchSuggestion_test(SearchSuggestion):

    #Use Case 1*: Validate functional validation of the Search Suggestions. for stock
    @pytest.mark.functional_validation_for_stocksearch
    @pytest.mark.Android
    @pytest.mark.SearchSuggestion
    @allure.story("F-18: SearchSuggestion")
    def test_functional_validation_for_stockSearch(self):
        try:
            self.execute_script('lambda-name=test_functional_validation_for_stockSearch')
            self.login_and_verify_homepage_for_reg_user(user_data['reg_no_2'])
            self.click_on_search_btn_on_homepage()
            self.validate_keyboard_option_on_search_box()
            self.verify_text_disappear_after_type_word_in_search_box()
            self.validate_selection_of_tab_before_search()
            self.validate_last_4_search_stock_function()
            self.verify_search_suggestion_after_reopen_app_user_for_kyc_user()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_functional_validation_for_stockSearch', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_functional_validation_for_stockSearch', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    #Use Case 1*: Validate functional validation of the Search Suggestions. for stock with non kyc user
    @pytest.mark.functional_validation_for_stocksearch_NonKyc
    @pytest.mark.Android
    @pytest.mark.SearchSuggestion
    @allure.story("F-18: SearchSuggestion")
    def test_functional_validation_for_stockSearch_NonKyc(self):
        try:
            self.execute_script('lambda-name=test_functional_validation_for_stockSearch_NonKyc')
            self.login_and_verify_homepage_for_non_kyc_user(user_data['unkyc_reg_no_2'])
            self.click_on_search_btn_on_homepage()
            self.validate_keyboard_option_on_search_box()
            self.verify_text_disappear_after_type_word_in_search_box()
            self.validate_selection_of_tab_before_search()
            self.validate_last_4_search_stock_function()
            self.verify_search_suggestion_after_reopen_app_user_for_non_kyc_user()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_functional_validation_for_stockSearch_NonKyc', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_functional_validation_for_stockSearch_NonKyc', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)