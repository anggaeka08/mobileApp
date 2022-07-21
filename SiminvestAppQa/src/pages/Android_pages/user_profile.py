from appiumbase import BaseCase
from SiminvestAppQa.src.data.userData import user_data
from SiminvestAppQa.src.pages.Android_pages.home_page import HomePage
import allure
from SiminvestAppQa.src.utilities.genericUtilities import generate_random_integer

#locators
profile = '//android.widget.TextView[@text="Profile"]'
first_star = 'ProfilePageRateStar11'
second_star = 'ProfilePageRateStar12'
third_star ='ProfilePageRateStar13'
fourth_star = 'ProfilePageRateStar14'
fifth_star = 'ProfilePageRateStar15'
emoji = 'ProfilePageRateEmoji'
feedback_section ='ProfilePageFeedbackEdit'
send_btn='ProfilePageFeedBackSendImage'
kirim_btn =  '//android.widget.TextView[@text="Kirim Rating"]'
phone__number_profile ='ScreenProfilePageNumber.'
ajak_akun_btn = 'ScreenProfileCardTextSubEntryEntry0'
submit_pop_text = '//android.widget.TextView[@text="Saya menyetujui, syarat dan ketentuan yang berlaku"]'
check_box = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ImageView'
submit_btn = '//android.widget.TextView[@text="SUBMIT"]'
referral_page_header ='RefferalPageHeader'
salin_btn ='RefferalPageCodeCopyBtn'
begikan_btn ='RefferalPageBegikan'
refer_friend ='//android.widget.TextView[@text="Refer a friend"]'
gift_icon='RefferalPageGiftIcon'
Stock_Reward_header = '//android.widget.TextView[@text="Stock Reward"]'


class UserProfile(HomePage):

    @allure.step("Login with new number")
    def login_with_new_number(self, number):
        number = generate_random_integer(length=7, prefix='844')
        self.sleep(4)
        self.click_mulai_sekarang()
        self.type_mobile_no(number)
        self.click_selanjutnya()
        self.enter_otp(user_data['valid_otp'])
        self.set_pin(user_data['setup_pin_value'])
        self.close_home_page_banner()
        self.verify_home_page()

    @allure.step("Click on first star")
    def click_on_first_star(self):
        self.click(first_star)

    @allure.step("Click on second star")
    def click_on_second_star(self):
        self.click(second_star)

    @allure.step("Click on third star")
    def click_on_third_star(self):
        self.click(third_star)

    @allure.step("Click on fourth star")
    def click_on_fourth_star(self):
        self.click(fourth_star)

    @allure.step("Click on fifth star")
    def click_on_fifth_star(self):
        self.click(fifth_star)

    @allure.step("Verify feedback section")
    def verify_feedback_section(self):
        self.assert_equal(self.is_element_visible(feedback_section), True)

    @allure.step("Verify emoji section")
    def verify_emoji_section(self):
        self.sleep(3)
        self.assert_equal(self.is_element_visible(emoji), True)

    @allure.step("Verify_comment_in_feedback_section")
    def verify_comment_in_feedback_section(self, text):
        self.set_text(feedback_section, text)
        self.sleep(2)
        self.assert_equal(self.get_attribute(feedback_section, 'text'), text)

    @allure.step("Verify send btn for feedback")
    def verify_send_btn_for_feedback(self, condition):
        self.assert_equal(self.is_element_visible(send_btn), condition)

    @allure.step("Verify Kirim btn")
    def verify_kirim_btn(self):
        self.assert_equal(self.is_element_visible(kirim_btn), True)

    @allure.step("Click to kirim btn")
    def click_on_kirim_btn(self):
        self.click(kirim_btn)

    @allure.step("Click to send btn")
    def click_on_send_btn(self):
        self.sleep(2)
        self.double_tap(send_btn)
        self.sleep(1)

    @allure.step("Verify phone number available on prifile page")
    def verify_phone_number_available_on_profile_page(self):
        self.assert_equal(self.is_element_visible(phone__number_profile), True)

    @allure.step("Click on ajak akun and validate redirection")
    def click_on_ajak_akun_and_validate_redirection(self):
        self.click(ajak_akun_btn)
        self.sleep(2)
        self.assert_equal(self.is_element_visible(submit_pop_text), True)

    @allure.step("Click to check box")
    def click_to_check_box(self):
        self.click(check_box)

    @allure.step("Click on submit btn")
    def click_on_submit_btn(self):
        self.click(submit_btn)
        self.sleep(2)

    @allure.step("Verify redirection to referral page")
    def verify_redirection_to_referral_page(self):
        self.assert_equal(self.is_element_visible(referral_page_header), True)

    @allure.step("Click on ajak akun")
    def click_on_ajak_akun(self):
        self.click(ajak_akun_btn)
        self.sleep(2)

    @allure.step("Copy referral code")
    def copy_referral_code(self):
        self.click(salin_btn)

    @allure.step("Click on begikan btn")
    def click_on_begikan_btn_and_redirection(self):
        self.click(begikan_btn)
        self.sleep(2)
        self.assert_equal(self.is_element_visible(refer_friend), True)

    @allure.step("Click on gift icon and verify redirection")
    def click_on_gift_icon_and_verify_redirection(self):
        self.click(gift_icon)
        self.sleep(2)
        self.assert_equal(self.is_element_visible(Stock_Reward_header),True)





