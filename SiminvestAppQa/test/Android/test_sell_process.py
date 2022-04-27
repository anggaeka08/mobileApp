import pytest
from SiminvestAppQa.src.pages.Android_pages.sell_process import SellProcess
from SiminvestAppQa.src.data.userData import user_data

@pytest.mark.usefixtures("unittest_setUpClass_fixture_Sell_test")
class Sell_test(SellProcess):

    # Validate user is able to sell stock.
    @pytest.mark.Sell_SMMA_502
    @pytest.mark.Sell
    @pytest.mark.Android
    @pytest.mark.timeBased
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
        self.sleep(4)
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
        self.sleep(4)
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
        self.sleep(2)
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
    @pytest.mark.timeBased
    def test_validate_pop_for_sell_after_exchange_hours(self):
        self.open_and_verify_portfolio(user_data['reg_no'])
        self.click_on_portfolio_entry_2()
        self.verify_sdp_page()
        self.click_on_jual_btn()
        self.sleep(2)
        self.verify_buy_page()
        self.click_on_jual_btn()
        self.click_on_setuju()
        self.verify_error_message_after_exchange_market()
        self.click_on_ok_btn()

    #alidate user is able to increase or decrease the value of sell at price "beli di harga" via + and - button.
    @pytest.mark.Sell_SMMA_510
    @pytest.mark.Sell
    @pytest.mark.Android
    def test_validate_plus_minus_for_lot_and_harga_on_sell_page(self):
        self.open_and_verify_portfolio(user_data['reg_no'])
        self.click_on_portfolio_entry_2()
        self.verify_sdp_page()
        self.click_on_jual_btn()
        self.verify_lot_count("1")
        self.click_on_lot_increase_no()
        self.verify_lot_count("2")
        self.click_on_lot_decrease_btn()
        self.verify_lot_count("1")
        self.verify_plus_minus_btn_beli()

    #Validate the lot size can not be written more then the lot purchaesd and the value changed automaticaaly to correct value if he force to type more value.
    @pytest.mark.Sell_SMMA_512
    @pytest.mark.Sell
    @pytest.mark.Android
    def test_validate_lot_value_stay_in_limit_according_to_available_lot(self):
        self.open_and_verify_portfolio(user_data['reg_no'])
        self.click_on_portfolio_entry_2()
        self.click_on_jual_btn()
        self.verify_lot_value_change_default()


    #Validate the error should prompt at top when user trying to sell the stock above the available limit.
    @pytest.mark.Sell_SMMA_516
    @pytest.mark.Sell
    @pytest.mark.Android
    def test_validate_error_message_for_sell_stock_above_available_limit(self):
        self.open_and_verify_portfolio(user_data['reg_no'])
        self.click_on_portfolio_entry_2()
        self.click_on_jual_btn()
        self.verify_error_message_for_sell_stock_exceed_limit()

   # Validate the bid and ask price is replicated on jual di harga option when user clicks on any visible prices in bid and ask.
    @pytest.mark.Sell_SMMA_517
    @pytest.mark.Sell
    @pytest.mark.Android
    def test_validate_values_of_harga_according_to_click_on_bit_and_ask(self):
        self.open_and_verify_portfolio(user_data['reg_no'])
        self.click_on_portfolio_entry_2()
        self.click_on_jual_btn()
        self.verify_value_change_in_harga_accord_to_click()