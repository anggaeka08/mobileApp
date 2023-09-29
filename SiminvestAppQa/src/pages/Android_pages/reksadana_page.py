import json

import elftools.elf.segments
from appiumbase import BaseCase
from selenium.common.exceptions import NoSuchElementException

from SiminvestAppQa.src.pages.Android_pages.login_page import LoginPage
from SiminvestAppQa.src.pages.Android_pages.home_page import HomePage
import logging as logger
import allure
from SiminvestAppQa.src.data.userData import user_data
from SiminvestAppQa.src.utilities.requestUtilities import RequestsUtilities
from datetime import datetime,date,timedelta

request_utilities = RequestsUtilities()
# reksadana homepage Locator'
reksadana ="//android.view.ViewGroup[@content-desc='Homepage_reksadana_btn']/android.widget.TextView"
Portfolio_reksadana ='(//android.view.ViewGroup/android.view.ViewGroup[7]/android.widget.TextView[1])[1]'
total_amount='//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[7]/android.widget.TextView[2]'
percentage_today ='//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[7]/android.widget.TextView[3]'
transaction ="//android.widget.TextView[@text='Transaction']"
saham ="//android.widget.TextView[@text='Saham']"
saham_tab = '//android.widget.TextView[@content-desc="Saham_tab"]'
Home = '//android.widget.TextView[@text="Home"]'
profile = '//android.widget.TextView[@text="Profile"]'
today = '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[7]/android.widget.TextView[3]'
Pasar_uang = 'reksadana_pasarUang_text1'
icon_pasar_uang = 'reksadana_pasarUang_Image1'
Pasar_uang_title = 'reksadana_psruang_tittle'
back_btn_pasar_uang = 'reksadana_psruang_backbutton'
product_pasar_uang = 'reksadana_psruang_subtitle'
title_product_pasar_uang_1 = '(//android.widget.TextView[@content-desc="reksadana_psruang_entry_1_text"])[1]'
title_product_pasar_uang_2 = '(//android.widget.TextView[@content-desc="reksadana_psruang_entry_1_text"])[2]'
title_product_pasar_uang_3 = '(//android.widget.TextView[@content-desc="reksadana_psruang_entry_1_text"])[3]'


btn_beli = '//android.view.ViewGroup[@content-desc="button_beli"]/android.widget.TextView'
back_btn_rdp = 'back_button'
product_pasar_uang_1 = '(//android.widget.TextView[@content-desc="reksadana_psruang_entry_1_text"])[1]'
btn_beli_psr_uang = '//android.view.ViewGroup[@content-desc="button_beli"]/android.widget.TextView'
title_rdp_psr_uang = 'text_title'
Pasar_uang_value_amount = '(//android.widget.TextView[@content-desc="reksadana_psruang_entry_1_nominal"])[1]'
rdp_psr_uang_value_amount= '//android.view.ViewGroup[@content-desc="nav_chart_details"]/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]'
Pasar_uang_value_Aum = '(//android.widget.TextView[@content-desc="reksadana_psruang_entry_1_aum"])[1]'
Pasar_uang_value_Percentage = '(//android.widget.TextView[@content-desc="reksadana_psruang_entry_1_percentage"])[1]'
Pasar_uang_value_Date = '(//android.widget.TextView[@content-desc="reksadana_psruang_entry_1_date"])[1]'
icon_pendapatan_tetap = 'reksadana_PendapatanTtp_Image1'
Pendapatan_Tetap = 'reksadana_PendapatanTtp_text1'
Pendapatan_tetap_title = 'reksadana_pndptn_tetap_title'
product_pendapatan_tetap = 'reksadana_pndptn_tetap_subtitle'
back_btn_pendapatan_tetap = 'reksadana_pndptn_tetap_backbtn'
icon_saham = 'reksadana_saham_Image1'
Saham = 'reksadana_saham_tetx1'
Saham_title = 'reksadana_saham_tittle'
product_saham = 'reksadana_saham_subtitle'
back_btn_saham = 'reksadana_saham_backbutton'
icon_campuran = 'reksadana_Campuran_Image1'
Campuran = 'reksadana_Campuran_text1'
Campuran_title = 'reksadana_campuran_Title'
product_campuran = 'reksadana_campuran_subtitle'
back_btn_campuran = 'reksadana_campuran_backbtn'
text_title_rdp = 'text_title'

top_reksadana_title= '//android.view.ViewGroup[@content-desc="Top_reksadana_title1"]/android.widget.TextView'
icon_i = '//android.view.ViewGroup[@content-desc="Top_reksadana_title1"]/android.widget.ImageView'
half_card_title = 'top_reksadana_title'
half_card_subtitle = 'top_reksadana_subtitle'
half_card_btn_close = 'top_reksadana_btn_close'

#product list mutual fund
list_product_mf1 = '(//android.view.ViewGroup[@content-desc="Top_reksadana_box1"])[1]'
list_product_mf2 = '(//android.view.ViewGroup[@content-desc="Top_reksadana_box1"])[2]'
list_product_mf3 = '(//android.view.ViewGroup[@content-desc="Top_reksadana_box1"])[3]'
list_product_mf4 = '(//android.view.ViewGroup[@content-desc="Top_reksadana_box1"])[4]'
list_product_mf5 = '(//android.view.ViewGroup[@content-desc="Top_reksadana_box1"])[5]'
list_product_mf6 = '(//android.view.ViewGroup[@content-desc="Top_reksadana_box1"])[6]'
list_product_mf7 = '(//android.view.ViewGroup[@content-desc="Top_reksadana_box1"])[7]'
list_product_mf8 = '(//android.view.ViewGroup[@content-desc="Top_reksadana_box1"])[8]'
list_product_mf9 = '(//android.view.ViewGroup[@content-desc="Top_reksadana_box1"])[9]'
list_product_mf10 = '(//android.view.ViewGroup[@content-desc="Top_reksadana_box1"])[10]'


logo_product_mf1 = '(//android.view.ViewGroup[@content-desc="Top_reksadana_box1"])[1]/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup'
logo_product_mf2 = '(//android.view.ViewGroup[@content-desc="Top_reksadana_box1"])[2]/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup'
logo_product_mf3 = '(//android.view.ViewGroup[@content-desc="Top_reksadana_box1"])[3]/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup'
logo_product_mf4 = '(//android.view.ViewGroup[@content-desc="Top_reksadana_box1"])[4]/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup'
logo_product_mf5 = '(//android.view.ViewGroup[@content-desc="Top_reksadana_box1"])[5]/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup'
logo_product_mf6 = '(//android.view.ViewGroup[@content-desc="Top_reksadana_box1"])[6]/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup'
logo_product_mf7 = '(//android.view.ViewGroup[@content-desc="Top_reksadana_box1"])[7]/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup'
logo_product_mf8 = '(//android.view.ViewGroup[@content-desc="Top_reksadana_box1"])[8]/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup'
logo_product_mf9 = '(//android.view.ViewGroup[@content-desc="Top_reksadana_box1"])[9]/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup'
logo_product_mf10 = '(//android.view.ViewGroup[@content-desc="Top_reksadana_box1"])[10]/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup'

return_1Y_mf='(//android.widget.TextView[@content-desc="Top_reksadana_Returntext1"])[1]'
return_percentage = '(//android.widget.TextView[@content-desc="Top_reksadana_percentage1"])[1]'
return_percentage_4 = '(//android.widget.TextView[@content-desc="Top_reksadana_percentage1"])[4]'
return_percentage_10 = '(//android.widget.TextView[@content-desc="Top_reksadana_percentage1"])[10]'

title_mf_1= '(//android.view.ViewGroup[@content-desc="Top_reksadana_box1"])[1]/android.view.ViewGroup[1]/android.widget.TextView[1]'

#ringkasan tab
ringkasan_tab = '//android.view.ViewGroup[@content-desc="ringkasan_tab"]/android.widget.TextView'
default_line = '//android.view.ViewGroup[@content-desc="ringkasan_tab"]/android.view.ViewGroup'
min_initial_purchase = '//android.view.ViewGroup[@content-desc="resume_product"]/android.widget.TextView[2]'
min_resale_price =  '//android.view.ViewGroup[@content-desc="resume_product"]/android.widget.TextView[6]'
alert_header = 'alert_header'
button_batal = 'alert_button_batal'
button_top_up_rdp = 'Button_topup'
button_buy_rdp = 'Button_jual1'
button_prospektus = 'button_prospektus'
button_fact_sheet = 'button_fact_sheet'

#informasi tab
informasi_tab = '//android.view.ViewGroup[@content-desc="informasi_tab"]/android.widget.TextView'
line_informasi_tab = '//android.view.ViewGroup[@content-desc="informasi_tab"]/android.view.ViewGroup'
title_manajer = 'entry_name_manajer'
title_company = 'entry_name_company'
title_bank = 'entry_name_bank_1'

#kalkulator tab
kalkulator_tab = '//android.view.ViewGroup[@content-desc="kalkulator_tab"]/android.widget.TextView'
line_kalkulator_tab = '//android.view.ViewGroup[@content-desc="informasi_tab"]/android.view.ViewGroup'
button_i = '//android.view.ViewGroup[@content-desc="kalkulator_button_informasi"]/android.widget.ImageView'
title_disclaimer = 'disclaimer_title'
button_close = '//android.view.ViewGroup[@content-desc="disclaimer_button_close"]/android.widget.ImageView'
default_number = 'kalkulator_input_value'
period_1_year = 'kalkulator_text_year_1'
period_3_year = 'kalkulator_text_year_3'
period_5_year = 'kalkulator_text_year_5'
product_value = 'kalkulator_entry_1_value'
deposito_value = 'kalkulator_entry_2_value'

#nonkyc
buttonBukaAccount = '//android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView'

#portfolio page
reksadana_btn_portfolio = '(//android.view.ViewGroup[@content-desc="PortPageSahamTab"])[2]'
reksadana_portfolio_text= '(//android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.TextView)[2]'
reksadana_portfolio_icon= '//android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.ImageView'
icon_popup = '//android.view.ViewGroup[3]/android.view.ViewGroup[1]/android.widget.TextView'
icon_popup_close_btn ='//android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.ImageView'
semua_tab = '//android.widget.ScrollView/android.view.ViewGroup/android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[1]'
pasar_uang = '//android.widget.ScrollView/android.view.ViewGroup/android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[2]'
saham_port_tab = '//android.widget.ScrollView/android.view.ViewGroup/android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[3]'
pendapatan_tab = '//android.widget.ScrollView/android.view.ViewGroup/android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[4]'
campuran_tab = '//android.widget.ScrollView/android.view.ViewGroup/android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[4]'
aperd_type='//android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.TextView[2]'
saham_tab_rek='(//android.view.ViewGroup[@content-desc="PortPageReksadanaTab"])[1]'
three_dots = '//android.view.ViewGroup[3]/android.view.ViewGroup[2]/android.widget.ImageView'
three_dot_pop = '//android.widget.TextView[1][@text="Simas Satu Prima"]'
three_dot_pop_jual = '//android.view.ViewGroup[2]/android.widget.TextView[@text="Jual"]'
three_dot_pop_tukar = '//android.view.ViewGroup[3]/android.widget.TextView[1][@text="Tukar"]'
three_pop_close = '(//android.view.ViewGroup[1]/android.widget.ImageView)[2]'
jual_pop = 'tittle_unit_Jual'
jual_pop_close = 'Button_close'
tukar_page_header = '//android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[1]'
port_down_arrow = '//android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[4]/android.widget.ImageView'
port_up_arrow = '//android.view.ViewGroup[3]/android.view.ViewGroup[5]/android.widget.ImageView'
port_topup = '//android.widget.TextView[@text="Top Up"]'
b_25_juta_btn = 'Bottomsheet_pilih_denom_25 juta'
topup_on_kamu = 'Bottomsheet_btn_beli'
saya_mengerti='ketentuan_unit_button_saya_mengerti'
konfirmasi_pemesanan_pilih='knfirmasi_pmesnan_text_2'
pilih_metode_transfer_bank='bottomsheet_name_bank'
knfirmasi_pmesnan_cek_box = 'knfirmasi_pmesnan_cek_box'
knfirmasi_pmesnan_button_bayar='knfirmasi_pmesnan_button_bayar'
knfirmasi_pmesnan_btn_close = 'knfirmasi_pmesnan_btn_close'
transaction_page = 'ReksadanaEnrty0Name'
port_mf_name = '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.TextView[1]'
sell_all_btn = 'Button_sell_all'
sell_btn = 'Button_jual2'
sell_conf_checkbox ='//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[5]/android.widget.ImageView'
sell_conf_btn = 'button_Confirm_sell'
warning_ok_btn = '//android.widget.TextView[@text="OK"]'
order_details_header = 'MFOderDetailsHeader'
pilih_produk ='//android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.widget.ImageView'
pilih_select = '//android.view.ViewGroup[3]/android.view.ViewGroup[1]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]'
tukar_semua = '//android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[5]'
investasi_sekarang = '//android.view.ViewGroup[4]/android.widget.TextView'


class ReksadanaPage(HomePage):
    @allure.step("open reksadana page")
    def open_reksadana_page(self,phone_number):
        self.sleep(4)
        self.click_mulai_sekarang()
        self.type_mobile_no(phone_number)
        self.click_selanjutnya()
        self.enter_otp(user_data['valid_otp'])
        self.enter_pin()
        self.verify_home_page_reg_user()
        
        
    @allure.step("Validate_text_reksadana")
    def Validate_text_reksadana(self): 
        self.click(reksadana)
        self.sleep(2)
        self.assert_equal(self.is_element_visible(reksadana), True)   
        self.sleep(1)
        self.assert_equal(self.get_attribute(Portfolio_reksadana, 'text'), 'Portfolio reksadana')
        
        
    @allure.step("validate_amount")
    def validate_amount(self):
        self.sleep(1)
        self.assert_equal(self.is_element_visible(total_amount), True)
        homepage_rp_with_rp = self.get_attribute(total_amount, 'text')
        homepage_rp_value = homepage_rp_with_rp[3:]
        self.assert_in(',', homepage_rp_value) 

    
    @allure.step("validate_refresh_functionality_for_reksadana_page")
    def validate_refresh_functionality_for_reksadana_page(self):
        self.scroll_down()
        self.assert_equal(self.is_element_visible(Portfolio_reksadana), True)
        self.assert_equal(self.get_attribute(Portfolio_reksadana, 'text'), 'Portfolio reksadana')
        self.sleep(2)
       

    @allure.step("validate_text_today")
    def validate_text_today(self):
        self.sleep(1)
        self.assert_equal(self.get_attribute(today, 'text'), '0(0%) Today')        


    @allure.step("Validate_Reopen_showing_saham_page")
    def Validate_Reopen_showing_saham_page(self):
      self.launch_app_again()
      self.login_and_verify_homepage_for_reg_user(user_data['reg_no_6'])
      self.sleep(2)
      self.assert_equal(self.get_attribute(saham, 'text'), 'Saham')
      self.sleep(2)
      self.click(reksadana)
      self.sleep(2)
      self.assert_equal(self.is_element_visible(reksadana), True)
      

    @allure.step("validate_refresh_for_reksadana_page_when_tab_other")
    def validate_refresh_for_reksadana_page_when_tab_other(self):
        self.click(transaction)
        self.sleep(2)
        self.click(profile)
        self.sleep(2)
        self.click(Home)
        self.sleep(2) 
        self.assert_equal(self.get_attribute(Portfolio_reksadana, 'text'), 'Portfolio reksadana')
                
    
    @allure.step("validate_pasar_uang_page")
    def validate_pasar_uang_page(self):
        self.sleep(1)
        self.assert_equal(self.get_attribute(Pasar_uang, 'text'), 'Pasar Uang')
        self.assert_equal(self.is_element_visible(icon_pasar_uang),True)
        self.click(Pasar_uang)   
        self.sleep(2)
        self.assert_equal(self.get_attribute(Pasar_uang_title, 'text'), 'PASAR UANG') 
        self.assert_equal(self.is_element_visible(product_pasar_uang),True)
        self.assert_equal(self.get_attribute(product_pasar_uang, 'text'), '3 Products')
        self.assert_equal(self.is_element_visible(title_product_pasar_uang_1),True)
        self.assert_equal(self.get_attribute(title_product_pasar_uang_1, 'text'), 'Danamas Rupiah Plus')
        self.assert_equal(self.is_element_visible(title_product_pasar_uang_2),True)
        self.assert_equal(self.get_attribute(title_product_pasar_uang_2, 'text'), 'Simas Kas Prima')
        self.assert_equal(self.is_element_visible(title_product_pasar_uang_3),True)
        self.assert_equal(self.get_attribute(title_product_pasar_uang_3, 'text'), 'Danamas Rupiah')
        Pasar_uang_amount = self.get_attribute(Pasar_uang_value_amount, "text")
        Pasar_uang_value = Pasar_uang_amount[:]
        Pasar_uang_Aum = self.get_attribute(Pasar_uang_value_Aum, "text")
        Pasar_uang_Percentage = self.get_attribute(Pasar_uang_value_Percentage, "text")
        Pasar_uang_Date = self.get_attribute(Pasar_uang_value_Date, "text")
        self.assert_equal(self.is_element_visible(back_btn_pasar_uang),True)
        self.click(product_pasar_uang_1)
        self.sleep(2)
        self.assert_equal(self.is_element_visible(title_rdp_psr_uang),True)
        self.assert_equal(self.get_attribute(title_rdp_psr_uang, 'text'), 'Danamas Rupiah Plus')
        rdp_psr_uang_amount = self.get_attribute(rdp_psr_uang_value_amount, "text")
        rdp_psr_uang_value= rdp_psr_uang_amount[:]
        self.click(back_btn_rdp)
        self.sleep(2)
        self.assert_equal(self.get_attribute(Pasar_uang_title, 'text'), 'PASAR UANG')
        self.click(back_btn_pasar_uang)
        self.sleep(2)
        self.assert_equal(self.get_attribute(Portfolio_reksadana, 'text'), 'Portfolio reksadana')

    
    @allure.step("click_list_product_mf1")
    def click_list_product_mf1(self):
        self.click(list_product_mf1)
        self.sleep(1)

    @allure.step("validate_RDP")
    def validate_RDP(self): 
        self.assert_equal(self.is_element_visible(btn_beli),True)
        self.assert_equal(self.get_attribute(btn_beli, 'text'), 'BELI')
        self.click(back_btn_rdp)
        self.sleep(3)      
        self.assert_equal(self.get_attribute(Portfolio_reksadana, 'text'), 'Portfolio reksadana')
        self.click(list_product_mf1) 
        self.sleep(3)
        self.assert_equal(self.is_element_visible(btn_beli),True)
        self.driver.back()
        self.sleep(3)      
        self.assert_equal(self.get_attribute(Portfolio_reksadana, 'text'), 'Portfolio reksadana')
        
    @allure.step("validate_pendapatan_tetap_page")
    def validate_pendapatan_tetap_page(self): 
        self.assert_equal(self.is_element_visible(icon_pendapatan_tetap),True)
        self.assert_equal(self.get_attribute(Pendapatan_Tetap, 'text'), 'Pendapatan Tetap')
        self.click(Pendapatan_Tetap)
        self.sleep(3)
        self.assert_equal(self.get_attribute(Pendapatan_tetap_title, 'text'), 'PENDAPATAN TETAP') 
        self.assert_equal(self.is_element_visible(product_pendapatan_tetap),True)
        self.assert_equal(self.get_attribute(product_pendapatan_tetap, 'text'), '5 Products')
        self.assert_equal(self.is_element_visible(back_btn_pendapatan_tetap),True)
        self.click(back_btn_pendapatan_tetap)
        self.sleep(3)
       
    @allure.step("validate_saham_page")
    def validate_saham_page(self): 
        self.assert_equal(self.is_element_visible(icon_saham),True)
        self.assert_equal(self.get_attribute(Saham, 'text'), 'Saham')
        self.click(Saham)
        self.sleep(3)
        self.assert_equal(self.get_attribute(Saham_title, 'text'), 'SAHAM') 
        self.assert_equal(self.is_element_visible(product_saham),True)
        self.assert_equal(self.get_attribute(product_saham, 'text'), '6 Products')
        self.assert_equal(self.is_element_visible(back_btn_saham),True)
        self.click(back_btn_saham)
        self.sleep(3)
        
    @allure.step("validate_campuran_page")
    def validate_campuran_page(self): 
        self.assert_equal(self.is_element_visible(icon_campuran),True)
        self.assert_equal(self.get_attribute(Campuran, 'text'), 'Campuran')
        self.click(Campuran)
        self.sleep(3)
        self.assert_equal(self.get_attribute(Campuran_title, 'text'), 'CAMPURAN') 
        self.assert_equal(self.is_element_visible(product_campuran),True)
        self.assert_equal(self.get_attribute(product_campuran, 'text'), '4 Products')
        self.assert_equal(self.is_element_visible(back_btn_campuran),True)
        self.click(back_btn_campuran)
        self.sleep(3)
        
    @allure.step("validate_half_card")
    def validate_half_card(self): 
        self.assert_equal(self.get_attribute(top_reksadana_title, 'text'), 'Top Reksadana')
        self.assert_equal(self.is_element_visible(icon_i),True)
        self.click(icon_i)
        self.sleep(3)
        self.assert_equal(self.get_attribute(half_card_title, 'text'), 'Top Reksadana') 
        self.assert_equal(self.is_element_visible(half_card_subtitle),True)
        self.assert_equal(self.get_attribute(half_card_subtitle, 'text'), 'Informasi Reksa Dana adalah berdasarkan kinerja pergerakan NAV per unit reksa dana sejak awal tahun (YTD)') 
        self.assert_equal(self.is_element_visible(half_card_btn_close),True)
        self.click(half_card_btn_close)
        self.assert_equal(self.is_element_visible(half_card_subtitle),False)
        self.click(icon_i)
        self.sleep(2)
        self.driver.back()
        self.assert_equal(self.is_element_visible(half_card_subtitle),False)
        self.sleep(3)
        
    @allure.step("scroll down mf")
    def scroll_down_mf(self):
        self.scroll_screen(start_x=206, start_y=449, end_x=534, end_y=404, duration=10000)
        self.sleep(2)
    
    @allure.step("scroll up mf")
    def scroll_up_mf(self):
        self.scroll_screen(start_x=258, start_y=558, end_x=465, end_y=1700, duration=10000)
        self.sleep(2)    
           
    
    @allure.step("validate_list_mutual_fund")
    def validate_list_mutual_fund(self):
        self.assert_equal(self.is_element_visible(list_product_mf1), True)
        self.assert_equal(self.is_element_visible(logo_product_mf1), True)
        self.assert_equal(self.is_element_visible(list_product_mf2), True)
        self.assert_equal(self.is_element_visible(list_product_mf3), True)
        self.scroll_up_mf()
        page_no_scroll= self.is_element_visible(logo_product_mf3)
        if page_no_scroll == True:      
         self.assert_equal(self.is_element_visible(logo_product_mf3), True)
         self.scroll_up_mf()
         self.assert_equal(self.is_element_visible(list_product_mf4), True)
         self.assert_equal(self.is_element_visible(logo_product_mf4), True)
         self.assert_equal(self.is_element_visible(list_product_mf5), True)
         self.scroll_up()
         self.assert_equal(self.is_element_visible(logo_product_mf5), True)
         self.scroll_up()
         self.assert_equal(self.is_element_visible(list_product_mf7), True)
         self.scroll_up()
         self.assert_equal(self.is_element_visible(logo_product_mf8), True)
         self.assert_equal(self.is_element_visible(list_product_mf10), True)
         self.assert_equal(self.is_element_visible(logo_product_mf10), True)
        else:
         self.assert_equal(self.is_element_visible(logo_product_mf1), True)    
       
    @allure.step("validate_return_mutual_fund")
    def validate_return_mutual_fund(self): 
        self.assert_equal(self.is_element_visible(return_1Y_mf),True)
        self.sleep(2)
    
    @allure.step("click_list_product_mf2")
    def click_list_product_mf2(self):
        self.click(list_product_mf2)
        self.sleep(1)
        self.assert_equal(self.is_element_visible(text_title_rdp),True)
        self.click(back_btn_rdp)
        self.sleep(3)      
        self.assert_equal(self.get_attribute(Portfolio_reksadana, 'text'), 'Portfolio reksadana')
        self.click(list_product_mf2)
        self.sleep(3)
        self.assert_equal(self.is_element_visible(text_title_rdp),True)
        self.driver.back()
        self.sleep(3)      
        self.assert_equal(self.get_attribute(Portfolio_reksadana, 'text'), 'Portfolio reksadana')
    
    @allure.step("scroll up homepage")
    def scroll_up_homepage(self):
        self.scroll_screen(start_x=470, start_y=1176, end_x=439, end_y=796, duration=10000)
        self.sleep(2)   
     
    @allure.step("scroll up homepage")
    def scroll_up_homepage_2(self):
        self.scroll_screen(start_x=382, start_y=1891, end_x=558, end_y=630, duration=10000)
        self.sleep(2)  
     
    @allure.step("mathematical validation on homepage")
    def mathematical_validation_on_homepage(self):
        self.click(reksadana)
        self.sleep(2)
        self.assert_equal(self.is_element_visible(reksadana), True)   
        self.sleep(1)
        self.assert_equal(self.get_attribute(Portfolio_reksadana, 'text'), 'Portfolio reksadana')
        
        current_price = self.get_attribute(total_amount, 'text')
        current_percentage = self.get_attribute(today, 'text')
        current_percentage_return = self.get_attribute(return_percentage, 'text')
        
        c = '('
        index = current_price.find(c)
        resposnePrice = (current_price[:])
        
        d = current_percentage.find('%')
        response_percentage = (current_percentage[2:d])
        
        e = current_percentage_return.find('%')
        response_return_percentage = (current_percentage_return[0:e])
        
        self.scroll_up_homepage()
        self.scroll_up_homepage_2()
        
        current_percentage_return_4 = self.get_attribute(return_percentage_4, 'text')
        e = current_percentage_return_4.find('%')
        response_return_percentage_4 = (current_percentage_return_4[0:e])
        
        current_percentage_return_10 = self.get_attribute(return_percentage_10, 'text')
        e = current_percentage_return_10.find('%')
        response_return_percentage_10 = (current_percentage_return_10[0:e])
        
        logger.info(current_price)
        logger.info(current_percentage)
        logger.info(current_percentage_return)
        logger.info(current_percentage_return_10)
        
        logger.info(f'resposnePrice {resposnePrice}')
        logger.info(f'response_percentage_today {response_percentage}')
        logger.info(f'response_percentage_max {response_return_percentage}')
        logger.info(f'response_percentage_midle {response_return_percentage_4}')
        logger.info(f'response_percentage_min {response_return_percentage_10}')
        

    @allure.step("validate the data with api and app ui")
    def validate_data_with_api_and_ui(self):
        self.click(reksadana)
        self.sleep(2)
        self.assert_equal(self.is_element_visible(reksadana), True)
        
        saldo_reksadana_with_rp = (self.get_attribute(total_amount, 'text')).replace(',', '')
        saldo_reksadana_value =  str(saldo_reksadana_with_rp[3:])
        amount_invested_value = (saldo_reksadana_value [:8])
        logger.info(saldo_reksadana_value)
        logger.info(amount_invested_value)
        
        category_value= self.get_attribute(Campuran, 'text')
        logger.info(category_value)
        
        token_value = self.login_with_a_number(user_data['reg_no_7'])
        token = {
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJidlJnbGsyVDB3cWhxQ3U0Mm1OOGsyVEZmMFIwc2I0MyIsInN1YiI6IlNpbWFzSW52ZXN0In0.IBV4PRj9HG9TCm6lVNXmkgbsA9a43ngRIlDZ4o4rNdY"}
        token['Authorization'] = 'Bearer ' + token_value
        reksadana_homepage_api = request_utilities.get(base_url='https://stg-api.siminvest.co.id/',endpoint=f"api/v1/users/auth/fund/portfoliov3/{user_data['reg_no_7']}", headers=token, expected_status_code=200)
        
        for i in range(len(reksadana_homepage_api['accounts'])):
            saldo_value_api = reksadana_homepage_api['accounts'][i]['balance']
            saldo_api= str(saldo_value_api)
            logger.info(saldo_value_api)
            self.assert_equal(saldo_api, saldo_reksadana_value)
            
            amount_invested_api = reksadana_homepage_api['accounts'][i]['amount_invested']
            amount_invested_value_api= str( amount_invested_api)
            logger.info(amount_invested_value_api)
            self.assert_equal(amount_invested_value_api, amount_invested_value)
            
            category_name_api = str(reksadana_homepage_api['accounts'][i]['investments']['mixed'][i]['category'])
            self.assert_equal(category_name_api, category_value)
            logger.info(category_name_api)
            
    @allure.step("Validate_title_rdp")
    def Validate_title_rdp(self): 
        self.click(reksadana)
        self.sleep(3)
        self.assert_equal(self.is_element_visible(reksadana), True)
        self.assert_equal(self.get_attribute(Portfolio_reksadana, 'text'), 'Portfolio reksadana')
        
        title_mf_homepage = self.get_attribute(title_mf_1, 'text')
        self.click(list_product_mf1)
        self.sleep(2)
        title_mf_rdp = self.get_attribute(text_title_rdp, 'text')
        self.assert_equal(title_mf_homepage, title_mf_rdp)
    
    @allure.step("scroll up RDP")
    def scroll_up_RDP(self):
        self.scroll_screen(start_x=537, start_y=1514, end_x=610, end_y=486, duration=10000)
        self.sleep(2)
      
    @allure.step("validate_ringkasan_tab")
    def validate_ringkasan_tab(self):
        self.scroll_up_RDP()
        self.sleep(2)
        self.assert_equal(self.is_element_visible(ringkasan_tab), True)
        self.assert_equal(self.get_attribute(ringkasan_tab, 'text'), 'RINGKASAN')
        self.assert_equal(self.is_element_visible(default_line), True)
        
        min_initial_purchase_value = self.get_attribute(min_initial_purchase, 'text')
        logger.info(min_initial_purchase_value)
        min_resale_price_value = self.get_attribute(min_resale_price, 'text')
        logger.info( min_resale_price_value)
        
        self.assert_equal(self.is_element_visible(button_prospektus), True)
        self.click(button_prospektus)
        self.sleep(2)
        self.driver.back()
        self.sleep(2)
        title_mf_rdp = self.get_attribute(text_title_rdp, 'text')
        logger.info(title_mf_rdp)
        self.scroll_up_RDP()
        self.sleep(2)
        
        self.assert_equal(self.is_element_visible(button_fact_sheet), True)
        self.click(button_fact_sheet)
        self.sleep(2)
        self.driver.back()
        self.sleep(2)
        title_mf_rdp = self.get_attribute(text_title_rdp, 'text')
        logger.info(title_mf_rdp)
        self.scroll_up_RDP()
        self.sleep(2)

    @allure.step("validate_half_card_rdp")
    def validate_half_card_rdp(self):
        self.click(btn_beli)
        self.sleep(2)
        self.assert_equal(self.is_element_visible(alert_header), True)
        self.assert_equal(self.get_attribute(alert_header, 'text'), 'Tingkat resiko tidak sesuai')
        self.click(button_batal)
        self.sleep(1)
        
    @allure.step("validate_button_on_rdp")
    def validate_button_on_rdp(self):
        self.driver.back()
        self.sleep(2)
        
        self.scroll_up_homepage()
        self.scroll_up_homepage_2()
        
        self.click(list_product_mf3)
        self.sleep(2)
        self.assert_equal(self.is_element_visible(button_top_up_rdp), True)
        self.assert_equal(self.is_element_visible(button_buy_rdp), True)
         
    
    @allure.step("validate_button_buka_account_reksadana")
    def validate_button_buka_account_reksadana(self): 
        self.click(reksadana)
        self.sleep(3)
        self.click(list_product_mf1)
        self.sleep(2)
        self.assert_equal(self.get_attribute(buttonBukaAccount, 'text'), 'Buka Akun Reksadana')
    
    @allure.step("validate_informasi_tab")
    def validate_informasi_tab(self):
        self.driver.back()
        self.sleep(2)
        self.click(list_product_mf1)
        self.sleep(3)
        self.click(informasi_tab)
        self.sleep(2)
        self.assert_equal(self.get_attribute(informasi_tab, 'text'), 'INFORMASI')
        self.assert_equal(self.is_element_visible(line_informasi_tab), True)
        self.scroll_up_RDP()
        self.assert_equal(self.is_element_visible(title_manajer), True)
        self.assert_equal(self.is_element_visible(title_company), True)
        self.assert_equal(self.is_element_visible(title_bank), True)
      
    @allure.step("validate_kalkulator_tab")
    def validate_kalkulator_tab(self):
        self.click(kalkulator_tab)
        self.sleep(2)
        self.assert_equal(self.get_attribute(kalkulator_tab, 'text'), 'KALKULATOR')
        self.assert_equal(self.is_element_visible(line_kalkulator_tab), True)
        self.click(button_i)
        self.sleep(2)
        
        self.assert_equal(self.get_attribute(title_disclaimer, 'text'), 'Disclaimer')
        self.assert_equal(self.is_element_visible(button_close), True)
        self.click(button_close)
        self.assert_equal(self.is_element_visible(button_i), True)
        self.assert_equal(self.get_attribute(default_number, 'text'), '0')
        
        max_number = '123456789'
        self.update_text(default_number, max_number)
        amount_max_value= (self.get_attribute(default_number, 'text'),  max_number[:9])
        logger.info(amount_max_value)
        self.sleep(1)
        
        min_number = '1'
        self.update_text(default_number, min_number)
        amount_min_value= (self.get_attribute(default_number, 'text'), min_number[:1])
        logger.info(amount_min_value)
        
        self.click(period_1_year)
        self.sleep(1)
        self.assert_equal(self.is_element_visible(product_value), True)
        
        self.click(period_3_year)
        self.sleep(1)
        self.assert_equal(self.is_element_visible(product_value), True)
        
        self.click(period_5_year)
        self.sleep(1)
        self.assert_equal(self.is_element_visible(deposito_value), True)
        
        input_amount = '20400'
        self.update_text(default_number, input_amount)
        self.click(period_1_year)
        self.sleep(1)
        amount_product_value= self.get_attribute(product_value, 'text')
        logger.info(amount_product_value)
        amount_deposito_value= self.get_attribute(deposito_value, 'text')
        logger.info(amount_deposito_value)
        
        self.click(informasi_tab)
        self.click(kalkulator_tab)
        self.sleep(2)
        self.assert_equal(self.get_attribute(default_number, 'text'), '0')

    @allure.step("click on reksadana tab on portfolio page")
    def click_on_reksadana_tab_on_portfolio_page(self):
        self.click(reksadana_btn_portfolio)
        self.sleep(2)

    @allure.step("validate mf type")
    def validate_mf_type(self, type):
        try:
            for i in range(3, 5):
                self.assert_equal(self.get_attribute(f'//android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[{i}]/android.widget.TextView[2]','text'), type)
        except NoSuchElementException as E:
            pass


    @allure.step("Validate redirection and functional flow for reksadana tab on portoflio")
    def validate_redirection_and_functional_flow_for_reksadana_tab_on_portoflio(self):
        self.assert_equal(self.is_element_visible(reksadana_portfolio_text), True)
        self.click(reksadana_portfolio_icon)
        self.assert_equal(self.get_attribute(icon_popup, 'text'), 'Portfolio NAV Update')
        self.go_back()
        self.sleep(1)
        self.click(reksadana_portfolio_icon)
        self.assert_equal(self.get_attribute(icon_popup, 'text'), 'Portfolio NAV Update')
        self.go_back()
        self.click(pasar_uang)
        self.sleep(1)
        self.validate_mf_type('Pasar Uang')
        self.click(saham_port_tab)
        self.sleep(1)
        self.validate_mf_type('Saham')
        self.click(pendapatan_tab)
        self.sleep(1)
        self.validate_mf_type('Pendapatan Tetap')
        self.scroll_with_two_element(semua_tab,pendapatan_tab)
        self.sleep(1)
        self.click(campuran_tab)
        self.sleep(1)
        self.validate_mf_type('Campuran')
        self.click(saham_tab_rek)
        self.sleep(2)
        self.click(reksadana_btn_portfolio)
        self.sleep(1)
        self.click(three_dots)
        self.sleep(1)
        self.assert_equal(self.is_element_visible(three_dot_pop), True)
        self.assert_equal(self.is_element_visible(three_dot_pop_jual), True)
        self.assert_equal(self.is_element_visible(three_dot_pop_tukar), True)
        self.click(three_pop_close)
        self.sleep(1)
        #self.assert_equal(self.is_element_visible(three_dot_pop), True)
        self.click(three_dots)
        self.sleep(1)
        self.click(three_dot_pop_jual)
        self.assert_equal(self.is_element_visible(jual_pop), True)
        self.click(jual_pop_close)
        self.click(three_dots)
        self.click(three_dot_pop_tukar)
        self.assert_equal(self.is_element_visible(tukar_page_header), True)
        self.go_back()
        self.sleep(1)
        self.assert_equal(self.is_element_visible(semua_tab), True)
        self.click(port_down_arrow)
        for i in range(7,14,2):
            self.assert_equal(self.is_element_visible(f'//android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.TextView[{i}]'), True)
        self.click(port_up_arrow)
        self.assert_equal(self.is_element_visible('//android.widget.TextView[@text="NAV"]'), False)
        self.click(port_topup)
        self.sleep(2)
        self.assert_equal(self.is_element_visible(title_rdp_psr_uang), True)
        self.go_back()
        self.sleep(2)
        self.small_scroll_down()
        self.assert_equal(self.is_element_visible(pasar_uang), True)

    @allure.step("Top up process")
    def top_up_process(self):
        port_mf_name_text = self.get_attribute(port_mf_name, 'text')
        self.click(port_topup)
        self.sleep(3)
        self.click(btn_beli)
        self.sleep(2)
        if self.is_element_visible('//android.widget.TextView[@text="Lanjutkan"]') == True:
            self.click('//android.widget.TextView[@text="Lanjutkan"]')
            self.sleep(1)
            self.click(b_25_juta_btn)
            self.click(topup_on_kamu)
            self.click(saya_mengerti)
            self.click(konfirmasi_pemesanan_pilih)
            self.click(pilih_metode_transfer_bank)
            self.click(knfirmasi_pmesnan_cek_box)
            self.click(knfirmasi_pmesnan_button_bayar)
            self.click(knfirmasi_pmesnan_btn_close)
            self.assert_equal(self.get_attribute(transaction_page,'text'), port_mf_name_text.upper())
        else:
            self.click(b_25_juta_btn)
            self.click(topup_on_kamu)
            self.click(saya_mengerti)
            self.click(konfirmasi_pemesanan_pilih)
            self.click(pilih_metode_transfer_bank)
            self.click(knfirmasi_pmesnan_cek_box)
            self.click(knfirmasi_pmesnan_button_bayar)
            self.click(knfirmasi_pmesnan_btn_close)
            self.assert_equal(self.get_attribute(transaction_page, 'text'), port_mf_name_text.upper())

    @allure.step("Jual Process")
    def jual_process(self):
        self.click(three_dots)
        self.click(three_dot_pop_jual)
        self.click(sell_all_btn)
        self.click(sell_btn)
        self.click(sell_conf_checkbox)
        self.click(sell_btn)
        self.click(sell_conf_btn)
        self.click(warning_ok_btn)
        self.assert_equal(self.is_element_visible(order_details_header), True)
        self.go_back()
        self.sleep(1)
        self.go_back()

    @allure.step("Tukar process")
    def tukar_process(self):
        self.click(three_dots)
        self.click(three_dot_pop_tukar)
        self.click(pilih_produk)
        self.click(pilih_select)
        self.click(tukar_semua)
        self.go_back()
    @allure.step("click on pasar uang")
    def click_on_pasar_uang(self):
        self.click(pasar_uang)
        self.sleep(2)

    @allure.step("click on saham")
    def click_on_saham(self):
        self.click(saham_port_tab)

    @allure.step("click on Pendapatan Tetap")
    def click_on_Pendapatan_Tetap(self):
        self.click(pendapatan_tab)

    @allure.step("validate non transaction user ui for port")
    def validate_non_transaction_user_ui_for_port(self):
        self.assert_equal(self.is_element_visible(investasi_sekarang), True)
        self.click(investasi_sekarang)
        self.sleep(2)
        self.assert_equal(self.is_element_visible(Pasar_uang), True)




























