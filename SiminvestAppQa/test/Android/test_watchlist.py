import allure
import pytest
from SiminvestAppQa.src.pages.Android_pages.watchlist import Watchlist
from SiminvestAppQa.src.utilities.genericUtilities import generate_random_string
from SiminvestAppQa.src.data.userData import user_data
import logging as logger
from selenium.common.exceptions import NoSuchElementException


class Watchlist_test(Watchlist):

    #SMMA-005 Validate user will able to have maximum 10 watchlists and verify stock details in watchlist.
    @pytest.mark.Wat_SMMA_005_018_019_020
    @pytest.mark.Android
    @pytest.mark.watchlist
    @allure.story("F-1:Watchlist Feature")
    @pytest.mark.Revamp
    def test_validate_user_able_to_add_maximum_10_watchlist(self):
        try:
            self.execute_script('lambda-name=test_validate_user_able_to_add_maximum_10_watchlist')
            self.go_to_watchlist_option_after_login(user_data['reg_no_2'])
            #self.scroll_up()
            self.verify_stock_code_and_name_in_watchlist_stocks()
            self.click_on_defaults_btn()
            #self.verify_watchlist_activation()
            for i in range(10):
                self.click_on_plus_btn()
                self.enter_watchlist_name(f'test{i}')
            self.validate_pop_message()
            #self.go_back()
            self.click_on_cross_btn()
            for i in range(9):
                self.click_on_delete()
                self.click_on_Hapus()
                self.sleep(1)
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_validate_user_able_to_add_maximum_10_watchlist', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_validate_user_able_to_add_maximum_10_watchlist', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)



    #Validate user able to create duplicate name watchlist and able to add stock
    @pytest.mark.Wat_SMMA_021_022
    @pytest.mark.Android
    @pytest.mark.watchlist
    @pytest.mark.Revamp
    @allure.story("F-1:Watchlist Feature")
    def test_user_able_to_create_duplicate_name_watchlist_and_able_to_add_stock(self):
        try:
            self.execute_script('lambda-name=test_user_able_to_create_duplicate_name_watchlist_and_able_to_add_stock')
            self.go_to_watchlist_option_after_login(user_data['reg_no_3'])
            self.click_on_defaults_btn()
            self.click_on_plus_btn()
            self.enter_watchlist_name('Default')
            self.validate_watchlist_entry('Default')
            self.click_on_watchlist_entry_2()
            self.sleep(1)
            self.scroll_up()
            self.empty_watchlist_msg()
            self.click_on_tambah_saham()
            self.search_stock('REAL')
            self.click_to_add_remove()
            self.go_back()
            self.go_back()
            self.scroll_ups()
            self.verify_watchlist_entry()
            self.click_on_defaults_btn()
            self.click_on_selected_watchlist()
            self.click_on_Hapus()
            self.sleep(2)
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_user_able_to_create_duplicate_name_watchlist_and_able_to_add_stock', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_user_able_to_create_duplicate_name_watchlist_and_able_to_add_stock', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    @pytest.mark.Wat_SMMA_024_028
    @pytest.mark.Android
    @pytest.mark.watchlist
    @pytest.mark.Revamp
    @allure.story("F-1:Watchlist Feature")
    def test_validate_selected_watchlist_visible_after_reopen_app_and_sdp_open_after_click_stock(self):
        try:
            self.execute_script('lambda-name=Wat_SMMA_024_028')
            self.go_to_watchlist_option_after_login(user_data['reg_no_4'])
            self.click_on_defaults_btn()
            self.click_on_plus_btn()
            self.enter_watchlist_name('test')
            self.validate_watchlist_entry('test')
            self.click_on_watchlist_entry_2()
            self.app_in_background(20)
            self.scroll_up()
            self.click_on_test()
            self.click_on_selected_watchlist()
            self.click_on_Hapus()
            self.go_back()
            self.click_on_stock_code_in_watclist()
            self.verify_sdp_page()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('Wat_SMMA_024_028', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('Wat_SMMA_024_028', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    @pytest.mark.cover_many_testcase
    @pytest.mark.Android
    @pytest.mark.watchlist
    @pytest.mark.Revamp
    @allure.story("F-1:Watchlist Feature")
    def test_validate_maximum_watchlist_test_cases(self):
        try:
            self.execute_script('lambda-name=test_validate_maximum_watchlist_test_cases')
            self.go_to_watchlist_option_after_login(user_data['reg_no_3'])
            self.scroll_up()
            self.click_on_defaults_btn()
            self.validate_only_default_watchlist_for_a_user()
            self.verify_delete_btn()
            self.go_back()
            self.sleep(1)
            self.scroll_up()
            self.validate_avail_check_for_stock_on_watchlist()
            self.click_on_defaults_btn()
            self.click_on_plus_btn()
            self.enter_watchlist_name('test')
            self.validate_watchlist_entry('test')
            self.click_on_watchlist_entry_2()
            self.sleep(1)
            self.scroll_up()
            self.empty_watchlist_msg()
            self.click_on_tambah_saham()
            self.verify_top_gainer_presence()
            self.click_on_top_gainer()
            self.verify_stock_type_selection()
            self.go_back()
            self.go_back()
            self.sleep(2)
            self.small_scroll_down()
            self.click_on_edit_for_stock()
            self.search_stock('A')
            self.verify_stock_list_after_single_character_search()
            self.search_stock('ARGO')
            self.verify_stock_search_by_full_code()
            self.click_to_add_remove()
            self.sleep(3)
            self.click_to_add_remove()
            self.click_on_ok()
            self.go_back()
            self.sleep(1)
            self.scroll_up()
            self.click_on_test()
            self.click_on_edit_btn()
            name = generate_random_string(65)
            self.sleep(2)
            self.edit_watchlist_name(name)
            self.click_on_simpan()
            self.validate_watchlist_entry("test"+name[:56])
            self.Cancel_delete_and_delete_watchlist()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_validate_maximum_watchlist_test_cases', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_validate_maximum_watchlist_test_cases', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    @pytest.mark.Wat_SMMA_013_015
    @pytest.mark.Android
    @pytest.mark.watchlist
    @pytest.mark.Revamp
    @allure.story("F-1:Watchlist Feature")
    def test_user_not_able_to_add_more_then_15_stock_in_watchlist(self):
        try:
            self.execute_script('lambda-name=test_user_not_able_to_add_more_then_15_stock_in_watchlist')
            self.go_to_watchlist_option_after_login(user_data['reg_no_4'])
            self.click_on_defaults_btn()
            self.click_on_plus_btn()
            self.enter_watchlist_name('test')
            self.validate_watchlist_entry('test')
            self.click_on_watchlist_entry_2()
            self.sleep(1)
            self.scroll_up()
            self.click_on_tambah_saham()
            self.add_stock_in_watchlist()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_user_not_able_to_add_more_then_15_stock_in_watchlist', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_user_not_able_to_add_more_then_15_stock_in_watchlist', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    @pytest.mark.Wat_SMMA_25
    @pytest.mark.Android
    @pytest.mark.watchlist
    @pytest.mark.Revamp
    @allure.story("F-1:Watchlist Feature")
    def test_validate_same_stock_will_be_added_to_many_watchlist(self):
        try:
            self.execute_script('lambda-name=test_validate_same_stock_will_be_added_to_many_watchlist')
            self.go_to_watchlist_option_after_login(user_data['reg_no_2'])
            self.scroll_up()
            self.click_on_defaults_btn()
            for i in range(9):
                self.click_on_plus_btn()
                self.enter_watchlist_name(f'test{i}')
            self.go_back()
            self.add_stock_in_all_watchlist()
            self.go_back()
            self.sleep(1)
            self.go_back()
            self.sleep(1)
            self.scroll_up()
            self.click_on_defaults_btn()
            self.verify_stock_in_all_watchlist()
            for i in range(9):
                self.click_on_delete()
                self.click_on_Hapus()
                self.sleep(1)
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_validate_same_stock_will_be_added_to_many_watchlist', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_validate_same_stock_will_be_added_to_many_watchlist', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)
































