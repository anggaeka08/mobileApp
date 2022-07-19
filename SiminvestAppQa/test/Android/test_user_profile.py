import pytest
from SiminvestAppQa.src.pages.Android_pages.user_profile import UserProfile
from SiminvestAppQa.src.utilities.genericUtilities import generate_random_integer


@pytest.mark.usefixtures("_unittest_setUpClass_fixture_userProfile_test")
class userProfile_test(UserProfile):

    @pytest.mark.User_profile_RateFeature
    @pytest.mark.android
    @pytest.mark.userProfile
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











