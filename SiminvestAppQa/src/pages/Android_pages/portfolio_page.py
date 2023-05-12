from SiminvestAppQa.src.pages.Android_pages.home_page import HomePage
from SiminvestAppQa.src.pages.Android_pages.stock_detail_page import StockDetailPage
from SiminvestAppQa.src.pages.Android_pages.sell_process import SellProcess
from SiminvestAppQa.src.pages.Android_pages.buy_process import BuyProcess
from SiminvestAppQa.src.data.userData import user_data
from datetime import datetime
import allure
import logging as logger

saham_tab = '(//android.view.ViewGroup[@content-desc="PortPageSahamTab"])[1]'
reksadhana_tab = '(//android.view.ViewGroup[@content-desc="PortPageSahamTab"])[2]'
buying_power_value = 'PortPageText9'
p_l_value = 'PortPageText3'
invested_value = 'PortPageText5'
cash_value = 'PortPageText11'
open_buy = 'PortPageText7'
open_sell = 'PortPageText13'
code_value = 'PortPageEntry0Code'
lot_value ='PortPageEntry0Lot'
avg_value = 'PortPageEntry0Avg'
last_value= 'PortPageEntry0Last'
plidr_value = 'PortPageEntry0PL'
pl_percentage = 'PortPageEntry0PLPercentage'
invested_values='PortPageEntry0Invested'
value_value = 'PortPageEntry0Value'
stock_row = 'PortPageEntry0'
jual_btn = 'SDPPageSellBtn'
total_nilai = 'SDPPortPageText3'
lot_dimiki = 'SDPPortPageText5'
harga = 'SDPPortPageText9'
portfolio_entry_1 = 'PortPageEntry0'
buka_akun_reksadana = '//android.widget.TextView[@text="Buka Akun Reksadana"]'
order_buy = '//android.widget.TextView[@text="ORDER BELI"]'
portfolio_value_H = 'HomepageRp'
pl_h = 'HomepageRpAmount'
rdn_h = 'HomePageRdnValue'
portfolio_value_port = 'PortPagePortfolioValue'
pl_port = 'PortPageText3'
cash_balance = 'PortPageText11'
help_btn = "//android.widget.TextView[@text = 'Hubungi Customer Care']"
chrome_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[2]/android.view.View[1]/android.view.View'
pl_percentage_over="PortPageText2"
sell_success= "BuyTransactionMarketOpenPopUpHeading"
homepage_btn= "//android.widget.TextView[@text='Home']"
ok_btn_close = 'BuyTransactionMarketCloseButton'
exchange_notification= '//android.widget.TextView[contains(@text, "Bursa Tidak Beroperasi")]'
investasi_sekarang_saham= '//android.widget.TextView[@text="INVESTASI SEKARANG"]'
investasi_sekarang_reksadana='//android.widget.TextView[@text="Investasi Sekarang"]'



class Portfolio(HomePage):

    @allure.step("Verify saham tab clickable")
    def verify_saham_tab_clickable(self):
        self.assert_equal(self.get_attribute(saham_tab, 'clickable'), 'true')

    @allure.step("Verify reksadhana tab clickable")
    def verify_reksadhana_tab_clickable(self):
        self.assert_equal(self.get_attribute(reksadhana_tab, 'clickable'), 'true')

    @allure.step("Verify buypower and other value's presence")
    def verify_buypower_and_other_values_presence(self):
        self.assert_equal(self.is_element_visible(buying_power_value), True)
        self.assert_equal(self.is_element_visible(p_l_value), True)
        self.assert_equal(self.is_element_visible(invested_value), True)
        self.assert_equal(self.is_element_visible(cash_value), True)
        self.assert_equal(self.is_element_visible(open_buy), True)
        self.assert_equal(self.is_element_visible(open_sell), True)

    @allure.step("Verify presence of Code,Lot,Avg.Last,P/L IDR P/L%, invested value")
    def verify_presence_of_Code_Lot_Avg_Last_PL_IDR_PL_percentage_invested_value(self):
        self.assert_equal(self.is_element_visible(code_value), True)
        self.assert_equal(self.is_element_visible(lot_value), True)
        self.assert_equal(self.is_element_visible(avg_value), True)
        self.assert_equal(self.is_element_visible(plidr_value), True)
        self.assert_equal(self.is_element_visible(pl_percentage), True)
        self.assert_equal(self.is_element_visible(invested_values), True)
        self.assert_equal(self.is_element_visible(value_value), True)

    @allure.step("Validate Stock row availability in portfolio")
    def validate_stock_row_availability_in_portfolio(self):
        self.assert_equal(self.is_element_visible(stock_row), True)

    @allure.step("Verify jual btn on home page")
    def verify_jual_btn_on_home_page(self):
        self.assert_equal(self.is_element_visible(jual_btn), True)


    @allure.step("Comparing the value between portfolio page and sdp")
    def comparing_the_value_between_portfolio_page_and_sdp(self):
        lot_port = self.get_attribute(lot_value, 'text')
        avg_price_port = self.get_attribute(avg_value, 'text')
        p_l_value_port = self.get_attribute(plidr_value, 'text')
        pl_per_value_port = self.get_attribute(pl_percentage, 'text')
        self.click_on_portfolio_entry_1()
        total_nilai_value = self.get_attribute(total_nilai, 'text')
        c = '('
        index = total_nilai_value.find(c)
        p_l_value_sdp = total_nilai_value[2:index-1]
        p_l_per_value=total_nilai_value[index+1:-1]
        lot_value_sdp = self.get_attribute(lot_dimiki, 'text')
        harga_value_sdp = self.get_attribute(harga, 'text')
        self.assert_equal(lot_value_sdp, lot_port)
        self.assert_equal(harga_value_sdp, avg_price_port)
        self.assert_equal(p_l_value_sdp, p_l_value_port)
        self.assert_equal(p_l_per_value, pl_per_value_port)

    @allure.step("Validate redirection from portfolio to sdp")
    def validate_redirection_from_portfolio_to_sdp(self):
        self.click(f'PortPageEntry0')
        self.sleep(2)
        self.verify_sdp_page()
        self.go_back()
        self.click('PortPageEntry1')
        self.sleep(2)
        self.verify_sdp_page()

    @allure.step("Click on reksadhana_tab")
    def click_on_reksadhana_tab(self):
        self.click(reksadhana_tab)

    @allure.step("Verify Tab on Reksadhana")
    def verify_tab_on_reksadhana(self):
        self.assert_equal(self.get_attribute(reksadhana_tab, 'focusable'), "true")

    @allure.step("Verify redirection of reksadhana tab")
    def verify_redirection_reksadhana_tab(self):
        self.assert_equal(self.is_element_visible(buka_akun_reksadana), True)

    @allure.step("Right swipe on portfolio")
    def right_swipe_on_portfolio(self):
        self.scroll_screen(start_x=76, start_y=1065, end_x=691, end_y=1065, duration=10000)

    @allure.step("Left swipe on portfolio")
    def left_swipe_on_portfolio(self):
        self.scroll_screen(start_x=691, start_y=1065, end_x=76, end_y=1065, duration=10000)

    @allure.step("Verify half card page buy")
    def verify_half_card_page_buy(self):
        self.assert_equal(self.is_element_visible(order_buy), True)

    @allure.step("Compare portfolio_value_buying_power_PL_value with homepage")
    def Compare_values_between_homepage_and_portfolio(self):
        Portfolio_value_H = self.get_attribute(portfolio_value_H, "text").replace(' ', '')
        PL_H = self.get_attribute(pl_h, "text")
        c = '('
        index = PL_H.find(c)-1
        PL_H_value = PL_H[:index]
        RDN_H = self.get_attribute(rdn_h, "text")
        RDN_H_Value = RDN_H[3:]
        self.click_on_portfolio_btn()
        Portfolio_value_Port = self.get_attribute(portfolio_value_port, "text").replace(' ','')
        PL_Port = self.get_attribute(pl_port, "text")
        Cash_balance = self.get_attribute(cash_balance, "text")
        self.assert_equal(Portfolio_value_H,Portfolio_value_Port)
        self.assert_equal(PL_H_value, PL_Port)
        self.assert_equal(RDN_H_Value, Cash_balance)

    @allure.step('Click to help btn')
    def click_to_help_btn(self):
        self.click(help_btn)

    @allure.step("Verify redirection after click on customer support")
    def verify_redirection_after_click_on_customer_support(self):
        self.sleep(3)
        self.assert_equal(self.is_element_visible(chrome_xpath), True)

    @allure.step("Verify PL value")
    def verify_pl_value(self):
        PL_value = self.get_attribute(pl_port, "text")
        invest_value = self.get_attribute(invested_value, "text")
        self.assert_equal(PL_value[1:], invest_value)


    @allure.step("verify PL Percentage")
    def verify_pl_percentage(self):
        PL_value = int(self.get_attribute(pl_port, "text").replace(',', ''))
        invest_value = int(self.get_attribute(invested_value, "text").replace(',', ''))
        PL_per = str((invest_value*100) / PL_value)
        percentage_value = self.get_attribute(pl_percentage_over, "text")
        percentage = percentage_value[1:7]
        self.assert_equal(PL_per, percentage)

    @allure.step("verify buy sell success")
    def verify_buy_sell_success(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        logger.info(f"Current Time = {current_time}")
        if (current_time >= '7:30' and current_time <= '10:00') or (
                current_time >= '12:00' and current_time <= '15:00'):
            self.assert_equal(self.is_element_visible(sell_success), True)
            self.click_on_ok_btn()
        else :
            logger.info("Out of time")
            self.assert_equal(self.is_element_visible(sell_success), False)
            self.click(ok_btn_close)
            self.go_back()
            self.go_back()

    @allure.step("Click on homepage")
    def click_on_home_page(self):
        self.click(homepage_btn)

    @allure.step("Verify app closed")
    def verify_app_closed(self):
        self.assert_equal(self.is_element_visible(homepage_btn), False)

    @allure.step("Validate portfolio for non kyc user")
    def validate_portfolio_for_non_kyc_user(self):
        self.assert_equal(self.is_element_visible(investasi_sekarang_saham), True)
        self.click(reksadhana_tab)
        self.assert_equal(self.is_element_visible(investasi_sekarang_reksadana), True)




