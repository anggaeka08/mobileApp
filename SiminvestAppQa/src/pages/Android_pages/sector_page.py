from SiminvestAppQa.src.utilities.requestUtilities import RequestsUtilities
from SiminvestAppQa.src.pages.Android_pages.stock_detail_page import StockDetailPage
import allure

request_utilities = RequestsUtilities()
sector_page_header = 'SektorPageHeader'
count_on_list = '(//android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView)[2]'
header_on_list = '(//android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView)[1]'
sector_name = ['Energi', 'Barang Baku', 'Perindustrian', 'Barang Konsumen Non-Primer', 'Barang Konsumen Primer', 'Kesehatan', 'Keuangan', 'Properti & Real Estat', 'Teknologi','Infrastruktur', 'Transportasi & Logistik']
stock_icon = '//android.widget.ImageView'
sector_entry = '//android.view.ViewGroup/android.view.ViewGroup[4]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]'
sdp_header = 'SDPStockCode'

class SectorPage(StockDetailPage):

    @allure.step("verify_redirection_to_sector_page")
    def verify_redirection_to_sector_page(self):
        self.assert_equal(self.is_element_visible(sector_page_header), True)

    @allure.step("Open sector page")
    def open_sector_page(self, number):
        self.login_and_verify_homepage_for_reg_user(number)
        self.click_on_sector_button()
        self.sleep(2)
        self.verify_redirection_to_sector_page()

    @allure.step("Validate 11 entries available on sector page")
    def Validate_11_entries_available_on_sector_page(self):
        for i in range(11):
            self.assert_equal(self.is_element_visible(f"SectorPageName{i}"), True)
            self.assert_equal(self.is_element_visible(f"SectorPageCount{i}"), True)
            self.assert_equal(self.is_element_visible(f"SectorPageImage{i}"), True)

    @allure.step("validate the  number of stock on list page and sector page")
    def validate_the_number_of_stock_on_list_page_and_sector_page(self):
        for i in range(11):
            count_sector_page = self.get_attribute(f'SectorPageCount{i}', 'text')
            self.click(f'SectorPageType{i}')
            self.sleep(3)
            self.assert_equal(sector_name[i], self.get_attribute(header_on_list,'text'))
            count_on_list_page = self.get_attribute(count_on_list, 'text')
            self.assert_equal(count_sector_page, count_on_list_page)
            stock_code_list = []
            for i in range(1,7):
                self.assert_equal(self.is_element_visible(stock_icon), True)
                stock_code = self.get_attribute(f'//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[{i}]/android.widget.TextView[1]', 'text')
                stock_code_list.append(stock_code)
                self.assert_equal(self.is_element_visible(f'//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[{i}]/android.widget.TextView[2]'), True)
            sorted_list_code = sorted(stock_code_list)
            self.assert_equal(sorted_list_code, stock_code_list)
            self.click(sector_entry)
            self.sleep(3)
            self.assert_equal(self.get_attribute(sdp_header,'text'), stock_code_list[0])
            self.go_back()
            self.sleep(2)
            self.scroll_up()
            count_on_list_page_after_scroll = self.get_attribute(count_on_list, 'text')
            self.assert_equal(count_sector_page, count_on_list_page_after_scroll)
            self.go_back()
