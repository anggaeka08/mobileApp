from SiminvestAppQa.src.pages.Android_pages.home_page import HomePage
from SiminvestAppQa.src.data.userData import user_data
import allure

#LOCATORS
reseach_tab = '//android.widget.TextView[@text="Research"]'
research_header = 'ResearchPageHeader'
search_btn ='ResearchPageSearchBtn'
search_option = 'StockSearch'
last_report_search = '//android.widget.TextView[@text="Last Report"]'
news_search = '//android.widget.TextView[@text="News"]'
news_entry = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.widget.TextView'
last_reports_entry = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.widget.TextView'
stock_signal = 'ResearchPageTabHeader0'
last_report='ResearchPageTabHeader1'
news='ResearchPageTabHeader2'
media = 'ResearchPageTabHeader3'
news_entry_research = 'ResearchPageNewsEnrty0'
media_entry_title='ResearchPageMediaTitle0'
search_entry = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.widget.TextView'



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
        self.sleep(2)
        self.assert_equal(self.is_element_visible(last_reports_entry), True)

    @allure.step("Verify tabs on research page")
    def verify_tabs_on_research_page(self):
        self.sleep(2)
        self.assert_equal(self.is_element_visible(stock_signal), True)
        self.assert_equal(self.is_element_visible(last_report), True)
        self.assert_equal(self.is_element_visible(news), True)
        self.assert_equal(self.is_element_visible(media), True)

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
        self.sleep(3)
        self.assert_equal(self.is_element_visible(search_entry), True)









