import pytest
from SiminvestAppQa.src.pages.Android_pages.watchlist import Watchlist
from SiminvestAppQa.src.utilities.genericUtilities import generate_random_string
from SiminvestAppQa.src.data.userData import user_data
import logging as logger

@pytest.mark.usefixtures("_unittest_setUpClass_fixture_Watchlist_test")
class Watchlist_test(Watchlist):

    #Cover all 5 test cases in single test
    @pytest.mark.Wat_SMMA_001_004
    @pytest.mark.Android
    @pytest.mark.watchlist
    def test_validate_user_able_create_rename_deleteCancel_delete_watchlist(self):
        self.go_to_watchlist_option_after_login(user_data['reg_no'])
        self.click_on_defaults_btn()
        self.click_on_plus_btn()
        self.enter_watchlist_name('test')
        self.validate_watchlist_entry('test')
        self.click_on_edit_btn()
        self.edit_watchlist_name()
        self.click_on_simpan()
        self.validate_watchlist_entry('testtest')
        self.Cancel_delete_and_delete_watchlist()

    #SMMA-005 Validate user will able to have maximum 10 watchlists.
    @pytest.mark.Wat_SMMA_005
    @pytest.mark.Android
    @pytest.mark.watchlist
    def test_validate_user_able_to_add_maximum_10_watchlist(self):
        self.go_to_watchlist_option_after_login(user_data['reg_no'])
        self.click_on_defaults_btn()
        for i in range(10):
            self.click_on_plus_btn()
            self.enter_watchlist_name(f'test{i}')
        self.validate_pop_message()
        self.click_on_cross_btn()
        for i in range(9):
            self.click_on_delete()
            self.click_on_Hapus()
            self.sleep(1)

    # Validate If there is no stock inside watchlist, please show empty stock with button tamnah saham.
    @pytest.mark.Wat_SMMA_007
    @pytest.mark.Android
    @pytest.mark.watchlist
    def test_validate_msg_when_watchlist_empty(self):
        self.go_to_watchlist_option_after_login(user_data['reg_no'])
        self.click_on_defaults_btn()
        self.click_on_plus_btn()
        self.enter_watchlist_name('test')
        self.validate_watchlist_entry('test')
        self.click_on_watchlist_entry_2()
        self.scroll_ups()
        self.empty_watchlist_msg()
        self.click_on_test()
        self.click_on_selected_watchlist()
        self.click_on_Hapus()

    #Validate only new Siminvest’s will have default watchlis
    @pytest.mark.Wat_SMMA_008
    @pytest.mark.Android
    @pytest.mark.watchlist
    def test_validate_default_watchlist_for_new_user(self):
        self.go_to_watchlist_option_after_login(user_data['unkyc_reg_no'])
        self.validate_default_watchlist()

    # Validate stocks for default watchlist are BBCA, BBRI, TLKM, BMRI, ARTO
    @pytest.mark.Wat_SMMA_009
    @pytest.mark.Android
    @pytest.mark.watchlist
    def test_validate_stock_list_in_default_watchlist(self):
        self.go_to_watchlist_option_after_login(user_data['unkyc_reg_no'])
        self.validate_avail_check_for_stock_on_watchlist()

    #Validate watchlist name will have maximum 60 characters.
    @pytest.mark.Wat_SMMA_010
    @pytest.mark.Android
    @pytest.mark.watchlist
    def test_validate_watchlist_name_max_60_character(self):
        self.go_to_watchlist_option_after_login(user_data['reg_no'])
        self.click_on_defaults_btn()
        self.click_on_plus_btn()
        name = generate_random_string(65)
        self.enter_watchlist_name(name)
        self.validate_watchlist_entry(name[:60])
        self.click_on_delete()
        self.click_on_Hapus()

    #Validate as default show top gainer at the time of adding stock.
    @pytest.mark.Wat_SMMA_012_013
    @pytest.mark.Android
    @pytest.mark.watchlist
    def test_validate_default_show_top_gainer(self):
        self.go_to_watchlist_option_after_login(user_data['reg_no'])
        self.click_on_defaults_btn()
        self.click_on_plus_btn()
        self.enter_watchlist_name('test')
        self.validate_watchlist_entry('test')
        self.click_on_watchlist_entry_2()
        self.scroll_ups()
        self.empty_watchlist_msg()
        self.click_on_tambah_saham()
        self.verify_top_gainer_presence()
        self.click_on_top_gainer()
        self.verify_stock_type_selection()
        self.go_back()
        self.go_back()
        self.click_on_test()
        self.click_on_selected_watchlist()
        self.click_on_Hapus()

   #Validate test cases from count 014 to 018.
    @pytest.mark.Wat_SMMA_014_018
    @pytest.mark.Android
    @pytest.mark.watchlist
    def test_validate_test_case_smma_014_to_smma_018(self):
        self.go_to_watchlist_option_after_login(user_data['reg_no'])
        self.click_on_edit_for_stock()
        self.search_stock('A')
        self.verify_stock_list_after_single_character_search()
        self.search_stock('ARGO')
        self.verify_stock_search_by_full_code()
        self.click_to_add_remove()
        self.sleep(3)
        self.click_to_add_remove()
        self.click_on_ok()

    #Validate test cases from count 019 to 020.
    @pytest.mark.Wat_SMMA_019_020
    @pytest.mark.Android
    @pytest.mark.watchlist
    def test_validate_stock_sorting_and_delete_disable_for_single_watchlist(self):
        self.go_to_watchlist_option_after_login(user_data['unkyc_reg_no'])
        self.click_on_edit_for_stock()
        self.validate_avail_check_for_stock_on_watchlist()
        self.go_back()
        self.go_back()
        self.click_on_defaults_btn()
        self.verify_delete_btn()

    #Validate user able to create duplicate name watchlist and able to add stock
    @pytest.mark.Wat_SMMA_021_022
    @pytest.mark.Android
    @pytest.mark.watchlist
    def test_user_able_to_create_duplicate_name_watchlist_and_able_to_add_stock(self):
        self.go_to_watchlist_option_after_login(user_data['reg_no'])
        self.click_on_defaults_btn()
        self.click_on_plus_btn()
        self.enter_watchlist_name('Default')
        self.validate_watchlist_entry('Default')
        self.click_on_watchlist_entry_2()
        self.scroll_ups()
        self.empty_watchlist_msg()
        self.click_on_tambah_saham()
        self.search_stock('ARGO')
        self.click_to_add_remove()
        self.go_back()
        self.go_back()
        self.scroll_ups()
        self.verify_watchlist_entry()
        self.click_on_defaults_btn()
        self.click_on_selected_watchlist()
        self.click_on_Hapus()

    @pytest.mark.Wat_SMMA_024_028
    @pytest.mark.Android
    @pytest.mark.watchlist
    @pytest.mark.timeBased
    def test_validate_selected_watchlist_visible_after_reopen_app_and_sdp_open_after_click_stock(self):
        self.go_to_watchlist_option_after_login(user_data['reg_no'])
        self.click_on_defaults_btn()
        self.click_on_plus_btn()
        self.enter_watchlist_name('test')
        self.validate_watchlist_entry('test')
        self.click_on_watchlist_entry_2()
        self.app_in_background(20)
        self.scroll_ups()
        self.click_on_test()
        self.click_on_selected_watchlist()
        self.click_on_Hapus()
        self.go_back()
        self.click_on_stock_code_in_watclist()
        self.verify_sdp_page()

    @pytest.mark.Wat_SMMA_036_to_40
    @pytest.mark.Android
    @pytest.mark.watchlist
    def test_validate_right_swipe_with_buy_feature(self):
        self.go_to_watchlist_option_after_login(user_data['reg_no'])
        self.swipe_right()
        harga_value = self.harga_value()
        self.harga_increase()
        self.harga_decrease()
        harga_value_1 = self.harga_value()
        self.assert_equal(harga_value_1, harga_value)
        lot_value = self.lot_value()
        self.lot_increase()
        self.lot_decrease()
        lot_value_1 = self.lot_value()
        self.assert_equal(lot_value_1, lot_value)
        self.click_on_beli()
        self.click_on_confirm_btn()
        self.verify_trasaction_page_or_market_close()


    @pytest.mark.Wat_SMMA_41_43_44_45_46_48_50_51
    @pytest.mark.Android
    @pytest.mark.watchlist
    @pytest.mark.timeBased
    def test_validate_test_case_41_43_44_45_46_48_50_51(self):
        self.go_to_watchlist_option_after_login(user_data['reg_no'])
        self.swipe_left_without_buy()
        self.swipe_left_with_buy()
        self.sleep(2)
        self.verify_half_card_for_sell()
        harga_value = self.harga_value()
        self.harga_increase()
        self.harga_decrease()
        harga_value_1 = self.harga_value()
        self.assert_equal(harga_value_1, harga_value)
        lot_value = self.lot_value()
        self.lot_increase()
        self.lot_decrease()
        lot_value_1 = self.lot_value()
        self.assert_equal(lot_value_1, lot_value)
        self.click_on_max_sell()
        self.assert_not_equal(self.lot_value(), 1)
        self.unclick_on_max_sell()
        self.change_lot_value()
        #self.assert_equal(self.lot_value(), '5')
        self.click_on_jual()
        self.click_on_confirm_sell()
        #self.close_home_page_banner()
        self.verify_transaction_page()

    #Validate user should receive an error prompt when user trying to purchase the stock outside exchange hours.
    @pytest.mark.Wat_SMMA_42
    @pytest.mark.Android
    @pytest.mark.watchlist
    @pytest.mark.timeBased
    def test_validate_purchase_outside_exchange_hours(self):
        self.go_to_watchlist_option_after_login(user_data['reg_no'])
        self.swipe_right()
        self.click_on_beli()
        self.click_on_confirm_sell()
        self.verify_trasaction_page_or_market_close()

    #Validate user is redirected to home page when user click on cancel button when user is on preview order page.
    @pytest.mark.Wat_SMMA_47
    @pytest.mark.Android
    @pytest.mark.watchlist
    def test_validate_redirection_after_cancel_buy(self):
        self.go_to_watchlist_option_after_login(user_data['reg_no'])
        self.swipe_left_with_buy()
        self.click_on_jual()
        self.click_on_Batal()
        self.click_on_defaults_btn()


    #Validate buy with limit option.
    @pytest.mark.Wat_SMMA_54_56
    @pytest.mark.Android
    @pytest.mark.watchlist
    @pytest.mark.timeBased
    def test_validate_buy_with_limit_option(self):
        self.click_mulai_sekarang()
        self.type_mobile_no(user_data['reg_no'])
        self.click_selanjutnya()
        self.enter_otp(user_data['valid_otp'])
        self.enter_pin()
        self.close_home_page_banner()
        buying_power = self.find_buying_power()
        self.scroll_up()
        self.swipe_right()
        self.click_on_limit_option()
        total_beli_amountt = self.total_beli_amount()
        self.assertGreater(buying_power, total_beli_amountt)
        harga = int((self.harga_value()).replace(',',''))
        less_harga = self.less_price(price=harga)
        self.enter_harga_amount(less_harga)
        self.click_on_beli()
        self.click_on_confirm_sell()
        #self.close_home_page_banner()
        self.verify_transaction_page()

    #Validate buy with cash option.
    @pytest.mark.Wat_SMMA_55_57
    @pytest.mark.Android
    @pytest.mark.watchlist
    @pytest.mark.timeBased
    def test_validate_buy_with_cash_option(self):
        self.click_mulai_sekarang()
        self.type_mobile_no(user_data['reg_no'])
        self.click_selanjutnya()
        self.enter_otp(user_data['valid_otp'])
        self.enter_pin()
        self.close_home_page_banner()
        rp_amountt = self.find_RP_amount()
        self.scroll_up()
        self.swipe_right()
        self.click_on_cash_option()
        total_beli_amountt = self.total_beli_amount()
        self.assertGreater(rp_amountt, total_beli_amountt)
        self.click_on_beli()
        self.click_on_confirm_sell()
        #self.close_home_page_banner()
        self.verify_transaction_page()

    #Validate redirection_after_click_on_cross_btn
    @pytest.mark.Wat_SMMA_58
    @pytest.mark.Android
    @pytest.mark.watchlist
    def test_validate_redirection_after_cross_btn(self):
        self.go_to_watchlist_option_after_login(user_data['reg_no'])
        self.swipe_right()
        self.click_on_cross_btn_FS()
        self.click_on_defaults_btn()

    #Validate thousand separator
    @pytest.mark.Wat_SMMA_59
    @pytest.mark.Android
    @pytest.mark.watchlist
    def test_validate_thousand_separator(self):
        self.go_to_watchlist_option_after_login(user_data['reg_no'])
        self.swipe_right()
        harga_value = self.harga_value()
        beli_amount = self.total_beli_amount()
        self.click_on_beli()
        harga_value_on_con = self.harga_value_on_conf_page()
        jumlah_on_con = self.jumlah_on_conf_page()
        try:
            self.add_thousand_seprator(harga_value)
            self.add_thousand_seprator(beli_amount)
            self.add_thousand_seprator(harga_value_on_con)
            self.add_thousand_seprator(jumlah_on_con)
            logger.info("separator is not available")
        except:
            logger.info("separator is available")

    #Valdiate watchlist half card and keyboard open and close
    @pytest.mark.Wat_N_03_04_05_07
    @pytest.mark.Android
    @pytest.mark.watchlist
    def test_valdiate_watchlist_half_card_and_keyboard_open_and_close(self):
        self.go_to_watchlist_option_after_login(user_data['reg_no'])
        self.click_on_defaults_btn()
        self.verify_half_card_page_for_watchlist(True)
        self.click_on_plus_btn()
        self.verify_keyboard_on_off(True)
        self.click_on_cross_btn()
        self.verify_keyboard_on_off(False)
        self.scroll_down()
        self.verify_half_card_page_for_watchlist(False)
























