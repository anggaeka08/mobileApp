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
date_nav = '//android.view.ViewGroup[@content-desc="nav_chart_details"]/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]'
btn_saya_mengerti = 'ketentuan_unit_button_saya_mengerti'
btn_back_saya_mengerti = '//android.view.ViewGroup[@content-desc="ketentuan_unit_back_button"]/android.widget.ImageView'
ketentuan_unit_title1 = 'ketentuan_unit_title_1'
ketentuan_unit_sub_title1 = 'ketentuan_unit_sub_title_1'
ketentuan_unit_title2 = 'ketentuan_unit_title_2'
ketentuan_unit_sub_title3 = 'ketentuan_unit_sub_title_3'
title_konfirmasi_pesanan = 'knfirmasi_pmesnan_header'
back_btn_konfirmasi = '//android.view.ViewGroup[@content-desc="knfirmasi_pmesnan_back_btn"]/android.widget.ImageView'
product_tiga_campuran = '//android.widget.TextView[@text="Simas Satu Prima"]'
btn_top_up = '//android.view.ViewGroup[@content-desc="Button_topup"]/android.widget.TextView'
title_order_detail = 'knfirmasi_pmesnan_text_3'
text_product = 'knfirmasi_pmesnan_text_4'
text_jenis_product = 'knfirmasi_pmesnan_text_5'
text_biaya = 'knfirmasi_pmesnan_text_6'
text_total_tagihan = 'knfirmasi_pmesnan_text_7'
btn_pilih = '//android.view.ViewGroup[@content-desc="knfirmasi_pmesnan_text_2"]/android.widget.TextView'
halfcard_title = 'bottomsheet_header'
close_btn = '//android.view.ViewGroup[@content-desc="bottomsheet_btn_close"]/android.widget.ImageView'
text_bank = 'bottomsheet_name_bank'
name_bank_konfirmasi_page = '//android.widget.TextView[@text="BANK SINARMAS"]'
text_ganti_konfirmasi_page = '//android.widget.TextView[@text="ganti"]'
cek_box = '//android.view.ViewGroup[@content-desc="knfirmasi_pmesnan_cek_box"]/android.widget.ImageView'
text_aggrement = 'knfirmasi_pmesnan_agreement_text'
title_rdp = 'text_title'
text_warning = 'knfirmasi_pmesnan_text_warning'
btn_bayar_konfirmasi_pesanan = '//android.view.ViewGroup[@content-desc="knfirmasi_pmesnan_button_bayar"]/android.widget.TextView'
title_detail_order = 'knfirmasi_pmesnan_header'
order_id = 'knfirmasi_pmesnan_order_id'
btn_close_detail_order = '//android.view.ViewGroup[@content-desc="knfirmasi_pmesnan_btn_close"]/android.widget.ImageView'
default_orderlist_selected = '(//android.view.ViewGroup[@content-desc="ReksadanaOrderlist"])[1]'
default_orderlist_riwayat = '(//android.view.ViewGroup[@content-desc="ReksadanaOrderlist"])[2]'
riwayat_selected_orderlist = '(//android.view.ViewGroup[@content-desc="ReksadanaRiwayat"])[1]'
riwayat_selected_riwayat = '(//android.view.ViewGroup[@content-desc="ReksadanaRiwayat"])[2]'
all_types = '//android.widget.TextView[@text="All Types"]'
all_Status = '//android.widget.TextView[@text="All Status"]'


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


    @allure.step("Validate_konfirmasi_page")
    def Validate_konfirmasi_page(self):
        self.click(campuran)
        self.sleep(2)
        self.click(product_satu_campuran)
        self.sleep(2)
        self.click(btn_beli)
        self.sleep(2)
        
        input_amount = '20400'
        self.update_text(bottomsheet_input_amount, input_amount)
        self.assert_equal(self.is_element_visible(btn_bottomsheet_beli), True)
        self.click(btn_close)
        self.sleep(1)
        self.assert_equal(self.is_element_visible(btn_beli), True)
        
        self.click(btn_beli)
        self.sleep(1)
        max_number = '123456789012'
        self.update_text(bottomsheet_input_amount, max_number)
        amount_max_value= (self.get_attribute(bottomsheet_input_amount, 'text'),  max_number[:12])
        logger.info(amount_max_value)
        self.sleep(1)
        
        self.click(bottomsheet_pilih_denom_100rb)
        self.click(btn_bottomsheet_beli)
        self.sleep(2)
        self.assert_equal(self.is_element_visible(btn_saya_mengerti), True)
        self.assert_equal(self.is_element_visible(btn_back_saya_mengerti), True)
        self.assert_equal(self.get_attribute(ketentuan_unit_title1, 'text'), 'Transaksi pukul 00.00 WIB - 12.00 WIB')
        self.assert_equal(self.get_attribute(ketentuan_unit_sub_title1, 'text'), 'Mendapatkan harga unit/hari ini.')
        self.assert_equal(self.get_attribute(ketentuan_unit_title2, 'text'), 'Transaksi pukul 12.01 WIB - 23.59 WIB')
        self.assert_equal(self.get_attribute(ketentuan_unit_sub_title3, 'text'), 'Mendapatkan harga unit/hari bursa berikutnya.')

        self.click(btn_back_saya_mengerti)
        self.sleep(2)
        self.assert_equal(self.is_element_visible(btn_beli), True)
        self.click(btn_beli)
        self.click(bottomsheet_pilih_denom_100rb)
        self.click(btn_bottomsheet_beli)
        self.sleep(2)
        self.assert_equal(self.is_element_visible(btn_saya_mengerti), True)
        self.click(btn_saya_mengerti)
        self.sleep(2)
        self.assert_equal(self.is_element_visible(title_konfirmasi_pesanan), True)
        self.assert_equal(self.is_element_visible(back_btn_konfirmasi), True)


    @allure.step("verify_top_up_page")
    def verify_top_up_page(self):
        self.click(campuran)
        self.sleep(2)
        self.click(product_tiga_campuran)
        self.sleep(2)
        self.click(btn_top_up)
        self.sleep(2)
        self.click(bottomsheet_pilih_denom_100rb)
        self.click(btn_bottomsheet_beli)
        self.sleep(2)
        self.click(btn_saya_mengerti)
        self.sleep(2)
        self.assert_equal(self.is_element_visible(title_konfirmasi_pesanan), True)
        self.click(back_btn_konfirmasi)
        self.sleep(2)
        self.assert_equal(self.get_attribute(title_rdp, 'text'), 'Simas Satu Prima')
        self.click(back_btn_product_sdp)
        self.sleep(2)
    
    @allure.step("Validate_konfirmasi_pesanan")
    def Validate_konfirmasi_pesanan(self):
        self.click(product_satu_campuran)
        self.sleep(2)
        self.click(btn_beli)
        self.sleep(2)
        self.click(bottomsheet_pilih_denom_100rb)
        self.click(btn_bottomsheet_beli)
        self.sleep(2)
        self.click(btn_saya_mengerti)
        self.sleep(2)
        self.assert_equal(self.is_element_visible(title_konfirmasi_pesanan), True)
        self.click(back_btn_konfirmasi)
        self.sleep(2)
        self.assert_equal(self.is_element_visible(btn_beli), True)
        self.click(btn_beli)
        self.sleep(2)
        self.click(bottomsheet_pilih_denom_100rb)
        self.click(btn_bottomsheet_beli)
        self.sleep(2)
        self.click(btn_saya_mengerti)
        self.sleep(2)
        self.assert_equal(self.is_element_visible(title_konfirmasi_pesanan), True)
        self.assert_equal(self.is_element_visible(title_order_detail), True)
        self.assert_equal(self.is_element_visible(text_product), True)
        self.assert_equal(self.is_element_visible(text_jenis_product), True)
        self.assert_equal(self.is_element_visible(text_biaya), True)
        self.assert_equal(self.is_element_visible(text_total_tagihan), True)
        self.click(btn_pilih)
        self.sleep(2)
        self.assert_equal(self.get_attribute(halfcard_title, 'text'), 'Pilih Metode Pembayaran')
        self.assert_equal(self.get_attribute(text_bank, 'text'), 'BANK SINARMAS')
        self.click(text_bank)
        self.sleep(2)
        self.assert_equal(self.is_element_visible(name_bank_konfirmasi_page), True)
        self.assert_equal(self.is_element_visible(cek_box), True)
        self.assert_equal(self.is_element_visible(text_aggrement), True)
        
        
    @allure.step("Verify_order_detail")
    def Verify_order_detail(self):
        self.click(campuran)
        self.sleep(2)
        self.click(product_satu_campuran)
        self.sleep(2)
        self.click(btn_beli)
        self.sleep(2)
        self.click(bottomsheet_pilih_denom_100rb)
        self.click(btn_bottomsheet_beli)
        self.sleep(2)
        self.click(btn_saya_mengerti)
        self.sleep(2)
        self.assert_equal(self.is_element_visible(title_konfirmasi_pesanan), True) 
        self.click(btn_pilih)
        self.sleep(1)
        self.click(text_bank)
        self.sleep(2)
        self.click(cek_box)
        self.sleep(1)
        self.click(cek_box)
        self.sleep(1)
        self.click(cek_box)
        self.assert_equal(self.is_element_visible(text_warning), True)
        self.click(btn_bayar_konfirmasi_pesanan)
        self.sleep(2) 
        self.assert_equal(self.is_element_visible(title_detail_order), True)
        self.assert_equal(self.is_element_visible(order_id), True)
        self.assert_equal(self.is_element_visible(btn_close_detail_order), True)
        self.click(btn_close_detail_order)
        self.sleep(2) 
        self.assert_equal(self.is_element_visible(default_orderlist_selected), True)
        self.assert_equal(self.is_element_visible(default_orderlist_riwayat), True)
        self.assert_equal(self.is_element_visible(all_types), True)
        self.assert_equal(self.is_element_visible(all_Status), True)
   