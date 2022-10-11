from appiumbase import BaseCase
from SiminvestAppQa.src.data.userData import user_data
from SiminvestAppQa.src.pages.Android_pages.home_page import HomePage
import allure
from SiminvestAppQa.src.utilities.genericUtilities import generate_random_integer

mulai_sekarang = "WelcomeScreenMulaiSekarangButton"
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
daftar_masuk_btn = '//android.widget.TextView[@text="Daftar / Masuk"]'
masuk_page_header = '//android.widget.TextView[@text="Masuk"]'
informasi_btn = '//android.widget.TextView[@text="Informasi RDN"]'
profile_icon = 'ProfilePageImage'
#profile_icon = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]'
batan_btn = '//android.widget.TextView[@text="Batal"]'
batan_btn1 = '//android.widget.TextView[@text="BATAL"]'
camera_option = '//android.widget.TextView[@text="Camera"]'
take_pic_allow = '//android.widget.Button[@text="ALLOW"]'
location_allow = '//android.widget.Button[@text="Allow only while using the app"]'
take_pic = 'Shutter'
done_btn = 'Done'
crop_btn = 'Crop'
gallery_option = '//android.widget.TextView[@text="Upload From Photos"]'
image = '//android.widget.LinearLayout[@content-desc="Laptop_with_code.jpg, 2.48 MB, 4:58 AM"]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.ImageView'
slider_on_akun = 'RefferalPageStarpointSlider'
teman_telah_btn = 'RefferalPageTeman'
teman_page_header = '//android.widget.TextView[@text="Daftar Teman"]'
syrat_btn = 'RefferalPageSyarat'
syrat_page_header = '//android.widget.TextView[@text="Syarat dan ketentuan"]'
text_after_loading = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[4]/android.webkit.WebView'
Cara_Kerja_btn = 'RefferalPageCara'
Cara_Keraja_page_header = '//android.widget.TextView[@text="Cara Kerja"]'
Cara_kerja_loading = '//android.widget.TextView[@text="Oops, this help center no longer exists"]'
#Akun Pengguna
akun_pengguna = 'ScreenProfileCardTextSubEntryEntry1'
informtion_tab = 'ProfileDetailsPersonalTab'
personal_tab ='(//android.view.ViewGroup[@content-desc="ProfileDetailsPersonalTab"])[2]'
serkuritas_tab = '(//android.view.ViewGroup[@content-desc="ProfileDetailsPersonalTab"])[2]'
sid='ProfileDetailsSID'
sid_value = 'ProfileDetailsSIDValue'
name = 'ProfileDetailsName'
name_value = 'ProfileDetailsNameValue'
number_details = 'ProfileDetailsNo'
number_value = 'ProfileDetailsNoValue'
email = 'ProfileDetailsEmail'
email_value = 'ProfileDetailsEmailValue'
address = 'ProfileDetailsAddress'
address_value = 'ProfileDetailsAddressValue'
#serkuritas tab
clientID = 'ProfileDetailsClientID'
clientID_value = 'ProfileDetailsClientIDValue'
Sub_Rekening = "ProfileDetailsRekening"
Sub_Rekening_value='ProfileDetailsRekeningValue'
bank = 'ProfileDetailsBankName'
bank_value = 'ProfileDetailsBankNameValue'
pemilik = 'ProfileDetailsPemilik'
pemilik_value ='ProfileDetailsPemilikValue'
no_rekening = 'ProfileDetailsNoRem'
#no_rekening_value = 'ProfileDetailsNoRemValue'
personal_bank = 'ProfileDetailsPersonalBank'
personal_bank_value = 'ProfileDetailsPersonalBankValue'
personal_pemilik = 'ProfileDetailsPersonalPemilik'
personal_pemilik_value = 'ProfileDetailsPersonalPemilikValue'
personal_no_rekening = 'ProfileDetailsPersonalNo'
personal_no_rekening_value = '//android.widget.TextView[@content-desc="ProfileDetailsPersonaNoValue"]'
#informasi tab
informasi_tab='ScreenProfileCardTextSubEntryEntry2'
RDn_page_header = 'RdnBalanceHeader'
RDN_balance = 'RdnBalanceValue'
top_up_btn = 'RdnBalanceTopIcon'
tarik_dana_btn = 'RdnBalanceTarikIcon'
riwayat_btn = 'RdnBalanceRiwayatIcon'
informasi_saldo_tab = 'RdnBalanceSaldo'
informasi_rekening_tab ='RdnBalanceRekening'
top_page_header= 'TopupPageHeader'
simbosi_title = 'TopupPageSimobiTitle'
top_up_bank_title= 'TopupPageBankTitle'
tarik_dana_page_header = 'Tarik DanaHeader'
tarik_dana_nominal='TarikPageNominal'
tarik_page_btn ='TarikPageBtn'
pop_up_msg_11 = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[2]'
pop_up_msg_11_text='Permintaan penarikkan dana diatas pukul 11.00 WIB akan di proses di hari kerja bursa berikutnya.'
pop_up_msg_rquired_fund='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[2]'
pop_up_msg_rquired_fund_text='Cash Withdrawal Required more Fund.'
riwayat_page_header ='RiwayatHeader'
riwayat_page_entry= 'RiwayatPageEntry0'
entry_name = 'RiwayatPageName0'
entry_date = 'RiwayatPageTime0'
entry_value = 'RiwayatPageRpValue0'
entry_status = 'RiwayatPageStatus0'
#pengaturan tab locators
pengaturan_tab = 'ScreenProfileCardTextSubEntryEntry3'
Pengaturan_Page_Header='PengaturanPageHeader'
ganti_pin_siminvest = 'PengaturanPagePinSiminvest'
ganti_pin_sekuritas = 'PengaturanPageGantiPin'
ganti_passsword_tab = '(//android.view.ViewGroup[@content-desc="GantiPagePasswordTab"])[1]'
ganti_pin_tab = '(//android.view.ViewGroup[@content-desc="GantiPagePasswordTab"])[2]'
password_lama = '//android.view.ViewGroup[@content-desc="GantiPagePasswordLama"]/android.widget.EditText'
password_lama_show = 'GantiPagePasswordLamaShow'
password_baru = '//android.view.ViewGroup[@content-desc="GantiPagePasswordBaru"]/android.widget.EditText'
password_baru_show = 'GantiPagePasswordBaruShow'
conf_pass_baru = '//android.view.ViewGroup[@content-desc="GantiPagePasswordConfirm"]/android.widget.EditText'
conf_pass_baru_show = 'GantiPagePasswordConfirmShow'
password_baru_error = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[5]/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[3]'
password_baru_error_2_text = 'Password Baru minimal 6 karakter'
password_baru_error_1_text = 'Password Baru must contain at least one uppercase letter.'
conf_pass_baru_error ='hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[5]/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[4]'
conf_pass_baru_error_text ='Konfirmasi Password Baru tidak sama. Mohon ulangi lagi'
pin_lama ='//android.view.ViewGroup[@content-desc="GantiPagePinLama"]/android.widget.EditText'
pin_lama_show = 'GantiPagePinLamaShow'
pin_baru = '//android.view.ViewGroup[@content-desc="GantiPagePinBaru"]/android.widget.EditText'
pin_baru_show = 'GantiPagePinBaruShow'
pin_baru_error = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[5]/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[3]'
pin_baru_error_1_text ='PIN Baru minimal 6-15 karakter'
pin_baru_error_2_text = 'PIN Baru maksimal 15 karakter'
pin_conf_baru ='//android.view.ViewGroup[@content-desc="GantiPageBaruConfirm"]/android.widget.EditText'
pin_conf_baru_show = 'GantiPageBaruConfirmShow'
pin_conf_baru_error ='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[5]/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[4]'
pin_conf_baru_error_1_text = 'Konfirmasi PIN Baru salah. Mohon ulangi lagi'
#other tabs locators
pt_sinarmas = '(//android.view.ViewGroup[@content-desc="ProfilePageEntry0"])[2]'
equity_page = '//android.view.View[@text="EQUITY"]'
hubunagi_tab = '(//android.view.ViewGroup[@content-desc="ProfilePageEntry1"])[2]'
hubungi_header = '//android.widget.TextView[@text="Hubungi Kami"]'
hubungi_email = '//android.widget.TextView[@text="cs@sinarmassekuritas.co.id"]'
hubungi_number = '//android.widget.TextView[@text="150555"]'
hubungi_whatsapp = '//android.widget.TextView[@text="Whatsapp"]'
FAQs_tab = '(//android.view.ViewGroup[@content-desc="ProfilePageEntry2"])[2]'
FAQ_header = '//android.widget.TextView[@text="FAQs"]'
logout_btn ='ProfilePageLogoutButton'
Home_page_locator = "//android.widget.TextView[@text='Mulai Investasi Yuk…']"
Home_page_text = "Mulai Investasi Yuk…"

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

    @allure.step("Login with new number")
    def login_with_non_kyc_number(self, number):
        self.click_mulai_sekarang()
        self.type_mobile_no(number)
        self.click_selanjutnya()
        self.enter_otp(user_data['valid_otp'])
        self.enter_pin()
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
        self.sleep(1)
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
        self.sleep(2)
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

    @allure.step("Verify daftar masuk btn available")
    def verify_daftar_masuk_btn(self):
        self.assert_equal(self.is_element_visible(daftar_masuk_btn), True)

    @allure.step("Click on daftar masuk btn")
    def click_on_Daftar_masuk_btn(self):
        self.click(daftar_masuk_btn)
        self.sleep(2)

    @allure.step("Verify redirection to masuk page")
    def verify_redirection_masuk_page(self):
        self.assert_equal(self.is_element_visible(masuk_page_header), True)

    @allure.step("Verify informasi btn on profile page for non kyc user")
    def verify_informasi_btn_on_profile_page_for_non_kyc_user(self):
        self.sleep(2)
        self.assert_equal(self.is_element_visible(informasi_btn), False)

    @allure.step("Click on akun pengaturn")
    def click_on_akun_pengaturn(self):
        self.sleep(2)
        self.click(akun_pengguna)
        self.sleep(1)

    @allure.step("Click on profile icon")
    def click_on_profile_icon(self):
        self.click(profile_icon)
        self.sleep(2)

    @allure.step("Click on batal btn")
    def click_batal_btn(self):
        self.click(batan_btn)
        self.sleep(1)

    @allure.step("Click on batal btn")
    def click_batal1_btn(self):
        self.click(batan_btn1)
        self.sleep(1)

    @allure.step("Verify image icon availability")
    def verify_image_icon_availability(self):
        self.sleep(3)
        self.assert_equal(self.is_element_visible(profile_icon), True)

    @allure.step("Upload image by camera option")
    def upload_image_by_camera_option(self):
        self.click(camera_option)
        self.sleep(2)
        self.click(take_pic_allow)
        self.sleep(2)
        self.click(take_pic_allow)
        self.sleep(2)
        #self.click(location_allow)
        #self.sleep(2)
        self.click(take_pic)
        self.sleep(2)
        self.click(done_btn)
        self.sleep(3)
        self.click(crop_btn)
        self.sleep(2)
        self.verify_image_icon_availability()

    @allure.step("Upload cancel process")
    def uplaod_cancel_process(self):
        self.click(camera_option)
        self.sleep(2)
        self.click(take_pic)
        self.click(done_btn)
        self.sleep(2)
        self.click_on_cancel()
        self.sleep(2)

    @allure.step("Upload image using gallery")
    def upload_image_using_gallery_option(self):
        self.click(gallery_option)
        self.sleep(1)
        self.click(take_pic_allow)
        self.sleep(1)
        self.tap(image)
        self.sleep(1)
        self.click(crop_btn)

    @allure.step("Verify slider on referral page")
    def verify_slider_on_referral_page(self):
        self.assert_equal(self.is_element_visible(slider_on_akun), True)

    @allure.step("Verify Teman telah btn")
    def verify_teman_telah_btn(self):
        self.click(teman_telah_btn)
        self.sleep(1)
        self.assert_equal(self.is_element_visible(teman_page_header), True)

    @allure.step("Verify Syarat dan btn")
    def verify_syarat_dan_btn(self):
        self.click(syrat_btn)
        self.sleep(1)
        self.assert_equal(self.is_element_visible(syrat_page_header), True)
        self.sleep(5)
        self.assert_equal(self.is_element_visible(text_after_loading), True)

    @allure.step("Verify Cara Kerja btn")
    def verify_cara_kerja_tab(self):
        self.sleep(1)
        self.click(Cara_Kerja_btn)
        self.sleep(1)
        self.assert_equal(self.is_element_visible(Cara_Keraja_page_header), True)
        self.sleep(5)
        self.assert_equal(self.is_element_visible(text_after_loading), True)

    @allure.step("Click on akun penggunna tab")
    def click_on_akun_penggunna_tab(self):
        self.click(akun_pengguna)
        self.sleep(2)

    @allure.step("Verify personal tab details in akun penggunna")
    def Verify_personal_tab_details_in_akun_penggunna(self, number):
        self.assert_equal(self.is_element_visible(informtion_tab), True)
        self.assert_equal(self.is_element_visible(sid), True)
        self.assert_equal(self.get_attribute(sid_value, 'text'), '')
        self.assert_equal(self.is_element_visible(name), True)
        self.assert_equal(self.get_attribute(name_value, 'text'), '-')
        self.assert_equal(self.is_element_visible(number_details), True)
        self.assert_equal(self.get_attribute(number_value, 'text'), number)
        self.assert_equal(self.is_element_visible(email), True)
        self.assert_equal(self.get_attribute(email_value, 'text'), '-')
        self.assert_equal(self.is_element_visible(address), True)
        self.assert_equal(self.get_attribute(address_value, 'text'), '-')

    @allure.step("Click on serkuritas tab")
    def click_on_serkuritas_tab(self):
        self.click(serkuritas_tab)
        self.sleep(2)

    @allure.step("Verify serkuritas tab details in akun penggunna")
    def Verify_serkuritas_tab_details_in_akun_penggunna(self):
        self.assert_equal(self.is_element_visible(clientID), True)
        self.assert_not_equal(self.get_attribute(clientID_value, 'text'), '-')
        self.assert_equal(self.is_element_visible(Sub_Rekening), True)
        self.assert_equal(self.get_attribute(Sub_Rekening_value, 'text'), '-')
        self.assert_equal(self.is_element_visible(bank), True)
        self.assert_equal(self.get_attribute(bank_value, 'text'), '-')
        self.assert_equal(self.is_element_visible(pemilik), True)
        self.assert_equal(self.get_attribute(pemilik_value, 'text'), '-')
        self.assert_equal(self.is_element_visible(no_rekening), True)
       # self.assert_equal(self.get_attribute(no_rekening_value, 'text'), '-')
        self.assert_equal(self.is_element_visible(personal_bank), True)
        self.assert_equal(self.get_attribute(personal_bank_value, 'text'), '-')
        self.assert_equal(self.is_element_visible(personal_pemilik), True)
        self.assert_equal(self.get_attribute(personal_pemilik_value, 'text'), '-')
        self.assert_equal(self.is_element_visible(personal_no_rekening), True)
        self.assert_equal(self.get_attribute(personal_no_rekening_value, 'text'), '-')

    @allure.step("Click on informasi tab")
    def click_on_informasi_tab(self):
        self.click(informasi_tab)

    @allure.step("Verify top up page")
    def verify_top_up_page(self):
        self.click(top_up_btn)
        self.sleep(1)
        self.assert_equal(self.is_element_visible(top_page_header), True)
        self.assert_equal(self.is_element_visible(simbosi_title), True)
        self.assert_equal(self.is_element_visible(top_up_bank_title), True)
        self.go_back()

    @allure.step("verify limit msg on tarik dana page")
    def verify_limit_msg_on_tarik_dana_page(self):
        self.set_text(tarik_dana_nominal, '1000')
        self.click(tarik_page_btn)
        self.assert_equal(self.get_attribute(pop_up_msg_rquired_fund,'text'),pop_up_msg_rquired_fund_text)
        self.click_on_ok_btn()
        self.set_text(tarik_dana_nominal, '100000')
        self.click(tarik_page_btn)
        self.assert_equal(self.get_attribute(pop_up_msg_11,'text'),pop_up_msg_11_text)
        self.click_on_ok_btn()
        self.sleep(1)
        self.assert_equal(self.is_element_visible(riwayat_page_header), True)
        self.go_back()

    @allure.step("verify riwayat page with details")
    def verify_riwayat_page_with_details(self):
        self.click(riwayat_btn)
        self.sleep(1)
        self.verify_riwayat_page()
        self.assert_equal(self.is_element_visible(entry_name), True)
        self.assert_equal(self.is_element_visible(entry_date), True)
        self.assert_equal(self.is_element_visible(entry_value), True)
        self.assert_equal(self.is_element_visible(entry_status), True)
        self.go_back()

    @allure.step("Verify Header of pengaturan tab page")
    def verify_pengaturan_page(self):
        self.sleep(2)
        self.assert_equal(self.is_element_visible(Pengaturan_Page_Header), True)
        self.assert_equal(self.is_element_visible(ganti_pin_siminvest), True)
        self.assert_equal(self.is_element_visible(ganti_pin_sekuritas), True)

    @allure.step("Verify Ganti password tab")
    def verify_ganti_password_tab(self):
        self.set_text(password_lama, '123457')
        self.assert_equal(self.get_attribute(password_lama, 'text'), '••••••')
        self.click(password_lama_show)
        self.assert_equal(self.get_attribute(password_lama, 'text'), '123457')
        self.set_text(password_baru, '1234')
        self.assert_equal(self.get_attribute(password_baru, 'text'), '••••')
        self.click(password_baru_show)
        self.assert_equal(self.get_attribute(password_baru, 'text'), '1234')
        self.assert_equal(self.get_attribute(password_baru_error, 'text'),password_baru_error_2_text)
        self.set_text(password_baru, '12347689')
        self.assert_equal(self.get_attribute(password_baru_error, 'text'), password_baru_error_1_text)
        self.set_text(conf_pass_baru, '1234')
        self.assert_equal(self.get_attribute(conf_pass_baru, 'text'), '••••')
        self.click(conf_pass_baru_show)
        self.assert_equal(self.get_attribute(conf_pass_baru, 'text'), '1234')
        #self.assert_equal(self.get_attribute(conf_pass_baru_error, 'text'), conf_pass_baru_error_text)

    def verify_ganti_pin_tab(self):
        self.click(ganti_pin_tab)
        self.set_text(pin_lama, '123567')
        self.assert_equal(self.get_attribute(pin_lama, 'text'), '••••••')
        self.click(pin_lama_show)
        self.sleep(1)
        self.assert_equal(self.get_attribute(pin_lama, 'text'), '123567')
        self.set_text(pin_baru, '1234')
        self.assert_equal(self.get_attribute(pin_baru, 'text'), '••••')
        self.click(pin_baru_show)
        self.assert_equal(self.get_attribute(pin_baru, 'text'), '1234')
        self.assert_equal(self.get_attribute(pin_baru_error, 'text'), pin_baru_error_1_text)
        self.set_text(pin_baru, '1234567890123456')
        self.assert_equal(self.get_attribute(pin_baru_error, 'text'), pin_baru_error_2_text)
        self.set_text(pin_baru, '123456')
        self.set_text(pin_conf_baru, '1234')
        self.assert_equal(self.get_attribute(pin_conf_baru, 'text'), '••••')
        self.click(pin_conf_baru_show)
        self.assert_equal(self.get_attribute(pin_conf_baru, 'text'), '1234')
        self.assert_equal(self.get_attribute(pin_conf_baru_error, 'text'), pin_conf_baru_error_1_text)

    @allure.step("Click and verify to PT Sinarmas tab")
    def click_and_verify_to_pt_sinarmas_tab(self):
        self.click(pt_sinarmas)
        self.sleep(16)
        #self.assert_equal(self.is_element_visible(equity_page), True)
        self.go_back()
        self.sleep(1)
        self.verify_phone_number_available_on_profile_page()

    @allure.step("Click and verify to hubunagi tab")
    def click_and_verify_to_hubunagi_tab(self):
        self.click(hubunagi_tab)
        self.sleep(1)
        self.assert_equal(self.is_element_visible(hubungi_header), True)
        self.assert_equal(self.is_element_visible(hubungi_email), True)
        self.assert_equal(self.is_element_visible(hubungi_number), True)
        self.assert_equal(self.is_element_visible(hubungi_whatsapp), True)
        self.go_back()
        self.sleep(1)
        self.verify_phone_number_available_on_profile_page()


    @allure.step("Click and verify to FAQs tab")
    def click_and_verify_to_FAQs_tab(self):
        self.click(FAQs_tab)
        self.sleep(3)
        self.assert_equal(self.is_element_visible(FAQ_header), True)
        self.sleep(2)
        self.go_back()
        self.sleep(2)
        self.verify_phone_number_available_on_profile_page()

    @allure.step("Verify mulai text on profile page")
    def verify_mulai_text_on_profile_page(self):
        Home_page_locator_text = self.get_attribute(Home_page_locator, "text")
        self.assert_equal(Home_page_locator_text, Home_page_text)

    @allure.step("click mulai sekarang")
    def click_mulai_sekarang_after_profile(self):
        #self.sleep(1)
        self.click(mulai_sekarang)

    @allure.step("login and verify homepage for rg user")
    def login_and_verify_homepage_from_logout(self, phone_number):
        self.sleep(4)
        self.click_mulai_sekarang_after_profile()
        self.type_mobile_no(phone_number)
        self.click_selanjutnya()
        self.enter_otp('1234')
        self.enter_pin()
        #self.close_home_page_banner()
        self.verify_home_page()