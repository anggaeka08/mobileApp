import allure
import pytest
from selenium.common.exceptions import NoSuchElementException
from SiminvestAppQa.src.pages.Android_pages.login_page import LoginPage
from SiminvestAppQa.src.pages.Android_pages.home_page import HomePage
from SiminvestAppQa.src.utilities.genericUtilities import generate_random_integer
from SiminvestAppQa.src.data.userData import user_data
import time
import logging as logger


# helper of this test is in homepage due to duplicacy of locators.
class mover_page_test(HomePage, LoginPage):

    # Validate global search bar.
    @pytest.mark.StockValidationForMoverOnHomePage
    @pytest.mark.MoverPage
    @pytest.mark.Android
    @pytest.mark.Revamp
    @allure.story("F-6:MoverPage Feature")
    def test_validate_mover_stock_on_homepage(self):
        try:
            self.execute_script('lambda-name=test_validate_mover_stock_on_homepage')
            self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
            self.scroll_up()
            self.verify_top_frequency_presention()
            self.validate_all_details_about_stock_list_on_homepage()
            self.click_on_TF_down_arrow()
            self.verify_all_value_on_half_card_and_tick()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_validate_mover_stock_on_homepage', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_validate_mover_stock_on_homepage', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)