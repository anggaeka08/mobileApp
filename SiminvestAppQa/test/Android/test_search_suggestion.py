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

#Use Case 1*: Validate functional validation of the Search Suggestions. for MF with kyc user
    @pytest.mark.functional_validation_for_MF_search_for_kyc_user
    @pytest.mark.Android
    @pytest.mark.SearchSuggestion
    @allure.story("F-18: SearchSuggestion")
    def test_functional_validation_for_MF_search_for_kyc_user(self):
        try:
            self.execute_script('lambda-name=test_functional_validation_for_MF_search_for_kyc_user')
            self.login_and_verify_homepage_for_reg_user(user_data['reg_no_3'])
            self.click_on_search_btn_on_homepage()
            self.verify_search_suggestion_for_mf_redirection_after_search()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_functional_validation_for_MF_search_for_kyc_user', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_functional_validation_for_MF_search_for_kyc_user', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

#Use Case 1*: Validate functional validation of the Search Suggestions. for MF with non kyc user
    @pytest.mark.functional_validation_for_MF_search_for_nonkyc_user
    @pytest.mark.Android
    @pytest.mark.SearchSuggestion
    @allure.story("F-18: SearchSuggestion")
    def test_functional_validation_for_MF_search_for_nonkyc_user(self):
        try:
            self.execute_script('lambda-name=test_functional_validation_for_MF_search_for_nonkyc_user')
            self.login_and_verify_homepage_for_non_kyc_user(user_data['unkyc_reg_no_2'])
            self.click_on_search_btn_on_homepage()
            self.verify_search_suggestion_for_mf_redirection_after_search()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_functional_validation_for_MF_search_for_nonkyc_user', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_functional_validation_for_MF_search_for_nonkyc_user', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    #Use Case 2*: Validate Ui and grammarfor stcok with kyc and non kyc user
    @pytest.mark.validation_ui_and_grammar_for_kyc_user_with_stock
    @pytest.mark.Android
    @pytest.mark.SearchSuggestion
    @allure.story("F-18: SearchSuggestion")
    def test_validation_ui_and_grammar_for_kyc_user_with_stock(self):
        try:
            self.execute_script('lambda-name=test_validation_ui_and_grammar_for_kyc_user_with_stock')
            self.login_and_verify_homepage_for_reg_user(user_data['reg_no_3'])
            self.click_on_search_btn_on_homepage()
            self.Validate_grammar_for_search_suggestions()
            self.launch_app_again()
            self.login_and_verify_homepage_for_non_kyc_user(user_data['unkyc_reg_no_2'])
            self.click_on_search_btn_on_homepage()
            self.Validate_grammar_for_search_suggestions()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_validation_ui_and_grammar_for_kyc_user_with_stock', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_validation_ui_and_grammar_for_kyc_user_with_stock', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    #Use Case 2*: Validate Ui and grammar for MF with kyc and non kyc user
    @pytest.mark.validation_ui_and_grammar_with_MF
    @pytest.mark.Android
    @pytest.mark.SearchSuggestion
    @allure.story("F-18: SearchSuggestion")
    def test_validation_ui_and_grammar_with_MF(self):
        try:
            self.execute_script('lambda-name=test_validation_ui_and_grammar_with_MF')
            self.login_and_verify_homepage_for_reg_user(user_data['reg_no_4'])
            self.click_on_search_btn_on_homepage()
            self.switch_to_reksadana_tab()
            self.Validate_grammar_for_search_suggestions_mf()
            self.launch_app_again()
            self.login_and_verify_homepage_for_non_kyc_user(user_data['unkyc_reg_no_2'])
            self.click_on_search_btn_on_homepage()
            self.switch_to_reksadana_tab()
            self.Validate_grammar_for_search_suggestions_mf()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_validation_ui_and_grammar_with_MF', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_validation_ui_and_grammar_with_MF', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)