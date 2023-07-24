from SiminvestAppQa.src.pages.Android_pages.home_page import HomePage
from datetime import datetime
import allure
import logging as logger
from SiminvestAppQa.src.utilities.requestUtilities import RequestsUtilities


request_utilities = RequestsUtilities()
saham_tab = '(//android.view.ViewGroup[@content-desc="PortPageSahamTab"])[1]'
reksadana_to_saham_btn = '(//android.view.ViewGroup[@content-desc="PortPageReksadanaTab"])[1]'
reksadhana_tab = '(//android.view.ViewGroup[@content-desc="PortPageSahamTab"])[2]'
buying_power_value = 'PortPageText9'
buying_power_H = 'HomepagebuyPower'
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
diinvestasikan_value= 'SDPPortPageText8'
portfolio_entry_1 = 'PortPageEntry0'
buka_akun_reksadana = '//android.widget.TextView[@text="Buka Akun Reksadana"]'
order_buy = '//android.widget.TextView[@text="ORDER BELI"]'
order_jual = "FastBSHeader"
portfolio_value_H = 'HomepageRp'
pl_h = 'HomepageRpAmount'
rdn_h = 'HomePageRdnValue'
portfolio_value_port = 'PortPagePortfolioValue'
pl_port = 'PortPageText3'
cash_balance = 'PortPageText11'
help_btn = "//android.widget.TextView[@text = 'Hubungi Customer Care']"
chrome_xpath = "//android.widget.TextView[@text = 'PusatBantuanSimInvest']"
select_browser = "//android.widget.TextView[@text = 'Open links with']"
pl_percentage_over="PortPageText2"
sell_success= "BuyTransactionMarketOpenPopUpHeading"
homepage_btn= "//android.widget.TextView[@text='Home']"
ok_btn_close = 'BuyTransactionMarketCloseButton'
exchange_notification= '//android.widget.TextView[contains(@text, "Bursa Tidak Beroperasi")]'
investasi_sekarang_saham= '//android.widget.TextView[@text="INVESTASI SEKARANG"]'
investasi_sekarang_reksadana='//android.widget.TextView[@text="INVESTASI SEKARANG"]'
portfolio_btn = '//android.widget.TextView[@text="Portfolio"]'
code="PortPageTextHeader1"
lot="PortPageTextHeader2"
avg="PortPageTextHeader3"
last="PortPageTextHeader4"
PL_idr="PortPageTextHeader5"
PL_percent="PortPageTextHeader6"
invested="PortPageTextHeader7"
value="PortPageTextHeader8"


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
        invested_value_port = self.get_attribute(invested_values, 'text')
        self.click_on_portfolio_entry_1()
        total_nilai_value = self.get_attribute(total_nilai, 'text')
        c = '('
        index = total_nilai_value.find(c)
        p_l_value_sdp = total_nilai_value[2:index-1]
        p_l_per_value=total_nilai_value[index+1:-1]
        lot_value_sdp = self.get_attribute(lot_dimiki, 'text')
        harga_value_sdp = self.get_attribute(harga, 'text')
        diinvestasikan_value_sdp= self.get_attribute(diinvestasikan_value, 'text')
        self.assert_equal(lot_value_sdp, lot_port)
        self.assert_equal(harga_value_sdp, avg_price_port)
        #self.assert_equal(p_l_value_sdp, p_l_value_port)
        #self.assert_equal(p_l_per_value, pl_per_value_port)
        #self.assert_equal(invested_value_port, diinvestasikan_value_sdp)

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
        self.sleep(2)

    @allure.step("Click on saham tab")
    def click_on_saham_tab(self):
        self.click(saham_tab)

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

    @allure.step("Verify half card for sell")
    def verify_half_card_for_sell(self):
        self.assert_equal(self.is_element_visible(order_jual), True)

    @allure.step("Compare portfolio_value_buying_power_PL_value with homepage")
    def Compare_values_between_homepage_and_portfolio(self):
        #extract portfolio value from homepage
        Portfolio_value_H = self.get_attribute(portfolio_value_H, "text").replace(' ', '')
        #extract P/L value from homepage
        PL_H = self.get_attribute(pl_h, "text")
        c = '('
        index = PL_H.find(c)-1
        PL_H_value = PL_H[:index]
        #extract P/L Percentage from homepage
        index1 = PL_H.find('(')
        index2=  PL_H.find(')')+1
        PL_H_percentage= PL_H[index1:index2]
        #extract RDN value from homepage
        RDN_H = self.get_attribute(rdn_h, "text")
        RDN_H_Value = RDN_H[3:]
        # extract buying power from homepage
        buying_power=  self.get_attribute(buying_power_H, "text")
        buying_power_H_value=buying_power[16:]
        self.click_on_portfolio_btn()
        # extract portfolio value from pf
        Portfolio_value_Port = self.get_attribute(portfolio_value_port, "text").replace(' ','')
        # extract P/L value from pf
        PL_Port = self.get_attribute(pl_port, "text")
        # extract P/L Percentage from pf
        PL_percentage_Port = self.get_attribute(pl_percentage_over, "text")
        # extract cash balance value from PF
        Cash_balance = self.get_attribute(cash_balance, "text")
        # extract buying power from PF
        buying_power_port = self.get_attribute(buying_power_value, "text")
        self.assert_equal(Portfolio_value_H,Portfolio_value_Port)
        self.assert_equal(PL_H_value, PL_Port)
        self.assert_equal(RDN_H_Value, Cash_balance)
        self.assert_equal(PL_H_percentage, PL_percentage_Port)
        self.assert_equal(buying_power_H_value, buying_power_port)

    @allure.step('Click to help btn')
    def click_to_help_btn(self):
        self.click(help_btn)

    @allure.step("Verify redirection after click on customer support")
    def verify_redirection_after_click_on_customer_support(self):
        self.sleep(3)
        if self.is_element_visible(select_browser)==True:
            self.assert_equal(self.is_element_visible(select_browser), True)
        else:
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
        PL_per = str((PL_value*100) / invest_value)
        percentage_value = self.get_attribute(pl_percentage_over, "text")
        percentage = percentage_value[1:7]
        self.assert_equal(PL_per, percentage)

    @allure.step("verify PL value for stock")
    def verify_pl_value_for_stock(self):
        current_value = int(self.get_attribute(value_value, "text").replace(',', ''))
        invest_value = int(self.get_attribute(invested_values, "text").replace(',', ''))
        PL_value_expected= str(current_value-invest_value)
        PL_value_actual = self.get_attribute(plidr_value, "text").replace(',', '')
        self.assert_equal(PL_value_expected, PL_value_actual)

    @allure.step("verify PL Percentage for stock")
    def verify_pl_percentage_for_stock(self):
        PL_value = int(self.get_attribute(plidr_value, "text").replace(',', ''))
        invest_value = int(self.get_attribute(invested_values, "text").replace(',', ''))
        PL_per = str((PL_value * 100) / invest_value)
        percentage_value = (self.get_attribute(pl_percentage, "text"))[:-2]
        self.assert_equal(PL_per, percentage_value)

    @allure.step("verify portfolio value")
    def verify_portfolio_value(self):
        PL_value = int(self.get_attribute(p_l_value, "text").replace(',', ''))
        invest_value = int(self.get_attribute(invested_value, "text").replace(',', ''))
        portfolio_value_expected = str((PL_value+invest_value))
        portfolio_value_actual = ((self.get_attribute(portfolio_value_port, "text"))[4:]).replace(',','')
        self.assert_equal(portfolio_value_expected, portfolio_value_actual)

    @allure.step("verify buy sell success")
    def verify_buy_sell_success(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        logger.info(f"Current Time = {current_time}")
        if (current_time >= '7:30' or current_time <= '15:00'):
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

    @allure.step("Verify sub heading")
    def verify_sub_heading(self):
        self.assert_equal(self.is_element_visible(code), True)
        self.assert_equal(self.is_element_visible(lot), True)
        self.assert_equal(self.is_element_visible(avg), True)
        self.assert_equal(self.is_element_visible(last), True)
        self.assert_equal(self.is_element_visible(PL_idr), True)
        self.assert_equal(self.is_element_visible(PL_percent), True)
        self.assert_equal(self.is_element_visible(invested), True)
        self.assert_equal(self.is_element_visible(value), True)

    @allure.step("Verify portfolio stock code sorting")
    def verify_portfolio_stock_code_sorting(self):
        self.assert_equal(self.get_attribute('PortPageEntry0Code', "text"), "ANTM" )
        self.assert_equal(self.get_attribute('PortPageEntry1Code', "text"), "APLN" )
        self.assert_equal(self.get_attribute('PortPageEntry2Code', "text"), "ASII" )
        self.assert_equal(self.get_attribute('PortPageEntry3Code', "text"), "BBCA" )
        self.assert_equal(self.get_attribute('PortPageEntry4Code', "text"), "BBNI" )


    @allure.step("verify ui feature for portfolio")
    def verify_ui_feature_for_portfolio(self):
        self.assert_equal(self.is_element_visible(portfolio_btn), True)
        self.click_on_portfolio_btn()
        self.verify_buypower_and_other_values_presence()
        self.assert_equal(self.is_element_visible(saham_tab), True)
        self.verify_saham_tab_clickable()
        self.assert_equal(self.is_element_visible(reksadhana_tab), True)
        self.verify_reksadhana_tab_clickable()
        self.click_on_reksadhana_tab()
        self.assert_equal(self.is_element_visible(investasi_sekarang_reksadana), True)
        self.click_on_home_page()
        self.click_on_portfolio_btn()
        self.assert_equal(self.is_element_visible(investasi_sekarang_reksadana), True)
        self.click(reksadana_to_saham_btn)
        self.verify_presence_of_Code_Lot_Avg_Last_PL_IDR_PL_percentage_invested_value()
        self.scroll_up()
        self.scroll_down()
        self.assert_equal(self.is_element_visible(portfolio_entry_1), True)
        self.right_swipe_on_portfolio()
        self.sleep(2)
        self.assert_equal(self.is_element_visible(order_jual), True)
        self.go_back()
        self.left_swipe_on_portfolio()
        self.sleep(2)
        self.assert_equal(self.is_element_visible(order_jual), True)
        self.go_back()
        self.scroll_screen(start_x=500, start_y=1820, end_x=500, end_y=-4000, duration=10000)
        self.sleep(1)
        self.assert_equal(self.is_element_visible(help_btn), True)
        self.click_to_help_btn()
        self.verify_redirection_after_click_on_customer_support()
        self.go_back()
        self.sleep(1)
        self.assert_equal(self.is_element_visible(saham_tab), True)
        self.sleep(1)
        self.scroll_screen(start_x=600, start_y=420, end_x=600, end_y=6000, duration=10000)
        self.verify_sub_heading()
        self.scroll_down()
        self.sleep(2)
        self.verify_portfolio_stock_code_sorting()
        self.click_on_reksadhana_tab()
        self.click(reksadana_to_saham_btn)
        self.verify_portfolio_stock_code_sorting()
        self.click_on_home_page()
        self.click_on_portfolio_btn()
        self.verify_portfolio_stock_code_sorting()

    @allure.step("Collect api data for portfolio")
    def collect_api_data_for_portfolio(self):
        token_value = self.login()
        token = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJpWlYzdUJkTkJyTDA4dVIzQUR2bmg4akdTdHNkSHpQVSIsInN1YiI6IlNpbWFzSW52ZXN0In0.Kj31bgBrbc94NaUDKWgbx-N4ZBQNFsrZBmF7xtZ4hNo"}
        token['Authorization'] = 'Bearer ' + token_value
        homepage_rs = request_utilities.get(base_url='https://stg-api.siminvest.co.id/', endpoint='api/v1/oms/equities/trading-account/53617?stock_code=', headers=token,expected_status_code=200)
        logger.info(homepage_rs)
        rdn_balance_api = str(homepage_rs['data']['rdn_balance'])
        trading_balance_api = str(homepage_rs['data']['trading_balance'])
        portfolio_rs = request_utilities.get(base_url='https://stg-api.siminvest.co.id/',endpoint='api/v1/users/portfolios/equities/53617', headers=token, expected_status_code=202)
        logger.info(portfolio_rs)
        buying_power_api = str(portfolio_rs['data']['buying_power'])
        buyopen_api = str(portfolio_rs['data']['buyopen'])
        cash_balance_api = str(portfolio_rs['data']['cash_balance'])
        earnings_api = portfolio_rs['data']['earnings']
        market_value_api = str(portfolio_rs['data']['market_value'])
        return_api = str(portfolio_rs['data']['return'])
        sellopen_api = str(portfolio_rs['data']['sellopen'])
        total_investment_api = str(portfolio_rs['data']['total_investment'])
        return rdn_balance_api, trading_balance_api, buying_power_api, buyopen_api,cash_balance_api,earnings_api,market_value_api,return_api,sellopen_api,total_investment_api

    @allure.step("Collect ui data for portfolio")
    def collect_ui_data_for_portfolio(self):
        RDN_H = self.get_attribute(rdn_h, "text")
        rdn_balance_ui = RDN_H[3:].replace(',','')
        buying_power = self.get_attribute(buying_power_H, "text")
        trading_balance_ui = buying_power[16:].replace(',','')
        self.click_on_portfolio_btn()
        buying_power_ui = self.get_attribute(buying_power_value, "text").replace(',','')
        buyopen_ui = self.get_attribute(open_buy, "text").replace(',','')
        cash_balance_ui = self.get_attribute(cash_balance, "text").replace(',','')
        earnings_ui = int(self.get_attribute(p_l_value, "text").replace(',', ''))
        market_value_ui = (self.get_attribute(portfolio_value_port, "text"))[4:]
        return_ui = (self.get_attribute(pl_percentage_over, "text"))[1:5]
        sellopen_ui = self.get_attribute(open_sell, "text")
        total_investment_ui=self.get_attribute(invested_value, "text").replace(',', '')
        return rdn_balance_ui, trading_balance_ui, buying_power_ui, buyopen_ui, cash_balance_ui, earnings_ui, market_value_ui, return_ui, sellopen_ui, total_investment_ui





