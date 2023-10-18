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
current_min_pembelian = '(//android.view.ViewGroup[@content-desc="Top_reksadana_box1"])[1]/android.view.ViewGroup[1]/android.widget.TextView[3]'
bottomsheet_nominal = 'Bottomsheet_nominal'
bottomsheet_input_amount = 'Bottomsheet_input_amount'
title_nav = 'Bottomsheet_text_date'
error_message = '//android.widget.TextView[@text="Min. Rp 100,000"]'
bottomsheet_pilih_denom_100rb = 'Bottomsheet_pilih_denom_100000'
bottomsheet_pilih_denom_500rb = 'Bottomsheet_pilih_denom_500000'
bottomsheet_pilih_denom_1jt = 'Bottomsheet_pilih_denom_1 juta'
bottomsheet_pilih_denom_3jt = 'Bottomsheet_pilih_denom_3 juta'
bottomsheet_pilih_denom_5jt = 'Bottomsheet_pilih_denom_5 juta'
bottomsheet_pilih_denom_10jt = 'Bottomsheet_pilih_denom_10 juta'
bottomsheet_pilih_denom_25jt = 'Bottomsheet_pilih_denom_25 juta'
btn_bottomsheet_beli = 'Bottomsheet_btn_beli'
	
denom_text = '//android.view.ViewGroup[@content-desc="Bottomsheet_pilih_denom_100000"]/android.widget.TextView'

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
        
    @allure.step("Validate_bottomsheet_kamu")
    def Validate_bottomsheet_kamu(self):
        current_min_pembelian_value= self.get_attribute(current_min_pembelian, 'text')
        log_min_pembelian = (current_min_pembelian_value[32:])
        logger.info(log_min_pembelian)
        
        self.click(campuran)
        self.sleep(2)
        self.click(product_satu_campuran)
        self.sleep(2)
        self.click(btn_beli)
        self.sleep(2)
        self.assert_equal(self.is_element_visible(title_bottomsheet_kamu), True)
        min_amount_value= self.get_attribute(bottomsheet_input_amount, 'text')
        log_min_amount = (min_amount_value[8:])
        logger.info(log_min_amount)
        
        self.assert_equal(log_min_pembelian, log_min_amount)
        
        self.assert_equal(self.is_element_visible(title_nav), True)
        self.assert_equal(self.get_attribute(bottomsheet_nominal, 'text'), '0')
        
        input_amount = '20400'
        self.update_text(bottomsheet_input_amount, input_amount)
        self.assert_equal(self.is_element_visible(error_message), True)
        
        self.click(bottomsheet_pilih_denom_100rb)
        self.assert_equal(self.is_element_visible(bottomsheet_pilih_denom_100rb), True)
        
        self.click(bottomsheet_pilih_denom_500rb)
        self.assert_equal(self.is_element_visible(bottomsheet_pilih_denom_500rb), True)
        
        self.click(bottomsheet_pilih_denom_1jt)
        self.assert_equal(self.is_element_visible(bottomsheet_pilih_denom_1jt), True)
        
        self.click(bottomsheet_pilih_denom_3jt)
        self.assert_equal(self.is_element_visible(bottomsheet_pilih_denom_3jt), True)
        
        self.click(bottomsheet_pilih_denom_5jt)
        self.assert_equal(self.is_element_visible(bottomsheet_pilih_denom_5jt), True)
        
        self.click(bottomsheet_pilih_denom_10jt)
        self.assert_equal(self.is_element_visible(bottomsheet_pilih_denom_10jt), True)
        
        self.click(bottomsheet_pilih_denom_25jt)
        self.assert_equal(self.is_element_visible(bottomsheet_pilih_denom_25jt), True)
        
        #separator
        self.assert_equal(self.is_element_visible(denom_text), True)
        bottomsheet_rp_with_rp = self.get_attribute(denom_text, 'text')
        bottomsheet_rp_value = bottomsheet_rp_with_rp[3:]
        self.assert_in(',', bottomsheet_rp_value)
        logger.info(bottomsheet_rp_with_rp)
        logger.info(bottomsheet_rp_value)
        
        self.assert_equal(self.is_element_visible(btn_bottomsheet_beli), True)
        
        
        
             