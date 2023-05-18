from SiminvestAppQa.src.utilities.requestUtilities import RequestsUtilities
from SiminvestAppQa.src.pages.Android_pages.stock_detail_page import StockDetailPage
import allure

request_utilities = RequestsUtilities()
sector_page_header = 'SektorPageHeader'


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
            self.assert_equal(self.is_element_visible(f"SectorPageName{i}"))
            self.assert_equal(self.is_element_visible(f"SectorPageCount{i}"))
            self.assert_equal(self.is_element_visible(f"SectorPageImage{i}"))