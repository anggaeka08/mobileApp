from SiminvestAppQa.src.pages.Android_pages.home_page import HomePage
from SiminvestAppQa.src.data.userData import user_data
import allure
import logging as logger
from SiminvestAppQa.src.utilities.requestUtilities import RequestsUtilities

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
txt_1_swp4 = 'starPoint_text_2_4'
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

Term_cond_txt1 = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View'
Term_cond_txt2 =  '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View'
Term_cond_txt3 = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ListView/android.view.View[1]/android.widget.TextView[3]'
pagedown_term_cond = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View'

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
      self.scroll_screen(start_x=1061, start_y=953, end_x=19, end_y=953, duration=10000)
      self.sleep(2)

   @allure.step("cover test 001, 002, 003, 004,005, and 006 ")
   def Validate_starPoint_Swipe_and_Value(self):
      self.click(Star_point_txt)
      self.sleep(2)
      page_tutorial_starpoint= self.is_element_visible(starpoint_icon1)
      if page_tutorial_starpoint == True:
         self.assert_equal(self.is_element_visible(starpoint_icon1), True)
         about_starpoint_txt = self.get_attribute(About_startpoint, "text")
         self.assert_equal(about_starpoint_txt,"StarPoin")
         starpoint_swp1_txt2 = self.get_attribute(txt_2_swp1, "text")
         self.assert_equal(starpoint_swp1_txt2,"Investasi Sekarang")
         self.sleep(2)
         self.swipe_right_to_left()
         self.sleep(2)
         self.assert_equal(self.is_element_visible(starpoint_icon2), True)
         starpoint_swipe2_txt = self.get_attribute(txt_2_swp2, "text")
         self.assert_equal(starpoint_swipe2_txt,"Setiap")
         self.sleep(2)
         self.swipe_right_to_left()
         self.assert_equal(self.is_element_visible(starpoint_icon3), True)
         starpoint_swipe3_txt = self.get_attribute(txt_2_swp3, "text")
         self.assert_equal(starpoint_swipe3_txt,"Semakin")
         self.sleep(2)
         self.swipe_right_to_left()
         self.assert_equal(self.is_element_visible(starpoint_icon4), True)
         starpoint_swipe4_txt = self.get_attribute(txt_1_swp4, "text")
         self.assert_equal(starpoint_swipe4_txt,"Share")
         self.sleep(2)
         self.swipe_right_to_left()
         self.assert_equal(self.is_element_visible(starpoint_icon5), True)
         starpoint_swipe5_txt = self.get_attribute(txt_3_swp5, "text")
         self.assert_equal(starpoint_swipe5_txt,"Sekarang")
         self.sleep(2)
         self.swipe_right_to_left()
         self.assert_equal(self.is_element_visible(starpoint_icon6), True)
         starpoint_swipe6_txt = self.get_attribute(txt_2_swp6, "text")
         self.assert_equal(starpoint_swipe6_txt,"adalah")
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
      self.sleep(2)
      self.assert_equal(self.is_element_visible(Term_cond_txt1), True)
      self.assert_equal(self.is_element_visible(Term_cond_txt2), True)
      self.scroll_down()
      self.assert_equal(self.is_element_visible(Term_cond_txt1), True)
      self.scroll_up()
      self.assert_equal(self.is_element_visible(pagedown_term_cond) , True)
      self.sleep(2)
      self.click(back_btn)
      self.sleep(2)
