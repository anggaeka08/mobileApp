import allure
import pytest
from selenium.common.exceptions import NoSuchElementException
from SiminvestAppQa.src.data.userData import user_data
from SiminvestAppQa.src.pages.Android_pages.sector_page import SectorPage



class saldoRdn_test(SectorPage):

    #all btns related test case
    @pytest.mark.functional_feature_sector_page
    @pytest.mark.Android
    @pytest.mark.SectorPage
    @allure.story("F-15: SectorPage")
    def test_validate_functional_feature_sector_page(self):
        try:
            self.execute_script('lambda-name=test_validate_functional_feature_sector_page')
            self.open_sector_page(user_data['reg_no_2'])
            self.Validate_11_entries_available_on_sector_page()
        except AssertionError as E:
            self.save_screenshot('test_validate_functional_feature_sector_page', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_validate_functional_feature_sector_page', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)