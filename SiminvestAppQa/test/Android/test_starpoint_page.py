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
            self.login_and_verify_homepage_for_reg_user(user_data['reg_no_5'])
            self.verify_starpoint_page()
            self.verify_star_point_btn()
            self.Validate_starPoint_Swipe_and_Value()
            self.validate_show_TC_afterTutorial()
            self.click_checkbox_btn()
            self.click_to_submit()
            self.Validate_starpoint_Home_and_Tukar()
            self.Validate_starpoint_riwayat()
            self.validate_scroll_up_and_down_on_Riwayat_page()
            self.Validate_Back_btn_riwayat()
            #self.validate_thousand_separator_in_starpoin_Riwayat()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_starpoint_History_Page_Functional_validation', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_starpoint_History_Page_Functional_validation', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)
    
    @pytest.mark.api_data_validation_for_Starpoint
    @pytest.mark.Android
    @pytest.mark.starpoint
    @allure.story("F-20 :StarPoint Page")
    def test_api_data_validation_for_Starpoint(self):
        try:
            self.execute_script('lambda-name=test_api_data_validation_for_Starpoint')
            self.login_and_verify_homepage_for_reg_user(user_data['reg_no_5'])
            self.verify_starpoint_page()
            self.verify_star_point_btn()
            self.Validate_starPoint_Swipe_and_Value()
            self.validate_show_TC_afterTutorial()
            self.click_checkbox_btn()
            self.click_to_submit()    
            self.api_data_validation_for_Starpoint()        
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_api_data_validation_for_Starpoint', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_api_data_validation_for_Starpoint', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)



    @pytest.mark.validation_functional_part1_Starpoint
    @pytest.mark.Android
    @pytest.mark.starpoint
    @allure.story("F-20 :StarPoint Page")
    def test_validation_functional_part1_Starpoint(self):
        try:
            self.execute_script('lambda-name=test_validation_functional_part1_Starpoint')
            self.login_and_verify_homepage_for_reg_user(user_data['reg_no_4'])
            self.verify_starpoint_page()
            self.verify_star_point_btn()
            self.Validate_starPoint_Swipe_and_Value()
            self.validate_show_TC_afterTutorial()
            self.click_checkbox_btn()
            self.click_to_submit()    
            self.validate_tukarpage_Starpoint_less_Minimun()  
            self.validate_thousand_separator_in_starpoin_Riwayat()
            self.Compare_values_between_homepage_and_starpoint()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_validation_functional_part1_Starpoint', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_validation_functional_part1_Starpoint', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    @pytest.mark.validation_functional_part2_Starpoint
    @pytest.mark.Android
    @pytest.mark.starpoint
    @allure.story("F-20 :StarPoint Page")
    def test_validation_functional_part2_Starpoint(self):
        try:
            self.execute_script('lambda-name=test_validation_functional_part2_Starpoint')
            self.login_and_verify_homepage_for_reg_user(user_data['reg_no_5'])
            self.verify_starpoint_page()
            self.verify_star_point_btn()
            self.Validate_starPoint_Swipe_and_Value()
            self.validate_show_TC_afterTutorial()
            self.click_checkbox_btn()
            self.click_to_submit()     
            self.validate_elemnt_tukar_menu()
            self.Validate_kill_app()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_validation_functional_part2_Starpoint', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_validation_functional_part2_Starpoint', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    @pytest.mark.validation_functional_part3_Starpoint
    @pytest.mark.Android
    @pytest.mark.starpoint
    @allure.story("F-20 :StarPoint Page")
    def test_validation_functional_part3_Starpoint(self):
        try:
            self.execute_script('lambda-name=test_validation_functional_part3_Starpoint')
            self.login_and_verify_homepage_for_reg_user(user_data['reg_no_5'])
            self.verify_starpoint_page()
            self.verify_star_point_btn()
            self.Validate_starPoint_Swipe_and_Value()
            self.validate_show_TC_afterTutorial()
            self.click_checkbox_btn()
            self.click_to_submit()     
            self.validate_back_dashboardStarpoint_and_poin()
            self.validate_back_homepagestarpoin_and_point()
            self.Validate_kill_app()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_validation_functional_part3_Starpoint', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_validation_functional_part3_Starpoint', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)
        
    @pytest.mark.validation_historypage_functional_starpoint
    @pytest.mark.Android
    @pytest.mark.starpoint
    @allure.story("F-20 :StarPoint Page")
    def test_validation_historypage_functional_starpoint(self):
        try:
            self.execute_script('lambda-name=test_validation_historypage_functional_starpoint')
            self.login_and_verify_homepage_for_reg_user(user_data['reg_no_5'])
            self.verify_starpoint_page()
            self.verify_star_point_btn()
            self.Validate_starPoint_Swipe_and_Value()
            self.validate_show_TC_afterTutorial()
            self.click_checkbox_btn()
            self.click_to_submit()     
            self.Validate_formatdate_5trx_plusminus()
            self.validate_thousand_separator_should_show()
            self.Validate_starpoint_riwayat()
            self.validate_correct_redirection_to_riwayat()
            self.validate_25_transaction_Riwayat_page()
            self.Validate_Back_btn_riwayat()
            self.validate_correct_redirection()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_validation_historypage_functional_starpoint', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_validation_historypage_functional_starpoint', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)