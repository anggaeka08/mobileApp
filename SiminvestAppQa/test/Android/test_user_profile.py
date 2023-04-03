import allure
import pytest
from SiminvestAppQa.src.data.userData import user_data
from SiminvestAppQa.src.pages.Android_pages.user_profile import UserProfile
from SiminvestAppQa.src.utilities.genericUtilities import generate_random_integer
from selenium.common.exceptions import NoSuchElementException

class userProfile_test(UserProfile):

    @pytest.mark.User_profile_RateFeature_01
    @pytest.mark.android
    @pytest.mark.userProfile_Not_run
    @pytest.mark.Revamp
    @allure.story("F-3:Profile Feature")
    def test_validate_rate_feature_all_testcases(self):
        try:
            self.execute_script('lambda-name=test_validate_rate_feature_all_testcases')
            number = generate_random_integer(length=7, prefix='844')
            self.login_with_new_number(number)
            self.click_on_profile_btn()
            self.click_on_first_star()
            self.verify_emoji_section()
            self.verify_feedback_section()
            self.go_back()
            self.click_on_second_star()
            self.verify_emoji_section()
            self.verify_feedback_section()
            self.verify_comment_in_feedback_section('t')
            self.verify_send_btn_for_feedback(False)
            self.verify_comment_in_feedback_section('Good')
            self.verify_send_btn_for_feedback(True)
            self.click_on_third_star()
            self.verify_emoji_section()
            self.verify_feedback_section()
            self.click_on_fourth_star()
            self.verify_emoji_section()
            self.verify_kirim_btn()
            self.click_on_kirim_btn()
            self.verify_kirim_btn()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_validate_rate_feature_all_testcases', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_validate_rate_feature_all_testcases', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)




    @pytest.mark.User_profile_RateFeature_02
    @pytest.mark.android
    @pytest.mark.userProfile_Not_run
    @pytest.mark.Revamp
    @allure.story("F-3:Profile Feature")
    def test_validate_on_two_start_rating(self):
        try:
            self.execute_script('lambda-name=test_validate_on_two_start_rating')
            number = generate_random_integer(length=6, prefix='8442')
            self.login_with_new_number(number)
            self.click_on_profile_btn()
            self.click_on_second_star()
            self.verify_emoji_section()
            self.verify_comment_in_feedback_section('Good')
            self.go_back()
            self.scroll_up()
            self.click_on_send_btn()
            self.verify_send_btn_for_feedback(False)
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_validate_on_two_start_rating', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_validate_on_two_start_rating', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)


    @pytest.mark.User_profile_RateFeature_03
    @pytest.mark.android
    @pytest.mark.userProfile_Not_run
    @pytest.mark.Revamp
    @allure.story("F-3:Profile Feature")
    def test_validate_submit_feedback_by_default_keyboard_btn(self):
        try:
            self.execute_script('lambda-name=test_validate_submit_feedback_by_default_keyboard_btn')
            number = generate_random_integer(length=6, prefix='8442')
            self.login_with_new_number(number)
            self.click_on_profile_btn()
            self.click_on_second_star()
            self.verify_emoji_section()
            self.verify_comment_in_feedback_section('Good')
            self.tap_by_coordinates(1290, 2617)
            self.sleep(2)
            self.verify_send_btn_for_feedback(False)
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_validate_submit_feedback_by_default_keyboard_btn', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_validate_submit_feedback_by_default_keyboard_btn', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    @pytest.mark.User_profile_Ajak_akun_informasi_tab
    @pytest.mark.android
    @pytest.mark.userProfile
    @pytest.mark.otherFeature
    @pytest.mark.Revamp
    @allure.story("F-3:Profile Feature")
    def test_validate_ajak_btn_and_refferal_and_akun_pennegguna_informasi_tab_feature(self):
        try:
            self.execute_script('lambda-name=test_validate_ajak_btn_and_refferal_and_akun_pennegguna_informasi_tab_feature')
            self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
            self.click_on_profile_btn()
            self.scroll_up()
            self.scroll_down()
            self.verify_phone_number_available_on_profile_page()
            self.click_on_ajak_akun_and_validate_redirection()
            self.scroll_up()
            self.scroll_down()
            self.click_to_check_box()
            self.click_on_submit_btn()
            self.verify_redirection_to_referral_page()
            #self.verify_slider_on_referral_page()
            self.click_on_gift_icon_and_verify_redirection()
            self.go_back()
            self.verify_redirection_to_referral_page()
            #self.copy_referral_code()
            self.click_on_begikan_btn_and_redirection()
            self.go_back()
            self.verify_redirection_to_referral_page()
            self.verify_teman_telah_btn()
            self.go_back()
            self.verify_redirection_to_referral_page()
            self.verify_syarat_dan_btn()
            self.go_back()
            self.verify_cara_kerja_tab()
            self.go_back()
            self.verify_redirection_to_referral_page()
            self.go_back()
            self.verify_phone_number_available_on_profile_page()
            self.click_on_akun_penggunna_tab()
            self.Verify_personal_tab_details_in_akun_penggunna(f"62{user_data['reg_no']}")
            self.click_on_serkuritas_tab()
            self.Verify_serkuritas_tab_details_in_akun_penggunna()
            self.go_back()
            self.verify_phone_number_available_on_profile_page()
            self.click_on_informasi_tab()
            self.verify_rdn_balance_page()
            self.scroll_down()
            self.verify_rdn_balance_page()
            self.verify_top_up_page()
            self.click_on_tarik_dana_btn()
            self.verify_tarik_dana_page()
            self.verify_limit_msg_on_tarik_dana_page()
            self.verify_riwayat_page_with_details()
            self.go_back()
            self.verify_phone_number_available_on_profile_page()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_validate_ajak_btn_and_refferal_and_akun_pennegguna_informasi_tab_feature', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_validate_ajak_btn_and_refferal_and_akun_pennegguna_informasi_tab_feature', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)


    @pytest.mark.User_profile_pengaturan_tab
    @pytest.mark.android
    @pytest.mark.userProfile
    @pytest.mark.otherFeature
    @pytest.mark.Revamp
    @allure.story("F-3:Profile Feature")
    def test_validate_pengaturan_tab(self):
        try:
            self.execute_script('lambda-name=test_validate_pengaturan_tab')
            self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
            self.click_on_profile_btn()
            self.click_on_pengaturan_btn()
            self.verify_pengaturan_page()
            self.Click_to_Ganti_pin_siminvest()
            self.sleep(1)
            self.go_back()
            self.sleep(1)
            self.go_back()
            self.verify_pengaturan_page()
            self.click_on_ganti_pin_password_btn()
            self.verify_header_of_Ganti_pin_password_page()
            self.verify_ganti_password_tab()
            self.verify_ganti_pin_tab()
            self.go_back()
            self.verify_pengaturan_page()
            self.go_back()
            self.verify_phone_number_available_on_profile_page()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_validate_pengaturan_tab', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_validate_pengaturan_tab', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)


    @pytest.mark.User_profile_others_tab
    @pytest.mark.android
    @pytest.mark.userProfile
    @pytest.mark.otherFeature
    @pytest.mark.Revamp
    @allure.story("F-3:Profile Feature")
    def test_validate_profile_others_tab(self):
        try:
            self.execute_script('lambda-name=test_validate_profile_others_tab')
            self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
            self.click_on_profile_btn()
            #self.verify_phone_number_available_on_profile_page()
            self.click_and_verify_to_pt_sinarmas_tab()
            self.click_and_verify_to_hubunagi_tab()
            self.click_and_verify_to_FAQs_tab()
            self.scroll_up()
            self.click_on_kelur_btn()
            self.click_batal1_btn()
            self.click_on_kelur_btn()
            self.click_on_YA_btn()
            self.login_and_verify_homepage_from_logout(user_data['unkyc_reg_no'])
            self.click_on_profile_btn()
            self.verify_mulai_text_on_profile_page()
            self.assert_equal(self.is_element_visible('ProfileDetailsPersonalTab'), False)
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_validate_profile_others_tab', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_validate_profile_others_tab', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)


    @pytest.mark.User_profile_otherPages_03
    @pytest.mark.android
    @pytest.mark.userProfile
    @pytest.mark.otherFeature
    @pytest.mark.Revamp
    @allure.story("F-3:Profile Feature")
    def test_validate_user_profile_image_upload_option(self):
        try:
            self.execute_script('lambda-name=test_validate_user_profile_image_upload_option')
            self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
            self.click_on_profile_btn()
            self.click_on_profile_icon()
            self.click_batal_btn()
            self.verify_image_icon_availability()
            self.click_on_profile_icon()
            self.go_back()
            self.verify_image_icon_availability()
            self.click_on_profile_icon()
            self.upload_image_by_camera_option()
            self.click_on_profile_icon()
            self.uplaod_cancel_process()
            self.verify_image_icon_availability()
            self.execute_script("lambda-status=passed")
        except AssertionError as E:
            self.save_screenshot('test_validate_user_profile_image_upload_option', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.__str__(), pytrace=True)
        except NoSuchElementException as E:
            self.save_screenshot('test_validate_user_profile_image_upload_option', 'SiminvestAppQa/src/data/ScreenShots')
            self.execute_script("lambda-status=failed")
            pytest.fail(E.msg, pytrace=True)

    """@pytest.mark.User_profile_otherPages_04
    @pytest.mark.android
    @pytest.mark.userProfile
    @pytest.mark.otherFeature
    @allure.story("F-3:Profile Feature")
    def test_validate_user_profile_image_upload_by_gallery(self):
        self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
        self.click_on_profile_btn()
        self.click_on_profile_icon()
        self.upload_image_using_gallery_option()
        self.verify_image_icon_availability()"""


















