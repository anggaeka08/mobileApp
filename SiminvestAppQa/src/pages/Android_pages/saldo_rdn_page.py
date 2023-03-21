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
        first_coordinate = self.get_attribute(up_head_sign, 'bounds')
        lst_1 = first_coordinate.split(',')
        first_x = int(lst_1[0][1:])
        first_y = int(lst_1[1][0:4])
        second_coordinate = self.get_attribute(bank_title, 'bounds')
        lst_2 = second_coordinate.split(',')
        sec_x = int(lst_2[0][1:])
        sec_y = int(lst_2[1][0:4])
        # logger.info(f'{second_coordinate} {type(second_coordinate)} {second_coordinate[1]}')
        # logger.info(f'{fist_coordinate} {type(fist_coordinate)} {fist_coordinate[1]}')
        self.scroll_screen(start_x=first_x, start_y=first_y, end_x=sec_x, end_y=sec_y, duration=5000)
        self.sleep(2)

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






