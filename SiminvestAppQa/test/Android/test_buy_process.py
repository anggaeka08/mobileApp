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
        self.check_for_buy_without_sell_btn()

    #Validate that there is two button buy/sell if stock is already purchased for KYC user.
    @pytest.mark.BP_SMMA_302
    @pytest.mark.BuyProcess
    @pytest.mark.Android
    def test_validate_buy_sell_btn_on_sdp_page(self):
        self.open_sdp_by_portfolio_with_kyc_user(user_data['reg_no'])
        self.check_for_sell_btn()
        self.check_for_buy_with_sell_btn()

    #Validate the non KYC user should redirect to referral page when user click on beli button.
    @pytest.mark.BP_SMMA_309
    @pytest.mark.BuyProcess
    @pytest.mark.Android
    def test_validate_redirect_to_refferal_page_by_click_on_buy_for_non_kyc(self):
        self.open_sdp_page_with_non_kyc_user(user_data['unkyc_reg_no'], 'ACES')
        self.check_for_buy_without_sell_btn()
        self.click_on_buy_btn_without_sell_btn()
        self.verify_refferal_page()

    #Validate user is able to cancel the order after click on buy button using cancel button.
    @pytest.mark.BP_SMMA_305
    @pytest.mark.BuyProcess
    @pytest.mark.Android
    def test_validate_cancel_btn_on_buy_page(self):
        self.open_sdp_page_with_kyc_user(user_data['reg_no'], 'ACES')
        self.check_for_buy_without_sell_btn()
        self.click_on_buy_btn_without_sell_btn()
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
        self.check_for_buy_without_sell_btn()
        self.click_on_buy_btn_without_sell_btn()
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
        self.get_current_date()

