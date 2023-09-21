from SiminvestAppQa.src.utilities.requestUtilities import RequestsUtilities
from SiminvestAppQa.src.pages.Android_pages.home_page import HomePage
import time
from SiminvestAppQa.src.data.userData import user_data
import allure
import logging as logger

request_utilities = RequestsUtilities()
#locators
saldo_rdn_btn = "HomePageRDN"
rdn_balance = 'RdnBalanceValue'
rdn_header = 'RdnBalanceHeader'
rdn_back_btn = "//android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.ImageView[@index = '0']"
top_up_btn = "RdnBalanceTopIcon"
tarik_dana_btn = 'RdnBalanceTarikIcon'
riwayat_btn = 'RdnBalanceRiwayatIcon'
rdn_fund_account_text = 'RdnBalanceFundAccNumber'
rdn_update_msg = 'RdnBalanceUpdateMsg'
homepage_rdn_balance_l = 'HomePageRdnValue'
bank_name = 'RdnBalanceBankName'
account_owner_name = 'RdnBalanceBankOwner'
bank_acc_number = 'RdnBalanceAccNumber'
saldo_efektif = '//android.widget.TextView[@text="Saldo efektif"]'
top_up_text = 'RdnBalanceTopBtn'
tarik_dana_text = 'RdnBalanceTarikBtn'
riwyat_text = 'RdnBalanceRiwayatBtn'
informasi_saldo_text = 'RdnBalanceSaldo'
informasi_rekening = 'RdnBalanceRekening'
bank_name_text = 'RdnBalanceIssuingBank'
bank_acc_owner_text = 'RdnBalanceAccOwner'
bank_acc_number_text ='RdnBalanceFundAccNumber'
profile_btn = '//android.widget.TextView[@text="Profile"]'
informasi_profile = 'ProfilePageEntry2'
profile_name = 'ScreenProfilePageName'
homepage_btn = '//android.widget.TextView[@text="Home"]'
#Top up page locators
top_up_header = "TopupPageHeader"
simobi_arrow = "TopupPageSimobiOpenIcon"
simobi_text_1 = "TopupPageSimobiText1"
bank_arrow = "TopupPageBankOpenIcon"
bank_text_1 = "TopupPageBankText1"
up_head_sign = "//android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[1]/android.view.ViewGroup[1]"
bank_title = 'TopupPageBankTitle'
#Tarik dana page locators
tarik_dana_header = "Tarik DanaHeader"
tarik_page_back_btn = "//android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.ImageView[@index = '0']"
dana_tersedia_text = "//android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[1]"
TarikPagePenarikan_text = 'TarikPagePenarikan'
TarikPageTransfer_text = 'TarikPageTransfer'
tariK_msg_text = 'TarikPageText1'
TarikPageNominal_text = 'TarikPageNominal'
tarik_dana_btn_tarik = '//android.view.ViewGroup[@content-desc="TarikPageBtn"]/android.widget.TextView'
tarik_dana_rdn = 'TarikPageRpValue'
nominal_msg_after_click = '//android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.TextView'
rp_sign_after_value = '//android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.TextView[2]'
tarik_dana_page_btn = 'TarikPageBtn'
ok_btn = "//*[@text='OK']"
fund_transfer_bank = 'FundBankTextStr'
#Riwayat page locators
riwayat_header = 'RiwayatHeader'
riwayat_page_back_btn = "//android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.ImageView[@index = '0']"
riwayat_entry_1 = 'RiwayatPageEntry0'
riwayat_entry_1_amount = 'RiwayatPageRpValue0'

class SaldoRdn(HomePage):

    @allure.step("click on saldo rdn btn")
    def click_on_saldo_rdn_btn(self):
        self.click(saldo_rdn_btn)
        self.sleep(2)

    @allure.step("Verify rdn homePage")
    def verify_rdn_homePage(self):
        self.sleep(3)
        self.assert_equal(self.is_element_visible(rdn_header), True)
        self.assert_equal(self.is_element_visible(rdn_balance), True)

    @allure.step("Swipe down to close top up page")
    def swipe_down_to_close_top_up_page(self):
        first_coordinate = self.get_attribute(top_up_header, 'bounds')
        lst_1 = first_coordinate.split(',')
        first_x = int(lst_1[0][1:])
        first_y = int(lst_1[1][0:3])
        second_coordinate = self.get_attribute('TopupPageBankImage', 'bounds')
        lst_2 = second_coordinate.split(',')
        sec_x = int(lst_2[0][1:])
        sec_y = int(lst_2[1][0:4])
        # logger.info(f'{second_coordinate} {type(second_coordinate)} {second_coordinate[1]}')
        # logger.info(f'{fist_coordinate} {type(fist_coordinate)} {fist_coordinate[1]}')
        self.scroll_screen(start_x=first_x, start_y=first_y, end_x=sec_x, end_y=sec_y, duration=10000)
        self.sleep(2)

    @allure.step("Tap outside of half card")
    def tap_out_side_of_half_acrd(self):
        first_coordinate = self.get_attribute(up_head_sign, 'bounds')
        lst_1 = first_coordinate.split(',')
        first_x = int(lst_1[0][1:])
        first_y = (int(lst_1[1][0:3])) - 37
        self.tap_by_coordinates(first_x,first_y)

    @allure.step("Verify arrow btn on top up page")
    def verify_arrow_btn_on_top_up_page(self):
        self.assert_equal(self.is_element_visible(simobi_text_1), True)
        self.click(simobi_arrow)
        self.assert_equal(self.is_element_visible(simobi_text_1), False)
        self.click(bank_arrow)
        self.assert_equal(self.is_element_visible(bank_text_1), True)
        self.click(bank_arrow)
        self.assert_equal(self.is_element_visible(bank_text_1), False)

    @allure.step("validate all btn on rdn balance page")
    def validate_all_btn_on_rdn_balance_page(self):
        self.verify_rdn_homePage()
        self.go_back()
        self.verify_home_page_reg_user()
        self.click_on_saldo_rdn_btn()
        self.verify_rdn_homePage()
        self.click(rdn_back_btn)
        self.verify_home_page_reg_user()
        self.click_on_saldo_rdn_btn()
        self.verify_rdn_homePage()
        self.click(top_up_btn)
        self.verify_topup_page()
        self.go_back()
        self.verify_rdn_homePage()
        self.click(top_up_btn)
        self.verify_topup_page()
        self.swipe_down_to_close_top_up_page()
        self.verify_rdn_homePage()
        self.click(top_up_btn)
        self.verify_topup_page()
        self.verify_arrow_btn_on_top_up_page()
        self.tap_out_side_of_half_acrd()
        self.verify_rdn_homePage()
        self.click(tarik_dana_btn)
        self.verify_tarik_dana_page()
        self.go_back()
        self.verify_rdn_homePage()
        self.click(tarik_dana_btn)
        self.verify_tarik_dana_page()
        self.click(tarik_page_back_btn)
        self.verify_rdn_homePage()
        self.click(riwayat_btn)
        self.verify_riwayat_page()
        self.go_back()
        self.verify_rdn_homePage()
        self.click(riwayat_btn)
        self.click(riwayat_page_back_btn)
        self.verify_rdn_homePage()

    @allure.step("Scroll down rdn page")
    def scroll_down_rdn_page(self):
        first_coordinate = self.get_attribute(rdn_balance, 'bounds')
        lst_1 = first_coordinate.split(',')
        first_x = int(lst_1[0][1:])
        first_y = int(lst_1[1][0:3])
        second_coordinate = self.get_attribute(rdn_fund_account_text, 'bounds')
        lst_2 = second_coordinate.split(',')
        sec_x = int(lst_2[0][1:])
        sec_y = int(lst_2[1][0:4])
        # logger.info(f'{second_coordinate} {type(second_coordinate)} {second_coordinate[1]}')
        # logger.info(f'{fist_coordinate} {type(fist_coordinate)} {fist_coordinate[1]}')
        self.scroll_screen(start_x=first_x, start_y=first_y, end_x=sec_x, end_y=sec_y, duration=10000)
        self.sleep(2)

    @allure.step("Functional validation of rdn page")
    def functional_validation_of_rdn_page(self):
        self.assert_equal(self.get_attribute(rdn_update_msg, 'text'), 'Last updated a few seconds ago')
        self.scroll_down_rdn_page()
        self.assert_equal(self.get_attribute(rdn_update_msg, 'text'), 'Last updated a few seconds ago')
        self.assert_equal(self.is_element_visible(rdn_balance), True)
        self.go_back()
        self.verify_home_page_reg_user()
        rdn_balance_homepage = self.get_attribute(homepage_rdn_balance_l, 'text')
        self.click(saldo_rdn_btn)
        rdn_balance_rdn_page = self.get_attribute(rdn_balance, 'text')
        self.assert_equal(rdn_balance_homepage,rdn_balance_rdn_page)
        self.assert_equal(self.get_attribute(bank_name, 'text'), 'SINARMAS')
        self.assert_equal(self.get_attribute(account_owner_name, 'text'), 'Testing Siminvest 1')
        self.assert_equal(self.get_attribute(bank_acc_number, 'text'), '0016428639')

    @allure.step("ui validation for rdn page")
    def ui_validation_for_rdn_page(self):
        self.assert_equal(self.get_attribute(rdn_header, 'text'), 'RDN Balance')
        self.assert_equal(self.get_attribute(saldo_efektif, 'text'), 'Saldo efektif')
        self.assert_equal(self.get_attribute(top_up_text, 'text'), 'Top up')
        self.assert_equal(self.get_attribute(riwyat_text, 'text'), 'Riwayat')
        self.assert_equal(self.get_attribute(tarik_dana_text, 'text'), 'Tarik dana')
        self.assert_equal(self.get_attribute(informasi_saldo_text, 'text'), 'Informasi saldo')
        for i in range(0,5):
            self.assert_equal(self.get_attribute(f'RdnBalanceText{i}', 'text'), f'Dana T+{i}')
            self.assert_equal(self.get_attribute(f'RdnBalanceText{i}Amount', 'text'), 'Rp 0')
        self.assert_equal(self.get_attribute(informasi_rekening, 'text'), 'Informasi rekening')
        self.assert_equal(self.get_attribute(bank_name_text, 'text'), 'Bank Penerbit')
        self.assert_equal(self.get_attribute(bank_acc_owner_text, 'text'), 'Nama Pemilik Akun')
        self.assert_equal(self.get_attribute(bank_acc_number_text, 'text'), 'Nomor Rekening Dana \nNasabah')

    @allure.step("Data comparison between homepage , profile page and rdn page")
    def data_comparison_btw_homepage_profile_and_rdn_page(self):
        rp_homepage = self.get_attribute(homepage_rdn_balance_l, 'text')
        self.click(profile_btn)
        self.sleep(2)
        self.click(informasi_profile)
        rp_profile_page = self.get_attribute(rdn_balance, 'text')
        bank_name_profile = self.get_attribute(bank_name, 'text')
        account_owner_name_profile = self.get_attribute(account_owner_name, 'text')
        bank_acc_number_profile = self.get_attribute(bank_acc_number, 'text')
        self.go_back()
        self.assert_equal(self.is_element_visible(profile_name), True)
        self.click(homepage_btn)
        self.sleep(4)
        self.click_on_saldo_rdn_btn()
        rp_rdn = self.get_attribute(rdn_balance, 'text')
        bank_name_rdn = self.get_attribute(bank_name, 'text')
        account_owner_name_rdn = self.get_attribute(account_owner_name, 'text')
        bank_acc_number_rdn = self.get_attribute(bank_acc_number, 'text')
        self.assert_equal(rp_homepage, rp_profile_page)
        self.assert_equal(rp_homepage, rp_rdn)
        self.assert_equal(bank_name_profile, bank_name_rdn)
        self.assert_equal(account_owner_name_profile, account_owner_name_rdn)
        self.assert_equal(bank_acc_number_profile, bank_acc_number_rdn)

    @allure.step("validate ui for tarikDana page")
    def validate_ui_for_tarikDana_page(self):
        self.assert_equal(self.get_attribute(tarik_dana_header, 'text'), 'Tarik Dana')
        self.assert_equal(self.get_attribute(dana_tersedia_text, 'text'), 'Dana tersedia')
        self.assert_equal(self.get_attribute(TarikPagePenarikan_text, 'text'), 'Penarikan dari RDN')
        self.assert_equal(self.get_attribute(TarikPageTransfer_text, 'text'), 'Transfer Ke Rekening')
        self.assert_equal(self.get_attribute(tariK_msg_text, 'text'), 'Permintaan penarikkan dana diatas pukul 11.00 WIB akan di proses di hari kerja bursa berikutnya.')
        self.assert_equal(self.get_attribute(TarikPageNominal_text, 'text'), 'Nominal Penarikan (Min. Rp 100.000)')
        self.assert_equal(self.get_attribute(tarik_dana_btn_tarik, 'text'), 'Tarik Dana')

    @allure.step("validate functional feature of tarikDana page")
    def validate_functional_feature_of_tarikDana_page(self):
        rdn_homepage = self.get_attribute(rdn_balance, 'text')
        rdn_balance_without_rp = int((rdn_homepage[3:]).replace(',', ''))
        self.click(tarik_dana_btn)
        rdn_tarik = self.get_attribute(tarik_dana_rdn, 'text')
        rdn_tarik_without_rp = int((rdn_tarik[3:]).replace(',', ''))
        logger.info(rdn_tarik_without_rp)
        logger.info(rdn_balance_without_rp-1)
        self.assert_equal(rdn_tarik_without_rp, rdn_balance_without_rp-1)
        limit_msg = self.get_attribute(TarikPageNominal_text, 'text')
        self.assert_equal(limit_msg , 'Nominal Penarikan (Min. Rp 100.000)')
        self.click(TarikPageNominal_text)
        self.assert_equal(self.get_attribute(nominal_msg_after_click, 'text') , 'Nominal Penarikan (Min. Rp 100.000)')
        self.set_text(TarikPageNominal_text,'100')
        self.assert_equal(self.get_attribute(nominal_msg_after_click, 'text') , 'Nominal Penarikan (Min. Rp 100.000)')
        self.assert_not_equal(self.get_attribute(TarikPageNominal_text, 'text') , 'Nominal Penarikan (Min. Rp 100.000)')
        self.assert_equal(self.get_attribute(rp_sign_after_value, 'text'), 'Rp')
        self.click(tariK_msg_text)
        self.click(tarik_dana_page_btn)
        self.verify_tarik_dana_page()
        #self.clear_text(TarikPageNominal_text)
        self.assert_equal(self.get_attribute(nominal_msg_after_click, 'text') , 'Nominal Penarikan (Min. Rp 100.000)')
        self.set_text(TarikPageNominal_text, '100000')
        self.click(tariK_msg_text)
        self.click(tarik_dana_page_btn)
        self.sleep(2)
        self.assert_equal(self.is_element_visible(ok_btn), True)
        self.click(ok_btn)
        self.sleep(2)
        self.verify_riwayat_page()

    @allure.step("Btn validation on tarikDana Page")
    def btn_validation_on_tarikDana_page(self):
        self.click_on_tarik_dana_btn()
        self.verify_tarik_dana_page()
        self.click(rdn_back_btn)
        self.verify_rdn_homePage()
        self.click_on_tarik_dana_btn()
        self.verify_tarik_dana_page()
        self.click(TarikPageNominal_text)
        self.set_text(TarikPageNominal_text, '100')
        self.assert_equal(self.get_attribute(nominal_msg_after_click, 'text') , 'Nominal Penarikan (Min. Rp 100.000)')
        self.verify_keyboard_on_off(True)
        self.click(tariK_msg_text)
        self.verify_keyboard_on_off(False)
        self.assert_equal(self.get_attribute(nominal_msg_after_click, 'text'), 'Nominal Penarikan (Min. Rp 100.000)')
        self.click(TarikPageNominal_text)
        self.verify_keyboard_on_off(True)

    @allure.step("API data validation")
    def api_data_validation(self):
        rdn_value_all = self.get_attribute(rdn_balance, 'text')
        rdn_value = int((rdn_value_all[3:]).replace(',',''))
        bank_account_name = self.get_attribute(account_owner_name, 'text')
        bank_name_rdn = self.get_attribute(bank_name, 'text')
        bank_account__number_rdn = self.get_attribute(bank_acc_number, 'text')
        self.click(tarik_dana_btn)
        name_of_bank_in_rekeraing_all = self.get_attribute(fund_transfer_bank, 'text')
        name_of_bank_in_rekeraing= name_of_bank_in_rekeraing_all[:3]
        number_of_bank_in_rekeraing= name_of_bank_in_rekeraing_all[6:]
        self.go_back()
        self.click(riwayat_btn)
        if self.is_element_visible(riwayat_entry_1) == True:
            riwayat_amount_rp = self.get_attribute(riwayat_entry_1_amount, 'text')
            riwayat_amount = int((riwayat_amount_rp[3:]).replace(',', ''))

        token_value = self.login_with_a_number(user_data['reg_no_3'])
        token = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJpWlYzdUJkTkJyTDA4dVIzQUR2bmg4akdTdHNkSHpQVSIsInN1YiI6IlNpbWFzSW52ZXN0In0.Kj31bgBrbc94NaUDKWgbx-N4ZBQNFsrZBmF7xtZ4hNo"}
        token['Authorization'] = 'Bearer ' + token_value
        portfolio_equity_rs = request_utilities.get(base_url='https://stg-api.siminvest.co.id/',endpoint='api/v1/users/portfolios/equities/53617', headers=token,expected_status_code=202)
        rdn_balance_api = portfolio_equity_rs['data']['cash_balance']
        user_account_res = request_utilities.get(base_url='https://stg-api.siminvest.co.id/',endpoint=f"api/v1/users/account/{user_data['reg_no_3']}", headers=token,expected_status_code=200)
        user_name = user_account_res['full_name']
        rdn_user_account_res = request_utilities.get(base_url='https://stg-api.siminvest.co.id/',endpoint="api/v1/users/rdn?account_id=45997", headers=token,expected_status_code=200)
        bank_name_api=rdn_user_account_res['data']['rdn_bank']
        bank_account_name_api = rdn_user_account_res['data']['bank_account_name']
        rekening_bank_name = rdn_user_account_res['data']['bank_name']
        rekening_bank_number = rdn_user_account_res['data']['bank_account_number']
        rdn_account_number = rdn_user_account_res['data']['rdn_account']
        withdraw_history_res = request_utilities.get(base_url='https://stg-api.siminvest.co.id/',endpoint=f"api/v1/users/rdn/history?page=1", headers=token,expected_status_code=200)
       # withdraw_history_account = withdraw_history_res['data']['statements'][0]['amount']
        self.assert_equal(rdn_value, rdn_balance_api)
        self.assert_equal(bank_name_rdn, bank_name_api)
        self.assert_equal(bank_account_name, bank_account_name_api)
        self.assert_equal(bank_account__number_rdn, rdn_account_number)
        self.assert_equal(name_of_bank_in_rekeraing, rekening_bank_name)
        self.assert_equal(number_of_bank_in_rekeraing, rekening_bank_number)
        #self.assert_equal(withdraw_history_account, riwayat_amount)







