import allure
import pytest
from selenium.common.exceptions import NoSuchElementException
import logging as logger
from SiminvestAppQa.src.data.userData import user_data
from SiminvestAppQa.src.pages.Android_pages.transaction import Transaction


@pytest.mark.usefixtures("unittest_setUpClass_fixture_Transaction_test")
class Transaction_test(Transaction):

    # Transaction page for order list
    @pytest.mark.tran_order_list_ui
    @pytest.mark.Android
    @pytest.mark.Transaction
    @allure.story("F-8:Transaction Page")
    def test_ui_functionality_of_order_list_tab(self):
        try:
            self.execute_script('lambda-name=test_ui_functionality_of_orderlist_tab')
            self.open_trans_page_with_reg_user(user_data['reg_no'])
            self.verify_common_details_for_all_tabs()
            self.verify_entries_details_on_transaction_tab_for_order_list()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_ui_functionality_of_orderlist_tab', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_ui_functionality_of_orderlist_tab', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    # Transaction page for order list
    @pytest.mark.trans_history_list_ui
    @pytest.mark.Android
    @pytest.mark.Transaction
    @allure.story("F-8:Transaction Page")
    def test_ui_functionality_of_history_list_tab(self):
        try:
            self.execute_script('lambda-name=test_ui_functionality_of_history_list_tab')
            self.open_trans_page_with_reg_user(user_data['reg_no'])
            self.verify_common_details_for_all_tabs()
            self.verify_entries_details_on_transaction_tab_for_history_list()
            self.verify_filter_option_for_history_list()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_ui_functionality_of_history_list_tab', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_ui_functionality_of_history_list_tab', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    # Transaction page for order list
    @pytest.mark.tran_order_list_details
    @pytest.mark.Android
    @pytest.mark.Transaction
    @allure.story("F-8:Transaction Page")
    def test_ui_for_order_details_page(self):
        try:
            self.execute_script('lambda-name=test_ui_for_order_details_page')
            self.open_trans_page_with_reg_user(user_data['reg_no'])
            self.verify_transaction_page()
            self.verify_order_details_page()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_ui_for_order_details_page', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_ui_for_order_details_page', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)


    #order detail  of transaction history
    @pytest.mark.order_details_of_history_list
    @pytest.mark.Android
    @pytest.mark.Transaction
    @allure.story("F-8:Transaction Page")
    def test_ui_for_order_details_of_history_list(self):
        try:
            self.execute_script('lambda-name=test_ui_for_order_details_of_history_list')
            self.open_trans_page_with_reg_user(user_data['reg_no'])
            self.verify_order_details_of_history_list()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_ui_for_order_details_of_history_list', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_ui_for_order_details_of_history_list', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    @pytest.mark.trans_gtc_list_ui
    @pytest.mark.Android
    @pytest.mark.Transaction
    @allure.story("F-8:Transaction Page")
    def test_ui_functionality_of_gtc_list_tab(self):
        try:
            self.execute_script('lambda-name=test_ui_functionality_of_gtc_list_tab')
            self.open_trans_page_with_reg_user(user_data['reg_no'])
            self.verify_ui_functionality_of_GTC_list_tab()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_ui_functionality_of_gtc_list_tab', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_ui_functionality_of_gtc_list_tab', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    @pytest.mark.order_details_of_gtc_list
    @pytest.mark.Android
    @pytest.mark.Transaction
    @allure.story("F-8:Transaction Page")
    def test_ui_for_order_details_of_gtc_list(self):
        try:
            self.execute_script('lambda-name=test_ui_for_order_details_of_gtc_list')
            self.open_trans_page_with_reg_user(user_data['reg_no'])
            self.verify_order_details_of_gtc_list()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_ui_for_order_details_of_gtc_list', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_ui_for_order_details_of_gtc_list', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    @pytest.mark.functional_feature_of_order_list
    @pytest.mark.Android
    @pytest.mark.Transaction
    @allure.story("F-8:Transaction Page")
    def test_functional_feature_of__order_list(self):
        try:
            self.execute_script('lambda-name=test_functional_feature_of__order_list')
            self.open_trans_page_with_reg_user(user_data['reg_no'])
            self.verify_search_bar_functionality()
            self.verify_swiping_functionality()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_functional_feature_of__order_list', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_functional_feature_of__order_list', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    @pytest.mark.order_list_Data_with_api
    @pytest.mark.Android
    @pytest.mark.SDP
    @allure.story("F-7:SDP Feature")
    def test_order_list_Data_with_api(self):
        try:
            self.execute_script('lambda-name=test_order_list_Data_with_api')
            self.open_trans_page_with_reg_user(user_data['reg_no'])
            code_ui,exectime_ui = self.collect_all_data_from_order_list_ui()
            code_api , exectime_api  = self.validate_all_api_data()
            logger.info(f'code_ui {code_ui}')
            logger.info(f'exectime_ui {exectime_ui}')
            logger.info(f'code_api {code_api}')
            logger.info(f'exectime_api {exectime_api}')
            for i in code_ui:
                assert i in code_api
            for i in exectime_ui:
                assert i in exectime_api
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_order_list_Data_with_api', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_order_list_Data_with_api', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    @pytest.mark.functional_feature_of_order_detail_page
    @pytest.mark.Android
    @pytest.mark.Transaction
    @allure.story("F-8:Transaction Page")
    def test_functional_feature_of_order_detail_page(self):
        try:
            self.execute_script('lambda-name=test_functional_feature_of_order_detail_page')
            self.open_trans_page_with_reg_user(user_data['reg_no'])
            self.verify_functional_features_of_order_detail_page()
            self.verify_withdraw_process_from_odp()
            self.verify_amend_process_from_odp()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_functional_feature_of_order_detail_page', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_functional_feature_of_order_detail_page', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    @pytest.mark.functional_feature_of_filter_in_order_list
    @pytest.mark.Android
    @pytest.mark.Transaction
    @allure.story("F-8:Transaction Page")
    def test_functional_feature_of_filter_in_order_list(self):
        try:
            self.execute_script('lambda-name=test_functional_feature_of_filter_in_order_list')
            self.open_trans_page_with_reg_user(user_data['reg_no'])
            self.verify_filter_in_order_list()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_functional_feature_of_filter_in_order_list', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_functional_feature_of_filter_in_order_list', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    @pytest.mark.functional_feature_of_history_list
    @pytest.mark.Android
    @pytest.mark.Transaction
    @allure.story("F-8:Transaction Page")
    def test_functional_feature_of_history_list(self):
        try:
            self.execute_script('lambda-name=functional_feature_of_history_list')
            self.open_trans_page_with_reg_user(user_data['reg_no'])
            self.verify_search_bar_functionality_of_history_list()
            self.verify_swiping_functionality_of_history_list()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('functional_feature_of_history_list', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('functional_feature_of_history_list', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    @pytest.mark.history_list_Data_with_api
    @pytest.mark.Android
    @pytest.mark.SDP
    @allure.story("F-7:SDP Feature")
    def test_history_list_Data_with_api(self):
        try:
            self.execute_script('lambda-name=test_history_list_Data_with_api')
            self.open_trans_page_with_reg_user(user_data['reg_no'])
            code_ui, trade_date_ui = self.collect_all_data_from_history_list_ui()
            code_api, trade_date_api = self.validate_history_list_api_data()
            logger.info(f'code_ui {code_ui}')
            logger.info(f'trade_date_ui {trade_date_ui}')
            logger.info(f'code_api {code_api}')
            logger.info(f'trade_date_api {trade_date_api}')
            for i in code_ui:
                assert i in code_api
            for i in trade_date_ui:
                assert i in trade_date_api
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_history_list_Data_with_api', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_history_list_Data_with_api', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    @pytest.mark.functional_feature_of_filter_in_history_list
    @pytest.mark.Android
    @pytest.mark.Transaction
    @allure.story("F-8:Transaction Page")
    def test_functional_feature_of_filter_in_history_list(self):
        try:
            self.execute_script('lambda-name=test_functional_feature_of_filter_in_history_list')
            self.open_trans_page_with_reg_user(user_data['reg_no'])
            self.verify_filter_in_history_list()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_functional_feature_of_filter_in_history_list',
                                 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_functional_feature_of_filter_in_history_list',
                                 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)


    # Cover all 5 test cases in single test
    @pytest.mark.T_SMMA_001_to_005
    @pytest.mark.Android
    def test_validate_transaction_btn_redirection_saham_reksadana_tab(self):
        self.open_trans_page_with_reg_user(user_data['reg_no'])
        self.verify_last_transaction_orderlist()

    @pytest.mark.T_SMMA_008
    @pytest.mark.Android
    def test_GTC_tab_contain_gtc_transactions(self):
        self.open_trans_page_with_reg_user(user_data['reg_no'])
        self.click_on_gtc_tab()
        self.verify_GTC_tab_entries()

    @pytest.mark.T_SMMA_010_to_017
    @pytest.mark.Android
    def test_verify_all_type_btn_feature(self):
        self.open_trans_page_with_reg_user(user_data['reg_no'])
        self.verify_search_bar()
        self.click_to_reksadana()
        self.verify_reksadana_tab()
        self.click_to_saham()
        self.verify_saham_tab()
        self.click_to_all_types()
        self.go_back()
        self.verify_saham_tab()
        self.click_to_all_types()
        self.verify_all_types_values()
        self.click_on_buy_all()
        self.verify_transaction_page_for_buy_all()
        self.click_to_all_types()
        self.click_on_sell_all()
        self.verify_transaction_page_for_sell_all()

    @pytest.mark.T_SMMA_019_to_026
    @pytest.mark.Android
    def test_verify_reksadana_transactions(self):
        self.open_trans_page_with_reg_user(user_data['mf_user'])
        self.click_to_reksadana()
        self.verify_all_types_and_all_status_btn()
        self.verify_orderlist_and_riwayat_tab()
        self.click_on_all_status_btn()
        self.verify_option_in_all_status_btn()
        self.click_on_in_progress()
        self.verify_status_after_sorting_by_inprogress()
        #self.click_on_all_status_btn()
        #self.click_on_awaiting_payment()
        #self.verify_status_after_sorting_by_awaitning_payemnt()
        self.scroll_up()
        self.scroll_down()
        self.click_to_saham()
        self.sleep(3)
        self.scroll_down()
        self.scroll_up()

    @pytest.mark.T_SMMA_028_29_30_34
    @pytest.mark.Android
    def test_verify_left_right_swipe_and_search_options(self):
        self.open_trans_page_with_reg_user(user_data['reg_no'])
        self.swipe_right()
        self.verify_all_types_btn_for_trade_list()
        self.swipe_right()
        self.verify_all_type_btn_for_history_list()
        self.swipe_right()
        self.verify_all_type_btn_for_gtc_list()
        self.swipe_left()
        self.swipe_left()
        self.swipe_left()
        self.verify_all_types_btn_for_order_list()
        self.enter_value_in_search_box('TEST')
        self.verify_enteries_after_enter_null_or_space_in_search_option()
        self.enter_value_in_search_box(' ')
        self.verify_enteries_after_enter_null_or_space_in_search_option()
        self.click_on_gtc_tab()
        self.click_on_gtc_first_entry()
        self.click_on_batal()
        self.click_on_YA()
        self.click_on_ok()
        self.verify_status_of_first_entry()

    @pytest.mark.T_SMMA_039_040
    @pytest.mark.Android
    def test_verify_gtc_order_page_and_help_option(self):
        self.open_trans_page_with_reg_user(user_data['reg_no'])
        self.click_on_gtc_tab()
        self.click_on_gtc_first_entry()
        self.verify_details_available_on_gtc_order_details_page()
        self.click_on_customer_btn()
        self.sleep(3)
        self.verify_redirection_after_click_on_customer_support()


    @pytest.mark.T_SMMA_035
    @pytest.mark.Android
    def test_verify_gtc_order_page_redirection(self):
        self.open_trans_page_with_reg_user(user_data['reg_no'])
        self.click_on_gtc_tab()
        self.click_on_gtc_first_entry()
        self.go_back()
        self.verify_gtc_first_entry_available()



















