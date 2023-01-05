import pytest
from SiminvestAppQa.src.pages.Android_pages.stock_detail_page import StockDetailPage
from SiminvestAppQa.src.pages.Android_pages.buy_process import BuyProcess
from SiminvestAppQa.src.data.userData import user_data
import logging as logger
from selenium.common.exceptions import NoSuchElementException


class SDP_test(StockDetailPage, BuyProcess):


    @pytest.mark.SDP_Grammar
    @pytest.mark.Android
    @pytest.mark.SDP
    def test_validate_Grammar_on_sdp_page(self):
        try:
            self.execute_script('lambda-name=test_validate_Grammar_on_sdp_page')
            self.open_sdp_page_with_kyc_user(user_data['reg_no'], 'ACES')
            self.validate_grammar_of_title()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_validate_Grammar_on_sdp_page', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_validate_Grammar_on_sdp_page', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)


    @pytest.mark.SDP_Data_with_api
    @pytest.mark.Android
    @pytest.mark.SDP
    def test_validate_sdp_page_with_api_data(self):
        try:
            self.execute_script('lambda-name=SDP_Data_with_api')
            self.open_sdp_page_with_kyc_user(user_data['reg_no_2'], 'ACES')
            UI_data = self.collect_all_data_from_ui()
            API_data =self.validate_all_api_data()
            for i in range(9):
                self.assert_equal(UI_data[i] , str(API_data[i]))
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('SDP_Data_with_api', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('SDP_Data_with_api', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    @pytest.mark.SDP_back_btn
    @pytest.mark.Android
    @pytest.mark.SDP
    def test_validate_back_btn_on_sdp_page(self):
        try:
            self.execute_script('lambda-name=validate_back_btn_on_sdp_page')
            self.open_sdp_page_with_kyc_user(user_data['reg_no_3'], 'ACES')
            self.verify_sdp_page_after_back()
            self.click_on_search_btn()
            self.verify_keyboard_on_off(True)
            self.go_back()
            self.verify_keyboard_on_off(False)
            self.go_back()
            self.verify_sdp_page_after_back()
            self.click_on_search_btn()
            self.click_on_back_btn()
            self.verify_sdp_page_after_back()
            self.click_on_search_btn()
            self.enter_stock_code('ACES')
            self.click_on_stocks()
            self.verify_sdp_page_after_back()
            self.go_back()
            self.go_back()
            self.verify_home_page_reg_user()
            self.scroll_up()
            self.click_stock_1_from_top_frequency_list()
            self.sleep(2)
            self.verify_sdp_page_after_back()
            self.click_on_back_btn_on_SDP()
            self.verify_home_page_reg_user_after_back_from_watchlist_new()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('validate_back_btn_on_sdp_page', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('validate_back_btn_on_sdp_page', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    @pytest.mark.SDP_search_btn
    @pytest.mark.Android
    @pytest.mark.SDP
    def test_validate_search_btn_on_sdp_page(self):
        try:
            self.execute_script('lambda-name=test_validate_search_btn_on_sdp_page')
            self.open_sdp_page_with_kyc_user(user_data['reg_no_4'], 'ACES')
            self.verify_sdp_page_after_back()
            self.click_on_search_btn()
            self.verify_text_in_search_bar()
            self.verify_search_option_in_search_bar()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_validate_search_btn_on_sdp_page', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_validate_search_btn_on_sdp_page', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    @pytest.mark.SDP_exchange_hour_notification
    @pytest.mark.Android
    @pytest.mark.SDP
    def test_validate_sdp_exchange_hour_notification(self):
        try:
            self.execute_script('lambda-name=test_validate_sdp_exchange_hour_notification')
            self.open_sdp_page_with_kyc_user(user_data['reg_no'], 'ACES')
            self.validate_position_of_elements_on_sdp()
            self.validate_notification_in_timeline()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_validate_sdp_exchange_hour_notification', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_validate_sdp_exchange_hour_notification', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    @pytest.mark.stock_special_notation
    @pytest.mark.Android
    @pytest.mark.SDP
    def test_validate_special_notation_on_stock(self):
        try:
            self.execute_script('lambda-name=test_validate_special_notation_on_stock')
            self.validate_special_notation()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_validate_special_notation_on_stock', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_validate_special_notation_on_stock', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    @pytest.mark.suspended_stock
    @pytest.mark.Android
    @pytest.mark.SDP
    def test_validate_suspended_testcases(self):
        try:
            self.execute_script('lambda-name=test_validate_suspended_testcases')
            self.validate_watchlist_buy_for_suspended_stock()
            self.validate_suspended_stock_on_sdp()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_validate_suspended_testcases', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_validate_suspended_testcases', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    # Validate user is able to star mark the stock/ Validate user is able to un-mark the star.
    @pytest.mark.Star_mark_test
    @pytest.mark.Android
    @pytest.mark.SDP
    def test_validate_star_mark_on_sdp(self):
        try:
            self.execute_script('lambda-name=test_validate_star_mark_on_sdp')
            self.open_sdp_page_with_kyc_user(user_data['reg_no_3'], 'ACES')
            self.verify_star_mark_on_sdp()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_validate_star_mark_on_sdp', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)

        except NoSuchElementException as E:
            self.save_screenshot('test_validate_star_mark_on_sdp', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    # Validate sdp chart.
    @pytest.mark.sdp_chart
    @pytest.mark.Android
    @pytest.mark.SDP
    def test_validate_sdp_chart(self):
        try:
            self.execute_script('lambda-name=test_validate_sdp_chart')
            self.open_sdp_page_with_kyc_user(user_data['reg_no_3'], 'ACES')
            self.validate_sdp_chart()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_validate_sdp_chart', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_validate_sdp_chart', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    # Validate sdp chart.
    @pytest.mark.SBP_UI_Functional
    @pytest.mark.Android
    @pytest.mark.SDP
    def test_validate_sbp_ui_function(self):
        try:
            self.execute_script('lambda-name=test_validate_sbp_ui_function')
            self.open_sdp_page_with_kyc_user(user_data['reg_no_4'], 'ACES')
            self.click_on_buy_btn()
            self.go_back()
            self.sleep(2)
            self.verify_sdp_page_after_back()
            self.click_on_buy_btn()
            self.verify_buy_page()
            self.verify_lot_count("1")
            self.click_on_lot_increase_no()
            self.verify_lot_count("2")
            self.click_on_lot_decrease_btn()
            self.verify_lot_count("1")
            self.verify_plus_minus_btn_beli()
            self.tap_on_gtc_option()
            self.click_on_date()
            self.go_back()
            self.verify_buy_page()
            self.verify_total_beli_amount()
            self.verify_lot_harga_jumlah_value()
            self.go_back()
            self.verify_ask_value_reflect_in_beli_de_harga()
            self.scroll_up()
           # self.verify_redirection_after_click_on_support_btn()
            #self.go_back()
            self.click_on_buy_btn_on_buy_page()
            self.verify_redirection_to_confirmation_page()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_validate_sbp_ui_function', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_validate_sbp_ui_function', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    # Validate sdp chart.
    @pytest.mark.SBP_GTC_Validation
    @pytest.mark.Android
    @pytest.mark.SDP
    def test_SBP_GTC_Validation(self):
        try:
            self.execute_script('lambda-name=test_SBP_GTC_Validation')
            self.open_sdp_page_with_kyc_user(user_data['reg_no'], 'ACES')
            self.check_for_buy_btn()
            self.click_on_buy_btn()
            self.verify_buy_page()
            self.tap_on_gtc_option()
            self.verify_default_date_after_tap_on_gtc_option()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_SBP_GTC_Validation', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_SBP_GTC_Validation', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    # Validate sdp chart.
    @pytest.mark.Stock_buy_conf_page
    @pytest.mark.Android
    @pytest.mark.SDP
    def test_Stock_buy_conf_page(self):
        try:
            self.execute_script('lambda-name=test_Stock_buy_conf_page')
            self.open_sdp_page_with_kyc_user(user_data['reg_no'], 'ASII')
            self.click_on_buy_btn()
            self.validate_order_confirmation_page_for_buy()
            self.validate_order_confirmation_page_for_sell()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_Stock_buy_conf_page', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_Stock_buy_conf_page', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)




"""    # Validate search option on sdp page
    @pytest.mark.SDP_SMMA_003_004
    @pytest.mark.Android
    def test_validate_search_option_on_sdp(self):
        self.open_sdp_page_with_kyc_user(user_data['reg_no'], 'ACES')
        self.click_on_search_btn()
        self.enter_stock_code('ACES')
        self.click_on_stocks()
        self.verify_sdp_page()
        self.go_back()
        self.go_back()
        self.verify_home_page_reg_user()

    # Validate test cases SMMA_013
    @pytest.mark.SDP_SMMA_006_013
    @pytest.mark.Android
    def test_Validate_test_cases_SMMA_006_013(self):
        self.open_sdp_page_with_kyc_user(user_data['reg_no'], 'ACES')
        self.chart_presence()
        self.order_book_tab_open()

  # Validate test cases  SMMA_016_021_022
    @pytest.mark.SDP_SMMA_016_021_022
    @pytest.mark.Android
    def test_Validate_profile_btn_and_header_details_of_values(self):
        self.open_sdp_page_with_kyc_user(user_data['reg_no'], 'ACES')
        self.verify_details_down_to_beli_btn()
        self.click_on_profile()
        self.scroll_up()
        self.verify_details_of_profile_tab()
        self.verify_stock_company_address()

    #Validate news tab on SDP page and news page details
    @pytest.mark.SDP_SMMA_023_to_027
    @pytest.mark.Android
    def test_Validate_news_tab_on_SDP_page_and_news_page_details(self):
        self.open_sdp_page_with_kyc_user(user_data['reg_no'], 'ACES')
        self.verify_news_availability_on_sdp()
        self.click_on_news()
        self.scroll_up_screen()
        self.verify_news_dates_list()
        self.verify_news_title()
        self.validate_domain_name_for_one_news()

    #Validate news tab on SDP page and news page details
    @pytest.mark.SDP_SMMA_028_to_031
    @pytest.mark.Android
    def test_Validate_news_tab_on_SDP_pages(self):
        self.open_sdp_page_with_kyc_user(user_data['reg_no'], 'ACES')
        self.verify_news_availability_on_sdp()
        self.click_on_news()
        self.scroll_up_screen()
        self.validate_maximum_available_news()
        self.validate_all_news_are_separated()

    # Validate user is redirected to customer care support page when user click on contact customer button available at the bottom on external browser.
    @pytest.mark.SDP_SMMA_45
    @pytest.mark.Android
    def test_Validate_redirection_after_click_on_customer_support_btn(self):
        self.open_sdp_by_portfolio_with_kyc_user(user_data['reg_no'])
        self.scroll_up_screen()
        self.scroll_up_screen()
        self.verify_redirection_after_click_on_support_btn()

    #Validate test cases  SMMA_014
    @pytest.mark.SDP_SMMA_014
    @pytest.mark.Android
    def test_validate_profile_details_for_stock_company_details_unavailable(self):
        self.open_sdp_page_with_kyc_user(user_data['reg_no'], 'WIFI-W')
        self.verify_details_down_to_beli_btn()
        self.click_on_profile()
        self.verify_stock_profile_when_details_not_available()

    #Validate test cases  SMMA_037
    @pytest.mark.SDP_SMMA_037
    @pytest.mark.Android
    def test_validate_user_will_able_to_see_value_at_below_of_the_stock_price(self):
        self.open_sdp_by_portfolio_with_kyc_user(user_data['reg_no'])
        self.verify_details_availability_when_move_to_sdp_by_portfolio_page()

    #Validate the response is written for all the required detail.
    @pytest.mark.SDP_SMMA_019
    @pytest.mark.Android
    def test_Validate_profile_details_doesnot_have_hiphan(self):
        self.open_sdp_page_with_kyc_user(user_data['reg_no'], 'ACES')
        self.verify_details_down_to_beli_btn()
        self.click_on_profile()
        self.scroll_up()
        self.verify_details_of_profile()

"""