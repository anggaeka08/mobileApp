import pytest
from SiminvestAppQa.src.pages.Android_pages.amend_page import AmendProcess
from SiminvestAppQa.src.pages.Android_pages.buy_process import BuyProcess
from SiminvestAppQa.src.data.userData import user_data

class Amend_test(AmendProcess,BuyProcess):

    #Validate user is able to increase and decrease the value of beli di harga and jumlah lot inside amend page of purchased stock.
    @pytest.mark.AMD_SMMA_001
    @pytest.mark.Amend
    @pytest.mark.Android
    def test_validate_increase_and_decrease_beli_harga_values_on_purchased(self):
        self.open_trans_page_with_reg_user(user_data['reg_no'])
        self.open_status_page_of_buy_order()
        self.verify_order_status_page()
        self.click_on_amend_btn()
        self.verify_plus_minus_btn_beli()

   #Validate user is able to see sending request when user proceed for amend top right corner of the screen.
    @pytest.mark.AMD_SMMA_003
    @pytest.mark.Amend
    @pytest.mark.Android
    def test_validate_status_on_amend_page(self):
        self.open_trans_page_with_reg_user(user_data['reg_no'])
        self.open_status_page_of_buy_order()
        self.verify_order_status_page()

    #Validate user is able to amend the stock price and submit it successfully at the time of buy.
    @pytest.mark.AMD_SMMA_004
    @pytest.mark.Amend
    @pytest.mark.Android
    def test_validate_amend_process_success_after_submit(self):
        self.open_trans_page_with_reg_user(user_data['reg_no'])
        self.open_status_page_of_buy_order()
        self.verify_order_status_page()
        self.click_on_amend_btn()
        self.verify_amend_purchase_page()
        self.click_on_lot_increase_no()
        self.click_on_price_increase()
        self.click_amend_btn_amend_page()
        self.click_on_confirm_btn()
        self.click_on_ok_btn()
        self.verify_transaction_page()

    #Validate user should not able to update the order outside exchange hours.
    @pytest.mark.AMD_SMMA_005
    @pytest.mark.Amend
    @pytest.mark.Android
    def test_validate_pop_for_amend_outside_exchange_hours(self):
        self.open_trans_page_with_reg_user(user_data['reg_no'])
        self.open_status_page_of_buy_order()
        self.verify_order_status_page()
        self.click_on_amend_btn()
        self.verify_amend_purchase_page()
        self.click_on_lot_increase_no()
        self.click_on_price_increase()
        self.click_amend_btn_amend_page()
        self.click_on_confirm_btn()
        self.verify_error_message_after_exchange_market()
