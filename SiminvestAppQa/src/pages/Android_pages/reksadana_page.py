import json

from appiumbase import BaseCase
from SiminvestAppQa.src.pages.Android_pages.login_page import LoginPage
from SiminvestAppQa.src.pages.Android_pages.home_page import HomePage
import logging as logger
import allure
from SiminvestAppQa.src.data.userData import user_data
from SiminvestAppQa.src.utilities.requestUtilities import RequestsUtilities
from datetime import datetime,date,timedelta

request_utilities = RequestsUtilities()
# reksadana homepage Locators
reksadana ="//android.widget.TextView[@text='Reksadana']"
Portfolio_reksadana ='(//android.view.ViewGroup/android.view.ViewGroup[7]/android.widget.TextView[1])[1]'
total_amount='//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[7]/android.widget.TextView[2]'
percentage_today ='//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[7]/android.widget.TextView[3]'
transaction ="//android.widget.TextView[@text='Transaction']"
saham ="//android.widget.TextView[@text='Saham']"
saham_tab = '//android.widget.TextView[@content-desc="Saham_tab"]'
Home = '//android.widget.TextView[@text="Home"]'
profile = '//android.widget.TextView[@text="Profile"]'
today = '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[7]/android.widget.TextView[3]'
Pasar_uang = '//android.widget.TextView[@content-desc="reksadana_pasarUang_text1"]'
icon_pasar_uang = '//android.widget.ImageView[@content-desc="reksadana_pasarUang_Image1"]'
Pasar_uang_title = '//android.widget.TextView[@content-desc="reksadana_psruang_tittle"]'
back_btn_pasar_uang = '//android.view.ViewGroup[@content-desc="reksadana_psruang_backbutton"]/android.widget.ImageView'
product_pasar_uang = '//android.widget.TextView[@content-desc="reksadana_psruang_subtitle"]'
title_product_pasar_uang_1 = '(//android.widget.TextView[@content-desc="reksadana_psruang_entry_1_text"])[1]'
title_product_pasar_uang_2 = '(//android.widget.TextView[@content-desc="reksadana_psruang_entry_1_text"])[2]'
title_product_pasar_uang_3 = '(//android.widget.TextView[@content-desc="reksadana_psruang_entry_1_text"])[3]'


btn_beli = '//android.view.ViewGroup[@content-desc="button_beli"]/android.widget.TextView'
back_btn_rdp = '//android.view.ViewGroup[@content-desc="back_button"]/android.widget.ImageView'
product_pasar_uang_1 = '(//android.widget.TextView[@content-desc="reksadana_psruang_entry_1_text"])[1]'
btn_beli_psr_uang = '//android.view.ViewGroup[@content-desc="button_beli"]/android.widget.TextView'
icon_pendapatan_tetap = '//android.widget.ImageView[@content-desc="reksadana_PendapatanTtp_Image1"]'
Pendapatan_Tetap = '//android.widget.TextView[@content-desc="reksadana_PendapatanTtp_text1"]'
Pendapatan_tetap_title = '//android.widget.TextView[@content-desc="reksadana_pndptn_tetap_title"]'
product_pendapatan_tetap = '//android.widget.TextView[@content-desc="reksadana_pndptn_tetap_subtitle"]'
back_btn_pendapatan_tetap = '//android.view.ViewGroup[@content-desc="reksadana_pndptn_tetap_backbtn"]/android.widget.ImageView'
icon_saham = '//android.widget.ImageView[@content-desc="reksadana_saham_Image1"]'
Saham = '//android.widget.TextView[@content-desc="reksadana_saham_tetx1"]'
Saham_title = '//android.widget.TextView[@content-desc="reksadana_saham_tittle"]'
product_saham = '//android.widget.TextView[@content-desc="reksadana_saham_subtitle"]'
back_btn_saham = '//android.view.ViewGroup[@content-desc="reksadana_saham_backbutton"]/android.widget.ImageView'
icon_campuran = '//android.widget.ImageView[@content-desc="reksadana_Campuran_Image1"]'
Campuran = '//android.widget.TextView[@content-desc="reksadana_Campuran_text1"]'
Campuran_title = '//android.widget.TextView[@content-desc="reksadana_campuran_Title"]'
product_campuran = '//android.widget.TextView[@content-desc="reksadana_campuran_subtitle"]'
back_btn_campuran = '//android.view.ViewGroup[@content-desc="reksadana_campuran_backbtn"]/android.widget.ImageView'
top_reksadana_title= '//android.view.ViewGroup[@content-desc="Top_reksadana_title1"]/android.widget.TextView'
icon_i = '//android.view.ViewGroup[@content-desc="Top_reksadana_title1"]/android.widget.ImageView'
half_card_title = '//android.widget.TextView[@content-desc="top_reksadana_title"]'
half_card_subtitle = '//android.widget.TextView[@content-desc="top_reksadana_subtitle"]'
half_card_btn_close = '//android.view.ViewGroup[@content-desc="top_reksadana_btn_close"]/android.widget.ImageView'

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
        
        
    @allure.step("luanch app again")
    def launch_app_again(self):
      self.launch()

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

        self.assert_equal(self.is_element_visible(back_btn_pasar_uang),True)
        self.click(product_pasar_uang_1)
        self.sleep(2)
        self.assert_equal(self.is_element_visible(btn_beli_psr_uang),True)
        self.assert_equal(self.get_attribute(btn_beli_psr_uang, 'text'), 'BELI')
        self.click(back_btn_rdp)
        self.sleep(2)
        self.assert_equal(self.get_attribute(Pasar_uang_title, 'text'), 'PASAR UANG')
        self.click(back_btn_pasar_uang)
        self.sleep(2)
        self.assert_equal(self.get_attribute(Portfolio_reksadana, 'text'), 'Portfolio reksadana')
  
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