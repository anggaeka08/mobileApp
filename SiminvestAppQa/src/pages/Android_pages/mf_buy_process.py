import json
from selenium.common.exceptions import InvalidElementStateException
from SiminvestAppQa.src.utilities.requestUtilities import RequestsUtilities
from datetime import datetime
request_utilities = RequestsUtilities()
from SiminvestAppQa.src.data.userData import user_data
from SiminvestAppQa.src.pages.Android_pages.login_page import LoginPage
from SiminvestAppQa.src.pages.Android_pages.home_page import HomePage
from SiminvestAppQa.src.pages.Android_pages.reksadana_page import ReksadanaPage
import time
import allure
from datetime import timedelta
from datetime import date
import logging as logger
from  numerize import numerize

# Locator
product_satu_campuran = '//android.widget.TextView[@text="Simas Satu"]'
btn_beli = '//android.view.ViewGroup[@content-desc="button_beli"]/android.widget.TextView'
campuran = '//android.widget.TextView[@text="Campuran"]'
title_bottomsheet_kamu = 'Bottomsheet_title'
btn_close = '//android.view.ViewGroup[@content-desc="Bottomsheet_btn_close"]/android.widget.ImageView'
back_btn_product_sdp = '//android.view.ViewGroup[@content-desc="back_button"]/android.widget.ImageView'
back_btn_campuran = 'reksadana_campuran_backbtn'
Saham = 'reksadana_saham_tetx1'
product_saham = '//android.widget.TextView[@text="Simas Saham Maksima"]'
title_alert_resiko = 'alert_header'
alert_btn_lanjutkan = '//android.view.ViewGroup[@content-desc="alert_button_lanjutkan"]/android.widget.TextView'
alert_btn_batal = '//android.view.ViewGroup[@content-desc="alert_button_batal"]/android.widget.TextView'




class buy_process(ReksadanaPage):

    @allure.step("Validate_buttomsheet_kamu")
    def Validate_buttomsheet_kamu(self):
        self.click(campuran)
        self.sleep(2)
        self.click(product_satu_campuran)
        self.sleep(2)
        self.click(btn_beli)
        self.sleep(2)
        self.assert_equal(self.is_element_visible(title_bottomsheet_kamu), True)
        self.click(btn_close)
        self.click(back_btn_product_sdp)
        self.click(back_btn_campuran)
        self.sleep(2)
    
    @allure.step("Validate_popup_resiko")
    def Validate_popup_resiko(self):
        self.click(Saham)
        self.sleep(2)
        self.click(product_saham)
        self.sleep(2)
        self.click(btn_beli)
        self.sleep(2)
        self.assert_equal(self.is_element_visible(title_alert_resiko), True)
        self.assert_equal(self.is_element_visible(alert_btn_lanjutkan), True)
        self.assert_equal(self.is_element_visible(alert_btn_batal), True)
        self.click(alert_btn_batal)
        self.assert_equal(self.is_element_visible(btn_beli), True)
        self.click(btn_beli)
        self.assert_equal(self.is_element_visible(alert_btn_lanjutkan), True)
        self.click(alert_btn_lanjutkan)
        self.assert_equal(self.get_attribute(title_bottomsheet_kamu, 'text'), 'JUMLAH INVESTASI KAMU')
        self.click(btn_close)
        self.sleep(2)    
        
        
        
        
             