import allure
import pytest
from SiminvestAppQa.src.pages.Android_pages.login_page import LoginPage
from SiminvestAppQa.src.utilities.genericUtilities import generate_random_integer
from SiminvestAppQa.src.data.userData import user_data
import time


class Login_test(LoginPage):

    # Verify that user should be redirecting to the welcome page after open the application.
    @pytest.mark.SMMA_001
    @pytest.mark.Android
    @pytest.mark.Login_Logout_1
    @allure.story("F-2:Login/logout Feature")
    def test_verify_redirect_to_welcome_after_open_app(self):
        self.verify_starting_page()

    # Verify that user should be redirecting to the input phone number page when user tap on 'Mulai Sekarang' button
    @pytest.mark.SMMA_002
    @pytest.mark.Android
    @pytest.mark.Login_Logout
    @allure.story("F-2:Login/logout Feature")
    def test_verify_redirect_to_phone_no_page_after_click_MulaiSekarang(self):
        #LoginPage.launch_app_again()
        #self.verify_starting_page()
        self.click_mulai_sekarang()
        self.verify_mobile_no_page()

    # Verify that 'Selanjutnya' button should be displayed activate after entering 7 digit phone number.
    @pytest.mark.SMMA_004
    @pytest.mark.Android
    @pytest.mark.Login_Logout
    @allure.story("F-2:Login/logout Feature")
    def test_verify_Selanjutnya_button_activate_after_6_digit_no(self):
        #LoginPage.launch_app_again()
        self.click_mulai_sekarang()
        self.type_mobile_no(user_data['wrong_length_no'])
        self.verify_selanjutnya()

    # Verify that user should redirect to the security code page after tap on 'Selanjutnya' button when user is on enter mobile number page
    @pytest.mark.SMMA_005
    @pytest.mark.Android
    @pytest.mark.Login_Logout
    @allure.story("F-2:Login/logout Feature")
    def test_verify_redirect_to_security_code_page_by_using_valid_no(self):
        number = generate_random_integer(length=7, prefix='844')
        #LoginPage.launch_app_again()
        self.click_mulai_sekarang()
        self.type_mobile_no(number)
        self.click_selanjutnya()
        self.verify_otp_page_with_phone_no(number)

    # Verify that user should redirect to the set up pin number page after entering the 4 digit security code when user login account first time
    @pytest.mark.SMMA_006
    @pytest.mark.Android
    @pytest.mark.Login_Logout
    @allure.story("F-2:Login/logout Feature")
    def test_verify_redirect_to_setup_pin_by_using_valid_no(self):
        number = generate_random_integer(length=7, prefix='844')
        #LoginPage.launch_app_again()
        self.click_mulai_sekarang()
        self.type_mobile_no(number)
        self.click_selanjutnya()
        self.verify_otp_page_with_phone_no(number)
        self.enter_otp(user_data['valid_otp'])
        self.verify_setup_pin_page()

    # Verify that user should redirect to the home page after entering the 6 digit pin number
    @pytest.mark.SMMA_007
    @pytest.mark.Android
    @pytest.mark.Login_Logout
    @allure.story("F-2:Login/logout Feature")
    def test_verify_redirect_to_home_page_after_enter_pin(self):
        #LoginPage.launch_app_again()
        self.click_mulai_sekarang()
        self.type_mobile_no(user_data['reg_no'])
        self.click_selanjutnya()
        self.enter_otp(user_data['valid_otp'])
        self.enter_pin()
        self.close_home_page_banner()
        self.verify_home_page_reg_user()

    # Verify that user should be redirecting to the welcome page after tap on logout link under profile section
    @pytest.mark.SMMA_008
    @pytest.mark.Android
    @pytest.mark.Login_Logout
    @allure.story("F-2:Login/logout Feature")
    def test_verify_redirect_to_welcome_page_after_logout_click(self):
        #LoginPage.launch_app_again()
        self.click_mulai_sekarang()
        self.type_mobile_no(user_data['reg_no'])
        self.click_selanjutnya()
        self.enter_otp(user_data['valid_otp'])
        self.click_on_enterPin_logout_button()
        self.verify_starting_page_without_ignore()


    # Validate user should redirected to home page when user login with same account 2nd time and in future.
    @pytest.mark.SMMA_011
    @pytest.mark.Android
    @pytest.mark.Login_Logout
    @allure.story("F-2:Login/logout Feature")
    def test_verify_redirect_to_home_when_login_with_same_no_second_time(self):
        number = generate_random_integer(length=7, prefix='844')
       # LoginPage.launch_app_again()
        self.click_mulai_sekarang()
        self.type_mobile_no(number)
        self.click_selanjutnya()
        self.enter_otp(user_data['valid_otp'])
        self.set_pin(user_data['setup_pin_value'])
        #LoginPage.verify_risk_profile_page()
        #LoginPage.click_agresif_profile()
        self.close_home_page_banner()
        self.verify_home_page()
        #launch again and use same no
        self.launch_app_again()
        self.click_mulai_sekarang()
        self.type_mobile_no(number)
        self.click_selanjutnya()
        self.enter_otp(user_data['valid_otp'])
        self.enter_pin()
        self.close_home_page_banner()
        self.verify_home_page()

    # Validate login in with invalid mobile number
    @pytest.mark.SMMA_012
    @pytest.mark.Android
    @pytest.mark.Login_Logout
    @allure.story("F-2:Login/logout Feature")
    def test_validate_login_with_invalid_mobile_number(self):
        #LoginPage.launch_app_again()
        self.click_mulai_sekarang()
        self.type_mobile_no(user_data['wrong_length_no'])
        self.verify_selanjutnya()

    # Validate enter mobile number page should accept maximum 12 digit number
    @pytest.mark.SMMA_013
    @pytest.mark.Android
    @pytest.mark.Login_Logout
    @allure.story("F-2:Login/logout Feature")
    def test_validate_entry_of_max_12_digit_no_in_phone_section(self):
        #LoginPage.launch_app_again()
        self.click_mulai_sekarang()
        self.type_mobile_no(user_data['max_lenth_no'])
        self.verify_count_of_mobile_no(user_data['max_lenth_no'])

    # Validate login with invalid PIN
    @pytest.mark.SMMA_015
    @pytest.mark.Android
    @pytest.mark.Login_Logout
    @allure.story("F-2:Login/logout Feature")
    def test_validate_login_with_invalid_pin(self):
        #LoginPage.launch_app_again()
        self.click_mulai_sekarang()
        self.type_mobile_no(user_data['unkyc_reg_no'])
        self.click_selanjutnya()
        self.enter_otp(user_data['valid_otp'])
        self.enter_wrong_pin()
        self.verify_wrong_pin_message()

    # Validate reset pin functionality is working fine
    @pytest.mark.SMMA_016
    @pytest.mark.Android
    @pytest.mark.Login_Logout
    @allure.story("F-2:Login/logout Feature")
    def test_validate_reset_pin_functinality(self):
        #LoginPage.launch_app_again()
        self.click_mulai_sekarang()
        self.type_mobile_no(user_data['unkyc_reg_no_2'])
        self.click_selanjutnya()
        self.enter_otp(user_data['valid_otp'])
        self.click_on_reset_pin()
        self.sleep(25)
        self.click_on_selanjutnya()
        self.enter_otp(user_data['valid_otp'])
        time.sleep(2)
        self.set_pin(user_data['setup_pin_value'])
        time.sleep(3)
        self.enter_confirm_pin(user_data['setup_pin_value'])
        time.sleep(2)
        #self.confirm_pin_reset()
        time.sleep(10)
        self.verify_redirect_to_pin_page()
        self.enter_pin()
        self.close_home_page_banner()
        self.verify_home_page()

    # Validate user is able to logout from the enter pin page.
    @pytest.mark.SMMA_017
    @pytest.mark.Android
    @pytest.mark.Login_Logout
    @allure.story("F-2:Login/logout Feature")
    def test_validate_user_able_to_logout_from_enter_pin_page(self):
        #number = generate_random_integer(length=7, prefix='844')
        #LoginPage.launch_app_again()
        self.click_mulai_sekarang()
        self.type_mobile_no(user_data['unkyc_reg_no'])
        self.click_selanjutnya()
        self.enter_otp(user_data['valid_otp'])
        self.sleep(1)
        self.click_on_enterPin_logout_button()
        self.verify_starting_page_without_ignore()

    # validate the back button is working fine at enter OTP page
    @pytest.mark.SMMA_018
    @pytest.mark.Android
    @pytest.mark.Login_Logout
    @allure.story("F-2:Login/logout Feature")
    def test_validate_back_btn_at_enter_otp_page(self):
        #LoginPage.launch_app_again()
        self.click_mulai_sekarang()
        self.type_mobile_no(user_data['reg_no'])
        self.click_selanjutnya()
        self.verify_otp_page_with_phone_no(user_data['reg_no'])
        self.go_back()
        self.go_back()
        self.verify_mobile_no_page()

    # Validate user is able to login after user click on resend OTP page
    @pytest.mark.SMMA_021
    @pytest.mark.Android
    @pytest.mark.Login_Logout
    @allure.story("F-2:Login/logout Feature")
    def test_validate_login_after_resend_otp(self):
        number = generate_random_integer(length=7, prefix='844')
        self.click_mulai_sekarang()
        self.type_mobile_no(number)
        self.click_selanjutnya()
        self.sleep(25)
        self.click_Kirim_Ulang()
        self.sleep(2)
        self.enter_otp(user_data['valid_otp'])
        self.set_pin(user_data['setup_pin_value'])
        self.verify_home_page()

    # validate the timeout of OTP page is running even after user switch the application while timeout is running.
    @pytest.mark.SMMA_022
    @pytest.mark.Android
    @pytest.mark.Login_Logout
    @allure.story("F-2:Login/logout Feature")
    def test_validate_otp_timout_timmer_while_app_in_backgroud(self):
        #LoginPage.launch_app_again()
        number = generate_random_integer(length=7, prefix='844')
        self.click_mulai_sekarang()
        self.type_mobile_no(number)
        self.click_selanjutnya()
        self.verify_otp_timmer()

    @pytest.mark.Ganti_pin_feature_logout
    @pytest.mark.Android
    @pytest.mark.Login_Logout
    @allure.story("F-2:Login/logout Feature")
    def test_validate_ganti_pin_and_logout_feature(self):
        self.click_mulai_sekarang()
        self.type_mobile_no(user_data['reg_no'])
        self.click_selanjutnya()
        self.enter_otp(user_data['valid_otp'])
        self.enter_pin()
        self.close_home_page_banner()
        self.verify_home_page_reg_user()
        self.click_on_profile_btn()
        self.click_on_pengaturan_btn()
        self.Click_to_Ganti_pin_siminvest()
        self.enter_old_pin('123678')
        self.validate_error_msg_on_pin_lama_page()
        self.enter_old_pin('123456')
        self.set_pin('654321')
        self.enter_confirm_pin('123456')
        self.validate_error_msg_on_confirm_pin_page_page()
        self.enter_confirm_pin('654321')
        self.click_on_ok_btn()
        self.enter_pin_after_ganti_pin()
        self.click_on_profile_btn()
        self.click_on_pengaturan_btn()
        self.Click_to_Ganti_pin_siminvest()
        self.enter_old_pin('654321')
        self.set_pin('123456')
        self.enter_confirm_pin('123456')
        self.click_on_ok_btn()
        self.enter_pin()
        self.click_on_profile_btn()
        self.click_on_pengaturan_btn()
        self.click_on_ganti_pin_password_btn()
        self.verify_header_of_Ganti_pin_password_page()
        self.go_back()
        self.go_back()
        self.sleep(2)
        self.scroll_up()
        self.click_on_kelur_btn()
        self.click_on_YA_btn()
        self.verify_starting_page_without_ignore()

    @pytest.mark.SMMA_039
    @pytest.mark.Android
    @pytest.mark.Login_Logout
    @allure.story("F-2:Login/logout Feature")
    def test_Validate_that_when_user_input_otp_and_close_the_app_next_time_user_get_redirected_to_Mulai_sekarang_page(self):
        number = generate_random_integer(length=7, prefix='844')
        self.click_mulai_sekarang()
        self.type_mobile_no(number)
        self.click_selanjutnya()
        self.enter_otp(user_data['valid_otp'])
        self.launch_app_again()
        self.verify_starting_page()

    @pytest.mark.UseCase_01
    @pytest.mark.Android
    @pytest.mark.Login_Logout
    @allure.story("F-2:Login/logout Feature")
    def test_Validate_WhatsApp_and_SMS_options_on_Login_page(self):
        self.click_mulai_sekarang()
        self.verify_otp_text_on_login_page()
        self.click_selanjutnya()
        self.verify_otp_text_on_login_page()
        self.type_mobile_no('1234567')
        self.click_selanjutnya()
        self.click_on_ok_btn()
        self.validate_wrong_phone_number_error()
        self.verify_mobile_number_field_when_user_taps_on_outside_field()
        self.validate_if_the_field_is_clear_the_seljutniya_button_should_be_disabled()
        self.validate_the_user_able_to_enter_15_digit_value_including_62()
        self.type_mobile_no('ABCDEFGHIJK')
        self.click_selanjutnya()
        self.verify_otp_text_on_login_page()
        number = generate_random_integer(length=7, prefix='844')
        self.type_mobile_no(number)
        self.click_on_whatsapp_btn()
        self.click_selanjutnya()
        self.verify_otp_page_with_whatsapp_phone_no(number)

    @pytest.mark.UseCase_02
    @pytest.mark.Android
    @pytest.mark.Login_Logout
    @allure.story("F-2:Login/logout Feature")
    def test_validate_user_is_receiving_OTP_on_WhatsApp_SMS(self):
        number = generate_random_integer(length=7, prefix='844')
        self.click_mulai_sekarang()
        self.type_mobile_no(number)
        self.click_selanjutnya()
        self.verify_otp_page_with_phone_no(number)
        self.enter_otp('1456')
        self.verify_wrong_otp_msg()
        self.go_back()
        self.verify_phone_nubmer_autofilled_after_back(number)
        self.sleep(15)
        self.click_on_whatsapp_btn()
        self.click_selanjutnya()
        self.verify_otp_page_with_whatsapp_phone_no(number)
        self.sleep(25)
        self.click_Kirim_Ulang()
        self.verify_keyboard_on_off(True)
        self.enter_otp('1456')
        self.verify_wrong_otp_msg()
        self.enter_otp('1234')
        self.verify_setup_pin_page()

    @pytest.mark.UseCase_03
    @pytest.mark.Android
    @pytest.mark.Login_Logout
    @allure.story("F-2:Login/logout Feature")
    def test_Validate_the_number_of_attempts_for_WhatsApp_or_sms_on_OTP_page(self):
        number = generate_random_integer(length=7, prefix='844')
        #number = 8440276346
        self.click_mulai_sekarang()
        self.type_mobile_no(number)
        self.click_selanjutnya()
        self.verify_timer_for_given_time(29)
        time.sleep(30)
        self.verify_kirim_otp_via_sms_otp()
        self.click_Kirim_Ulang()
        self.verify_timer_for_given_time(60)
        time.sleep(30)
        self.click_by_position()
        time.sleep(30)
        self.verify_kirim_otp_via_sms_otp()
        self.click_Kirim_Ulang()
        self.verify_timer_for_given_time(120)
        time.sleep(30)
        self.click_by_position()
        time.sleep(30)
        self.click_by_position()
        time.sleep(30)
        self.click_by_position()
        time.sleep(30)
        self.verify_kirim_otp_via_sms_otp()
        self.click_to_kirim_otp_btn()
        self.sleep(1)
        self.verify_timer_for_given_time(30)
        time.sleep(31)
        self.verify_kirim_otp_via_sms_otp()
        self.click_Kirim_Ulang()
        self.verify_timer_for_given_time(60)
        time.sleep(30)
        self.click_by_position()
        time.sleep(31)
        self.verify_kirim_otp_via_sms_otp()
        self.click_Kirim_Ulang()
        self.verify_timer_for_given_time(120)


    @pytest.mark.UseCase_04
    @pytest.mark.Android
    @pytest.mark.Login_Logout
    @allure.story("F-2:Login/logout Feature")
    def test_Validate_reset_funtionality_the_number_of_attempts_for_WhatsApp_or_sms_on_OTP_page(self):
        self.click_mulai_sekarang()
        self.type_mobile_no(user_data['unkyc_reg_no_2'])
        self.click_selanjutnya()
        self.enter_otp('1234')
        self.click_on_reset_pin()
        self.sleep(2)
        self.verify_redirection_after_click_on_reset_bn()
        self.verify_timer_on_otp_medium_seletion_page(23)
        self.verify_click_selanjutnya_btn_during_timer()
        self.verify_redirection_after_click_on_reset_bn()
        time.sleep(26)
        self.click_on_selanjutnya()
        self.verify_timer_for_given_time(59)
        self.go_back()
        self.go_back()
        time.sleep(30)
        self.click_by_position()
        time.sleep(30)
        self.click_on_selanjutnya()
        self.verify_timer_for_given_time(119)
        self.go_back()
        self.go_back()
        time.sleep(30)
        self.click_by_position()
        time.sleep(30)
        self.click_by_position()
        time.sleep(30)
        self.click_by_position()
        time.sleep(30)
        self.click_on_whatsapp_btn()
        self.click_on_selanjutnya()
        self.verify_timer_for_given_time(29)
        self.click_on_back_after_whatsapp_otp()
        time.sleep(30)
        self.click_on_selanjutnya()
        self.verify_timer_for_given_time(59)
        self.click_on_back_after_whatsapp_otp()
        time.sleep(30)
        self.click_by_position()
        time.sleep(30)
        self.click_on_selanjutnya()
       # self.verify_timer_for_given_time(119)
        self.enter_otp('1345')
        self.verify_wrong_otp_msg()
        self.enter_otp('1234')
        self.set_pin('123456')
        self.enter_confirm_pin('123456')
        self.sleep(5)
        self.verify_redirect_to_pin_page()
        self.enter_pin()
        self.verify_home_page()

    @pytest.mark.UseCase_05
    @pytest.mark.Android
    @pytest.mark.Login_Logout
    @allure.story("F-2:Login/logout Feature")
    def test_Validate_another_method_if_user_got_blocked_for_whatsApp_OTP(self):
        self.click_mulai_sekarang()
        self.type_mobile_no(user_data['unkyc_reg_no'])
        self.click_on_whatsapp_btn()
        self.click_selanjutnya()
        self.verify_timer_for_given_time(29)
        self.sleep(25)
        self.click_Kirim_Ulang()
        self.verify_timer_for_given_time(60)
        time.sleep(30)
        self.click_by_position()
        time.sleep(30)
        self.verify_kirim_otp_via_sms_otp()
        self.click_Kirim_Ulang()
        self.verify_timer_for_given_time(120)
        time.sleep(30)
        self.click_by_position()
        time.sleep(30)
        self.click_by_position()
        time.sleep(30)
        self.click_by_position()
        time.sleep(30)
        self.click_on_otp_send_by_sms()
        self.verify_timer_for_given_time(30)















