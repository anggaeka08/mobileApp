import pytest
from selenium.common.exceptions import NoSuchElementException
from SiminvestAppQa.src.data.userData import user_data
import allure
import logging as logger
from SiminvestAppQa.src.pages.Android_pages.stock_detail_page import StockDetailPage
from SiminvestAppQa.src.utilities.requestUtilities import RequestsUtilities
from datetime import datetime
month_dict = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}
back_btn="//android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.ImageView"
month_loc = '//android.view.ViewGroup[@content-desc="EventsCalendar"]/android.widget.HorizontalScrollView[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.SeekBar/android.widget.TextView'
calender_day= '//android.view.ViewGroup[@content-desc="EventsCalendar"]/android.widget.HorizontalScrollView[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.SeekBar/android.view.ViewGroup                   '
calender_week= 'HEADER_MONTH_NAME-calendar_1688688000000'
today_sub_1 = 'TodaySubHeader1'
today_sub_2 = 'TodaySubHeader7'
todays_sub_3 = 'TodaySubHeader8'
dividend_stock_code = 'DividendStockCode0'
dividend_rp = 'DividendRp0'
dividend_label = 'DividendLabel0'
rups_code = 'RUPSStockCode0'
rups_time = 'RUPSTime0'
expose_code = 'PublicExposeStockCode0'
expose_time = 'PublicExposeTime0'
dividend_tab = 'EventsPageHeaderTab1'
div_symbol = 'DividendTabHeaderStockCode'
div_div = 'DividendTabHeader1'
div_cum='DividendTabHeader2'
div_ex = 'DividendTabHeader3'
div_rec = 'DividendTabHeader4'
div_pay = 'DividendTabHeader5'
empty_page = '//android.widget.TextView[@text="Tidak ada agenda hari ini"]'
stock_split_tab ='EventsPageHeaderTab2'
reverse_split_tab = 'EventsPageHeaderTab3'
right_issue_tab='EventsPageHeaderTab4'
right_symbol = 'RightIssueTabHeaderSymbol'
right_ratio = 'RightIssueTabHeader1'
right_factorv='RightIssueTabHeader2'
right_symbol_0='RightIssueTabSymbol0'
right_factor_0 ='RightIssueTabFactor0'
right_ratio_0='RightIssueTabRatio0'
warrant_tab='EventsPageHeaderTab5'
warrant_symbol = 'WarrantTabHeaderSymbol'
warrant_exercise = 'WarrantTabHeader1'
warrant_trad_start = 'WarrantTabHeader2'
warrant_trad_end ='WarrantTabHeader3'
bonus_tab = 'EventsPageHeaderTab6'
rups_tab = 'EventsPageHeaderTab7'
public_expose_tab='EventsPageHeaderTab8'
public_symbol='PublicExposeTabHeaderSymbol'
public_date='PublicExposeTabHeader1'
public_time='PublicExposeTabHeader2'
public_venue='PublicExposeTabHeader3'
ipo_tab = 'EventsPageHeaderTab9'
class EventPage(StockDetailPage):

    @allure.step("Open event page")
    def click_on_back_btn_on_event(self):
        self.click(back_btn)

    @allure.step("verify all tab available")
    def verify_all_tab_available(self):
        tab_name=[]
        original_tab = ['Today', 'Dividend','Stock Split', 'Reverse Split','Right Issue', 'Warrant', 'Bonus', 'RUPS', 'Public Expose', 'IPO']
        for i in range(10):
            tab_name.append(self.get_attribute(f'//android.view.ViewGroup[@content-desc="EventsPageHeaderTab{i}"]/android.widget.TextView','text'))
            if i ==3:
                self.scroll_with_two_element(f'//android.view.ViewGroup[@content-desc="EventsPageHeaderTab0"]/android.widget.TextView', f'//android.view.ViewGroup[@content-desc="EventsPageHeaderTab{i}"]/android.widget.TextView')
            elif i ==5:
                self.scroll_with_two_element(f'//android.view.ViewGroup[@content-desc="EventsPageHeaderTab3"]/android.widget.TextView', f'//android.view.ViewGroup[@content-desc="EventsPageHeaderTab{i}"]/android.widget.TextView')
            elif i ==7:
                self.scroll_with_two_element(f'//android.view.ViewGroup[@content-desc="EventsPageHeaderTab5"]/android.widget.TextView', f'//android.view.ViewGroup[@content-desc="EventsPageHeaderTab{i}"]/android.widget.TextView')
        logger.info(tab_name)
        self.assert_equal(tab_name, original_tab)

    #scroll for with two component
    @allure.step("scroll for with two component")
    def scroll_with_two_element(self, first, second):
        self.sleep(2)
        second_coordinate = self.get_attribute(first, 'bounds')
        lst_1 = second_coordinate.split(',')
        fist_x = int(lst_1[0][1:])
        fist_y = int(lst_1[1][0:3])
        fist_coordinate = self.get_attribute(second, 'bounds')
        lst_2 = fist_coordinate.split(',')
        sec_x = int(lst_2[0][1:])
        sec_y = int(lst_2[1][0:3])
        # logger.info(f'{second_coordinate} {type(second_coordinate)} {second_coordinate[1]}')
        # logger.info(f'{fist_coordinate} {type(fist_coordinate)} {fist_coordinate[1]}')
        self.scroll_screen(start_x=sec_x, start_y=sec_y, end_x=fist_x, end_y=fist_y, duration=10000)
        self.sleep(2)

    @allure.step("verify today tab")
    def verify_today_tab(self):
        month_name = self.get_attribute(month_loc,'text')
        currentMonth = datetime.now().month
        currentYear = datetime.now().year
        self.assert_equal(month_name, f"{month_dict[currentMonth]} {currentYear}")
        self.assert_equal(self.get_attribute(today_sub_1, 'text'), ' Dividend ')
        self.assert_equal(self.is_element_visible(dividend_stock_code), True)
        self.assert_equal(self.is_element_visible(dividend_rp), True)
        self.assert_equal(self.is_element_visible(dividend_label), True)
        # self.assert_equal(self.get_attribute(today_sub_2, 'text'), ' RUPS ')
        # self.assert_equal(self.is_element_visible(rups_code), True)
        # self.assert_equal(self.is_element_visible(rups_time), True)
        self.assert_equal(self.get_attribute(todays_sub_3, 'text'), ' Public Expose ')
        self.assert_equal(self.is_element_visible(expose_code), True)
        self.assert_equal(self.is_element_visible(expose_time), True)
        for i in range(1, 8):
            self.assert_equal(self.is_element_visible(f'//android.view.ViewGroup[@content-desc="EventsCalendar"]/android.widget.HorizontalScrollView[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.SeekBar/android.view.ViewGroup/android.widget.TextView[{i}]'), True)

    @allure.step("Validate Dividend tab")
    def validate_dividend_tab(self):
        self.click(dividend_tab)
        self.sleep(3)
        self.assert_equal(self.get_attribute(div_symbol, 'text'), 'Symbol')
        self.assert_equal(self.get_attribute(div_div, 'text'), 'Dividend')
        self.assert_equal(self.get_attribute(div_cum, 'text'), 'Cum Date')
        self.assert_equal(self.get_attribute(div_ex, 'text'), 'Ex Date')
        cum_date = []
        ex_date = []
        for i in range(8):
            self.assert_equal(self.is_element_visible(f'DividendTabStockCode{i}'), True)
            self.assert_equal(self.is_element_visible(f'DividendTabDiv{i}'), True)
            cum_date.append(self.get_attribute(f'DividendTabCumDate{i}', 'text'))
            ex_date.append(self.get_attribute(f'DividendTabExDate{i}', 'text'))
        self.scroll_with_two_element('DividendTabDiv1', 'DividendTabExDate1')
        for i in range(8):
            self.assert_equal(self.is_element_visible(f'DividendTabRecDate{i}'), True)
            self.assert_equal(self.is_element_visible(f'DividendTabPayDate{i}'), True)
        sorted_cum_date = sorted(cum_date,reverse=True)
        sorted_ex_date = sorted(ex_date, reverse=True)
        self.assert_equal(sorted_cum_date, cum_date)
        self.assert_equal(sorted_ex_date, ex_date)

    @allure.step("validate stock split")
    def validate_stock_split(self):
        self.click(stock_split_tab)
        self.sleep(3)
        self.assert_equal(self.is_element_visible(empty_page), True)

    @allure.step("validate reverse split")
    def validate_reverse_split(self):
        self.click(reverse_split_tab)
        self.sleep(3)
        self.assert_equal(self.is_element_visible(empty_page), True)

    @allure.step("Validate Right issue")
    def validate_right_issue(self):
        self.click(right_issue_tab)
        self.sleep(3)
        self.assert_equal(self.is_element_visible(right_symbol), True)
        self.assert_equal(self.is_element_visible(right_ratio), True)
        self.assert_equal(self.is_element_visible(right_factorv), True)
        self.assert_equal(self.is_element_visible(right_symbol_0), True)
        self.assert_equal(self.is_element_visible(right_factor_0), True)
        self.assert_equal(self.is_element_visible(right_ratio_0), True)

    @allure.step("validate warrant tab")
    def validate_warrant_tab(self):
        trading_start_date = []
        trading_end_date=[]
        exercise_end_date = []
        self.click(warrant_tab)
        self.sleep(3)
        self.assert_equal(self.get_attribute(warrant_symbol, 'text'), 'Symbol')
        self.assert_equal(self.get_attribute(warrant_exercise, 'text'), 'Exercise Price')
        self.assert_equal(self.get_attribute(warrant_trad_start, 'text'), 'Trading Start')
        self.assert_equal(self.get_attribute(warrant_trad_end, 'text'), 'Trading End')
        for i in range(8):
            self.assert_equal(self.is_element_visible(f'WarrantTabSymbol{i}'), True)
            self.assert_equal(self.is_element_visible(f"WarrantTabSymbol{i}"), True)
            trading_start_date.append(self.get_attribute(f"WarrantTabTrdStart{i}", 'text'))
            trading_end_date.append(self.get_attribute(f'WarrantTabTrdEnd{i}', 'text'))
        self.scroll_with_two_element('WarrantTabPrice2', 'WarrantTabTrdEnd2')
        for i in range(8):
            exercise_end_date.append(self.get_attribute(f'WarrantTabExDate{i}', 'text'))
            #self.assertGreater(trading_end_date[i], trading_start_date[i])
        trading_end_sort = sorted(trading_end_date, reverse=True)
        exercise_end_sort = sorted(exercise_end_date, reverse=True)
     #   self.assert_equal(trading_end_sort, trading_end_date)
      #  self.assert_equal(exercise_end_sort, exercise_end_date)

    @allure.step("validate bonus tab")
    def validate_bonus_tab(self):
        self.click(bonus_tab)
        self.sleep(3)
        for i in range(1,4):
            self.assert_equal(self.is_element_visible(f"BonusTabHeader{i}"), True)

    @allure.step("validate rups tab")
    def validate_rups_tab(self):
        self.click(rups_tab)
        self.sleep(3)
        self.assert_equal(self.is_element_visible('RUPSTabHeaderSymbol0'), True)
        self.assert_in('Jakarta', self.get_attribute('RUPSTabHeaderVenue0', 'text'))

    @allure.step("validate Pubic expose tab")
    def validate_public_expose_tab(self):
        self.click(public_expose_tab)
        self.sleep(3)
        self.assert_equal(self.is_element_visible('PublicExposeTabSymbol0'), True)
        self.assert_in('Passcode', self.get_attribute('PublicExposeTabVenue0', 'text'))

    @allure.step("validate IPO Tab")
    def validate_IPO_tab(self):
        self.click(ipo_tab)
        self.sleep(3)
        self.assert_equal(self.is_element_visible('IPOTabHeaderCompName'), True)

    @allure.step("Api data validation for event page")
    def api_data_validation_for_event_page(self):
        today_data_ui = []
        dividend_data_ui = []
        right_data_ui = []
        warrant_data_ui = []
        bonus_data_ui = []
        rups_data_ui = []
        public_data_ui = []
        ipo_data_ui = []
        for i in range(7):
            today_data_ui.append(self.get_attribute(f'RUPSStockCode{i}', 'text'))
        self.click(dividend_tab)
        self.sleep(3)
        for i in range(5):
            dividend_data_ui.append(self.get_attribute(f'DividendTabStockCode{i}', 'text'))
        self.click(stock_split_tab)
        self.sleep(3)
        self.click(reverse_split_tab)
        self.sleep(3)
        self.click(right_issue_tab)
        self.sleep(3)
        right_data_ui.append(self.get_attribute('RightIssueTabSymbol0', 'text'))
        self.click(warrant_tab)
        self.sleep(3)
        for i in range(5):
            warrant_data_ui.append(self.get_attribute(f'WarrantTabSymbol{i}', 'text'))
        self.click(bonus_tab)
        self.sleep(3)
        bonus_data_ui.append(self.get_attribute('BonusTabStockCode0', 'text'))
        self.click(rups_tab)
        self.sleep(3)
        for i in range(5):
            rups_data_ui.append(self.get_attribute(f'RUPSTabHeaderSymbol{i}', 'text'))
        self.click(public_expose_tab)
        self.sleep(3)
        for i in range(5):
            public_data_ui.append(self.get_attribute(f'PublicExposeTabSymbol{i}', 'text'))
        self.click(ipo_tab)
        self.sleep(3)
        ipo_data_ui.append(self.get_attribute(f'IPOTabCompName0', 'text'))


    @allure.step("Open Event page")
    def open_event_page(self, number):
        self.login_and_verify_homepage_for_reg_user(number)
        self.click_on_event_btn()
        self.sleep(2)
        self.verify_event_page()
        
    @allure.step("Validate swipe up and swipe down the page")
    def validate_scroll_up_and_down_on_Event_page(self):
        self.scroll_up()
        self.assert_equal(self.is_element_visible(today_sub_1), False)
        self.scroll_down()
        self.assert_equal(self.is_element_visible(today_sub_1), True)

    @allure.step("Validate sunday to saturday")
    def validate_sunday_to_saturday(self):
       self.assert_equal(self.is_element_visible(calender_day), True)
    
    @allure.step("Validate week on calender")
    def validate_week_on_calender(self):
        self.scroll_up()
        self.assert_equal(self.is_element_visible(calender_week), False)
        self.scroll_down()
        self.assert_equal(self.is_element_visible(calender_week), True)
  
    @allure.step("validate Read venue Public Expose tab")
    def validate_warrant_tab(self):
        public_expo_date = []
        public_expo_time=[]
        public_expo_venue = []
        self.click(public_expose_tab)
        self.sleep(3)
        self.assert_equal(self.get_attribute(public_symbol, 'text'), 'Symbol')
        self.assert_equal(self.get_attribute(public_date, 'text'), 'Date')
        self.assert_equal(self.get_attribute(public_time, 'text'), 'Time')
        self.assert_equal(self.get_attribute(public_venue, 'text'), 'venue')
        for i in range(8):
            self.assert_equal(self.is_element_visible(f'PublicExposeTabSymbol{i}'), True)
            self.assert_equal(self.is_element_visible(f"PublicExposeTabSymbol{i}"), True)
            public_expo_date.append(self.get_attribute(f"PublicExposeTabDate{i}", 'text'))
            public_expo_time.append(self.get_attribute(f'PublicExposeTabTime{i}', 'text'))
        self.scroll_with_two_element('PublicExposeTabSymbol2', 'PublicExposeTabTime')
        for i in range(8):
            public_expo_venue.append(self.get_attribute(f'PublicExposeTabVenue{i}', 'text'))
       