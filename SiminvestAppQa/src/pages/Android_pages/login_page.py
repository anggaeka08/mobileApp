import logging as logger
import time
import os
import allure
from appiumbase import BaseCase

# Locators
mulai_sekarang = "WelcomeScreenMulaiSekarangButton"
mobile_no_page="EnterNumText1"
#mobile_no_page="Browser_StackENTERNUMBER"
text_input = 'EnterNumEdit'
selanjutnya = "selanjutana_btn"
otp_enter = 'PinTextInput'
#otp_enter = '(//android.widget.EditText[@content-desc="Browser_Stack"])[1]'
set_pin ="//android.widget.TextView[@text='Buat PIN Kamu']"
risk_profile_page="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView"
risk_profile = "Pilih tipe portfolio yang sesuai dengan Kamu."
agresif = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.widget.ImageView"
Home_page_locator = "//android.widget.TextView[@text='Buka Akun Investasi']"
Home_page_text = "Buka Akun Investasi"
#Home_page_reg_user_locator = "//android.widget.TextView[@text='Mulai Investasi Yuk…']"
Home_page_reg_user_locator = "HomePageRDN"
Home_page_reg_user_locator_text ="Saldo"
#Home_page_reg_user_locator_text ="Mulai Investasi Yuk…"
phone_no_page_text_r = "Nomor Ponsel"
phone_no_page_locator ="EnterNumText1"
click_1 = "//*[@text='1']"
click_2 = "//*[@text='2']"
click_3 = "//*[@text='3']"
click_4 = "//*[@text='4']"
click_5 = "//*[@text='5']"
click_6 = "//*[@text='6']"
Kirim_Ulang_click = 'OTPResendText'
Kirim_Ulang_unclick = 'OTPResendCounter'
otp_page_back = "OtpBackBtn"
otp_page_locator = "OtpText2"
wrong_pin_msg = "Pin masih salah, Silahkan coba 1x lagi"
wrong_pin_msg_locator = "EnterPinErrorMsg"
#reset_pin_btn = "//android.widget.TextView[@text='RESET PIN']"
reset_pin_btn = "//android.widget.TextView[@text='Lupa PIN SimInvest']"
pin_page_locator = "EnterPinText1"
confirm_pin_page_locator = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView'
pin_page_text_dir = "Masukkan PIN SimInvest"
pin_reset_confirm = "Berhasil"
banner_close = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ImageView"
logout_button_on_pin = "//android.widget.TextView[@text='Keluar']"
finger_print_on_off = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView"
finger_print_activate = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[1]/android.view.ViewGroup[2]"
finger_print_remove = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[1]/android.view.ViewGroup[2]"
profile_btn = '//android.widget.TextView[@text="Profile"]'
set_up_pin = 'setupPin'
error_msg = "//android.widget.TextView[@text='Pastikan memasukkan Nomor Ponsel dengan benar']"
send_otp_bia_sms = '//android.widget.TextView[@text="Kirim OTP via SMS"]'
pengaturan_btn = 'ProfilePageEntry3'
ganti_pin_siminvest='PengaturanPagePinSiminvest'
pin_lama = "//android.widget.EditText[@index = '3']"
old_pin_error_msg = "//android.widget.TextView[@index= '10']"
ok_btn = "//android.widget.TextView[@text= 'OK']"
YA_btn = "//android.widget.TextView[@text= 'YA']"
confirm_pin = 'cnfPin'
logout_btn_on_profile_page = 'ProfilePageLogoutText'
ganti_pin_password ='PengaturanPageGantiPin'
ganti_pin_password_page_header = 'GantiPAgeHeader'
sms_btn = 'SMSBtn'
whatsaap_btn = 'WhatsappBtn'
otp_verfiy = 'EnterNumText2'
otp_verify_text = 'Masukkan nomor ponsel untuk mendaftar. Pastikan nomor benar dan aktif.'
wrong_number_text = 'WrongNumText'
wrong_otp_msg = "//android.widget.TextView[@text='OTP Salah. Silahkan ulangi lagi']"
wrong_otp_msg_text ='OTP Salah. Silahkan ulangi lagi'
ignore_btn = "//android.widget.Button[@text= 'IGNORE']"
kirim_otp = "//android.widget.TextView[contains(@text, 'Kirim OTP via')]"
selanjutnya_otp_sel = '//android.widget.TextView[@text="SELANJUTNYA"]'
back_btn = "//android.view.ViewGroup/android.widget.ImageView[@index ='0']"
navigate_up = 'Navigate up'
bio_on_off = "//android.widget.TextView[@text = 'Nanti Saja']"
close_banner = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ImageView'
Saya_Setuju ='//android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.TextView'
tampilkan ="//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]/android.widget.ImageView"
Lewati = "//android.widget.TextView[@text ='Lewati']"

class LoginPage(BaseCase):

    @allure.step("luanch app again")
    def launch_app_again(self):
        self.launch()

    @allure.step("click mulai sekarang")
    def click_mulai_sekarang(self):
        self.sleep(10)
        if self.is_element_visible(ignore_btn) == True:
            self.tap(ignore_btn)
            self.sleep(3)
            self.click(mulai_sekarang)
            #self.tap_by_coordinates(511,1825)
        else:
            self.click(mulai_sekarang)
            #self.tap_by_coordinates(511, 1825)

    @allure.step("verify mobile no page")
    def verify_mobile_no_page(self):
        mobile_no_page_text = self.get_attribute(mobile_no_page, "text")
        self.assert_equal(mobile_no_page_text, "Nomor Ponsel")

    @allure.step("verify count of mobile no")
    def verify_count_of_mobile_no(self, phone_number):
        entered_no = self.get_attribute(text_input, "text")
        self.assert_equal(entered_no, phone_number[:13])

    @allure.step("type mobile no")
    def type_mobile_no(self, mobile_no):
        self.set_text(text_input, mobile_no)

    @allure.step("type mobile no")
    def type_mobile_no_update(self, mobile_no):
        self.update_text(text_input, mobile_no)

    @allure.step("click selanjutnya")
    def click_selanjutnya(self):
        self.click(selanjutnya)

    @allure.step("click_on_bio_off")
    def click_on_bio_off(self):
        self.click(bio_on_off)


    @allure.step("enter otp")
    def enter_otp(self, otp):
        self.set_text(otp_enter, otp)
        #self.execute_script('mobile: shell', {'command': 'input text', 'args': otp})

    @allure.step("enter set/confirm pin")
    def set_pin(self, pin):
        #os.system(f"start /wait cmd /c adb shell input text {pin}")
        #self.execute_script('mobile: shell', {'command': 'input text', 'args': pin})
       # self.set_text(set_up_pin, pin)
        self.sleep(2)
        for i in range(len(pin)):
            self.click(f"//*[@text='{pin[i]}']")

    @allure.step("verify set up pin page")
    def verify_setup_pin_page(self):
        setup_page_text = self.get_attribute(set_pin, "text")
        self.assert_equal(setup_page_text, "Buat PIN Kamu")

    @allure.step("verify risk profile page")
    def verify_risk_profile_page(self):
        #self.assert_element_present(risk_profile)
        time.sleep(5)
        risk_profile_text = self.get_attribute(risk_profile_page, "text")
        self.assert_equal(risk_profile,risk_profile_text)

    @allure.step("click agresif profile")
    def click_agresif_profile(self):
        self.click(agresif)
    
    # @allure.step("verify home page")
    # def verify_home_page(self):
    #     self.sleep(3)
    #     self.click(Saya_Setuju)
    #     self.sleep(2)
    #     self.click(Lewati)
    #     self.sleep(1)

    @allure.step("verify home page")
    def verify_home_page(self):
        self.sleep(3)
        self.click(Saya_Setuju)
        self.sleep(3)
        if self.is_element_visible(close_banner) == True:
            self.click(Lewati)
            self.sleep(2)
            Home_page_locator_text = self.get_attribute(Home_page_locator, "text")
            self.assert_equal(Home_page_locator_text, Home_page_text)
        else :
            self.sleep(2)
            Home_page_locator_text = self.get_attribute(Home_page_locator, "text")
            self.assert_equal(Home_page_locator_text, Home_page_text)
            
    def verify_home_page_reg_user(self):
        self.sleep(3)
        if self.is_element_visible(Saya_Setuju) == True:
            self.click(Saya_Setuju)
            self.sleep(3)
            self.click(tampilkan)
            Home_page_locator_text = self.get_attribute(Home_page_reg_user_locator, "text")
            self.assert_equal(Home_page_locator_text, Home_page_reg_user_locator_text)
        else:
            self.sleep(3)
            Home_page_locator_text = self.get_attribute(Home_page_reg_user_locator, "text")
            self.assert_equal(Home_page_locator_text, Home_page_reg_user_locator_text)
            
    @allure.step("verify home page reg user without banner")
    def verify_home_page_reg_user_without_banner(self):
        self.sleep(3)
        Home_page_locator_text = self.get_attribute(Home_page_reg_user_locator, "text")
        self.assert_equal(Home_page_locator_text, Home_page_reg_user_locator_text)


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
        self.click(bio_on_off)

    @allure.step("enter pin")
    def enter_pin_without_bio(self):
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
        self.assert_equal(phone_no_page_text_r, phone_no_page_text)
        #self.tearDown()

    @allure.step("enter pin")
    def set_up_pin(self):
        self.sleep(2)
        self.click(click_6)
        self.click(click_5)
        self.click(click_4)
        self.click(click_3)
        self.click(click_2)
        self.click(click_1)
        self.sleep(2)

    @allure.step("click kirim ulang")
    def click_Kirim_Ulang(self):
        self.click(Kirim_Ulang_click)
        #text_before_otp = self.get_attribute(Kirim_Ulang_unclick, "text")
        #self.assert_equal(text_before_otp, "Kirim Ulang (29)")

    @allure.step("verify otp timmer")
    def verify_otp_timmer(self):
        text_otp_timmer_before_backgd = self.get_attribute(Kirim_Ulang_unclick, "text")
        self.app_background(10)
        text_otp_timmer_after_backgd = self.get_attribute(Kirim_Ulang_unclick, "text")
        self.assert_not_equal(text_otp_timmer_before_backgd, text_otp_timmer_after_backgd)

    @allure.step("click back btn on otp page")
    def click_back_button_otp_page(self):
        self.click(otp_page_back)

    @allure.step("otp page with SMS phone no")
    def verify_otp_page_with_phone_no(self, phone_no):
        self.sleep(2)
        otp_page_text = self.get_attribute(otp_page_locator, "text")
        self.assert_equal(otp_page_text, f"4 digit OTP telah dikirim melalui SMS ke nomor +62{phone_no}")

    @allure.step("verify wrong pin message")
    def verify_wrong_pin_message(self):
        #wrong_pin_text = self.get_attribute(wrong_pin_msg_locator, "text")
        self.assert_equal(self.is_element_visible(wrong_pin_msg_locator), True)

    @allure.step("click on reset pin")
    def click_on_reset_pin(self):
        self.click(reset_pin_btn)

    @allure.step("verify redirect to pin page")
    def verify_redirect_to_pin_page(self):
        pin_page_text = self.get_attribute(pin_page_locator, "text")
        self.assert_equal(pin_page_text_dir , pin_page_text)

    @allure.step("confirm pin reset")
    def confirm_pin_reset(self):
        pin_page_text = self.get_attribute(confirm_pin_page_locator, "text")
        self.assert_equal(pin_reset_confirm , pin_page_text)

    @allure.step("app in background")
    def app_in_background(self, time):
        self.app_background(time)

    @allure.step("close home page banner")
    def close_home_page_banner(self):
        pass
        #self.click(banner_close)
        #self.sleep(2)
        self.sleep(3)
        if self.is_element_visible(Saya_Setuju) == True:
            self.click(Saya_Setuju)
            self.sleep(3)
            self.click(tampilkan)
            Home_page_locator_text = self.get_attribute(Home_page_reg_user_locator, "text")
            self.assert_equal(Home_page_locator_text, Home_page_reg_user_locator_text)
        else:
            self.sleep(3)
            Home_page_locator_text = self.get_attribute(Home_page_reg_user_locator, "text")
            self.assert_equal(Home_page_locator_text, Home_page_reg_user_locator_text)

    @allure.step("click on enter pin on logout btn")
    def click_on_enterPin_logout_button(self):
        self.click(logout_button_on_pin)

    @allure.step("verify starting page")
    def verify_starting_page(self):
        self.sleep(3)
        if self.is_element_visible(ignore_btn) == True:
            self.tap(ignore_btn)
        self.sleep(1)
        self.assert_equal(self.is_element_visible(mulai_sekarang), True)

    @allure.step("verify starting page without ignore")
    def verify_starting_page_without_ignore(self):
        self.sleep(3)
        #self.tap(ignore_btn)
        self.sleep(1)
        self.assert_equal(self.is_element_visible(mulai_sekarang), True)

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
        self.assert_equal(Home_page_locator_text, "Saldo RDN")

    @allure.step("verify error message after enter dots and sign")
    def verify_error_message_after_enter_dots_and_sign(self):
        self.assert_equal(self.get_attribute(error_msg, 'text'), 'Pastikan memasukkan Nomor Ponsel dengan benar')

    @allure.step("check for paste option in phone_number")
    def check_paste_option_in_phone_number(self):
        self.assert_equal(self.get_attribute(text_input, 'long-clickable'), 'true')

    @allure.step("check paste option in set pin")
    def check_paste_option_in_set_pin(self):
        self.assert_equal(self.get_attribute(set_up_pin, 'long-clickable'), 'true')

    @allure.step("click on otp send by sms")
    def click_on_otp_send_by_sms(self):
        self.click(send_otp_bia_sms)

    @allure.step("Click on pengaturan_btn")
    def click_on_pengaturan_btn(self):
        self.click(pengaturan_btn)

    @allure.step("Click to Ganti pin siminvest")
    def Click_to_Ganti_pin_siminvest(self):
        self.click(ganti_pin_siminvest)

    @allure.step("Enter Old Pin")
    def enter_old_pin(self, pin):
        self.set_text(pin_lama, pin)

    @allure.step("Validate error msg on pin lama page")
    def validate_error_msg_on_pin_lama_page(self):
        self.assert_equal(self.get_attribute(old_pin_error_msg, "text"), 'PIN salah. Mohon ulangi lagi')

    @allure.step("Enter confirm Pin")
    def enter_confirm_pin(self, pin):
        self.sleep(2)
        for i in range(len(pin)):
            self.click(f"//*[@text='{pin[i]}']")
        self.click(bio_on_off)
    @allure.step("Enter confirm Pin")
    def enter_confirm_pin_without_bio(self, pin):
        self.sleep(2)
        for i in range(len(pin)):
            self.click(f"//*[@text='{pin[i]}']")

    @allure.step("Validate error msg on confirm pin page")
    def validate_error_msg_on_confirm_pin_page_page(self):
        self.assert_equal(self.get_attribute(old_pin_error_msg, "text"), 'PIN tidak sama. Mohon ulangi lagi')

    @allure.step("Click on ok btn")
    def click_on_ok_btn(self):
        self.click(ok_btn)

    @allure.step("Click on kelur btn")
    def click_on_kelur_btn(self):
        self.click(logout_btn_on_profile_page)

    @allure.step("Click on ganti_pin_password btn")
    def click_on_ganti_pin_password_btn(self):
        self.sleep(2)
        self.click(ganti_pin_password)

    @allure.step("Click on YA btn")
    def click_on_YA_btn(self):
        self.click(YA_btn)

    @allure.step("Verify Header of Ganti pin password page")
    def verify_header_of_Ganti_pin_password_page(self):
        self.sleep(2)
        self.assert_equal(self.is_element_visible(ganti_pin_password_page_header), True)

    @allure.step("enter pin")
    def enter_pin_after_ganti_pin(self):
        self.sleep(2)
        self.click(click_6)
        self.click(click_5)
        self.click(click_4)
        self.click(click_3)
        self.click(click_2)
        self.click(click_1)
        self.sleep(2)

    @allure.step("scroll up")
    def scroll_up(self):
        self.scroll_screen(start_x=500, start_y=1820, end_x=523, end_y=809, duration=10000)
        self.sleep(2)

    '''@allure.step("SMS Button Enabled")
    def sms_btn_enabled(self):
        self.assert_equal(self.is_element_enabled(whatsaap_btn), True)'''

    @allure.step("Verify otp text on login page")
    def verify_otp_text_on_login_page(self):
        self.assert_equal(self.get_attribute(otp_verfiy, 'text'), otp_verify_text)

    @allure.step("Validate wrong phone number error")
    def validate_wrong_phone_number_error(self):
        self.assert_equal(self.get_attribute(wrong_number_text, 'text'), 'Nomor telepon tidak valid')

    @allure.step("Verify the mobile number field when user taps on outside the field")
    def verify_mobile_number_field_when_user_taps_on_outside_field(self):
        self.type_mobile_no('83671834752')
        self.tap_by_coordinates(x=793, y=874)
        self.sleep(2)
        self.click(text_input)
        self.assert_equal(self.get_attribute(text_input, 'text'), '83671834752')

    @allure.step("Validate if the field is clear the seljutniya button should be disabled")
    def validate_if_the_field_is_clear_the_seljutniya_button_should_be_disabled(self):
        self.update_text(text_input, '')
        self.click_selanjutnya()
        self.verify_otp_text_on_login_page()

    @allure.step("Validate the user able to enter 15 digit value including 62")
    def validate_the_user_able_to_enter_15_digit_value_including_62(self):
        number = '12345678912345'
        self.update_text(text_input, number)
        self.assert_equal(self.get_attribute(text_input, 'text'), number[:13])

    @allure.step("Click on whatsApp button ")
    def click_on_whatsapp_btn(self):
        self.click(whatsaap_btn)

    @allure.step("otp page with Whatsaap phone no")
    def verify_otp_page_with_whatsapp_phone_no(self, phone_no):
        self.sleep(2)
        otp_page_text = self.get_attribute(otp_page_locator, "text")
        self.assert_equal(otp_page_text, f"Kami mengirimkan kode melalui Whatsapp ke nomor +62{phone_no}")

    @allure.step("Verify phone number autofilled after back")
    def verify_phone_nubmer_autofilled_after_back(self, number):
        self.assert_equal(self.get_attribute(text_input,'text'), number)

    @allure.step('Verify wrong otp messege')
    def verify_wrong_otp_msg(self):
        self.sleep(5)
        self.assert_equal(self.get_attribute(wrong_otp_msg, 'text'), wrong_otp_msg_text)

    @allure.step("verify keyboard on off")
    def verify_keyboard_on_off(self, Status):
        keyboard_status = self.check_keyboard_shown()
        assert keyboard_status == Status, f"Keyboard is not available"

    @allure.step('Verify timer with given time')
    def verify_timer_for_given_time(self, time):
        otp_page_time = self.get_attribute(Kirim_Ulang_unclick, 'text', timeout=50000)
        timer_on_page = otp_page_time[22:]
        self.assert_equal(timer_on_page, str(time))

    @allure.step("Click by position")
    def click_by_position(self):
        self.tap_by_coordinates(x=506, y=1046)

    @allure.step("Verify kirim otp via sms/whatsapp btn")
    def verify_kirim_otp_via_sms_otp(self):
        self.sleep(3)
        self.assert_equal(self.is_element_visible(kirim_otp), True)

    @allure.step("Click to kirim otp buttun")
    def click_to_kirim_otp_btn(self):
        self.click(kirim_otp)

    @allure.step("verify redirection after click on reset_bn")
    def verify_redirection_after_click_on_reset_bn(self):
        self.assert_equal(self.is_element_visible(sms_btn), True)
        self.assert_equal(self.is_element_visible(whatsaap_btn), True)

    @allure.step("Verify Timer on opt medium selection page")
    def verify_timer_on_otp_medium_seletion_page(self, time):
        timer_with_text = self.get_attribute(selanjutnya_otp_sel, 'text')
        timer = timer_with_text[13:]
        self.assert_equal(timer, str(time)+')')

    @allure.step("Click on selanjutnya")
    def click_on_selanjutnya(self):
        self.click(selanjutnya_otp_sel)


    @allure.step("Click on back after whatsapp otp ")
    def click_on_back_after_whatsapp_otp(self):
        self.click(back_btn)


    @allure.step("Verify click selanjutnya btn during timer")
    def verify_click_selanjutnya_btn_during_timer(self):
        self.click(selanjutnya_otp_sel)

    @allure.step("Click on cancel")
    def click_on_cancel(self):
        self.click(navigate_up)














