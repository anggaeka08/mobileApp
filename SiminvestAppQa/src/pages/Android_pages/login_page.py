import time
import os
import allure
from appiumbase import BaseCase

# Locators
mulai_sekarang = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView"
mulai_sekarang_btn = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup"
mobile_no_page="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView[1]"
text_input = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.EditText"
selanjutnya = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup"
otp_enter = '(//android.widget.EditText[@content-desc="Browser_Stack"])[1]'
set_pin ="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[1]"
risk_profile_page="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView"
risk_profile = "Pilih tipe portfolio yang sesuai dengan Kamu."
agresif = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.widget.ImageView"
Home_page_locator = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[1]"
Home_page_text = "Mulai Investasi Yuk…"
Home_page_reg_user_locator = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView[1]"
Home_page_reg_user_locator_text ="Saldo RDN"
phone_no_page_text = "Bagaimana kami menghubungi Kamu?"
phone_no_page_locator ="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView[1]"
click_1 = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.TextView"
click_2 = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.widget.TextView"
click_3 = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[3]/android.widget.TextView"
click_4 = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.widget.TextView"
click_5 = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.widget.TextView"
click_6 = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[3]/android.widget.TextView"
Kirim_Ulang_click = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView"
Kirim_Ulang_unclick = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[4]"
otp_page_back = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ImageView"
otp_page_locator = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[2]"
wrong_pin_msg = "Nomor telepon atau PIN salah"
wrong_pin_msg_locator = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[2]"
reset_pin_btn = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup[1]/android.widget.TextView"
pin_page_locator = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView"
pin_page_text_dir ="Masukkan PIN SimInvest"
pin_reset_confirm = "Berhasil"
banner_close = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ImageView"
logout_button_on_pin = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView"
finger_print_on_off = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView"
finger_print_activate = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[1]/android.view.ViewGroup[2]"
finger_print_remove = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[1]/android.view.ViewGroup[2]"
profile_btn = '//android.widget.Button[@content-desc="Profile, tab, 5 of 5"]/android.view.ViewGroup'
set_up_pin = '//android.widget.EditText[@content-desc="Browser_Stack"]'

class LoginPage(BaseCase):

    @allure.step("luanch app again")
    def launch_app_again(self):
        self.launch()

    @allure.step("click mulai sekarang")
    def click_mulai_sekarang(self):
        time.sleep(3)
        self.click(mulai_sekarang)

    @allure.step("verify mobile no page")
    def verify_mobile_no_page(self):
        mobile_no_page_text = self.get_attribute(mobile_no_page, "text")
        self.assert_equal(mobile_no_page_text, "Bagaimana kami menghubungi Kamu?")

    @allure.step("verify count of mobile no")
    def verify_count_of_mobile_no(self, phone_number):
        entered_no = self.get_attribute(text_input, "text")
        self.assert_equal(entered_no, phone_number[:12])

    @allure.step("type mobile no")
    def type_mobile_no(self, mobile_no):
        self.update_text(text_input, mobile_no)

    @allure.step("click selanjutnya")
    def click_selanjutnya(self):
        self.click(selanjutnya)

    @allure.step("enter otp")
    def enter_otp(self, otp):
        self.set_text(otp_enter, otp)

    @allure.step("enter set/confirm pin")
    def set_pin(self,pin):
        #os.system(f"start /wait cmd /c adb shell input text {pin}")
        #self.execute_script('mobile: shell', {'command': 'input text', 'args': pin})
        self.set_text(set_up_pin, pin)

    @allure.step("verify set up pin page")
    def verify_setup_pin_page(self):
        setup_page_text = self.get_attribute(set_pin, "text")
        self.assert_equal(setup_page_text, "Setup PIN")

    @allure.step("verify risk profile page")
    def verify_risk_profile_page(self):
        #self.assert_element_present(risk_profile)
        time.sleep(5)
        risk_profile_text = self.get_attribute(risk_profile_page, "text")
        self.assert_equal(risk_profile,risk_profile_text)

    @allure.step("click agresif profile")
    def click_agresif_profile(self):
        self.click(agresif)

    @allure.step("verify home page")
    def verify_home_page(self):
        self.sleep(2)
        Home_page_locator_text = self.get_attribute(Home_page_locator, "text")
        self.assert_equal(Home_page_locator_text, Home_page_text)

    @allure.step("verify home page reg user")
    def verify_home_page_reg_user(self):
        self.sleep(2)
        Home_page_locator_text = self.get_attribute(Home_page_reg_user_locator, "text")
        self.assert_equal(Home_page_locator_text, Home_page_reg_user_locator_text)
        #self.tearDown()

    @allure.step("enter pin")
    def enter_pin(self):
        self.sleep(2)
        self.click(click_1)
        self.click(click_2)
        self.click(click_3)
        self.click(click_4)
        self.click(click_5)
        self.click(click_6)
        self.sleep(2)

    @allure.step("enter wrong pin")
    def enter_wrong_pin(self):
        self.sleep(2)
        self.click(click_1)
        self.click(click_3)
        self.click(click_2)
        self.click(click_5)
        self.click(click_4)
        self.click(click_6)
        self.sleep(2)

    @allure.step("verify selanjutnya")
    def verify_selanjutnya(self):
        self.sleep(2)
        self.click(selanjutnya)
        phone_no_page_text = self.get_attribute(phone_no_page_locator, "text")
        self.assert_equal(phone_no_page_text, phone_no_page_text)
        #self.tearDown()

    @allure.step("click kirim ulang")
    def click_Kirim_Ulang(self):
        self.click(Kirim_Ulang_click)
        text_before_otp = self.get_attribute(Kirim_Ulang_unclick, "text")
        self.assert_equal(text_before_otp, "Kirim Ulang (29)")

    @allure.step("verify otp timmer")
    def verify_otp_timmer(self):
        text_otp_timmer_before_backgd = self.get_attribute(Kirim_Ulang_unclick, "text")
        self.app_background(10)
        text_otp_timmer_after_backgd = self.get_attribute(Kirim_Ulang_unclick, "text")
        self.assert_not_equal(text_otp_timmer_before_backgd, text_otp_timmer_after_backgd)

    @allure.step("click back btn on otp page")
    def click_back_button_otp_page(self):
        self.click(otp_page_back)

    @allure.step("otp page with phone no")
    def verify_otp_page_with_phone_no(self, phone_no):
        otp_page_text = self.get_attribute(otp_page_locator, "text")
        self.assert_equal(otp_page_text, f"Kami mengirimkan kode melalui SMS ke nomor  +62{phone_no}")

    @allure.step("verify wrong pin message")
    def verify_wrong_pin_message(self):
        wrong_pin_text = self.get_attribute(wrong_pin_msg_locator, "text")
        self.assert_equal(wrong_pin_msg, wrong_pin_text)

    @allure.step("click on reset pin")
    def click_on_reset_pin(self):
        self.click(reset_pin_btn)

    @allure.step("verify redirect to pin page")
    def verify_redirect_to_pin_page(self):
        pin_page_text = self.get_attribute(pin_page_locator, "text")
        self.assert_equal(pin_page_text_dir , pin_page_text)

    @allure.step("confirm pin reset")
    def confirm_pin_reset(self):
        pin_page_text = self.get_attribute(pin_page_locator, "text")
        self.assert_equal(pin_reset_confirm , pin_page_text)

    @allure.step("app in background")
    def app_in_background(self, time):
        self.app_background(time)

    @allure.step("close home page banner")
    def close_home_page_banner(self):
        self.click(banner_close)
        self.sleep(2)

    @allure.step("click on enter pin on logout btn")
    def click_on_enterPin_logout_button(self):
        self.click(logout_button_on_pin)

    @allure.step("verify starting page")
    def verify_starting_page(self):
        text_starting_page = self.get_attribute(mulai_sekarang, "text")
        self.assert_equal(text_starting_page, "Mulai Sekarang")

    @allure.step("enable finger print")
    def enable_finger_print(self):
        touch_btn_text_off = self.get_attribute(finger_print_on_off, "text")
        self.assert_equal(touch_btn_text_off, "OFF")
        self.click(finger_print_on_off)
        self.sleep(2)
        self.click(finger_print_activate)
        self.sleep(2)
        touch_btn_text_on = self.get_attribute(finger_print_on_off, "text")
        self.assert_equal(touch_btn_text_on, "ON")

    @allure.step("disable finger print")
    def disable_finger_print(self):
        touch_btn_text_on = self.get_attribute(finger_print_on_off, "text")
        self.assert_equal(touch_btn_text_on, "ON")
        self.click(finger_print_on_off)
        self.sleep(2)
        self.click(finger_print_remove)
        self.sleep(2)
        touch_btn_text_off = self.get_attribute(finger_print_on_off, "text")
        self.assert_equal(touch_btn_text_off, "OFF")

    @allure.step("click on profile btn")
    def click_on_profile_btn(self):
        self.click(profile_btn)
        self.sleep(2)

    @allure.step("click on soldo rdn")
    def click_on_saldo_rdn(self):
        self.click(Home_page_reg_user_locator)

    @allure.step("verify home page reg user back from watchlist")
    def verify_home_page_reg_user_after_back_from_watchlist(self):
        Home_page_locator_text = self.get_attribute(Home_page_reg_user_locator, "text")
        self.assert_equal(Home_page_locator_text, "Portfolio saham")