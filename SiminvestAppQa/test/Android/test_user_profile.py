import allure
import pytest
from SiminvestAppQa.src.data.userData import user_data
from SiminvestAppQa.src.pages.Android_pages.user_profile import UserProfile
from SiminvestAppQa.src.utilities.genericUtilities import generate_random_integer


@pytest.mark.usefixtures("_unittest_setUpClass_fixture_userProfile_test")
class userProfile_test(UserProfile):

    @pytest.mark.User_profile_RateFeature_01
    @pytest.mark.android
    @pytest.mark.userProfile
    @allure.story("F-3:Profile Feature")
    def test_validate_rate_feature_all_testcases(self):
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


    @pytest.mark.User_profile_RateFeature_02
    @pytest.mark.android
    @pytest.mark.userProfile
    @allure.story("F-3:Profile Feature")
    def test_validate_on_two_start_rating(self):
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

    @pytest.mark.User_profile_RateFeature_03
    @pytest.mark.android
    @pytest.mark.userProfile
    @allure.story("F-3:Profile Feature")
    def test_validate_submit_feedback_by_default_keyboard_btn(self):
        number = generate_random_integer(length=6, prefix='8442')
        self.login_with_new_number(number)
        self.click_on_profile_btn()
        self.click_on_second_star()
        self.verify_emoji_section()
        self.verify_comment_in_feedback_section('Good')
        self.tap_by_coordinates(1290, 2617)
        self.sleep(2)
        self.verify_send_btn_for_feedback(False)

    @pytest.mark.User_profile_otherPages_01
    @pytest.mark.android
    @pytest.mark.userProfile
    @pytest.mark.otherFeature
    @allure.story("F-3:Profile Feature")
    def test_validate_ajak_btn_and_refferal_feature(self):
        self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
        self.click_on_profile_btn()
        self.scroll_up()
        self.scroll_down()
        self.verify_phone_number_available_on_profile_page()
        self.click_on_ajak_akun_and_validate_redirection()
        self.click_to_check_box()
        self.click_on_submit_btn()
        self.verify_redirection_to_referral_page()
        self.go_back()
        self.click_on_ajak_akun()
        self.verify_redirection_to_referral_page()
        self.copy_referral_code()
        self.click_on_begikan_btn_and_redirection()
        self.go_back()
        self.click_on_gift_icon_and_verify_redirection()

    @pytest.mark.User_profile_otherPages_02
    @pytest.mark.android
    @pytest.mark.userProfile
    @pytest.mark.otherFeature
    @allure.story("F-3:Profile Feature")
    def test_validate_profile_page_for_non_kyc_user(self):
        self.login_with_non_kyc_number(user_data['unkyc_reg_no'])
        self.click_on_profile_btn()
        self.verify_daftar_masuk_btn()
        self.click_on_Daftar_masuk_btn()
        self.verify_redirection_masuk_page()
        self.go_back()
        self.verify_daftar_masuk_btn()
        self.verify_informasi_btn_on_profile_page_for_non_kyc_user()
        self.click_on_akun_pengaturn()
        self.verify_redirection_masuk_page()

    @pytest.mark.User_profile_otherPages_03
    @pytest.mark.android
    @pytest.mark.userProfile
    @pytest.mark.otherFeature
    @allure.story("F-3:Profile Feature")
    def test_validate_user_profile_image_upload_option(self):
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

    @pytest.mark.User_profile_otherPages_04
    @pytest.mark.android
    @pytest.mark.userProfile
    @pytest.mark.otherFeature
    @allure.story("F-3:Profile Feature")
    def test_validate_user_profile_image_upload_by_gallery(self):
        self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
        self.click_on_profile_btn()
        self.click_on_profile_icon()
        self.upload_image_using_gallery_option()
        self.verify_image_icon_availability()


















