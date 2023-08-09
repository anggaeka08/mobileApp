from SiminvestAppQa.src.pages.Android_pages.home_page import HomePage
from SiminvestAppQa.src.data.userData import user_data
import allure
import logging as logger
from SiminvestAppQa.src.utilities.requestUtilities import RequestsUtilities
from datetime import datetime,date,timedelta

Star_point_txt =  'HomeStarPointText'
Star_point_value = 'HomepageStarPointValue'
starpoint_icon1 = 'starPoint_icon_1_1'

About_startpoint = '//android.view.ViewGroup[@content-desc="starPoint_text_1_1"]/android.widget.TextView[1]'
txt_1_swp1= '//android.view.ViewGroup[@content-desc="starPoint_text_1_1"]/android.widget.TextView[2]'
txt_2_swp1 = 'starPoint_text_2_1'
txt_3_swp1 = 'starPoint_text_3_1'
txt_4_swp1 = 'starPoint_text_4_1'
btn_mulai = 'starPoint_start_btn_text'
for_swipe1 = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup'
for_swipe1_icon = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.ImageView[2]'
starpoint_icon2 = 'starPoint_icon_1_2'
txt_1_swp2 = '//android.view.ViewGroup[@content-desc="starPoint_text_1_2"]/android.widget.TextView'
txt_2_swp2 = 'starPoint_text_2_2'
starpoint_icon3 = 'starPoint_icon_1_3'
txt_1_swp3 = '//android.view.ViewGroup[@content-desc="starPoint_text_1_3"]/android.widget.TextView'
txt_2_swp3 ='starPoint_text_2_3'
starpoint_icon4 = 'starPoint_icon_1_4'
txt_1_swp4 = '//android.view.ViewGroup[@content-desc="starPoint_text_1_4"]/android.widget.TextView[1]'
txt_1_swip4 = 'starPoint_text_2_4'
starpoint_icon5 = 'starPoint_icon_1_5'
txt_1_swp5 = '//android.view.ViewGroup[@content-desc="starPoint_text_1_5"]/android.widget.TextView[1]'
txt_2_swp5 = '//android.view.ViewGroup[@content-desc="starPoint_text_1_5"]/android.widget.TextView[2]'
txt_3_swp5 = 'starPoint_text_2_5'
starpoint_icon6 = 'starPoint_icon_1_6'
txt_1_swp6 = '//android.view.ViewGroup[@content-desc="starPoint_text_1_6"]/android.widget.TextView'
txt_2_swp6 = 'starPoint_text_2_6'

#after Submit data starpoint

Syarat_dan_Ketentuan_txt = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.TextView'
Agreement_txt = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView'
checklist = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ImageView'
btn_submit_TC = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]'

#3 Dot when klik

Tri_dot = '//android.view.ViewGroup[@content-desc="StarPoin_menu"]/android.widget.ImageView'
Term_cond_Work1 = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[1]/android.view.ViewGroup[2]'
Term_cond_txt1 = '//android.view.View[@content-desc="Home"]/android.widget.TextView' #Home
Term_cond_txt2 =  '//android.view.View[@content-desc="Program & Promo"]/android.widget.TextView' #Program & Promo
Term_cond_txt3 = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View[1]/android.view.View[1]'
back_btn2 = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.ImageView'


#dashboard starpoint


back_btn = 'StarPoin_backbtn'
kotak_starpoin = '//android.view.ViewGroup[@content-desc="StarPoin_value_area"]/android.widget.ImageView[2]'
starpoint_saya ='StarPoin_saya'
startpoint_value2 = 'StarPoin_value'
starpoint_riwayat_btn = 'StarPoin_riwayat_icon'
riwayat_text = 'StarPoin_riwayat_text'
tukar_btn = 'StarPoin_tukar_icon'
tukar_txt = 'StarPoin_tukar_text'
riwayat_simInvest = 'StarPoin_riwayat_di'
empty_history_txt = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[2]'
icon_empty_hitory = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.ScrollView/android.view.ViewGroup/android.widget.ImageView'

#Showing on Dashboard StarPoint
btn_tukar = '//android.view.ViewGroup[@content-desc="StarPoin_tukar_icon"]/android.view.ViewGroup'
btn_riwayat = '//android.view.ViewGroup[@content-desc="StarPoin_riwayat_icon"]/android.view.ViewGroup'
entry_txt1 = 'StarPoin_entry_1_text'
entry_txt2 = 'StarPoin_entry_2_text'
entry_txt3 = 'StarPoin_entry_3_text'
entry_txt5 = 'StarPoin_entry_3_text'
date_format1 = 'StarPoin_entry_1_date'
date_format2 = 'StarPoin_entry_2_date'
date_format3 = 'StarPoin_entry_3_date'
date_format4 = 'StarPoin_entry_4_date'
date_format5 = 'StarPoin_entry_5_date'
icon_image_homestar1 = '//android.view.ViewGroup[@content-desc="StarPoin_entry_1"]/android.view.ViewGroup'
icon_image_homestar2 = '//android.view.ViewGroup[@content-desc="StarPoin_entry_2"]/android.view.ViewGroup'
icon_image_homestar3 = '//android.view.ViewGroup[@content-desc="StarPoin_entry_3"]/android.view.ViewGroup'
icon_image_homestar5 = '//android.view.ViewGroup[@content-desc="StarPoin_entry_5"]/android.view.ViewGroup'
starpoin_entry_value1= 'StarPoin_entry_1_value'
starpoin_status1= 'StarPoin_entry_1_status'
starpoin_entry_value2= 'StarPoin_entry_2_value'
starpoin_status2 = 'StarPoin_entry_2_status'
starpoin_entry_value3 = 'StarPoin_entry_3_value'
starpoin_status3= 'StarPoin_entry_3_status'
starpoin_entry_value4 = 'StarPoin_entry_4_value'
starpoin_status4 = 'StarPoin_entry_4_status'

#When click riwayat

back_riwayat_btn= 'riwayat_back'
riwayat_page = 'riwayat_header'
riwayat1 = 'riwayat_entry_1'
riwayat24 = 'riwayat_entry_24'
riwayat25 = 'riwayat_entry_25'
icon_image_riwayat1 = '//android.view.ViewGroup[@content-desc="riwayat_entry_1"]/android.view.ViewGroup'
icon_image_riwayat2 = '//android.view.ViewGroup[@content-desc="riwayat_entry_2"]/android.view.ViewGroup'
riwayat_date_entry = 'riwayat_entry_1_date'
riwayat_entry1 = 'riwayat_entry_1_text'
riwayat_entry_value1 = 'riwayat_entry_1_value'
riwayat_status1 = 'riwayat_entry_1_status'
riwayat_date_entry2 = 'riwayat_entry_2_date'
riwayat_entry2 = 'riwayat_entry_2_text'
riwayat_entry4 = 'riwayat_entry_4_text'
riwayat_entry3 = 'riwayat_entry_3_text'
riwayat_entry5 = 'riwayat_entry_5_text'
riwayat_entry6 = 'riwayat_entry_6_text'
riwayat_entry7 = 'riwayat_entry_7_text'
riwayat_entry8 = 'riwayat_entry_8_text'
riwayat_entry9 = 'riwayat_entry_9_text'
riwayat_entry10 = 'riwayat_entry_10_text'
riwayat_entry15 = 'riwayat_entry_15_text'
riwayat_entry18 = 'riwayat_entry_18_text'
riwayat_entry22 = 'riwayat_entry_22_text'
riwayat_entry25 = 'riwayat_entry_25_text'

riwayat_entry_value2 = 'riwayat_entry_2_value'
riwayat_status2 = 'riwayat_entry_2_status'

#when click Tukar

back_tukar_btn = 'tukar_back'
tukar_icon = 'tukar_icon'
tukar_txt1 = 'tukar_text_1'
tukar_value1 = 'tukar_value'
tukar_txt2 = 'tukar_text_2'
tukar_txt4= 'tukar_text_4'



class StarPointPage(HomePage):
     
   @allure.step("Open StarPoint page")
   def click_on_back_btn_on_page(self):
      self.click(back_btn) 
    
   @allure.step("verify Starpoint page")
   def verify_starpoint_page(self):
      self.sleep(2)
      starpoint_page_header_text = self.get_attribute(Star_point_txt, "text")
      self.assert_equal(starpoint_page_header_text, "StarPoin")
    
   @allure.step("Swipe right to left")
   def swipe_right_to_left(self):
      self.sleep(2)
      self.scroll_screen(start_x=933, start_y=1095, end_x=89, end_y=1107, duration=10000)
      self.sleep(2)

   @allure.step("cover test 001, 002, 003, 004,005, and 006 ")
   def Validate_starPoint_Swipe_and_Value(self):
      self.sleep(2)
      page_tutorial_starpoint= self.is_element_visible(starpoint_icon1)
      if page_tutorial_starpoint == True:
         self.assert_equal(self.is_element_visible(starpoint_icon1), True)
         about_starpoint_txt = self.get_attribute(About_startpoint, "text")
         self.assert_equal(about_starpoint_txt,"All About StarPoin")
         starpoint_swp1_txt2 = self.get_attribute(txt_2_swp1, "text")
         self.assert_equal(starpoint_swp1_txt2,"Investasi Sekarang")
         self.sleep(2)
         self.swipe_right_to_left()
         self.sleep(2)
         self.assert_equal(self.is_element_visible(starpoint_icon2), True)
         starpoint_swipe2_txt = self.get_attribute(txt_2_swp2, "text")
         self.assert_equal(starpoint_swipe2_txt,"Setiap melakukan transaksi, otomatis StarPoin di Home SimInvest kamu akan bertambah")
         self.sleep(2)
         self.swipe_right_to_left()
         self.assert_equal(self.is_element_visible(starpoint_icon3), True)
         starpoint_swipe3_txt = self.get_attribute(txt_2_swp3, "text")
         self.assert_equal(starpoint_swipe3_txt,"Semakin sering transaksi, makin banyak StarPoin yang kamu dapat")
         self.sleep(2)
         self.swipe_right_to_left()
         self.assert_equal(self.is_element_visible(starpoint_icon4), True)
         starpoint_swipe4_txt = self.get_attribute(txt_1_swp4, "text")
         self.assert_equal(starpoint_swipe4_txt,"Share Kode Referral Dapat")
         self.sleep(2)
         self.swipe_right_to_left()
         self.assert_equal(self.is_element_visible(starpoint_icon5), True)
         starpoint_swipe5_txt = self.get_attribute(txt_3_swp5, "text")
         self.assert_equal(starpoint_swipe5_txt,"Sekarang, StarPoin bisa ditukar di SimInvest langsung jadi RDN kamu loh! Sehingga bisa jadi modal untuk beli saham.")
         self.sleep(2)
         self.swipe_right_to_left()
         self.assert_equal(self.is_element_visible(starpoint_icon6), True)
         starpoint_swipe6_txt = self.get_attribute(txt_2_swp6, "text")
         self.assert_equal(starpoint_swipe6_txt,"StarPoin adalah produk loyalty & reward kepada customer dan merupakan  bagian dari Sinar Mas Financial Service. StarPoin bisa ditukarkan untuk belanja di lebih dari 1.000 merchant yang bekerja sama. Plus, untuk investasi reksa dana atau saham.")
         self.sleep(2)
         self.click(btn_mulai)
         self.sleep(2)
      else:
         self.assert_equal(self.is_element_visible(starpoint_saya), True)
         self.assert_equal(self.is_element_visible(startpoint_value2), True)
         self.assert_equal(self.is_element_visible(starpoint_riwayat_btn), True)
         riwayat_check_txt = self.get_attribute(riwayat_text, "text")
         self.assert_equal(riwayat_check_txt,"Riwayat")
         self.assert_equal(self.is_element_visible(tukar_btn), True)
         tukar_check_txt = self.get_attribute(tukar_txt, "text")
         self.assert_equal(tukar_check_txt,"Riwayat")
         self.assert_equal(self.is_element_visible(riwayat_simInvest), True)
   
   @allure.step("when T&C showing and cover test ")
   def validate_show_TC_afterTutorial(self):
      self.assert_equal(self.is_element_visible(Syarat_dan_Ketentuan_txt), True)
      self.assert_equal(self.is_element_visible(Agreement_txt), True)
   
   @allure.step("Click to submit")
   def click_to_submit(self):
      self.click(btn_submit_TC)
      self.sleep(2)

   @allure.step("Click checkbox")
   def click_checkbox_btn(self):
      self.click(checklist)
      self.sleep(2)
   
   @allure.step("validate 3 dot")
   def Validate_3dot_when_Click(self):
      self.click(Tri_dot)
      self.sleep(2)
      self.click(Term_cond_Work1)
      self.sleep(5)
      tri_dot_TC1 = self.get_attribute(Term_cond_txt1, "text")
      self.assert_equal(tri_dot_TC1,"Home")
      tri_dot_TC2 = self.get_attribute(Term_cond_txt2, "text")
      self.assert_equal(tri_dot_TC2,"Program & Promo")
      self.sleep(5)
      self.click(back_btn2)
      self.sleep(2)
   
   @allure.step("luanch app again")
   def launch_app_again(self):
        self.launch()

   @allure.step("validate reopen T&C cover test 0012,0013,0014")
   def Validate_Reopen_not_showing(self):
      self.launch_app_again()
      self.login_and_verify_homepage_for_reg_user(user_data['reg_no_2'])
      self.verify_starpoint_page()
      self.verify_star_point_btn()
      self.sleep(2)

   @allure.step("validate 5 last transaction, status, date and plus minus simbol")
   def Validate_starpoint_Home_and_Tukar(self):
      self.sleep(2)
      self.assert_equal(self.is_element_visible(riwayat_simInvest) , True)
      self.assert_equal(self.is_element_visible(icon_image_homestar1) , True)
      self.assert_equal(self.is_element_visible(icon_image_homestar2) , True)
      self.assert_equal(self.is_element_visible(icon_image_homestar3) , True)
      self.assert_equal(self.is_element_visible(entry_txt1), True)
      self.assert_equal(self.is_element_visible(entry_txt2), True)
      self.assert_equal(self.is_element_visible(entry_txt3), True)
      self.assert_equal(self.is_element_visible(starpoin_entry_value1), True)
      self.assert_equal(self.is_element_visible(starpoin_entry_value2), True)
      self.assert_equal(self.is_element_visible(starpoin_entry_value3), True)
      self.assert_equal(self.is_element_visible(starpoin_status1), True)
      self.assert_equal(self.is_element_visible(starpoin_status2), True)
      self.assert_equal(self.is_element_visible(starpoin_status3), True)
      self.assert_equal(self.is_element_visible(starpoin_status4), True)
      date_in_entry = self.get_attribute(date_format1, 'text')
      in_date = datetime.strptime(date_in_entry, '%d %B %Y')
      out_date = datetime.strftime(in_date, '%d %B %Y')
      self.assert_equal(date_in_entry, str(out_date))
      self.sleep(2)
      self.scroll_up()
      self.assert_equal(self.is_element_visible(icon_image_homestar5) , True)
      self.assert_equal(self.is_element_visible(entry_txt5), True)
      self.sleep(2)
      self.click(btn_tukar)
      self.sleep(2)
      self.assert_equal(self.is_element_visible(tukar_icon), True)
      self.assert_equal(self.is_element_visible(tukar_txt1), True)
      self.assert_equal(self.is_element_visible(tukar_txt2), True)
      self.assert_equal(self.is_element_visible(tukar_txt4), True)
      self.assert_equal(self.is_element_visible(tukar_value1), True)
      self.click(back_tukar_btn)
      self.sleep(2)

   @allure.step ("Validate When click Riwayat")
   def Validate_starpoint_riwayat(self):
      self.sleep(2)
      self.click(btn_riwayat)
      self.sleep(2)

   @allure.step ("Validate Back btn Riwayat")
   def Validate_Back_btn_riwayat(self):
      self.sleep(2)
      self.click(back_riwayat_btn)
      self.sleep(2)
      
   @allure.step("Validate thousand separator in starpoin Riwayat")
   def validate_thousand_separator_in_starpoin_Riwayat(self):
            
      for i in range(1,5):
            self.assert_not_in(' ', self.get_attribute(f'StarPoin_entry_{i}_text', 'text'))
            price_value = self.get_attribute(f'StarPoin_entry_{i}_value', 'text')
            if len(price_value) >= 5:
                self.assert_in(',', price_value)

   @allure.step("Validate scroll up and down on Riwayat page and 25 Transaction")
   def validate_scroll_up_and_down_on_Riwayat_page(self):
        self.assert_equal(self.is_element_visible(riwayat_entry1), True)
        self.assert_equal(self.is_element_visible(riwayat_entry2), True)
        self.assert_equal(self.is_element_visible(riwayat_entry3), True)
        self.assert_equal(self.is_element_visible(riwayat_entry4), True)
        self.assert_equal(self.is_element_visible(riwayat_entry5), True)
        page_no_scroll_riwayat= self.is_element_visible(riwayat_entry7)
        if page_no_scroll_riwayat == True:      
         self.assert_equal(self.is_element_visible(riwayat_entry7), True)
         self.assert_equal(self.is_element_visible(riwayat_entry8), True)
         self.assert_equal(self.is_element_visible(riwayat_entry9), True)
         self.assert_equal(self.is_element_visible(riwayat_entry10), True)
         self.scroll_up()
         self.assert_equal(self.is_element_visible(riwayat_entry15), True)
         self.scroll_up()
         self.assert_equal(self.is_element_visible(riwayat_entry18), True)
         self.scroll_up()
         self.assert_equal(self.is_element_visible(riwayat_entry22), True)
         self.assert_equal(self.is_element_visible(riwayat_entry25), True)
        else:
         self.assert_equal(self.is_element_visible(riwayat_entry5), True)    
   
   
   @allure.step("API validation of Starpoint")
   def api_data_validation_for_Starpoint(self):
        ui_starpoinhistory_name = []
        api_starpoinhistory_name = []
        for i in range(1,4):
            ui_starpoinhistory_name.append(self.get_attribute(f'StarPoin_entry_{i}_text', 'text'))
        token_value = self.login()
        token = {
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJpWlYzdUJkTkJyTDA4dVIzQUR2bmg4akdTdHNkSHpQVSIsInN1YiI6IlNpbWFzSW52ZXN0In0.Kj31bgBrbc94NaUDKWgbx-N4ZBQNFsrZBmF7xtZ4hNo"}
        token['Authorization'] = 'Bearer ' + token_value
        starpoint_api = request_utilities.get(base_url='https://stg-api.siminvest.co.id/', endpoint='radix/v1/account/54522/balance/1', headers=token, expected_status_code=200)
        for i in range(len(starpoint_api['data'])):
            api_starpoinhistory_name(starpoint_api['data'][i]['value'])
        logger.info(ui_starpoinhistory_name)
        logger.info(api_starpoinhistory_name)
        for i in range(len( ui_starpoinhistory_name)):
            self.assert_in(ui_starpoinhistory_name , api_starpoinhistory_name)