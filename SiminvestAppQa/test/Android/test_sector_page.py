import allure
import pytest
from selenium.common.exceptions import NoSuchElementException
from SiminvestAppQa.src.data.userData import user_data
from SiminvestAppQa.src.pages.Android_pages.sector_page import SectorPage



class saldoRdn_test(SectorPage):

    #SMMA-7400: Use Case 1*: Validate the functional feature of sector tab.
    @pytest.mark.functional_feature_sector_page
    @pytest.mark.Android
    @pytest.mark.SectorPage
    @allure.story("F-16: SectorPage")
    def test_validate_functional_feature_sector_page(self):
        try:
            self.execute_script('lambda-name=test_validate_functional_feature_sector_page')
            self.open_sector_page(user_data['reg_no_2'])
            self.Validate_11_entries_available_on_sector_page()
            self.validate_the_number_of_stock_on_list_page_and_sector_page()
        except AssertionError as E:
            self.save_screenshot('test_validate_functional_feature_sector_page', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_validate_functional_feature_sector_page', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

   #SMMA-7400: Use Case 2*: Validate the UI and grammatical                                                                             and button feature of the sector tab.
    @pytest.mark.button_and_grammar_on_sector_page
    @pytest.mark.Android
    @pytest.mark.SectorPage
    @allure.story("F-16: SectorPage")
    def test_validate_button_and_grammar_on_sector_page(self):
        try:
            self.execute_script('lambda-name=test_validate_button_and_grammar_on_sector_page')
            self.open_sector_page(user_data['reg_no_4'])
            self.verify_redirection_after_back_btn_from_sector_page()
            self.validate_back_btn_and_grammar_on_sector_page_and_list_page()
        except AssertionError as E:
            self.save_screenshot('test_validate_button_and_grammar_on_sector_page', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_validate_button_and_grammar_on_sector_page', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

   #SMMA-7400: Use Case 3 validate ui data with api                                                                        and button feature of the sector tab.
    @pytest.mark.ui_data_validation_with_api
    @pytest.mark.Android
    @pytest.mark.SectorPage
    @allure.story("F-16: SectorPage")
    def test_ui_data_validation_with_api(self):
        try:
            self.execute_script('lambda-name=test_ui_data_validation_with_api')
            self.open_sector_page(user_data['reg_no_3'])
            self.validate_ui_data_with_api()
        except AssertionError as E:
            self.save_screenshot('test_ui_data_validation_with_api', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_ui_data_validation_with_api', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)