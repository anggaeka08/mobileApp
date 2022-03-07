from SiminvestAppQa.src.data.userData import user_data
from SiminvestAppQa.src.pages.Android_pages.home_page import HomePage
import allure

jaul_btn = '//*[@text="Jual"]'
Setuju_btn = '//*[@text="Setuju"]'
Batal_btn = '//*[@text="Batal"]'
bs_on_trans = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[5]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[4]'


class SellProcess(HomePage):

    @allure.step("ope and verify portfolio page")
    def open_and_verify_portfolio(self, number):
        self.click_mulai_sekarang()
        self.type_mobile_no(number)
        self.click_selanjutnya()
        self.enter_otp(user_data['valid_otp'])
        self.enter_pin()
        self.close_home_page_banner()
        self.verify_home_page_reg_user()
        self.click_on_portfolio_btn()
        self.verify_portfolio_for_kyc_user()

    @allure.step("Click on jual button on sdp page")
    def click_on_jual_btn(self):
        self.click(jaul_btn)

    @allure.step("click on setuju btn")
    def click_on_setuju(self):
        self.click(Setuju_btn)

    @allure.step("click on batal btn")
    def click_on_batal(self):
        self.click(Batal_btn)

    @allure.step("Verify transaction for sell")
    def verify_transaction_page_for_sell(self):
        self.assert_equal(self.get_attribute(bs_on_trans, "text"), 'SELL')
