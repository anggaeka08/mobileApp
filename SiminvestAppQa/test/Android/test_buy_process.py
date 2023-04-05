import allure
import pytest
from selenium.common.exceptions import NoSuchElementException
from SiminvestAppQa.src.pages.Android_pages.buy_process import BuyProcess
from SiminvestAppQa.src.data.userData import user_data


class BuyProcess_test(BuyProcess):

    #positive flow for buy
    @pytest.mark.positive_flow_for_buy
    @pytest.mark.Android
    @pytest.mark.BuyProcess
    @allure.story("F-11:BuyProcess")
    def test_positive_flow_for_buy(self):
        try:
            self.execute_script('lambda-name=test_positive_flow_for_buy')
            self.open_sdp_page_with_kyc_user(user_data['reg_no'],user_data['stock_code'][1] )
            self.check_for_buy_btn()
            self.click_on_buy_btn()
            self.verify_buy_page()
            self.click_on_buy_btn_on_buy_page()
            self.click_on_confirm_btn()
            self.verify_market_timing(user_data['stock_code'][1], 'BELI')
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_positive_flow_for_buy', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_positive_flow_for_buy', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    #data compare btw buy and order page
    @pytest.mark.data_compare_btw_buy_page_and_ODP
    @pytest.mark.Android
    @pytest.mark.BuyProcess
    @allure.story("F-11:BuyProcess")
    def test_data_compare_btw_buy_page_and_ODP(self):
        try:
            self.execute_script('lambda-name=test_data_compare_btw_buy_page_and_ODP')
            self.open_sdp_page_with_kyc_user(user_data['reg_no_3'], user_data['stock_code'][2])
            self.check_for_buy_btn()
            self.click_on_buy_btn()
            self.verify_buy_page()
            self.data_comparison_between_buy_page_and_OrderDP(user_data['stock_code'][2])
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_data_compare_btw_buy_page_and_ODP', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_data_compare_btw_buy_page_and_ODP', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)


    #positive flow for sell
    @pytest.mark.positive_flow_for_sell
    @pytest.mark.Android
    @pytest.mark.BuyProcess
    @allure.story("F-11:BuyProcess")
    def test_positive_flow_for_sell(self):
        try:
            self.execute_script('lambda-name=test_positive_flow_for_sell')
            self.login_and_verify_homepage_for_reg_user(user_data['reg_no_3'])
            self.click_on_portfolio_btn()
            stock_code = self.get_stock_code_on_portfolio_page()
            self.redirection_from_portfolio_to_sdp()
            self.click_on_sell_btn()
            self.sleep(2)
            self.verify_buy_page()
            self.click_on_buy_btn_on_buy_page()
            self.click_on_confirm_btn()
            self.verify_market_timing(stock_code, 'JUAL')
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_positive_flow_for_sell', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_positive_flow_for_sell', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)




    #Validate that user can see buy button on stock detail page
    @pytest.mark.BP_SMMA_301
    @pytest.mark.BuyProcess_Old
    @pytest.mark.Android
    def test_validate_buy_btn_on_sdp_page(self):
        self.open_sdp_page_with_kyc_user(user_data['reg_no'], 'ACES')
        self.check_for_buy_btn()

    #Validate that there is two button buy/sell if stock is already purchased for KYC user.
    @pytest.mark.BP_SMMA_302
    @pytest.mark.BuyProcess_Old
    @pytest.mark.Android
    def test_validate_buy_sell_btn_on_sdp_page(self):
        self.open_sdp_by_portfolio_with_kyc_user(user_data['reg_no'])
        self.check_for_sell_btn()
        self.check_for_buy_btn()

    #Validate the non KYC user should redirect to referral page when user click on beli button.
    @pytest.mark.BP_SMMA_309
    @pytest.mark.BuyProcess_Old
    @pytest.mark.Android
    def test_validate_redirect_to_refferal_page_by_click_on_buy_for_non_kyc(self):
        self.open_sdp_page_with_non_kyc_user(user_data['unkyc_reg_no'], 'ACES')
        self.check_for_buy_btn()
        self.click_on_buy_btn()
        self.verify_refferal_page()

    #Validate user is able to cancel the order after click on buy button using cancel button.
    @pytest.mark.BP_SMMA_305
    @pytest.mark.BuyProcess_Old
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
    @pytest.mark.BuyProcess_Old
    @pytest.mark.Android
    @pytest.mark.timeBased
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
    @pytest.mark.BuyProcess_Old
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
    @pytest.mark.BuyProcess_Old
    @pytest.mark.Android
    def test_validate_default_value_of_lot(self):
        self.open_sdp_page_with_kyc_user(user_data['reg_no'], 'ACES')
        self.check_for_buy_btn()
        self.click_on_buy_btn()
        self.verify_buy_page()
        self.verify_lot_count("1")

    # Validate that user can see the Beli button on stock detail page
    @pytest.mark.BP_SMMA_310
    @pytest.mark.BuyProcess_Old
    @pytest.mark.Android
    def test_validate_Beli_btn_on_sdp_page(self):
        self.open_sdp_page_with_kyc_user(user_data['reg_no'], 'ACES')
        self.check_for_buy_btn()

    #Validate user is able to increase and decrease the lot on buy page.
    @pytest.mark.BP_SMMA_311
    @pytest.mark.BuyProcess_Old
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
    @pytest.mark.BuyProcess_Old
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
    @pytest.mark.BuyProcess_Old
    @pytest.mark.Android
    @pytest.mark.timeBased
    def test_validate_error_message_after_exchange_hour(self):
        self.open_sdp_page_with_kyc_user(user_data['reg_no'], 'ACES')
        self.check_for_buy_btn()
        self.click_on_buy_btn()
        self.verify_buy_page()
        self.click_on_buy_btn_on_buy_page()
        self.click_on_confirm_btn()
        self.verify_error_message_after_exchange_market()
        self.click_on_ok_btn_after_market_close()

    #Validate user is able to increase or decrease the value at buy at price "beli di harga" via + and - button.
    @pytest.mark.BP_SMMA_316
    @pytest.mark.BuyProcess_Old
    @pytest.mark.Android
    def test_validate_plus_minus_for_beli_di_harga(self):
        self.open_sdp_page_with_kyc_user(user_data['reg_no'], 'ACES')
        self.check_for_buy_btn()
        self.click_on_buy_btn()
        self.verify_buy_page()
        self.verify_plus_minus_btn_beli()

    #Validate user should reciev an error promt"Nilai pembelian kamu melebihi trading limit" when user trying to buy the stock beyond the buying power.
    @pytest.mark.BP_SMMA_317
    @pytest.mark.BuyProcess_Old
    @pytest.mark.Android
    def test_validate_buy_power_exceed_msg(self):
        self.open_sdp_page_with_kyc_user(user_data['reg_no'], 'ACES')
        self.check_for_buy_btn()
        self.click_on_buy_btn()
        self.verify_buy_page()
        self.verify_buying_power_exceed_msg()

    #Validate the buy button gets disable when user trying to purchase stock beyond the buying power.
    @pytest.mark.BP_SMMA_318
    @pytest.mark.BuyProcess_Old
    @pytest.mark.Android
    def test_validate_after_buy_power_exceed_buy_btn_disable(self):
        self.open_sdp_page_with_kyc_user(user_data['reg_no'], 'ACES')
        self.check_for_buy_btn()
        self.click_on_buy_btn()
        self.verify_buy_page()
        self.verify_buying_power_exceed_msg()
        self.click_disabled_buy_btn()
        self.verify_buy_page_after_disable_buy_btn()

    #Validate the total beli amount should equal to multiple of beli di harga and jumlah lot.
    @pytest.mark.BP_SMMA_319
    @pytest.mark.BuyProcess_Old
    @pytest.mark.Android
    def test_validate_beli_ammount_is_multiple_of_harga_lot(self):
        self.open_sdp_page_with_kyc_user(user_data['reg_no'], 'ACES')
        self.check_for_buy_btn()
        self.click_on_buy_btn()
        self.verify_buy_page()
        self.verify_total_beli_amount()

    # Validate user redirected back to SDP page when user click on back button when user is on order page after completed the buying process.
    @pytest.mark.BP_SMMA_320
    @pytest.mark.BuyProcess_Old
    @pytest.mark.Android
    @pytest.mark.timeBased
    def test_validate_after_redirection_from_transaction_page(self):
        self.open_sdp_page_with_kyc_user(user_data['reg_no'], 'ACES')
        self.check_for_buy_btn()
        self.click_on_buy_btn()
        self.verify_buy_page()
        self.click_on_buy_btn_on_buy_page()
        self.click_on_confirm_btn()
        self.click_on_ok_btn()
        self.verify_transaction_page()
        self.go_back()
        self.verify_sdp_page()

    #Validate user is able to see sending status on transaction page when user purchase the stock successfully.
    @pytest.mark.BP_SMMA_321
    @pytest.mark.BuyProcess_Old
    @pytest.mark.Android
    @pytest.mark.timeBased
    def test_validate_status_on_transaction_page(self):
        self.open_sdp_page_with_kyc_user(user_data['reg_no'], 'ACES')
        self.check_for_buy_btn()
        self.click_on_buy_btn()
        self.verify_buy_page()
        self.click_on_buy_btn_on_buy_page()
        self.click_on_confirm_btn()
        self.click_on_ok_btn()
        self.verify_transaction_page()
        self.verify_status_on_transaction_page()

# Validate user is able to cancel the GTC option after date selection.
    @pytest.mark.BP_SMMA_322
    @pytest.mark.BuyProcess_Old
    @pytest.mark.Android
    def test_validate_cancel_gtc_option_after_selection(self):
        self.open_sdp_page_with_kyc_user(user_data['reg_no'], 'ACES')
        self.check_for_buy_btn()
        self.click_on_buy_btn()
        self.verify_buy_page()
        self.tap_on_gtc_option()
        self.click_on_date()
        self.select_date()
        self.tap_on_gtc_option()

    # Validate the stock value detail should equal to order confirmation detail page.
    @pytest.mark.BP_SMMA_323
    @pytest.mark.BuyProcess_Old
    @pytest.mark.Android
    def test_validate_lot_hagra_jumla_value_on_ocp_page(self):
        self.open_sdp_page_with_kyc_user(user_data['reg_no'], 'ACES')
        self.check_for_buy_btn()
        self.click_on_buy_btn()
        self.verify_buy_page()
        self.verify_lot_harga_jumlah_value()

    #Validate user able to see good till date on order confirmation page when user trying to buy the stock via GTC.
    @pytest.mark.BP_SMMA_324
    @pytest.mark.BuyProcess_Old
    @pytest.mark.Android
    def test_validate_date_for_gtc_ocp_page(self):
        self.open_sdp_page_with_kyc_user(user_data['reg_no'], 'ACES')
        self.check_for_buy_btn()
        self.click_on_buy_btn()
        self.verify_buy_page()
        self.tap_on_gtc_option()
        self.verify_gtc_date_on_ocp()

    #Validate the buying power should same on all SDP page and also compare to home page detail.
    @pytest.mark.BP_SMMA_325
    @pytest.mark.BuyProcess_Old
    @pytest.mark.Android
    def test_validate_buying_power_on_sdp_and_buy_page(self):
        self.click_mulai_sekarang()
        self.type_mobile_no(user_data['reg_no'])
        self.click_selanjutnya()
        self.enter_otp(user_data['valid_otp'])
        self.enter_pin()
        self.close_home_page_banner()
        self.verify_home_page_reg_user()
        power_on_home_page = self.buy_power_on_homepage()
        self.click_global_search_btn_and_saerch_stock('ACES')
        self.sleep(3)
        self.click_on_stock_code()
        self.verify_sdp_page()
        self.check_for_buy_btn()
        self.click_on_buy_btn()
        self.verify_buy_page()
        power_on_buy_page = self.buy_power_on_buy_page()
        self.assert_equal(power_on_home_page, power_on_buy_page)

     # Validate user should receive the prompt with the msg "Check one Open Buy/Sell Order with same price" when user trying to purchase same stock with same price.
    @pytest.mark.BP_SMMA_326
    @pytest.mark.BuyProcess_Old
    @pytest.mark.Android
    @pytest.mark.timeBased
    def test_validate_msg_when_buy_stock_on_same_price_again(self):
        self.open_sdp_page_with_kyc_user(user_data['reg_no'], 'ACES')
        self.check_for_buy_btn()
        self.click_on_buy_btn()
        self.verify_buy_page()
        self.click_on_buy_btn_on_buy_page()
        self.click_on_confirm_btn()
        self.click_on_ok_btn()
        self.verify_transaction_page()
        status = self.status_on_trans_page()
        self.assert_equal(status, "SENDING")
        self.go_back()
        self.check_for_buy_btn()
        self.click_on_buy_btn()
        self.verify_buy_page()
        self.click_on_buy_btn_on_buy_page()
        message = self.message_after_buy_again_on_same_price()
        self.assert_equal(message, "Check one Open Buy/Sell Order with same price")

    #  Post when user click on "OK" button he should redirected back to buy page.
    @pytest.mark.BP_SMMA_327
    @pytest.mark.BuyProcess_Old
    @pytest.mark.Android
    @pytest.mark.timeBased
    def test_validate_redirection_to_buy_page_when_buy_stock_on_same_price_again(self):
        self.open_sdp_page_with_kyc_user(user_data['reg_no'], 'ACES')
        self.check_for_buy_btn()
        self.click_on_buy_btn()
        self.verify_buy_page()
        self.click_on_buy_btn_on_buy_page()
        self.click_on_confirm_btn()
        self.click_on_ok_btn()
        self.verify_transaction_page()
        status = self.status_on_trans_page()
        self.assert_equal(status, "SENDING")
        self.go_back()
        self.check_for_buy_btn()
        self.click_on_buy_btn()
        self.verify_buy_page()
        self.click_on_buy_btn_on_buy_page()
        message = self.message_after_buy_again_on_same_price()
        self.assert_equal(message, "Check one Open Buy/Sell Order with same price")
        self.click_on_ok_btn()
        self.verify_buy_page()

    #Validate user is able to increase the value of lot and buy the stock.
    @pytest.mark.BP_SMMA_328
    @pytest.mark.BuyProcess_Old
    @pytest.mark.Android
    @pytest.mark.timeBased
    def test_validate_buy_process_after_increase_lot_no(self):
        self.open_sdp_page_with_kyc_user(user_data['reg_no'], 'ACES')
        self.check_for_buy_btn()
        self.click_on_buy_btn()
        self.verify_buy_page()
        self.click_on_lot_increase_no()
        self.click_on_buy_btn_on_buy_page()
        self.click_on_confirm_btn()
        self.click_on_ok_btn()
        self.verify_transaction_page()

    #Validate the bid and ask price is replicated on beli di harga option when user clicks on any visible prices in bid and ask.
    @pytest.mark.BP_SMMA_329
    @pytest.mark.BuyProcess_Old
    @pytest.mark.Android
    def test_validate_beli_di_harga_equal_to_bit_amount(self):
        self.open_sdp_page_with_kyc_user(user_data['reg_no'], 'ACES')
        self.check_for_buy_btn()
        self.click_on_buy_btn()
        self.verify_buy_page()
        self.verify_bit_amount_with_beli_di_harga()

    #The user can still place an order after market hours. But it will be Sending state until market opens again.
    @pytest.mark.BP_SMMA_330
    @pytest.mark.BuyProcess_Old
    @pytest.mark.Android
    @pytest.mark.timeBased
    def test_validate_status_sending_of_buy_order(self):
        self.open_sdp_page_with_kyc_user(user_data['reg_no'], 'ACES')
        self.check_for_buy_btn()
        self.click_on_buy_btn()
        self.verify_buy_page()
        self.click_on_buy_btn_on_buy_page()
        self.click_on_confirm_btn()
        self.click_on_ok_btn()
        self.verify_transaction_page()
        status = self.status_on_trans_page()
        self.assert_equal(status, "SENDING")






