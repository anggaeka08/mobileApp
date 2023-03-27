import pytest
from selenium.common.exceptions import InvalidElementStateException
from datetime import datetime
from SiminvestAppQa.src.data.userData import user_data
from SiminvestAppQa.src.pages.Android_pages.home_page import HomePage
import time
import allure
from datetime import timedelta
from datetime import date
import logging as logger
from  numerize import numerize

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
#Riwayat page locators
riwayat_header = 'RiwayatHeader'
riwayat_page_back_btn = "//android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.ImageView[@index = '0']"

class SaldoRdn(HomePage):

    @allure.step("click on saldo rdn btn")
    def click_on_saldo_rdn_btn(self):
        self.click(saldo_rdn_btn)
        self.sleep(2)

    @allure.step("Verify rdn homePage")
    def verify_rdn_homePage(self):
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
        self.sleep(2)
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



