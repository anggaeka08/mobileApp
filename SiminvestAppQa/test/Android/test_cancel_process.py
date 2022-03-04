import pytest
from SiminvestAppQa.src.pages.Android_pages.cancel_process import CancelProcess
from SiminvestAppQa.test.Android.test_buy_process import BuyProcess_test
from SiminvestAppQa.src.data.userData import user_data

class Cancel_test(CancelProcess, BuyProcess_test):

    #Validate user should redirected to order page when user click on OK button on cancel confirmation page.
    @pytest.mark.CAN_SMMA_010
    @pytest.mark.Amend
    @pytest.mark.Android
    def test_validate_positive_flow_for_cancel_feature(self):
        self.test_validate_status_on_transaction_page()
        self.open_status_page_of_buy_order()
        self.click_on_cancel_btn_on_status_page()
        self.click_on_cancel_confirmation_btn()
        self.click_on_ok_btn()
        self.verify_transaction_on_transaction_page_after_cancel()

    #Validate user should not allow to cancel the order outside exchange hours.
    @pytest.mark.CAN_SMMA_003
    @pytest.mark.Amend
    @pytest.mark.Android
    def test_validate_pop_message_after_outside_exchange_hour(self):
        self.open_trans_page_with_reg_user(user_data['reg_no'])
        self.open_status_page_of_buy_order()
        self.verify_order_status_page()
        self.click_on_cancel_btn_on_status_page()
        self.click_on_cancel_confirmation_btn()
        self.verify_error_message_after_exchange_market()
        self.click_on_ok_btn()
        self.verify_order_status_page()

