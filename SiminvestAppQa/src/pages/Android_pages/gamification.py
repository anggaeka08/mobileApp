from SiminvestAppQa.src.pages.Android_pages.home_page import HomePage
from SiminvestAppQa.src.data.userData import user_data
from datetime import datetime
import allure
import logging as logger
from SiminvestAppQa.src.utilities.requestUtilities import RequestsUtilities

request_utilities = RequestsUtilities()
gamification_check_box= "//android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ImageView"
gamification_button= "reward_entry"
sdp_keystate = "//android.widget.TextView[@text='Keystats']"
tc_submit= "//android.widget.TextView[@text='Submit']"
gamification_header= 'MissionHeader'
mission_status= 'Mission_status_text'
mission_xp= 'Mission_xp_value'
mission_msg= '//android.view.ViewGroup[@content-desc="Mission_text_1"]/android.widget.TextView[1]'
ob_entry_2='//android.view.ViewGroup[@content-desc="Onboarding_entry_2"]/android.view.ViewGroup'
ob_entry_1='//android.view.ViewGroup[@content-desc="Onboarding_entry_1"]/android.view.ViewGroup'
ob_entry_3='//android.view.ViewGroup[@content-desc="Onboarding_entry_3"]/android.view.ViewGroup'
harian_subtab= "Mission_Harian_kamu"
onboarding_subtab= "Onboarding_text"
transaksi_subtab= "Transaction_text"
frekuensi_subtab= "Frequency_text"
referral_subtab= "Referral_text"
back_button = "MissionPage_back"
kerja_webpage= "//android.view.ViewGroup[2]/android.widget.TextView"
webpage_back= "//android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.ImageView"
menu= "Mission_page_menu"
kerja_button= "//android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup"


class Gamification(HomePage):

    @allure.step("Open Gamification Page")
    def open_gamification_page(self,phone_number):
        self.sleep(4)
        self.click_mulai_sekarang()
        self.type_mobile_no(phone_number)
        self.click_selanjutnya()
        self.enter_otp('1234')
        self.enter_pin()
        self.verify_home_page_reg_user()
        self.click_on_profile_btn()
        self.click(gamification_button)
        self.sleep(1)
        if self.is_element_visible(gamification_check_box)==True:
            self.click(gamification_check_box)
            self.click(tc_submit)
            self.assert_equal(self.is_element_visible(gamification_header),True)
        else:
            self.assert_equal(self.is_element_visible(gamification_header),True)

    @allure.step("get mission xp")
    def get_mission_xp(self):
        value = self.get_attribute(mission_xp,"text")
        self.assert_in('/',value)
        index = value.find('/')
        xp_value = int(value[3:index-1].replace('.', ''))
        return xp_value

    @allure.step("get target mission xp")
    def get_target_mission_xp(self):
        value = self.get_attribute(mission_xp, "text")
        index = value.find('/')
        target_xp_value = int(value[index + 1:].replace('.', ''))
        return target_xp_value

    @allure.step("validate mission status")
    def validate_mission_status(self):
        status= self.get_attribute(mission_status,"text")
        value = self.get_mission_xp()
        if 0 <=value <=5000 :
            status == "Pemimpi"
        elif 5000< value <=25000 :
            status == "Juragan"
        elif 25000< value <=75000 :
            status == "Tajir"
        elif 75000< value <=150000 :
            status == "Konglo"
        elif 150000< value:
            status == "Sultan"

    @allure.step("validate mission message")
    def validate_mission_message(self):
        actual_message= self.get_attribute(mission_msg,"text")
        current_xp= self.get_mission_xp()
        target_xp= self.get_target_mission_xp()
        rest_xp= str(target_xp-current_xp)
        self.assert_in(rest_xp, actual_message)
        expected_message= rest_xp+" XP lagi buat naik ke level Juragan, yuk bisa yuk! "
        self.assert_equal(actual_message,expected_message)

    @allure.step("validate swipe functionality")
    def validate_swipe_functionality(self):
        self.scroll_screen(start_x=500, start_y=1820, end_x=523, end_y=1400, duration=10000)
        self.assert_equal(self.is_element_visible(ob_entry_1), True)
        self.swipe_between_element(ob_entry_2, ob_entry_3)
        self.sleep(1)
        self.assert_equal(self.is_element_visible(ob_entry_1), False)

    @allure.step("Validate sub tabs visiblity")
    def validate_subtabs_visiblity(self):
        self.assert_equal(self.is_element_visible(harian_subtab), True)
        self.assert_equal(self.is_element_visible(onboarding_subtab), True)
        self.scroll_screen(start_x=500, start_y=2000, end_x=500, end_y=300, duration=5000)
        self.assert_equal(self.is_element_visible(transaksi_subtab), True)
        self.assert_equal(self.is_element_visible(frekuensi_subtab), True)
        self.assert_equal(self.is_element_visible(referral_subtab), True)
        self.assert_equal(self.is_element_visible(back_button), True)
        self.scroll_screen(start_x=500, start_y=200, end_x=500, end_y=3000, duration=5000)
        self.sleep(1)

    @allure.step("validate cara kerja")
    def validate_cara_kerja(self):
        self.click(menu)
        self.click(kerja_button)
        self.sleep(2)
        self.assert_equal(self.is_element_visible(kerja_webpage), True)
        self.assert_equal(self.is_element_visible(webpage_back), True)

    @allure.step("Validate swipe functionality on cara kerja webpage")
    def validate_swipe_functionality_on_cara_kerja_webpage(self):
        self.scroll_screen(start_x=500, start_y=2000, end_x=500, end_y=500, duration=5000)
        self.assert_equal(self.is_element_visible(kerja_webpage), True)
        self.assert_equal(self.is_element_visible(webpage_back), True)

    @allure.step("Validate back button functionality on cara kerja webpage")
    def validate_back_button_functionality_on_cara_kerja_webpage(self):
        self.click(webpage_back)
        self.sleep(1)
        self.assert_equal(self.is_element_visible(gamification_header), True)












