import pytest
from SiminvestAppQa.src.pages.Android_pages.amend_page import AmendProcess
from SiminvestAppQa.src.data.userData import user_data

class Amend_test(AmendProcess):

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

    # Validate user is able to select buy and sell value from below given QTY buy page.
    @pytest.mark.AMD_SMMA_006
    @pytest.mark.Amend
    @pytest.mark.Android
    def test_user_able_to_select_price_from_ask_bid(self):
        self.open_trans_page_with_reg_user(user_data['reg_no'])
        self.open_status_page_of_buy_order()
        self.verify_order_status_page()
        self.click_on_amend_btn()
        self.verify_amend_purchase_page()
        self.verify_user_able_to_set_ask_bid_value_in_harga()

    #Validate if price and lot equal - no need to validate buying power at the time of amend.
    @pytest.mark.AMD_SMMA_009
    @pytest.mark.Amend
    @pytest.mark.Android
    def test_verify_price_and_lot_for_both_pages(self):
        self.open_trans_page_with_reg_user(user_data['reg_no'])
        self.open_status_page_of_buy_order()
        self.verify_order_status_page()
        self.verify_lot_harga_on_two_pages()

    #Validate if user decrease price or decrease lot - no need to validate buying power at the time of amend.
    @pytest.mark.AMD_SMMA_010
    @pytest.mark.Amend
    @pytest.mark.Android
    def test_validate_decrease_lot_and_harga(self):
        self.open_trans_page_with_reg_user(user_data['reg_no'])
        self.open_status_page_of_buy_order()
        self.verify_order_status_page()
        self.click_on_amend_btn()
        self.verify_amend_purchase_page()
        self.click_on_lot_decrease_btn()
        self.verify_amend_purchase_page()
        self.click_on_price_decrease()
        self.verify_amend_purchase_page()

    #Validate if user increase price or increase lot - validate with buying power at the time of amend
    @pytest.mark.AMD_SMMA_011
    @pytest.mark.Amend
    @pytest.mark.Android
    def test_validate_increase_lot_and_harga(self):
        self.open_trans_page_with_reg_user(user_data['reg_no'])
        self.open_status_page_of_buy_order()
        self.verify_order_status_page()
        self.click_on_amend_btn()
        self.verify_amend_purchase_page()
        self.click_on_lot_increase_no()
        self.verify_amend_purchase_page()
        self.click_on_price_increase()
        self.verify_amend_purchase_page()

    # Validate user should receive an error prompt "cannot increase the QTY" when user trying to increase the lot of purchased stock.
    @pytest.mark.AMD_SMMA_012
    @pytest.mark.Amend
    @pytest.mark.Android
    def test_validate_error_while_increase_lot_value(self):
        self.open_trans_page_with_reg_user(user_data['reg_no'])
        self.open_status_page_of_buy_order()
        self.verify_order_status_page()
        self.click_on_amend_btn()
        self.verify_amend_purchase_page()
        self.click_on_lot_increase_no()
        self.click_amend_btn_amend_page()
        self.click_on_confirm_btn()
        self.verify_auto_rejection_pop_message()

  #Validate user should redirected to amend page when user click on OK button on error prompt page.
    @pytest.mark.AMD_SMMA_013
    @pytest.mark.Amend
    @pytest.mark.Android
    def test_validate_redirection_after_error_while_increase_lot_value(self):
        self.open_trans_page_with_reg_user(user_data['reg_no'])
        self.open_status_page_of_buy_order()
        self.verify_order_status_page()
        self.click_on_amend_btn()
        self.verify_amend_purchase_page()
        self.click_on_lot_increase_no()
        self.click_amend_btn_amend_page()
        self.click_on_confirm_btn()
        self.verify_auto_rejection_pop_message()
        self.click_on_ok_btn_on_auto_rejection()
        self.verify_amend_purchase_page()

    #Validate user should get out of the app from the app when user click on back button on on transection page.
    @pytest.mark.AMD_SMMA_014
    @pytest.mark.Amend
    @pytest.mark.Android
    def test_validate_redirection_after_back_from_trans_page(self):
        self.open_trans_page_with_reg_user(user_data['reg_no'])
        self.go_back()
        self.check_phone_home_screen()

    #Validate user is redirected to order section page when user click on back button when user is on cancel and amend section page.
    @pytest.mark.AMD_SMMA_015
    @pytest.mark.Amend
    @pytest.mark.Android
    def test_validate_redirection_after_back_from_cancel_and_amend_page(self):
        self.open_trans_page_with_reg_user(user_data['reg_no'])
        self.open_status_page_of_buy_order()
        self.sleep(3)
        self.verify_order_status_page()
        self.go_back()
        self.sleep(2)
        self.verify_transaction_page()


    #Validate user is redirected to cancel and amend page when user click on back button when user is on amend page.
    @pytest.mark.AMD_SMMA_016
    @pytest.mark.Amend
    @pytest.mark.Android
    def test_validate_redirection_after_back_from_amend_page(self):
        self.open_trans_page_with_reg_user(user_data['reg_no'])
        self.open_status_page_of_buy_order()
        self.verify_order_status_page()
        self.click_on_amend_btn()
        self.verify_amend_purchase_page()
        self.go_back()
        self.sleep(1)
        self.verify_order_status_page()

    #Validate user is redirected to amend page when click on cancel button buton on amend confirmation page.
    @pytest.mark.AMD_SMMA_017
    @pytest.mark.Amend
    @pytest.mark.Android
    def test_validate_redirection_after_back_from_amend_confirmation_page(self):
        self.open_trans_page_with_reg_user(user_data['reg_no'])
        self.open_status_page_of_buy_order()
        self.verify_order_status_page()
        self.click_on_amend_btn()
        self.verify_amend_purchase_page()
        self.click_amend_btn_amend_page()
        self.go_back()
        self.verify_amend_purchase_page()
        self.click_amend_btn_amend_page()
        self.click_on_cancel_btn()
        self.verify_amend_purchase_page()

    #Validate user is redirected to transection order section page and the value of ordered stock is changed when user click on confirm button.
    @pytest.mark.AMD_SMMA_018
    @pytest.mark.Amend
    @pytest.mark.Android
    def test_validate_verify_amend_transaction_on_trans_page(self):
        self.open_trans_page_with_reg_user(user_data['reg_no'])
        self.open_status_page_of_buy_order()
        self.verify_order_status_page()
        self.click_on_amend_btn()
        self.verify_amend_purchase_page()
        self.verify_transaction_presence_after_amend_success()

    # Validate user should not allow to amend the stock when user is outside exchange hours and receive error promot.
    @pytest.mark.AMD_SMMA_019
    @pytest.mark.Amend
    @pytest.mark.Android
    def test_validate_pop_for_amend_outside_exchange_hour(self):
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

    #Validate user should redirected amend page when user click on x and ok button when user is on outside exchange hour error popup page.
    @pytest.mark.AMD_SMMA_020
    @pytest.mark.Amend
    @pytest.mark.Android
    def test_validate_redirect_to_amend_page_after_pop_of_market_close(self):
        self.open_trans_page_with_reg_user(user_data['reg_no'])
        self.open_status_page_of_buy_order()
        self.verify_order_status_page()
        self.click_on_amend_btn()
        self.verify_amend_purchase_page()
        self.click_on_price_increase()
        self.click_amend_btn_amend_page()
        self.click_on_confirm_btn()
        self.verify_error_message_after_exchange_market()
        self.click_on_ok_btn()
        self.verify_amend_purchase_page()

    # Validate detail of stock is mentioned in order transection page like lot price and value is same compare to cancel page.
    @pytest.mark.AMD_SMMA_021
    @pytest.mark.Amend
    @pytest.mark.Android
    def test_validate_values_between_trans_page_cancel_page(self):
        self.open_trans_page_with_reg_user(user_data['reg_no'])
        self.verify_lot_price_value_on_trans_page_and_amend_or_cancel_page()

    #Validate user is redirected to external browser when user click on Hubungi coustomer care button.
    @pytest.mark.AMD_SMMA_022
    @pytest.mark.Amend
    @pytest.mark.Android
    def test_validate_redirection_to_external_browser_after_click(self):
        self.open_trans_page_with_reg_user(user_data['reg_no'])
        self.open_status_page_of_buy_order()
        self.click_on_customer_support_link()

