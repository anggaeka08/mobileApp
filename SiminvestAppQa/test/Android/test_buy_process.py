import pytest
from SiminvestAppQa.src.pages.Android_pages.buy_process import BuyProcess
from SiminvestAppQa.src.data.userData import user_data

class BuyProcess_test(BuyProcess):

    #Validate that user can see buy button on stock detail page
    @pytest.mark.BP_SMMA_301
    @pytest.mark.BuyProcess
    @pytest.mark.Android
    def test_validate_buy_btn_on_sdp_page(self):
        self.open_sdp_page_with_kyc_user(user_data['reg_no'], 'ACES')
        self.check_for_buy_btn()

    #Validate that there is two button buy/sell if stock is already purchased for KYC user.
    @pytest.mark.BP_SMMA_302
    @pytest.mark.BuyProcess
    @pytest.mark.Android
    def test_validate_buy_sell_btn_on_sdp_page(self):
        self.open_sdp_by_portfolio_with_kyc_user(user_data['reg_no'])
        self.check_for_sell_btn()
        self.check_for_buy_btn()

    #Validate the non KYC user should redirect to referral page when user click on beli button.
    @pytest.mark.BP_SMMA_309
    @pytest.mark.BuyProcess
    @pytest.mark.Android
    def test_validate_redirect_to_refferal_page_by_click_on_buy_for_non_kyc(self):
        self.open_sdp_page_with_non_kyc_user(user_data['unkyc_reg_no'], 'ACES')
        self.check_for_buy_btn()
        self.click_on_buy_btn()
        self.verify_refferal_page()

    #Validate user is able to cancel the order after click on buy button using cancel button.
    @pytest.mark.BP_SMMA_305
    @pytest.mark.BuyProcess
    @pytest.mark.Android
    def test_validate_cancel_btn_on_buy_page(self):
        self.open_sdp_page_with_kyc_user(user_data['reg_no'], 'ACES')
        self.check_for_buy_btn()
        self.click_on_buy_btn()
        self.verify_buy_page()
        self.click_on_buy_btn_on_buy_page()
        self.click_on_cancel_btn()
        self.verify_buy_page()

    #Validate GTC option is working fine
    @pytest.mark.BP_SMMA_306
    @pytest.mark.BuyProcess
    @pytest.mark.Android
    def test_validate_gtc_buy_option(self):
        self.open_sdp_page_with_kyc_user(user_data['reg_no'], 'ACES')
        self.check_for_buy_btn()
        self.click_on_buy_btn()
        self.verify_buy_page()
        self.tap_on_gtc_option()
        self.click_on_date()
        self.select_date()
        self.click_on_buy_btn_on_buy_page()
        self.click_on_confirm_btn()
        self.click_on_ok_btn()
        self.verify_transaction_page()

    #Validate user is able top select date from GTC calender.
    @pytest.mark.BP_SMMA_307
    @pytest.mark.BuyProcess
    @pytest.mark.Android
    def test_validate_top_select_date(self):
        self.open_sdp_page_with_kyc_user(user_data['reg_no'], 'ACES')
        self.check_for_buy_btn()
        self.click_on_buy_btn()
        self.verify_buy_page()
        self.tap_on_gtc_option()
        self.verify_current_date()
        self.click_on_date()
        self.select_date()
        self.verify_date_changes_reflects()

    #Validate the default value for buy stock is 1.
    @pytest.mark.BP_SMMA_308
    @pytest.mark.BuyProcess
    @pytest.mark.Android
    def test_validate_default_value_of_lot(self):
        self.open_sdp_page_with_kyc_user(user_data['reg_no'], 'ACES')
        self.check_for_buy_btn()
        self.click_on_buy_btn()
        self.verify_buy_page()
        self.verify_lot_count("1")

    # Validate that user can see the Beli button on stock detail page
    @pytest.mark.BP_SMMA_310
    @pytest.mark.BuyProcess
    @pytest.mark.Android
    def test_validate_Beli_btn_on_sdp_page(self):
        self.open_sdp_page_with_kyc_user(user_data['reg_no'], 'ACES')
        self.check_for_buy_btn()

    #Validate user is able to increase and decrease the lot on buy page.
    @pytest.mark.BP_SMMA_311
    @pytest.mark.BuyProcess
    @pytest.mark.Android
    def test_validate_plus_minus_work_in_lot(self):
        self.open_sdp_page_with_kyc_user(user_data['reg_no'], 'ACES')
        self.check_for_buy_btn()
        self.click_on_buy_btn()
        self.verify_buy_page()
        self.verify_lot_count("1")
        self.click_on_lot_increase_no()
        self.verify_lot_count("2")
        self.click_on_lot_decrease_btn()
        self.verify_lot_count("1")

    # Validate the back button is working fine at the time of purchase process.
    @pytest.mark.BP_SMMA_312
    @pytest.mark.BuyProcess
    @pytest.mark.Android
    def test_validate_back_btn_on_buy_page(self):
        self.open_sdp_page_with_kyc_user(user_data['reg_no'], 'ACES')
        self.check_for_buy_btn()
        self.click_on_buy_btn()
        self.verify_buy_page()
        self.go_back()
        self.verify_sdp_page()
        self.go_back()
        self.verify_search_bar()

    #Validate  user should receive and error prompt of exchange not operating if user is trying to buy stock outside exchange operating hours.
    @pytest.mark.BP_SMMA_315
    @pytest.mark.BuyProcess
    @pytest.mark.Android
    def test_validate_error_message_after_exchange_hour(self):
        self.open_sdp_page_with_kyc_user(user_data['reg_no'], 'ACES')
        self.check_for_buy_btn()
        self.click_on_buy_btn()
        self.verify_buy_page()
        self.click_on_buy_btn_on_buy_page()
        self.click_on_confirm_btn()
        self.verify_error_message_after_exchange_market()
        self.click_on_ok_btn()

    #Validate user is able to increase or decrease the value at buy at price "beli di harga" via + and - button.
    @pytest.mark.BP_SMMA_316
    @pytest.mark.BuyProcess
    @pytest.mark.Android
    def test_validate_plus_minus_for_beli_di_harga(self):
        self.open_sdp_page_with_kyc_user(user_data['reg_no'], 'ACES')
        self.check_for_buy_btn()
        self.click_on_buy_btn()
        self.verify_buy_page()
        self.verify_plus_minus_btn_beli()

    #Validate user should reciev an error promt"Nilai pembelian kamu melebihi trading limit" when user trying to buy the stock beyond the buying power.
    @pytest.mark.BP_SMMA_317
    @pytest.mark.BuyProcess
    @pytest.mark.Android
    def test_validate_buy_power_exceed_msg(self):
        self.open_sdp_page_with_kyc_user(user_data['reg_no'], 'ACES')
        self.check_for_buy_btn()
        self.click_on_buy_btn()
        self.verify_buy_page()
        self.verify_buying_power_exceed_msg()

    #Validate the buy button gets disable when user trying to purchase stock beyond the buying power.
    @pytest.mark.BP_SMMA_318
    @pytest.mark.BuyProcess
    @pytest.mark.Android
    def test_validate_after_buy_power_exceed_buy_btn_disable(self):
        self.open_sdp_page_with_kyc_user(user_data['reg_no'], 'ACES')
        self.check_for_buy_btn()
        self.click_on_buy_btn()
        self.verify_buy_page()
        self.verify_buying_power_exceed_msg()
        self.click_on_buy_btn_on_buy_page()
        self.verify_buy_page()

    #Validate the total beli amount should equal to multiple of beli di harga and jumlah lot.
    @pytest.mark.BP_SMMA_319
    @pytest.mark.BuyProcess
    @pytest.mark.Android
    def test_validate_beli_ammount_is_multiple_of_harga_lot(self):
        self.open_sdp_page_with_kyc_user(user_data['reg_no'], 'ACES')
        self.check_for_buy_btn()
        self.click_on_buy_btn()
        self.verify_buy_page()
        self.verify_total_beli_amount()
