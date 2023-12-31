from SiminvestAppQa.src.pages.Android_pages.home_page import HomePage
from SiminvestAppQa.src.data.userData import user_data
import allure
from datetime import datetime,date,timedelta
import time
import logging as logger

#LOCATORS
reseach_tab = '//android.widget.TextView[@text="Research"]'
research_header = 'ResearchPageHeader'
search_btn ='ResearchPageSearchBtn'
search_option = 'StockSearch'
last_report_search = '//android.widget.TextView[@text="Last Report"]'
news_search = '//android.widget.TextView[@text="News"]'
news_entry = '//android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.widget.TextView'
last_reports_entry = 'ResearchPageReportEntry0'
stock_signal = 'ResearchPageTabHeader0'
article='ResearchPageTabHeader1'
lastreport='ResearchPageTabHeader2'
news = 'ResearchPageTabHeader3'
news_entry_research = 'ResearchPageNewsEnrty0'
media_entry_title='ResearchPageMediaTitle0'
search_entry = '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.widget.TextView'
daily_search= 'ResearchPageReportDailySearchText'
daily_search_header='//android.widget.TextView[@text = "Daily Research"]'
red_dont0_SS = 'ResearchPageSignalEntry0UnreadMark'
red_dont1_SS = 'ResearchPageSignalEntry1UnreadMark'
SS_entry0 = 'ResearchPageSignalEntry0'
signal_tandai = 'ResearchPageSignalTandaiText'
list_title_1 = 'ResearchPageSignalEntry0Name'
list_date_1 = 'ResearchPageSignalEntry0Date'
reseach_tab_icon = '//android.view.View[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup'
list_title_8 = 'ResearchPageSignalEntry7Name'
title_breakdown = "//*[@text='stock breakdown']"
title_page = '//android.widget.TextView[@text="stock breakdown"]'
date_stock_breakdown = '//android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[2]'
price_stock_breakdwon = '//android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.TextView[2]'
button_lihat_stock = '//android.widget.TextView[@text="Lihat Stock"]'
sdp_header = 'SDPStockCode'
button_perbesar = '//android.widget.TextView[@text="Perbesar"]'
button_close = '//android.view.ViewGroup/android.widget.ImageView'
image_banner = '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ImageView'


class Research(HomePage):

    @allure.step("Verify research tab on homepage")
    def verify_research_tab_on_homepage(self):
        self.assert_equal(self.is_element_visible(reseach_tab), True)

    @allure.step("Click on research btn")
    def click_on_research_btn(self):
        self.click(reseach_tab)
          
    @allure.step("Verify header of research page")
    def verify_header_of_research_page(self):
        self.sleep(2)
        self.assert_equal(self.is_element_visible(research_header), True)
        self.assert_equal(self.is_element_visible( signal_tandai), True)

    @allure.step("Verify search btn on research page")
    def Verify_search_btn_on_research_page(self):
        self.assert_equal(self.is_element_visible(search_btn), True)

    @allure.step("Click on search btn")
    def click_on_search_btn(self):
        self.click(search_btn)

    @allure.step("Verify redirection on search page")
    def verify_redirection_on_search_page(self):
        self.sleep(3)
        self.assert_equal(self.is_element_visible(search_option), True)

    @allure.step("Verify availability for last report and news on search option")
    def Verify_availability_for_last_report_and_news_on_search_option(self):
        self.assert_equal(self.is_element_visible(last_report_search), True)
        self.assert_equal(self.is_element_visible(news_search), True)

    @allure.step("Validate place holder in search option")
    def Validate_place_holder_in_search_option(self):
        self.assert_equal(self.get_attribute(search_option, "Text"), "Cari berita")

    @allure.step("Enter and verify some value in search option")
    def enter_and_verify_some_value_in_search_option(self):
        self.set_text(search_option, "REAL")
        self.assert_equal(self.get_attribute(search_option, "text"), 'REAL')

    @allure.step("Click to new and verify entry")
    def Click_to_new_and_verify_entry(self):
        self.click(news_search)
        self.sleep(2)
        self.assert_equal(self.is_element_visible(news_entry), True)

    @allure.step("Click to lastreport and verify entry")
    def click_to_lastreport_and_verify_entry(self):
        self.click(last_report_search)
        self.sleep(4)
        self.assert_equal(self.is_element_visible(last_reports_entry), True)

    @allure.step("Verify tabs on research page")
    def verify_tabs_on_research_page(self):
        self.sleep(2)
        self.assert_equal(self.is_element_visible(stock_signal), True)
        self.assert_equal(self.is_element_visible(article), True)
        self.assert_equal(self.is_element_visible(lastreport), True)
        self.assert_equal(self.is_element_visible(news), True)

    @allure.step("Click on news research tab and verify entry")
    def click_on_news_research_tab_and_verify_entry(self):
        self.click(news)
        self.sleep(2)
        self.assert_equal(self.is_element_visible(news_entry_research), True)

    @allure.step("Click on media tab and verify entry")
    def click_on_media_tab_and_verify_entry(self):
        self.click(media)
        self.sleep(2)
        self.assert_equal(self.is_element_visible(media_entry_title), True)

    @allure.step("Enter some value in search_option")
    def enter_some_value_in_search_option_verify_entry(self):
        self.set_text(search_option, 'REAL')
        self.sleep(5)
        self.assert_equal(self.is_element_visible(search_entry), True)

    @allure.step("Verify 10 entries on news section")
    def verify_10_entries_on_news_section(self):
        self.click(news)
        self.sleep(2)
        for i in range(9):
            self.assert_equal(self.is_element_visible(f'ResearchPageNewsEnrty{i}Title'), True)
            if i == 5:
                self.scroll_up()

    @allure.step("Click to daily search verify redirection")
    def click_to_daily_search_verify_redirection(self):
        self.click(last_report_search)
        self.sleep(2)
        self.click(daily_search)
        self.sleep(2)
        self.assert_equal(self.is_element_visible(daily_search_header), True)

    @allure.step("Click on stock signal")
    def click_on_stock_signal(self):
        self.click(stock_signal)

    @allure.step("Verify red dont on one entry")
    def verify_red_dont_on_one_entry(self):
        self.assert_equal(self.is_element_visible(red_dont0_SS), True)

    @allure.step("Click on entry and verify red dot remove from entry")
    def Click_on_entry_and_verify_red_dot_remove_from_entry(self):
        self.click(SS_entry0)
        self.sleep(2)
        self.go_back()
        self.assert_equal(self.is_element_visible(red_dont0_SS), False)

    @allure.step("Verify red dont on one entry")
    def verify_red_dont_on_one_entry_after_read(self):
        self.sleep(2)
        self.assert_equal(self.is_element_visible(red_dont0_SS), True)

    @allure.step("Click to signal tadai btn and verify red dots")
    def click_to_signal_tadai_and_verify_red_dots(self):
        self.sleep(1)
        self.click(signal_tandai)
        self.sleep(1)
        self.assert_equal(self.is_element_visible(red_dont0_SS), False)
        self.assert_equal(self.is_element_visible(red_dont1_SS), False)
        self.assert_equal(self.is_element_visible(signal_tandai), False)

    @allure.step("Verify exit from app on research page")
    def Verify_exit_from_app_on_research_page(self):
        self.sleep(2)
        self.assert_equal(self.is_element_visible(stock_signal), False)
        self.assert_equal(self.is_element_visible(last_report), False)
        self.assert_equal(self.is_element_visible(news), False)
        self.assert_equal(self.is_element_visible(media), False)

    @allure.step("Login with non kyc number")
    def login_with_non_kyc_number(self, number):
        self.click_mulai_sekarang()
        self.type_mobile_no(number)
        self.click_selanjutnya()
        self.enter_otp(user_data['valid_otp'])
        self.enter_pin()
        self.verify_home_page()
    
    @allure.step("verify_title_date_card")
    def verify_title_date_card(self):
        self.sleep(2)
        self.assert_equal(self.is_element_visible(list_title_1), True)
        self.assert_equal(self.is_element_visible(list_date_1), True)
        
        date_in_entry = self.get_attribute(list_date_1, "text")
        respon_date=date_in_entry[:11]
        logger.info( respon_date)
        
    @allure.step("validate_refresh_functionality_for_level_page")
    def validate_refresh_functionality_for_level_page(self):
        self.scroll_up()
        self.assert_equal(self.is_element_visible(list_title_8), True)
        self.sleep(1)
        self.scroll_down()
        self.assert_equal(self.is_element_visible(list_title_1), True)
        self.sleep(1)
        self.assert_equal(self.get_attribute(research_header, 'text'), "Research")
        
    @allure.step("verify_header_of_all_tab")
    def verify_header_of_all_tab(self):
        header_value = self.get_attribute(research_header, 'text')
        self.click(article)
        self.assert_equal(self.get_attribute(research_header, 'text'), header_value)
        self.sleep(1)
        self.click(lastreport)
        self.assert_equal(self.get_attribute(research_header, 'text'), header_value)
        self.sleep(1)
        self.click(news)
        self.assert_equal(self.get_attribute(research_header, 'text'), header_value)
        self.sleep(1)
        self.click(stock_signal)
        self.assert_equal(self.get_attribute(research_header, 'text'), header_value)

    @allure.step("verify_stock_breakdown_page")
    def verify_stock_breakdown_page(self):
        self.click(title_breakdown)
        self.sleep(2)
        self.assert_equal(self.get_attribute(title_page, 'text'), "stock breakdown")
        self.assert_equal(self.is_element_visible(date_stock_breakdown), True)
        self.assert_equal(self.is_element_visible(price_stock_breakdwon), True)
        self.assert_equal(self.get_attribute(button_lihat_stock, 'text'), "Lihat Stock")
       
    @allure.step("click_on_lihat_stock_btn")
    def click_on_lihat_stock_btn(self):
        self.click(button_lihat_stock)

    @allure.step("verify_on_sdp_page")
    def verify_on_sdp_page(self):
        self.sleep(3)
        self.assert_equal(self.is_element_visible(sdp_header), True)
        self.go_back()
        self.sleep(2)
        self.assert_equal(self.get_attribute(button_lihat_stock, 'text'), "Lihat Stock")
    
    @allure.step("verify_on_image")
    def verify_on_image(self):
        self.sleep(2)
        self.assert_equal(self.is_element_visible(button_perbesar), True) 
        self.click(button_perbesar)
        self.sleep(2)
        self.assert_equal(self.is_element_visible(button_close), True)
        self.click(button_close)
        self.sleep(2)
        self.assert_equal(self.get_attribute(button_lihat_stock, 'text'), "Lihat Stock")
        self.go_back()
        self.sleep(2)
        self.assert_equal(self.get_attribute(research_header, 'text'), "Research")
        
