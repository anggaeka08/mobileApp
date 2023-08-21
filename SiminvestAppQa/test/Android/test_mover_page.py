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
    @pytest.mark.StockValidationForMoverOnHomePageKYC
    @pytest.mark.MoverPage
    @pytest.mark.Android
    @pytest.mark.Revamp
    @allure.story("F-6:MoverPage Feature")
    def test_validate_stock_mover_stock_on_homepage_KYC(self):
        try:
            self.execute_script('lambda-name=test_validate_stock_mover_stock_on_homepage_KYC')
            self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
            self.scroll_up()
            self.verify_top_frequency_presention()
            self.validate_all_details_about_stock_list_on_homepage()
            self.click_on_TF_down_arrow()
            self.verify_all_value_on_half_card_and_tick_for_kyc_user(user_data['reg_no'])
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_validate_stock_mover_stock_on_homepage_KYC', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_validate_stock_mover_stock_on_homepage_KYC', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    # Validate global search bar.
    @pytest.mark.StockValidationForMoverOnHomePageNonKYC
    @pytest.mark.MoverPage
    @pytest.mark.Android
    @pytest.mark.Revamp
    @allure.story("F-6:MoverPage Feature")
    def test_validate_mover_stock_on_homepage_Non_KYC(self):
        try:
            self.execute_script('lambda-name=test_validate_mover_stock_on_homepage_Non_kyc')
            self.login_and_verify_homepage_for_non_kyc_user(user_data['unkyc_reg_no'])
            self.scroll_up()
            self.verify_top_frequency_presention()
            self.validate_all_details_about_stock_list_on_homepage()
            self.click_on_TF_down_arrow()
            self.verify_all_value_on_half_card_and_tick_for_non_kyc_user(user_data['unkyc_reg_no'])
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_validate_mover_stock_on_homepage_Non_kyc', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_validate_mover_stock_on_homepage_Non_kyc', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    # Validate global sbar.
    @pytest.mark.MoverPageForKYC
    @pytest.mark.MoverPage
    @pytest.mark.Android
    @pytest.mark.Revamp
    @allure.story("F-6:MoverPage Feature")
    def test_validate_mover_stock_on_homepage_KYC(self):
        API_RS = self.verify_stock_on_mover_page_with_api_for_top_frequency()
        try:
            self.execute_script('lambda-name=test_validate_mover_stock_on_homepage_KYC')
            self.login_and_verify_homepage_for_reg_user(user_data['reg_no_4'])
            self.scroll_up()
            self.compare_the_stock_details_with_mover_page()
            self.scroll_up_and_scroll_down_validation()
            self.stock_value_not_change_according_to_mover_change()
            self.validate_urutkan_half_card()
            #top frequency
            # MoverPage_TF = self.collect_all_value_from_mover_page()
            # logger.info(MoverPage_TF[0])
            # logger.info(API_RS[0])
            # check = all(item in API_RS[0] for item in MoverPage_TF[0])
            # self.assert_equal(check, True)
            # #top gainer
            # self.click_mover_dropDown_btn()
            # self.click('ScreenHomeTop gainers')
            # self.sleep(3)
            # MoverPage_TG = self.collect_all_value_from_mover_page()
            # logger.info(MoverPage_TG[0])
            # logger.info(API_RS[0])
            # check = all(item in API_RS[6] for item in MoverPage_TG[0])
            # self.assert_equal(check, True)
            # #Top Gainer Percentnage
            # self.click_mover_dropDown_btn()
            # self.click('ScreenHomeTop gainers %')
            # self.sleep(3)
            # MoverPage_TG = self.collect_all_value_from_mover_page()
            # logger.info(MoverPage_TG[0])
            # logger.info(API_RS[1])
            # check = all(item in API_RS[1] for item in MoverPage_TG[0])
            # self.assert_equal(check, True)
            # #topgainer Value
            # self.click_mover_dropDown_btn()
            # self.click('ScreenHomeTop value')
            # self.sleep(3)
            # MoverPage_TG = self.collect_all_value_from_mover_page()
            # logger.info(MoverPage_TG[0])
            # logger.info(API_RS[0])
            # check = all(item in API_RS[2] for item in MoverPage_TG[0])
            # self.assert_equal(check, True)
            # #top gainer Volume
            # self.click_mover_dropDown_btn()
            # self.click('ScreenHomeTop Volume')
            # self.sleep(3)
            # MoverPage_TG = self.collect_all_value_from_mover_page()
            # logger.info(MoverPage_TG[0])
            # logger.info(API_RS[0])
            # check = all(item in API_RS[3] for item in MoverPage_TG[0])
            # self.assert_equal(check, True)
            # #top losser
            # self.click_mover_dropDown_btn()
            # self.click('ScreenHomeTop losers')
            # self.sleep(4)
            # MoverPage_TG = self.collect_all_value_from_mover_page()
            # check = all(item in API_RS[4] for item in MoverPage_TG[0])
            # self.assert_equal(check, True)
            # # top losser percentange
            # self.click_mover_dropDown_btn()
            # self.click('ScreenHomeTop losers %')
            # self.sleep(4)
            # MoverPage_TG = self.collect_all_value_from_mover_page()
            # logger.info(MoverPage_TG[0])
            # logger.info(API_RS[0])
            # check = all(item in API_RS[5] for item in MoverPage_TG[0])
            # self.assert_equal(check, True)
            # #getaccelaration borad
            # self.click_mover_dropDown_btn()
            # self.click('ScreenHomePapan Akselerasi')
            # self.sleep(5)
            # MoverPage_TG = self.collect_all_value_from_mover_page()
            # logger.info(MoverPage_TG[0])
            # logger.info(API_RS[0])
            # check = all(item in API_RS[7] for item in MoverPage_TG[0])
            # self.assert_equal(check, True)
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_validate_mover_stock_on_homepage_KYC', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_validate_mover_stock_on_homepage_KYC', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    # Validate global search bar.
    @pytest.mark.MoverPageForNonKYC
    @pytest.mark.MoverPage
    @pytest.mark.Android
    @pytest.mark.Revamp
    @allure.story("F-6:MoverPage Feature")
    def test_MoverPageForNonKYC(self):
        try:
            API_RS = self.verify_stock_on_mover_page_with_api_for_top_frequency()
            self.execute_script('lambda-name=test_MoverPageForNonKYC')
            self.login_and_verify_homepage_for_non_kyc_user(user_data['unkyc_reg_no'])
            self.scroll_up()
            self.compare_the_stock_details_with_mover_page()
            self.scroll_up_and_scroll_down_validation()
            self.stock_value_not_change_according_to_mover_change()
            self.validate_urutkan_half_card()
            # top frequency
            # MoverPage_TF = self.collect_all_value_from_mover_page()
            # logger.info(MoverPage_TF[0])
            # logger.info(API_RS[0])
            # check = all(item in API_RS[0] for item in MoverPage_TF[0])
            # self.assert_equal(check, True)
            # # top gainer
            # self.click_mover_dropDown_btn()
            # self.click('ScreenHomeTop gainers')
            # self.sleep(3)
            # MoverPage_TG = self.collect_all_value_from_mover_page()
            # logger.info(MoverPage_TG[0])
            # logger.info(API_RS[0])
            # check = all(item in API_RS[6] for item in MoverPage_TG[0])
            # self.assert_equal(check, True)
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_MoverPageForNonKYC', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_MoverPageForNonKYC', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    @pytest.mark.SearchMoverPageKYC
    @pytest.mark.MoverPage
    @pytest.mark.Android
    @pytest.mark.Revamp
    @allure.story("F-6:MoverPage Feature")
    def test_validate_search_sdp_redirection(self):
        API_RS = self.verify_stock_on_mover_page_with_api_for_top_frequency()
        try:
            self.execute_script('lambda-name=test_validate_search_sdp_redirection')
            self.login_and_verify_homepage_for_reg_user(user_data['reg_no_2'])
            self.scroll_up()
            self.click_on_see_more_btn()
            self.click_on_mover_search_btn()
            self.global_search_stock('ACES')
            self.validate_saham_header_and_stock_code_and_stock_name('ACES')
            self.go_back()
            self.sleep(1)
            self.go_back()
            self.verify_mover_page()
            self.click_on_stock_in_mver()
            self.verify_sdp_page()
            self.go_back()
            self.verify_mover_page()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_validate_search_sdp_redirection', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_validate_search_sdp_redirection', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)