from SiminvestAppQa.src.pages.Android_pages.home_page import HomePage
from SiminvestAppQa.src.data.userData import user_data
from datetime import datetime
import allure
import logging as logger
from SiminvestAppQa.src.utilities.requestUtilities import RequestsUtilities

request_utilities = RequestsUtilities()
gamification_check_box= "//android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ImageView"
gamification_button= "reward_forward_icon"
sdp_keystate = "//android.widget.TextView[@text='Keystats']"
tc_submit= "//android.widget.TextView[@text='Submit']"
gamification_header= 'MissionHeader'
mission_status= 'Mission_status_text'
mission_xp= 'Mission_xp_value'
mission_msg= '//android.view.ViewGroup[@content-desc="Mission_text_1"]/android.widget.TextView[1]'
ob_entry_2='//android.view.ViewGroup[@content-desc="Onboarding_entry_2"]/android.view.ViewGroup'
ob_entry_1='//android.view.ViewGroup[@content-desc="Onboarding_entry_1"]/android.view.ViewGroup'
ob_entry_3='//android.view.ViewGroup[@content-desc="Onboarding_entry_3"]/android.view.ViewGroup'
harian_subtab= "Mission_Harian_kamu"
onboarding_subtab= "Onboarding_text"
transaksi_subtab= "Transaction_text"
frekuensi_subtab= "Frequency_text"
referral_subtab= "Referral_text"
back_button = "MissionPage_back"
kerja_webpage= "//android.view.ViewGroup[2]/android.widget.TextView"
webpage_back= "//android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.ImageView"
menu= "Mission_page_menu"
kerja_button= "//android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup"
level_btn= '//android.view.ViewGroup[@content-desc="Mission_level_icon"]/android.widget.ImageView'
level_backward='Level_backward'
level_forward='Level_forward'
level_header = "Level_header"
level_name='(//android.widget.TextView[@content-desc="Level_name"])[1]'
xp_level= '(//android.widget.TextView[@content-desc="Level_name"])[2]'
level_entry_1= '(//android.view.ViewGroup[@content-desc="Level_enrty_1"])[1]'
level_1_text= '(//android.widget.TextView[@content-desc="Level_enrty_1_text"])[1]'
level_entry_2= '(//android.view.ViewGroup[@content-desc="Level_enrty_1"])[2]'
level_2_text= '(//android.widget.TextView[@content-desc="Level_enrty_1_text"])[2]'
level_entry_3= '(//android.view.ViewGroup[@content-desc="Level_enrty_1"])[3]'
level_3_text= '(//android.widget.TextView[@content-desc="Level_enrty_1_text"])[3]'
level_entry_4= '(//android.view.ViewGroup[@content-desc="Level_enrty_1"])[4]'
level_4_text= '(//android.widget.TextView[@content-desc="Level_enrty_1_text"])[4]'
level_back_button= "level_back_btn"
level_value= 'Level_value'
riwayat_btn= '//android.view.ViewGroup[@content-desc="Mission_riwayat_icon"]/android.widget.ImageView'
riwayat_header = "Riwayat_header"
lihat_header='LihatSemua_header'
onboarding_lihat_btn =  '//android.view.ViewGroup[@content-desc="Onboarding_lihat"]/android.widget.TextView'
transaction_lihat_btn='//android.view.ViewGroup[@content-desc="Transaction_lihat"]/android.widget.TextView'
frequency_lihat_btn='//android.view.ViewGroup[@content-desc="Frequency_lihat"]/android.widget.TextView'
referral_lihat_btn='//android.view.ViewGroup[@content-desc="Referral_lihat"]/android.widget.TextView'
lihat_semua_entry_1= 'LihatSemua_entry_1_value'
jalankan_misi_btn =  "//android.widget.TextView[@text='Jalankan Misi']"
info_btn='//android.view.ViewGroup[@content-desc="Mission_details_icon"]/android.widget.ImageView'
info_experince= "//android.widget.TextView[@text='Experience Point']"
harian_1_activity= '//android.view.ViewGroup[@content-desc="Harian_entry_1_activity"]/android.widget.TextView'
onboarding_1_activity= '//android.view.ViewGroup[@content-desc="Onboarding_entry_1_activity"]/android.widget.TextView'
transaction_1_activity= '//android.view.ViewGroup[@content-desc="Transaction_entry_1_activity"]/android.widget.TextView'
frequency_1_activity= '//android.view.ViewGroup[@content-desc="Frequency_entry_1_activity"]/android.widget.TextView'
referral_1_activity= '//android.view.ViewGroup[@content-desc="Referral_entry_1_activity"]/android.widget.TextView'
Harian_entry_1_xp= 'Harian_entry_1_xp'
Onboarding_entry_1_xp= 'Onboarding_entry_1_xp'
Transaction_entry_1_xp= 'Transaction_entry_1_xp'
Frequency_entry_1_xp= 'Frequency_entry_1_xp'
Referral_entry_1_xp= 'Referral_entry_1_xp'
saham_tab= '(//android.view.ViewGroup[@content-desc="PortPageSahamTab"])[1]'
xp_aktif= 'Riwayat_aktif'
xp_kedaluwarsa='Riwayat_Kedaluwarsa'
riwayat_back_btn='Riwayat_back_btn'
until_date='(//android.widget.TextView[@content-desc="Riwayat_entry_1_text"])[1]'
riwayat_xp_value='(//android.widget.TextView[@content-desc="Riwayat_entry_1_value"])[1]'
riwayat_mission_name='(//android.widget.TextView[@content-desc="Riwayat_entry_1_type"])[1]'
riwayat_mission_time='(//android.widget.TextView[@content-desc="Riwayat_entry_1_time"])[1]'

empty_smile_face='//android.view.ViewGroup/android.widget.ImageView'
empty_kedaluwarsa_msg= "//android.widget.TextView[@text='Yuk, jalankan misi dan kumpulkan XP!']"


class Gamification(HomePage):

    @allure.step("Open Gamification Page")
    def open_gamification_page(self,phone_number):
        self.sleep(4)
        self.click_mulai_sekarang()
        self.type_mobile_no(phone_number)
        self.click_selanjutnya()
        self.enter_otp('1234')
        self.enter_pin()
        self.verify_home_page_reg_user()
        self.click_on_profile_btn()
        self.sleep(1)
        self.click(gamification_button)
        self.sleep(1)
        if self.is_element_visible(gamification_check_box)==True:
            self.click(gamification_check_box)
            self.click(tc_submit)
            self.assert_equal(self.is_element_visible(gamification_header),True)
        else:
            self.assert_equal(self.is_element_visible(gamification_header),True)

    @allure.step("get mission xp")
    def get_mission_xp(self):
        value = self.get_attribute(mission_xp,"text")
        self.assert_in('/',value)
        index = value.find('/')
        xp_value = int(value[3:index-1].replace('.', ''))
        return xp_value

    @allure.step("get target mission xp")
    def get_target_mission_xp(self):
        value = self.get_attribute(mission_xp, "text")
        index = value.find('/')
        target_xp_value = int(value[index + 1:].replace('.', ''))
        return target_xp_value

    @allure.step("validate mission status")
    def validate_mission_status(self):
        status= self.get_attribute(mission_status,"text")
        value = self.get_mission_xp()
        if 0 <=value <=5000 :
            status == "Pemimpi"
        elif 5000< value <=25000 :
            status == "Juragan"
        elif 25000< value <=75000 :
            status == "Tajir"
        elif 75000< value <=150000 :
            status == "Konglo"
        elif 150000< value:
            status == "Sultan"

    @allure.step("validate mission message")
    def validate_mission_message(self):
        actual_message= self.get_attribute(mission_msg,"text")
        current_xp= self.get_mission_xp()
        target_xp= self.get_target_mission_xp()
        rest_xp= str(target_xp-current_xp)
        self.assert_in(rest_xp, actual_message)
        expected_message= rest_xp+" XP lagi buat naik ke level Juragan, yuk bisa yuk! "
        self.assert_equal(actual_message,expected_message)

    @allure.step("validate swipe functionality")
    def validate_swipe_functionality(self):
        self.scroll_screen(start_x=500, start_y=1820, end_x=523, end_y=1400, duration=10000)
        self.assert_equal(self.is_element_visible(ob_entry_1), True)
        self.swipe_between_element(ob_entry_2, ob_entry_3)
        self.sleep(1)
        self.assert_equal(self.is_element_visible(ob_entry_1), False)

    @allure.step("Validate sub tabs visiblity")
    def validate_subtabs_visiblity(self):
        self.assert_equal(self.is_element_visible(harian_subtab), True)
        self.assert_equal(self.is_element_visible(onboarding_subtab), True)
        self.scroll_screen(start_x=500, start_y=2000, end_x=500, end_y=300, duration=5000)
        self.assert_equal(self.is_element_visible(transaksi_subtab), True)
        self.assert_equal(self.is_element_visible(frekuensi_subtab), True)
        self.assert_equal(self.is_element_visible(referral_subtab), True)
        self.assert_equal(self.is_element_visible(back_button), True)
        self.scroll_screen(start_x=500, start_y=200, end_x=500, end_y=3000, duration=5000)
        self.sleep(1)

    @allure.step("validate cara kerja")
    def validate_cara_kerja(self):
        self.click(menu)
        self.click(kerja_button)
        self.sleep(2)
        self.assert_equal(self.is_element_visible(kerja_webpage), True)
        self.assert_equal(self.is_element_visible(webpage_back), True)

    @allure.step("Validate swipe functionality on cara kerja webpage")
    def validate_swipe_functionality_on_cara_kerja_webpage(self):
        self.scroll_screen(start_x=500, start_y=2000, end_x=500, end_y=500, duration=5000)
        self.assert_equal(self.is_element_visible(kerja_webpage), True)
        self.assert_equal(self.is_element_visible(webpage_back), True)

    @allure.step("Validate back button functionality on cara kerja webpage")
    def validate_back_button_functionality_on_cara_kerja_webpage(self):
        self.click(webpage_back)
        self.sleep(1)
        self.assert_equal(self.is_element_visible(gamification_header), True)

    @allure.step("Validate level button functionality")
    def validate_level_button_functionality(self):
        self.click(level_btn)
        self.sleep(2)
        self.assert_equal(self.is_element_visible(level_header), True)
        self.go_back()
        self.sleep(1)

    @allure.step("Validate riwayat button functionality")
    def validate_riwayat_button_functionality(self):
        self.click(riwayat_btn)
        self.sleep(1)
        self.assert_equal(self.is_element_visible(riwayat_header), True)
        self.go_back()
        self.sleep(1)

    @allure.step("Validate info button functionality")
    def validate_info_button_functionality(self):
        self.click(info_btn)
        self.sleep(1)
        self.assert_equal(self.is_element_visible(info_experince), True)
        self.go_back()
        self.sleep(1)

    @allure.step("Validate lihat semua button functionality")
    def validate_lihat_semua_functionality(self):
        self.click(onboarding_lihat_btn)
        self.sleep(1)
        self.assert_equal(self.is_element_visible(lihat_semua_entry_1), True)
        self.go_back()
        self.sleep(1)

    @allure.step("Validate menu button functionality")
    def validate_menu_button_functionality(self):
        self.click(menu)
        self.sleep(1)
        self.assert_equal(self.is_element_visible(kerja_button), True)
        self.click(back_button)
        self.sleep(1)

    @allure.step("Validate back button functionality")
    def validate_back_button_functionality(self):
        self.click(back_button)
        self.sleep(1)
        self.assert_equal(self.is_element_visible(gamification_button), True)

    @allure.step("Collect api data for gamification")
    def collect_api_data_for_gamification(self):
        token_value = self.login()
        token = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJpWlYzdUJkTkJyTDA4dVIzQUR2bmg4akdTdHNkSHpQVSIsInN1YiI6IlNpbWFzSW52ZXN0In0.Kj31bgBrbc94NaUDKWgbx-N4ZBQNFsrZBmF7xtZ4hNo"}
        token['Authorization'] = 'Bearer ' + token_value
        gamification_rs = request_utilities.get(base_url='https://stg-api.siminvest.co.id/', endpoint='radix/v1/account/45997/balance/2', headers=token,expected_status_code=200)
        logger.info(gamification_rs)
        code_api = gamification_rs['code']
        xp_value_api =gamification_rs['data']['value']
        success_api = gamification_rs['is_success']
        message_api = gamification_rs['message']
        return code_api, xp_value_api, success_api, message_api

    @allure.step("Collect mission list api data")
    def collect_mission_list_api_data(self):
        token_value = self.login()
        token = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJpWlYzdUJkTkJyTDA4dVIzQUR2bmg4akdTdHNkSHpQVSIsInN1YiI6IlNpbWFzSW52ZXN0In0.Kj31bgBrbc94NaUDKWgbx-N4ZBQNFsrZBmF7xtZ4hNo"}
        token['Authorization'] = 'Bearer ' + token_value
        mission_list_rs = request_utilities.get(base_url='https://stg-api.siminvest.co.id/', endpoint='reverb/v1/account/45997/mission?limit=50&sort_by=type_id,status&is_asc=true', headers=token,expected_status_code=200)
        logger.info(mission_list_rs)
        ids_api= []
        lables_api=[]
        xps_api=[]
        for i in range(len(mission_list_rs['data'])):
            ids_api.append(mission_list_rs['data'][i]['id'])
            lables_api.append(mission_list_rs['data'][i]['campaign']['label'])
            xps_api.append(mission_list_rs['data'][i]['campaign']['extra']['reward_xp'])
        return ids_api,lables_api,xps_api

    @allure.step("Collect ui data for gamification")
    def collect_ui_data_for_gamification(self):
        harian_1= self.get_attribute(harian_1_activity,"text")
        harian_1_xp= (self.get_attribute(Harian_entry_1_xp,"text")).replace('+','').replace(',','').replace('XP', '')
        self.scroll_screen(start_x=500, start_y=2100, end_x=500, end_y=300, duration=6000)
        onboarding_1= self.get_attribute(onboarding_1_activity,"text")
        onboarding_1_xp = (self.get_attribute(Onboarding_entry_1_xp, "text")).replace('+', '').replace(',', '').replace('XP','')
        transaction_1= self.get_attribute(transaction_1_activity,"text")
        transaction_1_xp = (self.get_attribute(Transaction_entry_1_xp, "text")).replace('+', '').replace(',', '').replace('XP','')
        frequency_1= self.get_attribute(frequency_1_activity,"text")
        frequency_1_xp = (self.get_attribute(Frequency_entry_1_xp, "text")).replace('+', '').replace(',', '').replace('XP','')
        referral_1= self.get_attribute(referral_1_activity,"text")
        referral_1_xp = (self.get_attribute(Referral_entry_1_xp, "text")).replace('+', '').replace(',', '').replace('XP','')
        labels_ui= []
        labels_ui.extend([harian_1,onboarding_1,transaction_1,frequency_1, referral_1])
        XPs_Ui= []
        XPs_Ui.extend([int(harian_1_xp), int(onboarding_1_xp), int(transaction_1_xp), int(frequency_1_xp), int(referral_1_xp)])
        return labels_ui,XPs_Ui

    @allure.step("Get Level name from gamification page")
    def get_Level_name_from_gamification_page(self):
        status_on_gamification = self.get_attribute(mission_status, "text")
        return status_on_gamification

    @allure.step("Open Level Benefit page")
    def open_level_benefit_page(self):
        self.click(level_btn)
        self.sleep(1)

    @allure.step("Validate default level name")
    def validate_default_level_name(self):
        status_on_gamification= self.get_Level_name_from_gamification_page()
        self.open_level_benefit_page()
        status_on_level_page = self.get_attribute(level_name, "text")
        self.assert_equal(status_on_gamification,status_on_level_page)

    @allure.step("functional validation for level forward and backward button")
    def functional_validation_for_level_forward_and_backward_button(self):
        self.assert_equal(self.get_attribute(level_name, 'text'), 'Pemimpi')
        self.click(level_forward)
        self.assert_equal(self.get_attribute(level_name, 'text'), 'Juragan')
        self.click(level_backward)

    @allure.step("validate level entry are not clickable")
    def validate_level_entry_are_not_clickable(self):
        self.assert_equal(self.get_attribute(level_entry_1, 'clickable'), 'false')
        self.assert_equal(self.get_attribute(level_entry_2, 'clickable'), 'false')

    @allure.step("validate level back button is not scrollable")
    def validate_level_back_button_is_not_scrollable(self):
        self.assert_equal(self.get_attribute(level_back_button, 'scrollable'), 'false')
        self.assert_equal(self.get_attribute(level_header, 'scrollable'), 'false')

    @allure.step("Validate refresh functionality for level page")
    def validate_refresh_functionality_for_level_page(self):
        self.scroll_down()
        self.assert_equal(self.get_attribute(level_name, 'text'), 'Pemimpi')
        self.click(level_forward)
        self.assert_equal(self.get_attribute(level_name, 'text'), 'Juragan')
        self.click(level_back_button)
        self.sleep(1)
        self.click(level_btn)
        self.sleep(1)
        self.assert_equal(self.get_attribute(level_name, 'text'), 'Pemimpi')

    @allure.step("validate pemimpi level")
    def validate_pemimpi_level(self):
        self.assert_equal(self.get_attribute(level_value, 'text'), 'Level Kamu saat ini')
        self.assert_equal(self.get_attribute(xp_level, 'text'), 'XP 0')
        self.assert_equal(self.get_attribute(level_1_text, 'text'), 'StarPoin setiap transaksi')
        self.assert_equal(self.get_attribute(level_2_text, 'text'), 'Gratis Biaya Penarikan RDN')


    @allure.step("validate juragan level")
    def validate_juragan_level(self):
        self.click(level_forward)
        self.assert_equal(self.get_attribute(level_name, 'text'), 'Juragan')
        self.assert_equal(self.get_attribute(xp_level, 'text'), 'XP 5.000')
        self.assert_equal(self.get_attribute(level_1_text, 'text'), 'StarPoin setiap transaksi')
        self.assert_equal(self.get_attribute(level_2_text, 'text'), 'Gratis 500 XP')
        self.assert_equal(self.get_attribute(level_3_text, 'text'), 'Gratis Biaya Penarikan RDN')

    @allure.step("validate_tajir_konglo_sultan_level")
    def validate_tajir_konglo_sultan_level(self):
        self.click(level_forward)
        self.assert_equal(self.get_attribute(level_name, 'text'), 'Tajir')
        self.assert_equal(self.get_attribute(xp_level, 'text'), 'XP 25.000')
        self.assert_equal(self.get_attribute(level_1_text, 'text'), 'StarPoin setiap transaksi')
        self.assert_equal(self.get_attribute(level_2_text, 'text'), 'Gratis 1,000 XP')
        self.assert_equal(self.get_attribute(level_3_text, 'text'), 'Bonus StarPoin 10,000 poin')
        self.assert_equal(self.get_attribute(level_4_text, 'text'), 'Gratis Biaya Penarikan RDN')
        self.click(level_forward)
        self.assert_equal(self.get_attribute(level_name, 'text'), 'Konglo')
        self.assert_equal(self.get_attribute(xp_level, 'text'), 'XP 75.000')
        self.assert_equal(self.get_attribute(level_1_text, 'text'), 'StarPoin setiap transaksi')
        self.assert_equal(self.get_attribute(level_2_text, 'text'), 'Gratis 1,500 XP')
        self.assert_equal(self.get_attribute(level_3_text, 'text'), 'Bonus StarPoin 25,000 poin')
        self.assert_equal(self.get_attribute(level_4_text, 'text'), 'Gratis Biaya Penarikan RDN')
        self.click(level_forward)
        self.assert_equal(self.get_attribute(level_name, 'text'), 'Sultan')
        self.assert_equal(self.get_attribute(xp_level, 'text'), 'XP 150.000')
        self.assert_equal(self.get_attribute(level_1_text, 'text'), 'StarPoin setiap transaksi')
        self.assert_equal(self.get_attribute(level_2_text, 'text'), 'Gratis 2,000 XP')
        self.assert_equal(self.get_attribute(level_3_text, 'text'), 'Bonus StarPoin 50,000 poin')
        self.assert_equal(self.get_attribute(level_4_text, 'text'), 'Gratis Biaya Penarikan RDN')
        self.click(level_backward)
        self.assert_equal(self.get_attribute(level_name, 'text'), 'Konglo')
        self.click(level_backward)
        self.assert_equal(self.get_attribute(level_name, 'text'), 'Tajir')
        self.click(level_backward)
        self.assert_equal(self.get_attribute(level_name, 'text'), 'Juragan')
        self.click(level_backward)
        self.assert_equal(self.get_attribute(level_name, 'text'), 'Pemimpi')

    @allure.step("Collect level api data")
    def collect_level_api_data(self):
        token_value = self.login()
        token = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJpWlYzdUJkTkJyTDA4dVIzQUR2bmg4akdTdHNkSHpQVSIsInN1YiI6IlNpbWFzSW52ZXN0In0.Kj31bgBrbc94NaUDKWgbx-N4ZBQNFsrZBmF7xtZ4hNo"}
        token['Authorization'] = 'Bearer ' + token_value
        level_rs = request_utilities.get(base_url='https://stg-api.siminvest.co.id/',endpoint='reborn/v1/config?name=gamification&type=level',headers=token, expected_status_code=200)
        level_xp_api= []
        for i in range(len(level_rs['data']['gamification_level'])):
            level_xp_api.append(level_rs['data']['gamification_level'][i]['xp_min'])
        return level_xp_api

    @allure.step("Collect level ui data")
    def collect_level_ui_data(self):
        self.open_level_benefit_page()
        self.click(level_backward)
        value= self.get_attribute(xp_level, 'text')
        pemimpi_xp = int(value.replace('XP ', '').replace('.', ''))
        self.click(level_forward)
        value = self.get_attribute(xp_level, 'text')
        juragan_xp = int(value.replace('XP ', '').replace('.', ''))
        self.click(level_forward)
        value = self.get_attribute(xp_level, 'text')
        tajir_xp = int(value.replace('XP ', '').replace('.', ''))
        self.click(level_forward)
        value = self.get_attribute(xp_level, 'text')
        konglo_xp = int(value.replace('XP ', '').replace('.', ''))
        self.click(level_forward)
        value = self.get_attribute(xp_level, 'text')
        sultan_xp = int(value.replace('XP ', '').replace('.', ''))
        level_xp_ui = []
        level_xp_ui.extend([pemimpi_xp, juragan_xp, tajir_xp, konglo_xp, sultan_xp])
        return level_xp_ui

    @allure.step("Button Response Validation on mission list page")
    def button_response_validation_on_mission_list_page(self):
        self.click(onboarding_lihat_btn)
        self.sleep(1)
        self.assert_equal(self.is_element_visible(lihat_semua_entry_1), True)
        self.click(jalankan_misi_btn)
        self.sleep(1)
        self.go_back()
        self.assert_equal(self.is_element_visible(lihat_semua_entry_1), True)
        self.go_back()
        self.sleep(1)
        self.assert_equal(self.is_element_visible(gamification_header), True)

    @allure.step("open onboarding lihat semua")
    def open_onboarding_lihat_semua(self):
        self.click(onboarding_lihat_btn)
        self.sleep(1)
        self.assert_equal(self.get_attribute(lihat_header, 'text'), 'Onboarding ')
        self.assert_equal(self.get_attribute(lihat_header, 'scrollable'), 'false')
        self.go_back()

    @allure.step("open transaction lihat semua")
    def open_transaction_lihat_semua(self):
        self.scroll_screen(start_x=500, start_y=1900, end_x=500, end_y=300, duration=6000)
        self.click(transaction_lihat_btn)
        self.sleep(1)
        self.assert_equal(self.get_attribute(lihat_header, 'text'), 'Transaksi')
        self.assert_equal(self.get_attribute(lihat_header, 'scrollable'), 'false')
        self.go_back()

    @allure.step("open frequency lihat semua")
    def open_frequency_lihat_semua(self):
        self.click(frequency_lihat_btn)
        self.sleep(1)
        self.assert_equal(self.get_attribute(lihat_header, 'text'), 'Frekuensi')
        self.assert_equal(self.get_attribute(lihat_header, 'scrollable'), 'false')
        self.go_back()

    @allure.step("open refferal lihat semua")
    def open_refferal_lihat_semua(self):
        self.click(referral_lihat_btn)
        self.sleep(1)
        self.assert_equal(self.get_attribute(lihat_header, 'text'), 'Referral')
        self.assert_equal(self.get_attribute(lihat_header, 'scrollable'), 'false')
        self.go_back()

    @allure.step("Validate redirection of Jalankan Misi")
    def validate_redirection_of_jalankan_misi(self):
        #self.scroll_screen(start_x=500, start_y=200, end_x=500, end_y=3000, duration=5000)
        self.click(onboarding_lihat_btn)
        self.sleep(1)
        self.click(jalankan_misi_btn)
        self.sleep(2)
        self.assert_equal(self.is_element_visible(saham_tab),True)

    @allure.step("Collect mission list filtered api data")
    def collect_mission_list_filtered_api_data(self):
        token_value = self.login()
        token = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJpWlYzdUJkTkJyTDA4dVIzQUR2bmg4akdTdHNkSHpQVSIsInN1YiI6IlNpbWFzSW52ZXN0In0.Kj31bgBrbc94NaUDKWgbx-N4ZBQNFsrZBmF7xtZ4hNo"}
        token['Authorization'] = 'Bearer ' + token_value
        list_filtered_rs = request_utilities.get(base_url='https://stg-api.siminvest.co.id/', endpoint='reverb/v1/account/45997/mission?limit=50&sort_by=type_id,status&is_asc=true', headers=token,expected_status_code=200)
        ob_label_api = []
        ob_xp_api = []
        trans_label_api = []
        trans_xp_api = []
        freq_label_api = []
        freq_xp_api = []
        refer_label_api = []
        refer_xp_api = []
        for i in range(len(list_filtered_rs['data'])):
            if list_filtered_rs['data'][i]['campaign']['type_id']==4:
                ob_label_api.append(list_filtered_rs['data'][i]['campaign']['label'])
                ob_xp_api.append(list_filtered_rs['data'][i]['campaign']['extra']['reward_xp'])
            if list_filtered_rs['data'][i]['campaign']['type_id']==6:
                trans_label_api.append(list_filtered_rs['data'][i]['campaign']['label'])
                trans_xp_api.append(list_filtered_rs['data'][i]['campaign']['extra']['reward_xp'])
            if list_filtered_rs['data'][i]['campaign']['type_id']==9:
                freq_label_api.append(list_filtered_rs['data'][i]['campaign']['label'])
                freq_xp_api.append(list_filtered_rs['data'][i]['campaign']['extra']['reward_xp'])
            if list_filtered_rs['data'][i]['campaign']['type_id']==10:
                refer_label_api.append(list_filtered_rs['data'][i]['campaign']['label'])
                refer_xp_api.append(list_filtered_rs['data'][i]['campaign']['extra']['reward_xp'])
        return ob_label_api,ob_xp_api,trans_label_api,trans_xp_api,freq_label_api,freq_xp_api,refer_label_api,refer_xp_api

    @allure.step("Collect mission list filtered Ui data")
    def collect_mission_list_filtered_Ui_data(self):
        self.click(onboarding_lihat_btn)
        self.sleep(1)
        ob_label_ui=[]
        ob_xp_ui=[]
        for i in range (1,4):
            ob_xp_ui.append(int(self.get_attribute(f"LihatSemua_entry_{i}_value", 'text').replace('+', '').replace(',', '').replace('XP', '')))
            ob_label_ui.append(self.get_attribute(f"LihatSemua_entry_{i}_type", 'text'))
        self.go_back()
        self.scroll_screen(start_x=500, start_y=1900, end_x=500, end_y=300, duration=6000)
        self.click(transaction_lihat_btn)
        self.sleep(1)
        trans_xp_ui = []
        trans_label_ui=[]
        for i in range (1,4):
            trans_xp_ui.append(int(self.get_attribute(f"LihatSemua_entry_{i}_value", 'text').replace('+', '').replace(',', '').replace('XP', '')))
            trans_label_ui.append(self.get_attribute(f"LihatSemua_entry_{i}_type", 'text'))
        self.go_back()
        self.click(frequency_lihat_btn)
        self.sleep(1)
        freq_xp_ui=[]
        freq_label_ui=[]
        for i in range(1, 4):
            freq_xp_ui.append(
                int(self.get_attribute(f"LihatSemua_entry_{i}_value", 'text').replace('+', '').replace(',', '').replace(
                    'XP', '')))
            freq_label_ui.append(self.get_attribute(f"LihatSemua_entry_{i}_type", 'text'))
        self.go_back()
        self.click(referral_lihat_btn)
        self.sleep(1)
        refer_xp_ui=[]
        refer_label_ui=[]
        for i in range(1, 4):
            refer_xp_ui.append(
                int(self.get_attribute(f"LihatSemua_entry_{i}_value", 'text').replace('+', '').replace(',', '').replace(
                    'XP', '')))
            refer_label_ui.append(self.get_attribute(f"LihatSemua_entry_{i}_type", 'text'))
        return ob_label_ui,ob_xp_ui,trans_label_ui,trans_xp_ui,freq_label_ui,freq_xp_ui,refer_label_ui,refer_xp_ui

    @allure.step("Open Riwayat Page")
    def open_riwayat_page(self):
        self.click(riwayat_btn)
        self.sleep(1)
        self.assert_equal(self.is_element_visible(riwayat_header), True)

    @allure.step("Validate Active XP, Expired XP, back button, until date, xp value visibility")
    def validate_active_xp_expired_xp_back_button_until_date_xp_value_visibility(self):
        self.assert_equal(self.is_element_visible(xp_aktif),True)
        self.assert_equal(self.is_element_visible(xp_kedaluwarsa),True)
        self.assert_equal(self.is_element_visible(riwayat_back_btn),True)
        self.assert_equal(self.is_element_visible(until_date),True)
        self.assert_equal(self.is_element_visible(riwayat_xp_value),True)
        self.assert_equal(self.is_element_visible(riwayat_mission_name),True)
        self.assert_equal(self.is_element_visible(riwayat_mission_time),True)

    @allure.step("validate empty state page")
    def validate_empty_state_page(self):
        self.click(xp_kedaluwarsa)
        self.sleep(1)
        self.assert_equal(self.is_element_visible(empty_smile_face), True)
        self.assert_equal(self.is_element_visible(empty_kedaluwarsa_msg), True)

    @allure.step("Click Back Button on Gamification History Page")
    def click_back_button_on_gamification_history_page(self):
        self.click(riwayat_back_btn)
        self.sleep(1)
        self.assert_equal(self.is_element_visible(gamification_header),True)

    @allure.step("Validate Swipe Functionality in Riwayat Subtabs")
    def validate_swipe_functionality_in_riwayat_subtabs(self):
        self.scroll_screen(start_x=250, start_y=1081, end_x=900, end_y=1021, duration=5000)
        self.sleep(1)
        self.assert_equal(self.is_element_visible(riwayat_xp_value),True)

    @allure.step("Validate riwayat button is visible on gamification homepage")
    def validate_riwayat_button_is_visible_on_gamification_homepage(self):
        self.assert_equal(self.is_element_visible(riwayat_btn),True)

    @allure.step("Validate until date and time format")
    def validate_until_date_and_time_format(self):
        time_in_entry= self.get_attribute(riwayat_mission_time,'text')
        date_in_entry= (self.get_attribute(until_date,'text')).replace('Berlaku sampai ','')[:-1]
        in_date = datetime.strptime(date_in_entry, '%d %B %Y')
        out_date = datetime.strftime(in_date, '%d %B %Y')
        self.assert_equal(date_in_entry,out_date)
        in_time = datetime.strptime(time_in_entry, '%H:%M')
        out_time = datetime.strftime(in_time, '%H:%M')
        self.assert_equal(time_in_entry, out_time)

    @allure.step("Collect api data for gamification history")
    def collect_api_data_for_gamification_history(self):
        token_value = self.login()
        token = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJpWlYzdUJkTkJyTDA4dVIzQUR2bmg4akdTdHNkSHpQVSIsInN1YiI6IlNpbWFzSW52ZXN0In0.Kj31bgBrbc94NaUDKWgbx-N4ZBQNFsrZBmF7xtZ4hNo"}
        token['Authorization'] = 'Bearer ' + token_value
        history_rs = request_utilities.get(base_url='https://stg-api.siminvest.co.id/',endpoint='radix/v1/account/45997/reward-xp?status=1&campaign_id=&sort_by=id&is_asc=false&limit=20', headers=token,expected_status_code=200)
        label_api = []
        credit_api= []
        for i in range(len(history_rs['data'])):
            label_api.append(history_rs['data'][i]['campaign']['label'])
            credit_api.append(history_rs['data'][i]['credit'])
        logger.info(label_api)
        logger.info(credit_api)
        return label_api,credit_api

    @allure.step("Collect ui data for gamification history")
    def collect_ui_data_for_gamification_history(self):
        self.open_riwayat_page()
        label_ui= []
        credit_ui=[]
        l1=self.get_attribute('(//android.widget.TextView[@content-desc="Riwayat_entry_1_type"])[1]','text')
        l2=self.get_attribute('//android.widget.TextView[@content-desc="Riwayat_entry_2_type"]','text')
        l3=self.get_attribute('(//android.widget.TextView[@content-desc="Riwayat_entry_1_type"])[2]','text')
        l4=self.get_attribute('(//android.widget.TextView[@content-desc="Riwayat_entry_1_type"])[3]','text')
        label_ui.extend([l1,l2,l3,l4])
        c1=int(self.get_attribute('(//android.widget.TextView[@content-desc="Riwayat_entry_1_value"])[1]', 'text').replace('+', '').replace(',', '').replace('XP', ''))
        c2=int(self.get_attribute('//android.widget.TextView[@content-desc="Riwayat_entry_2_value"]', 'text').replace('+', '').replace(',', '').replace('XP', ''))
        c3=int(self.get_attribute('(//android.widget.TextView[@content-desc="Riwayat_entry_1_value"])[2]', 'text').replace('+', '').replace(',', '').replace('XP', ''))
        c4=int(self.get_attribute('(//android.widget.TextView[@content-desc="Riwayat_entry_1_value"])[3]', 'text').replace('+', '').replace(',', '').replace('XP', ''))
        credit_ui.extend([c1,c2,c3,c4])
        logger.info(label_ui)
        logger.info(credit_ui)
        return label_ui,credit_ui