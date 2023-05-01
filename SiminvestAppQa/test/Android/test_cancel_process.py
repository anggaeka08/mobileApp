import allure
import pytest
from selenium.common.exceptions import NoSuchElementException

from SiminvestAppQa.src.pages.Android_pages.cancel_process import CancelProcess
from SiminvestAppQa.src.data.userData import user_data


class Cancel_test(CancelProcess):

    @pytest.mark.Cancel_process_for_buy
    @pytest.mark.Cancel
    @pytest.mark.Android
    @allure.story("F-14: Cancel Feature")
    def test_Cancel_process_for_buy(self):
        try:
            self.execute_script('lambda-name=test_Cancel_process_for_buy')
            self.open_sdp_page_with_kyc_user(user_data['reg_no'], 'ACES')
            self.check_for_buy_btn()
            self.click_on_buy_btn()
            self.verify_buy_page()
            self.click_on_buy_btn_on_buy_page()
            self.click_on_confirm_btn()
            self.click_on_ok_btn()
            self.verify_transaction_page()
            self.verify_status_on_transaction_page()
            self.open_status_page_of_buy_order()
            self.click_on_cancel_btn_on_status_page()
            self.click_on_click_cancel_btn_at_confirmation_pop_up()
            self.verify_order_status_page()
            self.click_on_cancel_btn_on_status_page()
            self.click_by_position()
            self.validate_place_order_confirmation_pop_up()
            self.click_on_cancel_confirmation_btn()
            self.validate_place_order_success_text()
            self.click_on_ok_btn()
            self.verify_transaction_on_transaction_page_after_cancel()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_Cancel_process_for_buy', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_Cancel_process_for_buy', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    #Validate user should redirected to order page when user click on OK button on cancel confirmation page.
    @pytest.mark.CAN_SMMA_010
    @pytest.mark.Cancel_OLD
    @pytest.mark.Android
    @pytest.mark.timeBased
    def test_validate_positive_flow_for_cancel_feature(self):
        self.open_sdp_page_with_kyc_user(user_data['reg_no'], 'ACES')
        self.check_for_buy_btn()
        self.click_on_buy_btn()
        self.verify_buy_page()
        self.click_on_buy_btn_on_buy_page()
        self.click_on_confirm_btn()
        self.click_on_ok_btn()
        self.verify_transaction_page()
        self.verify_status_on_transaction_page()
        self.open_status_page_of_buy_order()
        self.click_on_cancel_btn_on_status_page()
        self.click_on_cancel_confirmation_btn()
        self.click_on_ok_btn()
        self.verify_transaction_on_transaction_page_after_cancel()

    #Validate user should not allow to cancel the order outside exchange hours.
    @pytest.mark.CAN_SMMA_003
    @pytest.mark.Cancel_OLD
    @pytest.mark.Android
    @pytest.mark.timeBased
    def test_validate_pop_message_after_outside_exchange_hour(self):
        self.open_trans_page_with_reg_user(user_data['reg_no'])
        self.open_status_page_of_buy_order()
        self.sleep(3)
        self.verify_order_status_page()
        self.click_on_cancel_btn_on_status_page()
        self.click_on_cancel_confirmation_btn()
        self.sleep(5)
        self.verify_error_message_after_exchange_market()
        self.click_on_ok_btn_after_market_close()
        self.verify_order_status_page()

    #Validate all the words are grammatically correct at the time of cancel process.
    @pytest.mark.CAN_SMMA_004
    @pytest.mark.Cancel_OLD
    @pytest.mark.Android
    def test_grammatically_correct_at_the_time_of_cancel_process(self):
        self.open_trans_page_with_reg_user(user_data['reg_no'])
        self.open_status_page_of_buy_order()
        self.verify_grammatical_error_on_order_status_page()

    #Validate user is redirected to cancel and amend page when user click on tidak button on cancel confirmation page.
    @pytest.mark.CAN_SMMA_011
    @pytest.mark.Cancel_OLD
    @pytest.mark.Android
    def test_validate_redirection_after_click_on_cancel(self):
        self.open_trans_page_with_reg_user(user_data['reg_no'])
        self.open_status_page_of_buy_order()
        self.verify_order_status_page()
        self.click_on_cancel_btn_on_status_page()
        self.click_on_click_cancel_btn_at_confirmation_pop_up()
        self.verify_order_status_page()
