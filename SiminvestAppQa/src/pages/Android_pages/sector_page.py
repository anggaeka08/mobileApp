from SiminvestAppQa.src.utilities.requestUtilities import RequestsUtilities
from SiminvestAppQa.src.pages.Android_pages.stock_detail_page import StockDetailPage
import allure
import logging as logger

request_utilities = RequestsUtilities()
sector_page_header = 'SektorPageHeader'
count_on_list = '(//android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView)[2]'
header_on_list = '(//android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView)[1]'
sector_name = ['Energi', 'Barang Baku', 'Perindustrian', 'Barang Konsumen Non-Primer', 'Barang Konsumen Primer', 'Kesehatan', 'Keuangan', 'Properti & Real Estat', 'Teknologi','Infrastruktur', 'Transportasi & Logistik']
stock_icon = '//android.widget.ImageView'
sector_entry = '//android.view.ViewGroup/android.view.ViewGroup[4]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]'
sdp_header = 'SDPStockCode'
stock_code =""
stock_fullname = ""
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


    @allure.step("validate back btn and grammar on sector page and list page")
    def validate_back_btn_and_grammar_on_sector_page_and_list_page(self):
        self.click_on_sector_button()
        self.sleep(2)
        for i in range(11):
            self.click(f'SectorPageType{i}')
            self.sleep(2)
            self.scroll_down()
            self.sleep(5)
            self.assert_equal(self.is_element_visible(sector_entry), True)
            for i in range(1,6):
                #cod4
                self.assert_equal(self.is_element_visible(f'//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[{i}]/android.widget.TextView[1]'), True)
                #comapny name
                self.assert_equal(self.is_element_visible(f'//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[{i}]/android.widget.TextView[2]'), True)
                #price
                self.assert_equal(self.is_element_visible(f'//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[{i}]/android.widget.TextView[3]'), True)
            self.click(sector_entry)
            self.sleep(2)
            self.go_back()
            self.sleep(2)
            self.assert_equal(self.is_element_visible(f'//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.TextView[1]'),True)
            self.go_back()
            self.sleep(1)

    @allure.step("Verify redirection after back btn from sector page")
    def verify_redirection_after_back_btn_from_sector_page(self):
        self.go_back()
        self.sleep(2)
        self.verify_home_page_reg_user()

    @allure.step("validate ui data with api")
    def validate_ui_data_with_api(self):
        sector_name_list = []
        stock_count_list = []
        stock_code_list_0 = []
        stock_code_list_1 = []
        stock_code_list_2 = []
        stock_code_list_3 = []
        stock_code_list_4 = []
        stock_code_list_5 = []
        stock_code_list_6 = []
        stock_code_list_7 = []
        stock_code_list_8 = []
        stock_code_list_9 = []
        stock_code_list_10 = []
        for i in range(11):
            sector_name_list.append(self.get_attribute(f'SectorPageName{i}', 'text'))
            stock_count_text = self.get_attribute(f'SectorPageCount{i}', 'text')
            index = (stock_count_text.find('S')) -1
            stock_count = int(stock_count_text[:index])
            stock_count_list.append(stock_count)
            self.click(f'SectorPageType{i}')
            self.sleep(3)
            for j in range(1,7):
                 stock_code = self.get_attribute(f'//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[{j}]/android.widget.TextView[1]', 'text')
                 # import pdb
                 # pdb.set_trace()
                 locals()[f"stock_code_list_{i}"].append(stock_code)
            self.go_back()
            self.sleep(2)
        # #sector api data
        token_value = self.login()
        token = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJpWlYzdUJkTkJyTDA4dVIzQUR2bmg4akdTdHNkSHpQVSIsInN1YiI6IlNpbWFzSW52ZXN0In0.Kj31bgBrbc94NaUDKWgbx-N4ZBQNFsrZBmF7xtZ4hNo"}
        token['Authorization'] = 'Bearer ' + token_value
        sector_list_api = request_utilities.get(base_url='https://stg-api.siminvest.co.id/', endpoint='emerson/v1/sector',headers=token, expected_status_code=200)
        for i in range(len(sector_list_api['data'])):
            self.assert_equal(sector_name_list[i], sector_list_api['data'][i]['description'])
        #for k in range(11):
            sector_stock_list = request_utilities.get(base_url='https://stg-api.siminvest.co.id/', endpoint=f"emerson/v1/stock?sector_code={sector_list_api['data'][i]['code']}&sort_by=code&is_asc=true&page=1&limit={sector_list_api['data'][i]['total_stock']}",headers=token, expected_status_code=200)
            for k in range(6):
                self.assert_equal(sector_stock_list['data'][k]['code'], locals()[f"stock_code_list_{i}"][k])