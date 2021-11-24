from appiumbase import BaseCase

# Locators
mulai_sekarang = "(//XCUIElementTypeOther[@name='Mulai Sekarang'])[14]"
text_input = "//*[@class='android.widget.EditText']"
selanjutnya = "//*[@text='SELANJUTNYA']"
set_pin = '//XCUIElementTypeOther[@name="Setup PIN Atur 6 digit nomor MPIN kamu untuk kenyamanan ' \
          'transaksimu"]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1] '
risk_profile = "Pilih tipe portfolio yang sesuai dengan Kamu."
agresif = "(//XCUIElementTypeOther[@name='Agresif Portfolio ini mempunyai toleransi terhadap resiko yang tinggi agar " \
          "dapat memperoleh return tertinggi. REKOMENDASI PORTFOLIO 50% Campuran 50% Saham'])[2] "


class LoginPage(BaseCase):

    def click_mulai_sekarang(self):
        self.click(mulai_sekarang)

    def type_mobile_no(self, mobile_no):
        self.set_text(text_input, mobile_no)

    def click_selanjutnya(self):
        self.click(selanjutnya)

    def enter_otp(self, otp):
        self.set_text(text_input, otp)

    def set_pin(self, pin):
        self.set_text(set_pin, pin)

    def verify_risk_profile_page(self):
        self.assert_element_present(risk_profile)

    def click_agresif_profile(self):
        self.click(agresif)


