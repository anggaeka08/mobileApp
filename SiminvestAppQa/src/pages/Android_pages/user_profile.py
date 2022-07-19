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



