import allure
import pytest
from SiminvestAppQa.src.pages.Android_pages.Star_Point_page import StarPointPage
from SiminvestAppQa.src.data.userData import user_data
import logging as logger
from selenium.common.exceptions import NoSuchElementException

class StartPoint_test(StarPointPage):


    @pytest.mark.starpoint_functional_feature
    @pytest.mark.Android
    @pytest.mark.starpoint
    @allure.story("F-20 :StarPoint Page")
    def test_validate_functional_feature_for_starpoint_page(self):
        try:
            self.execute_script('lambda-name=test_validate_functional_feature_for_starpoint_page')
            self.login_and_verify_homepage_for_reg_user(user_data['reg_no_2'])
            self.verify_starpoint_page()
            self.verify_star_point_btn()
            self.Validate_starPoint_Swipe_and_Value()
            self.validate_show_TC_afterTutorial()
            self.click_checkbox_btn()
            self.click_to_submit()
            self.Validate_3dot_when_Click()
            self.Validate_Reopen_not_showing()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_validate_functional_feature_for_starpoint_page', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_validate_functional_feature_for_starpoint_page', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)


    @pytest.mark.starpoint_History_Page_Functional_validation
    @pytest.mark.Android
    @pytest.mark.starpoint
    @allure.story("F-20 :StarPoint Page")
    def test_starpoint_History_Page_Functional_validation(self):
        try:
            self.execute_script('lambda-name=test_starpoint_History_Page_Functional_validation')
            self.login_and_verify_homepage_for_reg_user(user_data['reg_no_4'])
            self.verify_starpoint_page()
            self.verify_star_point_btn()
            self.Validate_starPoint_Swipe_and_Value()
            self.validate_show_TC_afterTutorial()
            self.click_checkbox_btn()
            self.click_to_submit()
            self.Validate_starpoint_Home_and_Tukar()
            self.Validate_starpoint_riwayat()
            self.validate_scroll_up_and_down_on_Riwayat_page()
           # self.validate_thousand_separator_in_starpoin_Riwayat()
            self.Validate_Back_btn_riwayat()
            
            
        except AssertionError as E:
            self.save_screenshot('test_starpoint_History_Page_Functional_validation', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_starpoint_History_Page_Functional_validation', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)