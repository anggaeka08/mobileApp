import allure
import pytest
from selenium.common.exceptions import NoSuchElementException
from SiminvestAppQa.src.pages.Android_pages.reksadana_page import ReksadanaPage
from SiminvestAppQa.src.utilities.genericUtilities import generate_random_integer
from SiminvestAppQa.src.data.userData import user_data
import time
import logging as logger


class Reksadana_HomePage_test(ReksadanaPage):

    @pytest.mark.functional_response_validation_of_reksadana_homepage
    @pytest.mark.Reksadana
    @pytest.mark.Android
    @allure.story("F-21 :Reksadana Homepage")
    def test_functional_response_validation_of_reksadana_homepage(self):
        try:
            self.execute_script('lambda-name=test_functional_response_validation_of_reksadana_homepage')
            self.open_reksadana_page(user_data['reg_no_6'])
            self.Validate_text_reksadana()
            self.validate_amount()
            self.validate_refresh_functionality_for_reksadana_page()
            self.validate_text_today()
            #self.Validate_Reopen_showing_saham_page()
            #self.validate_refresh_for_reksadana_page_when_tab_other()
            #self.validate_pasar_uang_page()
            #self.click(list_product_mf1) 
            #self.sleep(3) 
            #self.validate_RDP()
            #self.validate_pendapatan_tetap_page()
            #self.validate_saham_page()
            #self.validate_campuran_page()
            #self.validate_half_card()
            #self.validate_list_mutual_fund()
            #self.validate_return_mutual_fund()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_functional_response_validation_of_reksadana_homepage', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_functional_response_validation_of_reksadana_homepage', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)












    # Validate all buttons on homepage.
    @pytest.mark.AllButtons
    @pytest.mark.Homepage
    @pytest.mark.Android
    @pytest.mark.Revamp
    @allure.story("F-5:HomePage Feature")
    def test_validate_all_buttons_on_homepage(self):
        try:
            self.execute_script('lambda-name=test_validate_all_buttons_on_homepage')
            self.login_and_verify_homepage_for_reg_user(user_data['reg_no_2'])
            self.click_to_soldo_rdn()
            self.verify_rdn_balance_page()
            self.click_on_top_up_btn()
            self.verify_topup_page()
            self.go_back()
            self.click_on_tarik_dana_btn()
            self.verify_tarik_dana_page()
            self.go_back()
            self.click_on_riwayat_btn()
            self.verify_riwayat_page()
            self.go_back()
            self.go_back()
            self.verify_star_point_btn()
            self.go_back()
            self.verify_Reksadana_page()
            self.click_top_up_from_homepage()
            self.verify_topup_page()
            self.go_back()
            self.click_on_indeks_btn()
            self.verify_indeks_page()
            self.go_back()
            self.click_on_sector_button()
            self.verify_sector_page()
            self.go_back()
            self.click_on_event_btn()
            self.verify_event_page()
            self.go_back()
            self.sleep(2)
            self.scroll_up()
            self.click_on_eipo_btn()
            self.verify_eipo_page()
            #self.verify_eipo_entry()
            self.go_back()
            self.verify_top_frequency_presention()
            self.verify_stock_presence_in_top_frequency()
            self.click_on_TF_down_arrow()
            self.verify_half_card_page()
            self.go_back()
            self.verify_home_page_reg_user_after_back_from_watchlist_new()
            self.click_on_see_more_btn()
            self.verify_mover_page()
            self.go_back()
            self.verify_home_page_reg_user_after_back_from_watchlist_new()
            self.scroll_up()
            self.click_on_default_btn()
            self.verify_watchlist_card()
            self.verify_watchlist_details()
            self.go_back()
            self.verify_home_page_reg_user_after_back_from_watchlist_new()
            self.click_stock_1_from_top_frequency_list()
            self.sleep(3)
            self.verify_sdp_page_from_top_freqency_list()
            self.go_back()
            self.verify_home_page_reg_user_after_back_from_watchlist_new()
            self.click_on_default_watchlist_entry_1()
            self.verify_sdp_page_from_top_freqency_list()
            self.go_back()
            self.verify_home_page_reg_user_after_back_from_watchlist_new()
            self.verify_edit_btn()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_validate_all_buttons_on_homepage', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_validate_all_buttons_on_homepage', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)
