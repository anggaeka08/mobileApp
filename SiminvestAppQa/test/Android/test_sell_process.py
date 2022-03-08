import pytest
from SiminvestAppQa.src.pages.Android_pages.sell_process import SellProcess
from SiminvestAppQa.src.pages.Android_pages.buy_process import BuyProcess
from SiminvestAppQa.src.data.userData import user_data


class Sell_test(SellProcess, BuyProcess):

    # Validate user is able to sell stock.
    @pytest.mark.Sell_SMMA_502
    @pytest.mark.Sell
    @pytest.mark.Android
    def test_validate_user_able_to_sell_stock(self):
        self.open_and_verify_portfolio(user_data['reg_no'])
        self.click_on_portfolio_entry_2()
        self.verify_sdp_page()
        self.click_on_jual_btn()
        self.verify_buy_page()
        self.click_on_jual_btn()
        self.click_on_setuju()
        self.click_on_ok_btn()
        self.verify_transaction_page()
        self.verify_transaction_page_for_sell()

    #Validate user is able to cancel the order after click on jual button.
    @pytest.mark.Sell_SMMA_503
    @pytest.mark.Sell
    @pytest.mark.Android
    def test_validate_user_able_to_cancel_after_jual_btn(self):
        self.open_and_verify_portfolio(user_data['reg_no'])
        self.click_on_portfolio_entry_2()
        self.verify_sdp_page()
        self.click_on_jual_btn()
        self.verify_buy_page()
        self.click_on_jual_btn()
        self.click_on_batal()
        self.verify_buy_page()

    #Validate GTC option is working fine.
    @pytest.mark.Sell_SMMA_504
    @pytest.mark.Sell
    @pytest.mark.Android
    def test_validate_gtc_option_for_sell(self):
        self.open_and_verify_portfolio(user_data['reg_no'])
        self.click_on_portfolio_entry_2()
        self.verify_sdp_page()
        self.click_on_jual_btn()
        self.verify_buy_page()
        self.tap_on_gtc_option()
        self.click_on_date()
        self.select_date()
        self.click_on_jual_btn()
        self.click_on_setuju()
        self.click_on_ok_btn()
        self.verify_transaction_page()
        self.go_to_gtc_tab_on_trans_page()
        self.verify_transaction_page_for_sell_on_gtc_page()

    # Validate the default value for sell stock lot size is 1.
    #alidate the - button is disable when there is one stock selected in the lot.
    @pytest.mark.Sell_SMMA_505
    @pytest.mark.Sell
    @pytest.mark.Android
    def test_validate_initial_value_of_lot_is_1_and_minus_btn_disable(self):
        self.open_and_verify_portfolio(user_data['reg_no'])
        self.click_on_portfolio_entry_2()
        self.verify_sdp_page()
        self.click_on_jual_btn()
        self.verify_buy_page()
        self.check_initial_value_of_lot("1")
        self.click_on_lot_increase_no()
        self.check_initial_value_of_lot("2")

    #Validate on sell confirmation page the detail of stock is same with the sell page detail
    #Validate the thousand separator is added on all the required places during sell process.
    #not validating profit and loss values
    @pytest.mark.Sell_SMMA_507
    @pytest.mark.Sell
    @pytest.mark.Android
    def test_all_value_between_sell_page_and_sell_confirmation_page(self):
        self.open_and_verify_portfolio(user_data['reg_no'])
        self.click_on_portfolio_entry_2()
        self.click_on_jual_btn()
        self.verify_lot_harga_jumlah_value()


    #Validate user should receive and error prompt of exchange not operating if user is trying to sell the stock outside exchange operating hours.
    @pytest.mark.Sell_SMMA_509
    @pytest.mark.Sell
    @pytest.mark.Android
    def test_validate_pop_for_sell_after_exchange_hours(self):
        self.open_and_verify_portfolio(user_data['reg_no'])
        self.click_on_portfolio_entry_2()
        self.verify_sdp_page()
        self.click_on_jual_btn()
        self.verify_buy_page()
        self.click_on_jual_btn()
        self.click_on_setuju()
        self.verify_error_message_after_exchange_market()
        self.click_on_ok_btn()

