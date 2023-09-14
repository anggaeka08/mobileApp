import json

from appiumbase import BaseCase
from SiminvestAppQa.src.pages.Android_pages.login_page import LoginPage
import logging as logger
import allure
from SiminvestAppQa.src.data.userData import user_data
from SiminvestAppQa.src.utilities.requestUtilities import RequestsUtilities

request_utilities = RequestsUtilities()
# sdp page Locators
Cari_btn_before_click ='//android.view.ViewGroup[@content-desc="Browser_Stack"]/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText'
cari_btn_after_click ="StockSearch"
stock_entry_code = '(//android.widget.TextView[@content-desc="StockSearchCode"])[1]'
stock_code_btn ='StockSearchCode'
stock_search_name = 'StockSearchName'
search_header = 'StockSearchType'
stock_name ='SDPStockName'
chart_element ='SDPChartArea'
stock_buy_bttton ='SDPBeliBtn'
buy_btn_with_sell='SDPPageSellBtn'
sdp_orderbook ="//android.widget.TextView[@text='Order Book']"
sdp_news = "//android.widget.TextView[@text='News']"
sdp_keystate = "//android.widget.TextView[@text='Keystats']"
sdp_profile = "//android.widget.TextView[@text='Financials']"
sdp_bit = "//android.widget.TextView[@text='Bid']"
mf_saerched_entry = '//android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup'
mf_header = '//android.widget.TextView[@text="Simas Saham Bertumbuh"]'
#RDN Balance page locators
saldo_rdn_btn = 'HomePageRDN'
rdn_balance_page_header = 'RdnBalanceHeader'
rdn_balance = 'RdnBalanceValue'
topup_btn = 'RdnBalanceTopIcon'
trik_dana_btn = 'RdnBalanceTarikIcon'
riwayat_btn = 'RdnBalanceRiwayatIcon'
informasi_saldo = 'RdnBalanceSaldo'
informasi_rekening = 'RdnBalanceRekening'
home_rdn_value = 'HomePageRdnValue'
homepage_starpoint_value = 'HomepageStarPointValue'
#TarikDana page locators
tarik_dana_header = 'Tarik DanaHeader'
dana_tersedia = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[2]'
account_details = 'TarikPagePenarikan'
nominal_penarikan = 'TarikPageNominal'
tarik_dana_btn = 'TarikPageBtn'
#riwayat page locators
riwayat_page_header = 'RiwayatHeader'
riwayat_entry_1 = 'RiwayatPageEntry0 '
riwayat_entry_2 = 'RiwayatPageEntry1 '
riwayat_entry_3 = 'RiwayatPageEntry1 '
default_watchlist_btn="//android.widget.TextView[@text='Default']"
#locators to verify spellings
Saham ="//android.widget.TextView[@text='Saham']"
Reksadana ="//android.widget.TextView[@text='Reksadana']"
StarPoint ="HomeStarPointText"
Portfolio_Saham = "HomepagePortfolioText"
today = "HomepageRpAmount"
homepage_rp = 'HomepageRp'
Buying_Power="HomepagebuyPower"
Keren_dua = "HomepageText1"
Top_up = "//android.widget.TextView[@text='Top Up']"
Indeks = "//android.widget.TextView[@text='Indeks']"
Sektor = "//android.widget.TextView[@text='Sektor']"
Events = "//android.widget.TextView[@text='Events']"
eipo_btn = "//android.widget.TextView[@text='eIPO']"
eipo = "//android.widget.TextView[@text='eIPO']"
full_name_IHSG ='//android.view.ViewGroup[@content-desc="HomepageIHSGStock"]/android.widget.TextView[3]'
Top_Frequency = "//android.widget.TextView[@text='Top frequency']"
Home = '//android.widget.TextView[@text="Home"]'
Research ='//android.widget.TextView[@text="Research"]'
Portfolio = '//android.widget.TextView[@text="Portfolio"]'
Transaction ='//android.widget.TextView[@text="Transaction"]'
profile = '//android.widget.TextView[@text="Profile"]'
Dafter_btn = '//android.widget.TextView[@text="Daftar / Masuk"]'
Masuk_locator ="//android.widget.TextView[@index='0']"
Masuk_page_data = "//android.widget.TextView[@index='1']"
top_up_page_header = 'TopupPageHeader'
top_up_page_down = 'TopupPageText1'
Simobi_btn = 'TopupPageSimobiTitle'
Bank_lainnya = 'TopupPageBankTitle'
indeks_page_header = 'IndeksPageHeader'
indeks_page_entry_1 = 'IndeksEntryName0'
indeks_page_entry_2 = 'IndeksEntryName1'
indeks_page_entry_3 = 'IndeksEntryName2'
# Sector page locators
sector_page_header = 'SektorPageHeader'
energi = 'SectorPageType0'
barang_baku = 'SectorPageType1'
perindustrian ='SectorPageType2'
Barang_Konsum_non_primer ='SectorPageType3'
barang_konsum_primer = 'SectorPageType4'
kesehatan = 'SectorPageType5'
keuangan = 'SectorPageType6'
properties_real_estate ='SectorPageType7'
teknologi ='SectorPageType8'
infrastruktur = 'SectorPageType9'
transportasi = 'SectorPageType10'
# Event page locators
events_page_header = 'EventsPageHeader'
events_page_data = '//android.view.ViewGroup[@content-desc="EventsPageHeaderTab1"]/android.widget.TextView'
#eipo page locators
eipo_page_header = 'eIPOPageHeader'
eipo_panduan = 'eIPOPageDetailsOpen'
eipo_entry_1 = 'eIPOPageEntry0'
eipo_entry_2 = 'eIPOPageEntry1'
eipo_code_in_entry_1 = 'eIPOPageEntry0Code'
eipo_name_in_entry_1 = 'eIPOPageEntry0Name'
eipo_img_in_entry_1 = 'eIPOPageEntry0Image'
eipo_other_details_in_entry_1 = 'eIPOPage0PhaseValue'
eipo_entyr_data = 'eIPOPage0PhaseDate'
ipo_type_for_entry_1 = 'eIPOPage0Type'
IHSG_stock_element = 'HomepageIHSGStock'
homepage_stock_code = '//android.view.ViewGroup[@content-desc="HomepageIHSGStock"]/android.widget.TextView[1]'
homepage_stock_value = '//android.view.ViewGroup[@content-desc="HomepageIHSGStock"]/android.widget.TextView[2]'
homepage_stock_per = '//android.view.ViewGroup[@content-desc="HomepageIHSGStock"]/android.widget.TextView[4]'
homepag_stock_name = '//android.view.ViewGroup[@content-desc="HomepageIHSGStock"]/android.widget.TextView[3]'
top_frequency_stock_1 = 'HomepageTFStock0'
top_frequency_stock_2 = 'HomepageTFStock1'
top_frequency_stock_5 = 'HomepageTFStock3'
top_frequency_down_arrow = 'MoverPageDownArrow'
top_frequency_page_header ='TopFrequencyHeader'
half_card_entry ='ScreenHomeTop frequency'
see_more_btn ='//android.widget.TextView[@text="See more"]'
mover_page_header = 'MoverPageHeader'
mover_page_down = 'Mover'
mover_page_entry_1 = 'MoverPageEntry0'
mover_page_entry_2 = 'MoverPageEntry1'
default_btn ='//android.widget.TextView[@text="Default"]'
watchlist_header='WatchListHeader'
add_btn_watchlist ='WatchListAddBtn'
watchlist_entry ='WatchListName0'
watchlist_name = 'WatchListName0'
watchlist_right_btn='WatchListActiveBtn0'
watchlist_edit_btn ='WatchListNameEditBtn0'
watchlist_delete_btn='WatchListDeleteBtn0'
edit_btn = '//android.widget.TextView[@text="Edit"]'
portfolioe_saham ='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[5]/android.widget.TextView[1]'
portfolio_rp = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[5]/android.widget.TextView[2]'
default_watchlist_entry_1='HomepageWLEntry0'
research_header ='ResearchPageHeader'
last_report = 'ResearchPageTabHeader1'
news = 'ResearchPageTabHeader2'
media = 'ResearchPageTabHeader3'
Research_btn = '//android.widget.TextView[@text="Research"]'
stock_signal = '/ResearchPageTabHeader0'
stock_signal_entry_1 ='ResearchPageSignalEntry0'
stock_signal_entry_2 = 'ResearchPageSignalEntry1'
stock_signal_down = 'ResearchPageSignalTandai'
phone_home_screen='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/com.miui.home.launcher.ScreenView[1]/android.widget.FrameLayout[1]/android.view.ViewGroup'
portfolio_btn = '//android.widget.TextView[@text="Portfolio"]'
investasi_sekrang = '//android.widget.TextView[@text="INVESTASI SEKARANG"]'
kamu_belum ='//android.widget.TextView[@text="Kamu belum memiliki investasi"]'
portofolio_saham ='PortPagePorfilioText'
portfolio_entry_1 = 'PortPageEntry0'
portfolio_entry_2 = 'PortPageEntry1'
reksadhana_tab = '(//android.view.ViewGroup[@content-desc="PortPageSahamTab"])[2]'
transition_btn = '//android.widget.TextView[@text="Transaction"]'
saham_trans = 'Saham_tab'
order_tab = 'Order List_tab'
trade_list_tab = 'Trade List_tab'
history_tab = 'History_tab'
GTC_list_tab = 'GTC List_tab'
all_types = 'TransactionSahamOrderListDropDown'
cari_saham = 'TransactionSahamOrderListSearchBox'
trans_details_header = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[5]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup'
trans_entry_1 = 'order_list_entry_0'
entry_for_account = 'ProfilePageImage'
account_text = 'ScreenProfilePageName'
username_on_homepage = 'HomePageUserName'
stock_add_page_Header = 'StockAddPageHeader'
mulai_btn ='//android.widget.TextView[@text="Mulai"]'
reksadhana_home = '//android.widget.TextView[@text="Top Reksadana"]'
# locators for mover page
mover_type_list= ['ScreenHomeTop frequency', 'ScreenHomeTop gainers', 'ScreenHomeTop gainers %', 'ScreenHomeTop value', 'ScreenHomeTop Volume', 'ScreenHomeTop losers','ScreenHomeTop losers %','ScreenHomePapan Akselerasi']
marker = 'UrutkanSelectMark'
top_gainer = 'ScreenHomeTop gainers'
top_gainer_on_homepage = "//android.widget.TextView[@text='Top gainers']"
mover_stock_code = 'MoverPageEntry0Code'
mover_stock_code_1 = 'MoverPageEntry13Code'
search_btn_mover = 'MoverPageSearchBtn'
# locator sheild tracker
Saya_Setuju= "//android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.TextView[@text = 'Saya Setuju']"
Tidak_Setuju = "//android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.TextView[@text = 'Tidak Setuju']"
Syarat_dan_ketentuan = "//android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.widget.TextView[1][@text = 'Syarat dan ketentuan']"
btn_reksadana = 'Homepage_reksadana_btn'
reksadana_header ='(//android.view.ViewGroup/android.view.ViewGroup[7]/android.widget.TextView[1])[1]'
reksadana_value = '/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[7]/android.widget.TextView[2]'
reksadana_today = '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[7]/android.widget.TextView[3]'
tampilkan ="//android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[@text = 'Sembunyikan']"

class HomePage(LoginPage):

    @allure.step("click global search btn and search stock")
    def click_global_search_btn_and_saerch_stock(self, stock_code):
        self.click(Cari_btn_before_click)
        self.update_text(cari_btn_after_click, stock_code)

    @allure.step("click global search btn and search stock")
    def global_search_stock(self, stock_code):
        self.update_text(cari_btn_after_click, stock_code)

    @allure.step("click global search btn")
    def click_global_search_btn(self):
        self.click(Cari_btn_before_click)
        self.sleep(3)

    @allure.step("Validate Text in global search before click")
    def validate_text_in_global_search_before_click(self):
        self.sleep(3)
        self.assert_equal(self.get_attribute(Cari_btn_before_click, 'text'), 'Cari...')

    @allure.step("Validate text and keyboard on after click in global search")
    def Validate_text_and_keyboard_on_after_click_in_global_search(self):
        self.assert_equal(self.get_attribute(cari_btn_after_click, 'text'), 'Cari saham atau reksadana')
        self.assert_equal(self.check_keyboard_shown() , True)

    @allure.step("Validate search entry for invalid stock")
    def validate_search_entry_for_invalid_stock_and_saham_text(self):
        #self.click_global_search_btn_and_saerch_stock('ALLLI')
        self.update_text(cari_btn_after_click, 'ALLLI')
        self.assert_not_equal(self.get_attribute(cari_btn_after_click, 'text'), 'Cari saham atau reksadana')
        self.assert_equal(self.is_element_visible(stock_entry_code), False)

    @allure.step("Validate saham header and stock code and stock name")
    def validate_saham_header_and_stock_code_and_stock_name(self, name):
        self.assert_equal(self.get_attribute(cari_btn_after_click, 'text'), name)
        self.assert_equal(self.is_element_visible(search_header),True)
        self.assert_equal(self.get_attribute(search_header, 'text'),'SAHAM')
        self.assert_equal(self.is_element_visible(stock_code_btn),True)
        self.assert_equal(self.is_element_visible(stock_search_name),True)

    @allure.step("click on stock code")
    def click_on_stock_code(self):
        self.double_tap(stock_code_btn)
        self.sleep(5)

    @allure.step("verify stock page")
    def verify_sdp_page(self):
        self.assert_equal(self.is_element_visible(stock_name), True)
        #stock_name_text = self.get_attribute(stock_name, "text")
        #self.assert_equal(stock_name_text, "Ace Hardware Indonesia Tbk.")
        #self.is_element_visible(chart_element)
        #self.is_element_visible(stock_buy_bttton)
        beli_with_sell = self.is_element_visible(buy_btn_with_sell)
        if beli_with_sell == True:
            buy_btn_with_sell_present = self.is_element_visible(buy_btn_with_sell)
            assert buy_btn_with_sell_present == True, f"buy Btn Should be present"
        else :
            stock_buy_bttton_text = self.get_attribute(stock_buy_bttton, "text")
            self.assert_equal(stock_buy_bttton_text, "")
        #self.is_element_visible(sdp_orderbook)
        self.scroll_up()
        self.sleep(2)
        sdp_orderbook_text = self.get_attribute(sdp_orderbook, "text")
        self.assert_equal(sdp_orderbook_text, "Order Book")
        #self.is_element_visible(sdp_news)
        sdp_news_text = self.get_attribute(sdp_news, "text")
        self.assert_equal(sdp_news_text, "News")
        #self.is_element_visible(sdp_keystate)
        sdp_keystate_text = self.get_attribute(sdp_keystate, "text")
        self.assert_equal(sdp_keystate_text, "Keystats")
        #self.is_element_visible(sdp_profile)
        sdp_profile_text = self.get_attribute(sdp_profile, "text")
        self.assert_equal(sdp_profile_text, "Financials")
        #self.is_element_visible(sdp_bid)
        # sdp_bit_text = self.get_attribute(sdp_bit, "text")
        # self.assert_equal(sdp_bit_text, "Bid")

    @allure.step("Validate MF search in global search and redirection after click")
    def validate_MF_search_in_global_search_and_Redirection_after_click(self):
        self.assert_equal(self.is_element_visible(search_header), True)
        self.assert_equal(self.get_attribute(search_header, 'text'), 'REKSADANA')
        self.assert_equal(self.is_element_visible(mf_saerched_entry), True)
        self.click(mf_saerched_entry)
        self.sleep(5)
        self.assert_equal(self.is_element_visible(mf_header), True)
        self.go_back()
        self.sleep(3)
        self.assert_equal(self.is_element_visible(search_header), True)
        self.assert_equal(self.get_attribute(search_header, 'text'), 'REKSADANA')
        self.assert_equal(self.is_element_visible(mf_saerched_entry), True)

    @allure.step("Click to soldo rdn btn")
    def click_to_soldo_rdn(self):
        self.click(saldo_rdn_btn)
        self.sleep(2)

    @allure.step("verify rdn balance page")
    def verify_rdn_balance_page(self):
        rdn_balance_page_header_text = self.get_attribute(rdn_balance_page_header, "text")
        self.assert_equal(rdn_balance_page_header_text, "RDN Balance")
        rdn_balance_tag = self.is_element_visible(rdn_balance)
        assert rdn_balance_tag == True, f"Element should be visible"
        topup_btn_present = self.is_element_visible(topup_btn)
        assert topup_btn_present == True ,f"topup Btn Should be present"
        trik_dana_btn_present = self.is_element_visible(trik_dana_btn)
        assert trik_dana_btn_present == True, f"trik dana Btn Should be present"
        riwayat_btn_present = self.is_element_visible(riwayat_btn)
        assert riwayat_btn_present == True, f"riwayat Btn Should be present"
        informasi_saldo_present = self.is_element_visible(informasi_saldo)
        assert informasi_saldo_present == True, f"informasi Should be present"
        informasi_rekening_present = self.is_element_visible(informasi_rekening)
        assert informasi_rekening_present == True, f"informasi_rekening Should be present"

    @allure.step("click on tarik dana btn")
    def click_on_tarik_dana_btn(self):
        self.click(trik_dana_btn)
        self.sleep(2)

    @allure.step("verify tarik dana btn")
    def verify_tarik_dana_page(self):
        tarik_dana_header_text = self.get_attribute(tarik_dana_header, "text")
        self.assert_equal(tarik_dana_header_text, "Tarik Dana")
        #dana_tersedia_present = self.is_element_visible(dana_tersedia)
        #assert dana_tersedia_present == True, f"dana_tersedia Should be present"
        account_details_present = self.is_element_visible(account_details)
        assert account_details_present == True, f"account_details Should be present"
        nominal_penarikan_present = self.is_element_visible(nominal_penarikan)
        assert nominal_penarikan_present == True, f"nominal_penarikan Should be present"
        tarik_dana_btn_present = self.is_element_visible(tarik_dana_btn)
        assert tarik_dana_btn_present == True, f"tarik_dana_btn Should be present"

    @allure.step("click on riwayat btn")
    def click_on_riwayat_btn(self):
        self.click(riwayat_btn)
        self.sleep(2)

    @allure.step("verify riwayat page")
    def verify_riwayat_page(self):
        self.sleep(3)
        riwayat_page_header_text = self.get_attribute(riwayat_page_header, "text")
        self.assert_equal(riwayat_page_header_text, "Riwayat")
        #riwayat_entry_1_present = self.is_element_visible(riwayat_entry_1)
        #assert riwayat_entry_1_present == True, f"riwayat_entry_1 Should be present"


    @allure.step("scroll up")
    def scroll_up(self):
        self.scroll_screen(start_x=500, start_y=1820, end_x=523, end_y=809, duration=10000)
        self.sleep(2)

    @allure.step("scroll down")
    def scroll_down(self):
        self.scroll_screen(start_x=513, start_y=513, end_x=503, end_y=1754, duration=10000)
        self.sleep(2)

    @allure.step("small scroll down")
    def small_scroll_down(self):
        self.scroll_screen(start_x=513, start_y=513, end_x=513, end_y=750, duration=10000)
        self.sleep(2)

    @allure.step("verify spelling on homepage")
    def verify_spelling_on_homepage(self):
        Saham_text = self.get_attribute(Saham, "text")
        self.assert_equal(Saham_text, "Saham")
        Reksadana_text = self.get_attribute(Reksadana, "text")
        self.assert_equal(Reksadana_text, "Reksadana")
        StarPoint_text = self.get_attribute(StarPoint, "text")
        self.assert_equal(StarPoint_text, "StarPoin")
        Portfolio_Saham_text = self.get_attribute(Portfolio_Saham, "text")
        self.assert_equal(Portfolio_Saham_text, "Portfolio saham")
        today_text = self.get_attribute(today, "text")
        self.assert_equal(today_text[-5:], "Today")
        # Buying_Power_text = self.get_attribute(Buying_Power, "text") #removed from app
        # self.assert_equal(Buying_Power_text[:12], "Buying power")
        #Keren_dua_text = self.get_attribute(Keren_dua, "text")
        #self.assert_equal(Keren_dua_text, "Sudah siap? Yuk, mulai sekarang")
        Top_up_text = self.get_attribute(Top_up, "text")
        self.assert_equal(Top_up_text, "Top Up")
        Indeks_text = self.get_attribute(Indeks, "text")
        self.assert_equal(Indeks_text, "Indeks")
        sektor_text = self.get_attribute(Sektor, "text")
        self.assert_equal(sektor_text, "Sektor")
        Events_text = self.get_attribute(Events, "text")
        self.assert_equal(Events_text, "Events")
        eipo_text = self.get_attribute(eipo, "text")
        self.assert_equal(eipo_text, "eIPO")
        full_name_IHSG_text = self.get_attribute(full_name_IHSG, "text")
        self.assert_equal(full_name_IHSG_text, "Indeks Harga Saham Gabungan")
        top_frequency_text = self.get_attribute(Top_Frequency, "text")
        self.assert_equal(top_frequency_text, "Top frequency")
        home_text = self.get_attribute(Home, "text")
        self.assert_equal(home_text, "Home")
        research_text = self.get_attribute(Research, "text")
        self.assert_equal(research_text, "Research")
        portfolio_text = self.get_attribute(Portfolio, "text")
        self.assert_equal(portfolio_text, "Portfolio")
        Transaction_text = self.get_attribute(Transaction, "text")
        self.assert_equal(Transaction_text, "Transaction")
        Profile_text = self.get_attribute(profile, "text")
        self.assert_equal(Profile_text, "Profile")


    @allure.step("click on daftar masuk")
    def click_on_Daftar_masuk(self):
        self.click(Dafter_btn)

    @allure.step("verify registration page")
    def verify_registration_page(self):
        Masuk_locator_text = self.get_attribute(Masuk_locator, "text")
        self.assert_equal(Masuk_locator_text, "Masuk")
        Masuk_page_data_text = self.get_attribute(Masuk_page_data, "text")
        self.assert_equal(Masuk_page_data_text, "Masukkan username, password dan pin transaksi simas equity Kamu")

    @allure.step("click on top up btn")
    def click_on_top_up_btn(self):
        self.click(topup_btn)
        self.sleep(2)

    @allure.step("verify top up page")
    def verify_topup_page(self):
        top_up_page_header_text = self.get_attribute(top_up_page_header, "text")
        self.assert_equal(top_up_page_header_text, "Topup")
        top_up_page_down_text = self.get_attribute(top_up_page_down, "text")
        self.assert_equal(top_up_page_down_text, "Silahkan melakukan tranfer dana ke nomor RDN dibawah ini")
        Simobi_btn_text = self.get_attribute(Simobi_btn, "text")
        self.assert_equal(Simobi_btn_text, "Simobi +")
        Bank_lainnya_text = self.get_attribute(Bank_lainnya, "text")
        self.assert_equal(Bank_lainnya_text, "Bank lainnya")

    @allure.step("click on indeks btn")
    def click_on_indeks_btn(self):
        self.click(Indeks)

    @allure.step("verify indeks page")
    def verify_indeks_page(self):
        indeks_page_header_text = self.get_attribute(indeks_page_header, "text")
        self.assert_equal(indeks_page_header_text, "Indeks")
        #self.assert_equal(self.is_element_visible(indeks_page_entry_1), True)
        #self.assert_equal(self.is_element_visible(indeks_page_entry_2), True)
        #self.assert_equal(self.is_element_visible(indeks_page_entry_3), True)

    @allure.step("click on sector btn")
    def click_on_sector_button(self):
        self.click(Sektor)

    @allure.step("verify sector page")
    def verify_sector_page(self):
        sector_page_header_text = self.get_attribute(sector_page_header, "text")
        self.assert_equal(sector_page_header_text, "Sectors")
        energi_present = self.is_element_visible(energi)
        assert energi_present == True, f"Energi Should be present"
        barang_baku_present = self.is_element_visible(barang_baku)
        assert barang_baku_present == True, f"Barang Baku Should be present"
        perindustrian_present = self.is_element_visible(perindustrian)
        assert perindustrian_present == True, f"Perindustrian Should be present"
        perindustrian_present = self.is_element_visible(perindustrian)
        assert perindustrian_present == True, f"Perindustrian Should be present"
        Barang_Konsum_non_primer_present = self.is_element_visible(Barang_Konsum_non_primer)
        assert Barang_Konsum_non_primer_present == True, f"Barang Konsum non primer Should be present"
        barang_konsum_primer_present = self.is_element_visible(barang_konsum_primer)
        assert barang_konsum_primer_present == True, f"barang konsum primer Should be present"
        kesehatan_present = self.is_element_visible(kesehatan)
        assert kesehatan_present == True, f"kesehatan Should be present"
        keuangan_present = self.is_element_visible(keuangan)
        assert keuangan_present == True, f"keuangan Should be present"
        properties_real_estate_present = self.is_element_visible(properties_real_estate)
        assert properties_real_estate_present == True, f"properties real estate Should be present"
        teknologi_present = self.is_element_visible(teknologi)
        assert teknologi_present == True, f"teknologi Should be present"
        infrastruktur_present = self.is_element_visible(infrastruktur)
        assert infrastruktur_present == True, f"infrastruktur Should be present"
        transportasi_present = self.is_element_visible(transportasi)
        assert transportasi_present == True, f"transportasi Should be present"

    @allure.step("verify event btn")
    def click_on_event_btn(self):
        self.click(Events)

    @allure.step("verify event page")
    def verify_event_page(self):
        self.sleep(2)
        events_page_header_text = self.get_attribute(events_page_header, "text")
        self.assert_equal(events_page_header_text, "Events")
        events_page_data_text = self.get_attribute(events_page_data, "text")
        self.assert_equal(events_page_data_text, "Dividend")

    @allure.step("click on eipo btn")
    def click_on_eipo_btn(self):
        self.click(eipo_btn)

    @allure.step("verify eipo page")
    def verify_eipo_page(self):
        self.sleep(3)
        eipo_page_header_text = self.get_attribute(eipo_page_header, "text")
        self.assert_equal(eipo_page_header_text, "eIPO")
        # eipo_panduan_present = self.is_element_visible(eipo_panduan)
        # assert eipo_panduan_present == True, f"eipo panduan Should be present"
        # eipo_entry_1_present = self.is_element_visible(eipo_entry_1)
        # assert eipo_entry_1_present == True, f"eipo_entry_1 Should be present"
        # eipo_entry_2_present = self.is_element_visible(eipo_entry_2)
        # assert eipo_entry_2_present == True, f"eipo_entry_2 Should be present"

    @allure.step("verify eipo entry")
    def verify_eipo_entry(self):
        eipo_code_in_entry_1_present = self.is_element_visible(eipo_code_in_entry_1)
        assert eipo_code_in_entry_1_present == True, f"eipo code in entry 1 Should be present"
        eipo_name_in_entry_1_present = self.is_element_visible(eipo_name_in_entry_1)
        assert eipo_name_in_entry_1_present == True, f"eipo name in entry 1 Should be present"
        eipo_img_in_entry_1_present = self.is_element_visible(eipo_img_in_entry_1)
        assert eipo_img_in_entry_1_present == True, f"eipo img in entry 1 Should be present"
        eipo_other_details_in_entry_1_present = self.is_element_visible(eipo_other_details_in_entry_1)
        assert eipo_other_details_in_entry_1_present == True, f"eipo other details in entry 1 Should be present"
        eipo_entyr_data_present = self.is_element_visible(eipo_entyr_data)
        assert eipo_entyr_data_present == True, f"eipo entry data Should be present"
        ipo_type_for_entry_1_present = self.is_element_visible(ipo_type_for_entry_1)
        assert ipo_type_for_entry_1_present == True, f"ipo type for entry 1 Should be present"

    @allure.step("verify home page stock")
    def verify_homepage_stock(self):
        IHSG_stock_element_present = self.is_element_visible(IHSG_stock_element)
        assert IHSG_stock_element_present == True, f"IHSG_stock_element should be present"
        homepage_stock_code_text = self.get_attribute(homepage_stock_code, "text")
        self.assert_equal(homepage_stock_code_text, 'IHSG')
        homepage_stock_value_present = self.is_element_visible(homepage_stock_value)
        assert homepage_stock_value_present == True, f"homepage_stock_value should be present"
        homepage_stock_per_present = self.is_element_visible(homepage_stock_per)
        assert homepage_stock_per_present == True, f"homepage_stock_value should be present"
        homepag_stock_name_text = self.get_attribute(homepag_stock_name, "text")
        self.assert_equal(homepag_stock_name_text, 'Indeks Harga Saham Gabungan')

    @allure.step("verify top frequency presentation")
    def verify_top_frequency_presention(self):
        Top_Frequency_present = self.is_element_visible(Top_Frequency)
        assert Top_Frequency_present == True, f"top_frequency_stock_element Should be present"
        Top_Frequency_text = self.get_attribute(Top_Frequency, "text")
        self.assert_equal(Top_Frequency_text, 'Top frequency')

    @allure.step("verify stock presence in top frequency")
    def verify_stock_presence_in_top_frequency(self):
        #self.scroll_up()
        top_frequency_stock_1_present = self.is_element_visible(top_frequency_stock_1)
        assert top_frequency_stock_1_present == True, f"top_frequency_stock_1 Should be present"
        top_frequency_stock_2_present = self.is_element_visible(top_frequency_stock_2)
        assert top_frequency_stock_2_present == True, f"top_frequency_stock_2 Should be present"

    @allure.step("click on TF down arrow")
    def click_on_TF_down_arrow(self):
        self.click(top_frequency_down_arrow)

    @allure.step("verify half card page")
    def verify_half_card_page(self):
        top_frequency_page_header_text = self.get_attribute(top_frequency_page_header, "text")
        self.assert_equal(top_frequency_page_header_text, 'Urutkan')
        half_card_entry_text = self.get_attribute(half_card_entry, "text")
        self.assert_equal(half_card_entry_text, 'Top frequency')

    @allure.step("click on back btn")
    def go_back(self):
        self.back()
        self.sleep(1)

    @allure.step("click on see more btn")
    def click_on_see_more_btn(self):
        self.click(see_more_btn)

    @allure.step("verify mover page")
    def verify_mover_page(self):
        mover_page_header_text = self.get_attribute(mover_page_header, "text")
        self.assert_equal(mover_page_header_text, 'Mover')
        mover_page_down_text = self.get_attribute(mover_page_down, "text")
        self.assert_equal(mover_page_down_text, 'Top frequency')
        self.sleep(2)
        mover_page_entry_1_present = self.is_element_visible(mover_page_entry_1)
        assert mover_page_entry_1_present == True, f"mover page entry 1 Should be present"
        mover_page_entry_2_present = self.is_element_visible(mover_page_entry_2)
        assert mover_page_entry_2_present == True, f"mover page entry 2 Should be present"

    @allure.step("click on default btn")
    def click_on_default_btn(self):
        self.click(default_btn)

    @allure.step("verify watchlist card")
    def verify_watchlist_card(self):
        watchlist_header_text = self.get_attribute(watchlist_header, "text")
        self.assert_equal(watchlist_header_text, 'Watchlist')
        add_btn_watchlist_present = self.is_element_visible(add_btn_watchlist)
        assert add_btn_watchlist_present == True, f"add_btn_watchlist Should be present"
        watchlist_entry_present = self.is_element_visible(watchlist_entry)
        assert watchlist_entry_present == True, f"watchlist_entry Should be present"

    @allure.step("verify watchlist details")
    def verify_watchlist_details(self):
        watchlist_name_text = self.get_attribute(watchlist_name, "text")
        self.assert_equal(watchlist_name_text, 'Default')
        watchlist_right_btn_present = self.is_element_visible(watchlist_right_btn)
        assert watchlist_right_btn_present == True, f"watchlist_right_btn Should be present"
        watchlist_edit_btn_present = self.is_element_visible(watchlist_edit_btn)
        assert watchlist_edit_btn_present == True, f"watchlist_edit_btn Should be present"
        watchlist_delete_btn_present = self.is_element_visible(watchlist_delete_btn)
        assert watchlist_delete_btn_present == True, f"watchlist_delete_btn Should be present"

    @allure.step("verify portfolio on homepage")
    def verify_portfolio_on_homepage(self):
        portfolio_location = self.get_location_of_element(Portfolio_Saham)
        logger.info(portfolio_location)
        assert portfolio_location == (70, 908), f"Element is not present at given location (70, 908) actual location {portfolio_location} "
        today_location = self.get_location_of_element(today)
        assert today_location == (70, 1097), f"Element is not present at given location (70, 1097) actual location {today_location} "

    @allure.step("verify buying power location")
    def verify_buying_power_location(self):
        buying_power = self.get_location_of_element(Buying_Power)
        assert buying_power == (52, 891), f"Element is not present at given location (52,891)"

    @allure.step("click top up from homeopage")
    def click_top_up_from_homepage(self):
        self.click(Top_up)

    @allure.step("click stock 1 from top frequency list")
    def click_stock_1_from_top_frequency_list(self):
        self.click(top_frequency_stock_1)

    @allure.step("verify sdp page from top frequency list")
    def verify_sdp_page_from_top_freqency_list(self):
        stock_name_present = self.is_element_visible(stock_name)
        assert stock_name_present == True, f"stock_name Should be present"
        # stock_buy_bttton_text = self.get_attribute(stock_buy_bttton, "text")
        # self.assert_equal(stock_buy_bttton_text, "")
        # # self.is_element_visible(sdp_orderbook)
        # sdp_orderbook_text = self.get_attribute(sdp_orderbook, "text")
        # self.assert_equal(sdp_orderbook_text, "Order Book")
        # # self.is_element_visible(sdp_news)
        # sdp_news_text = self.get_attribute(sdp_news, "text")
        # self.assert_equal(sdp_news_text, "News")
        # # self.is_element_visible(sdp_keystate)
        # sdp_keystate_text = self.get_attribute(sdp_keystate, "text")
        # self.assert_equal(sdp_keystate_text, "Keystats")
        # # self.is_element_visible(sdp_profile)
        # sdp_profile_text = self.get_attribute(sdp_profile, "text")
        # self.assert_equal(sdp_profile_text, "Financials")
        # # self.is_element_visible(sdp_bid)
        # sdp_bit_text = self.get_attribute(sdp_bit, "text")
        # self.assert_equal(sdp_bit_text, "Bid")

    @allure.step("click on default watchlist entry 1")
    def click_on_default_watchlist_entry_1(self):
        self.click(default_watchlist_entry_1)
        self.sleep(3)

    @allure.step("click on research btn")
    def click_on_research_btn(self):
        self.click(Research_btn)
        self.sleep(4)

    @allure.step("verify research page")
    def verify_research_page(self):
        research_header_text = self.get_attribute(research_header, "text")
        self.assert_equal(research_header_text, "Research")
        last_report_present = self.is_element_visible(last_report)
        assert last_report_present == True, f"last_report Should be present"
        news_present = self.is_element_visible(news)
        assert news_present == True, f"news Should be present"
        media_present = self.is_element_visible(media)
        assert media_present == True, f"media Should be present"

    @allure.step("verify stock signal on research page")
    def verify_stock_signal_on_research_page(self):
        stock_signal_present = self.is_element_visible(stock_signal)
        assert stock_signal_present == True, f"stock_signal Should be present"
        stock_signal_entry_1_present = self.is_element_visible(stock_signal_entry_1)
        assert stock_signal_entry_1_present == True, f"stock_signal_entry_1 Should be present"
        stock_signal_entry_2_present = self.is_element_visible(stock_signal_entry_2)
        assert stock_signal_entry_2_present == True, f"stock_signal_entry_2 Should be present"
        stock_signal_down_present = self.is_element_visible(stock_signal_down)
        assert stock_signal_down_present == True, f"stock_signal_down Should be present"

    @allure.step("check phone home screen")
    def check_phone_home_screen(self):
       element_visible = self.is_element_visible(rdn_balance)
       assert element_visible == False, f"You are not on Home"

    @allure.step("click on portfolio btn")
    def click_on_portfolio_btn(self):
        self.click(portfolio_btn)
        self.sleep(1)

    @allure.step("verify portfolio for non kyc user")
    def verify_portfolio_for_non_kyc_user(self):
        #investasi_sekrang_presence = self.is_element_visible(investasi_sekrang)
        #assert investasi_sekrang_presence == True, f"Investasi is available on portfolio page"
        investasi_sekrang_text = self.get_attribute(investasi_sekrang, "text")
        self.assert_equal(investasi_sekrang_text, "INVESTASI SEKARANG")
        kamu_belum_text = self.get_attribute(kamu_belum, "text")
        self.assert_equal(kamu_belum_text, "Kamu belum memiliki investasi")

    @allure.step("verify portfolio for kyc user")
    def verify_portfolio_for_kyc_user(self):
        portofolio_saham_presence = self.is_element_visible(portofolio_saham)
        assert portofolio_saham_presence == True, f"Saham tab available"
        portfolio_entry_1_presence = self.is_element_visible(portfolio_entry_1)
        assert portfolio_entry_1_presence == True, f"portfolio_entry_1  available"
        portfolio_entry_2_presence = self.is_element_visible(portfolio_entry_2)
        assert portfolio_entry_2_presence == True, f"portfolio_entry_1  available"
        self.assert_equal(self.is_element_visible(reksadhana_tab), True)

    @allure.step("click on portfolio entry 2")
    def click_on_portfolio_entry_2(self):
        self.click(portfolio_entry_2)
        self.sleep(2)

    @allure.step("click on portfolio entry 1")
    def click_on_portfolio_entry_1(self):
        self.click(portfolio_entry_1)
        self.sleep(2)

    @allure.step("click on transaction btn")
    def click_on_transaction_btn(self):
        self.click(transition_btn)
        self.sleep(1)

    @allure.step("verify transaction page")
    def verify_transaction_page(self):
        self.sleep(3)
        self.assert_equal(self.is_element_visible(saham_trans), True)
        order_tab_presence = self.is_element_visible(order_tab)
        assert order_tab_presence == True, f"order_tab  available on transaction page"
        trade_list_tab_presence = self.is_element_visible(trade_list_tab)
        assert trade_list_tab_presence == True, f"trade_list_tab  available on transaction page"
        history_tab_presence = self.is_element_visible(history_tab)
        assert history_tab_presence == True, f"history_tab  available on transaction page"
        GTC_list_tab_presence = self.is_element_visible(GTC_list_tab)
        assert GTC_list_tab_presence == True, f"GTC_list_tab  available on transaction page"
        all_types_presence = self.is_element_visible(all_types)
        assert all_types_presence == True, f"all_types  available on transaction page"
        cari_saham_presence = self.is_element_visible(cari_saham)
        assert cari_saham_presence == True, f"cari_saham  available on transaction page"
        #trans_details_header_presence = self.is_element_visible(trans_details_header)
        #assert trans_details_header_presence == True, f"trans_details_header  available on transaction page"
        trans_entry_1_presence = self.is_element_visible(trans_entry_1)
        assert trans_entry_1_presence == True, f"trans_entry_1  available on transaction page"

    @allure.step("verify profile page")
    def verify_profile_page(self):
        entry_for_account_presence = self.is_element_visible(entry_for_account)
        assert entry_for_account_presence == True, f"entry_for_account  available on profile page"
        account_text_text = self.get_attribute(account_text, "text")
        self.assert_equal(account_text_text, "Test Wippy")

    @allure.step("verify username on homepage")
    def verify_username_on_homepage(self):
        username_on_homepage_text = self.get_attribute(username_on_homepage, "text")
        self.assert_equal(username_on_homepage_text, "Hi, Testing")

    @allure.step("login and verify homepage for rg user")
    def login_and_verify_homepage_for_reg_user(self, phone_number):
        self.sleep(4)
        self.click_mulai_sekarang()
        self.type_mobile_no(phone_number)
        self.click_selanjutnya()
        self.enter_otp('1234')
        self.enter_pin()
        #self.close_home_page_banner()
        #self.verify_home_page_reg_user()

    @allure.step("verify home page reg user after back from watchlist new")
    def verify_home_page_reg_user_after_back_from_watchlist_new(self):
        default_btn_presence = self.is_element_visible(default_btn)
        assert default_btn_presence == True, f"default_btn available on Home page"

    @allure.step("Verify Edit Btn")
    def verify_edit_btn(self):
        self.click(edit_btn)
        self.sleep(2)
        self.assert_equal(self.is_element_visible(stock_add_page_Header), True)

    @allure.step("Verify Star point btn")
    def verify_star_point_btn(self):
        self.click(StarPoint)
        self.sleep(2)
        self.assert_equal(self.is_element_visible(mulai_btn), True)

    @allure.step('Verify Reksadana page')
    def verify_Reksadana_page(self):
        self.click(Reksadana)
        self.sleep(1)
        self.assert_equal(self.is_element_visible(reksadhana_home), True)
        self.click(Saham)
        self.sleep(2)

    @allure.step("Verify data with api")
    def verify_data_with_api(self):
        saldo_rdn_with_rp = self.get_attribute(home_rdn_value, 'text')
        saldo_rdn_value = saldo_rdn_with_rp[3:]
        star_point_value = self.get_attribute(homepage_starpoint_value, 'text')
        homepage_rp_with_rp = self.get_attribute(homepage_rp, 'text')
        homepage_rp_value = homepage_rp_with_rp[3:]
        buying_power_with_buy = self.get_attribute(Buying_Power, 'text')
        buying_power = (buying_power_with_buy[16:]).replace(',', '')
        IHSG_value = (self.get_attribute(homepage_stock_value, 'text')).replace(',', '')
        token_value = self.login()
        token = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJpWlYzdUJkTkJyTDA4dVIzQUR2bmg4akdTdHNkSHpQVSIsInN1YiI6IlNpbWFzSW52ZXN0In0.Kj31bgBrbc94NaUDKWgbx-N4ZBQNFsrZBmF7xtZ4hNo"}
        token['Authorization'] = 'Bearer ' + token_value
        saldo_api = request_utilities.get(base_url='https://stg-api.siminvest.co.id/',endpoint='api/v1/users/rdn', headers=token,expected_status_code=200)
        star_point = request_utilities.get(base_url='https://stg-api.siminvest.co.id/',endpoint='radix/v1/account/45997/balance/1', headers=token,expected_status_code=200)
        buying_power_rs = request_utilities.get(base_url='https://stg-api.siminvest.co.id/',endpoint='api/v1/users/portfolios/equities/45997', headers=token,expected_status_code=202)
        ihsg_value_api= request_utilities.get(base_url='https://stg-api.siminvest.co.id/',endpoint='emerson/v1/index', headers=token,expected_status_code=200)
        self.assert_equal(saldo_api['data']['balance'],int(saldo_rdn_value.replace(',', '')))
        self.assert_equal(star_point['data']['value'], int(star_point_value))
        self.assert_equal(buying_power_rs['data']['buying_power'], int(buying_power))
        self.assert_equal(buying_power_rs['data']['market_value'], int(homepage_rp_value.replace(',', '')))
        list_of_index = ihsg_value_api['data']
        for i in range(len(list_of_index)):
            if list_of_index[i]['name'] == 'COMPOSITE':
                IHSG_value_api = list_of_index[i]['lp']
                break
        formated_value = "{:.2f}".format(IHSG_value_api)
        self.assert_equal(str(formated_value), IHSG_value)

    @allure.step("Validate default btn available after scroll up")
    def validate_default_btn_available_after_scroll_up(self):
        self.assert_equal(self.is_element_visible(default_watchlist_btn), True)


    @allure.step("Verify username on homepage after close")
    def verify_username_on_homepage_after_close(self):
        self.assert_equal(self.is_element_visible(saldo_rdn_btn), False)


    @allure.step("Login with an user ")
    def login(self):
        base_url = 'https://stg-api.siminvest.co.id/'
        endpoint = 'api/v1/users/signin/phone'
        data = {"phone_number": "628445557108","pin": "123456","device_id": "3F4330E5-4F07-4A26-A710-A6552D583FE8"}
        payload = json.dumps(data)
        rs_api = request_utilities.post(base_url=base_url,endpoint=endpoint, payload=payload,expected_status_code=201)
        logger.info(f"Given Endpoint : {endpoint} _______payload : {payload}___________ Response Body = {rs_api}")
        return rs_api['data']['access_token']
    
    @allure.step("Login with an starpoin user ")
    def loginstarpoin(self):
        base_url = 'https://stg-api.siminvest.co.id/'
        endpoint = 'api/v1/users/signin/phone'
        data = {"phone_number": "628445557119","pin": "123456","device_id": "3F4330E5-4F07-4A26-A710-A6552D583FE8"}
        payload = json.dumps(data)
        rs_api = request_utilities.post(base_url=base_url,endpoint=endpoint, payload=payload,expected_status_code=201)
        logger.info(f"Given Endpoint : {endpoint} _______payload : {payload}___________ Response Body = {rs_api}")
        return rs_api['data']['access_token']


    @allure.step("Login with an user ")
    def login_with_a_number(self, number):
        base_url = 'https://stg-api.siminvest.co.id/'
        endpoint = 'api/v1/users/signin/phone'
        data = {"phone_number": f"62{number}","pin": "123456","device_id": "3F4330E5-4F07-4A26-A710-A6552D583FE8"}
        payload = json.dumps(data)
        rs_api = request_utilities.post(base_url=base_url,endpoint=endpoint, payload=payload,expected_status_code=201)
        logger.info(f"Given Endpoint : {endpoint} _______payload : {payload}___________ Response Body = {rs_api}")
        return rs_api['data']['access_token']


# Helper methods for mover page
    @allure.step("Swipe right to left")
    def swipe_right_to_left(self):
        self.sleep(2)
        self.scroll_screen(start_x=767, start_y=1021, end_x=310, end_y=1081, duration=10000)
        self.sleep(2)

    @allure.step("Swipe left to right")
    def swipe_left_to_right(self):
        self.sleep(2)
        self.scroll_screen(start_x=310, start_y=1081, end_x=767, end_y=1021, duration=10000)
        self.sleep(2)

    @allure.step("Validate stock list on homepage")
    def validate_all_details_about_stock_list_on_homepage(self):

        for i in range(3):
            """if i == 4:
                self.swipe_right_to_left()
                self.assert_equal(self.is_element_visible(f'HomepageTFStock{i}'), True)
                self.assert_equal(self.is_element_visible(f'//android.view.ViewGroup[@content-desc="HomepageTFStock{i}"]/android.view.ViewGroup/android.widget.TextView[1]'), True)
                self.assert_equal(self.is_element_visible(f'//android.view.ViewGroup[@content-desc="HomepageTFStock{i}"]/android.view.ViewGroup/android.widget.TextView[2]'), True)
                self.assert_equal(self.is_element_visible(f'//android.view.ViewGroup[@content-desc="HomepageTFStock{i}"]/android.view.ViewGroup/android.widget.TextView[3]'), True)
               """# self.assert_equal(self.is_element_visible(f'//android.view.ViewGroup[@content-desc="HomepageTFStock{i}"]/android.view.ViewGroup/android.widget.ImageView'), True)

            self.assert_equal(self.is_element_visible(f'HomepageTFStock{i}'), True)
            self.assert_equal(self.is_element_visible(f'//android.view.ViewGroup[@content-desc="HomepageTFStock{i}"]/android.view.ViewGroup/android.widget.TextView[1]'), True)
            self.assert_equal(self.is_element_visible(f'//android.view.ViewGroup[@content-desc="HomepageTFStock{i}"]/android.view.ViewGroup/android.widget.TextView[2]'), True)
            self.assert_equal(self.is_element_visible(f'//android.view.ViewGroup[@content-desc="HomepageTFStock{i}"]/android.view.ViewGroup/android.widget.TextView[3]'), True)
           # self.assert_equal(self.is_element_visible(f'//android.view.ViewGroup[@content-desc="HomepageTFStock{i}"]/android.view.ViewGroup/android.widget.ImageView'),True)
        #self.swipe_left_to_right()
        self.assert_equal(self.is_element_visible(f'HomepageTFStock0'), True)

    @allure.step("Verify all value on half card and tick")
    def verify_all_value_on_half_card_and_tick_for_kyc_user(self, number):
        for i in range(len(mover_type_list)):
            self.assert_equal(self.is_element_visible(mover_type_list[i]), True)
        self.assert_equal(self.is_element_visible(marker), True)
        self.click(top_gainer)
        self.sleep(2)
        self.assert_equal(self.is_element_visible(top_gainer_on_homepage), True)
        self.launch_app_again()
        self.login_and_verify_homepage_for_reg_user(number)
        self.scroll_up()
        self.assert_equal(self.is_element_visible(top_gainer_on_homepage), False)
        self.verify_top_frequency_presention()
        self.click_on_TF_down_arrow()
        self.go_back()
        self.verify_top_frequency_presention()

    @allure.step("Verify all value on half card and tick")
    def verify_all_value_on_half_card_and_tick_for_non_kyc_user(self, number):
        for i in range(len(mover_type_list)):
            self.assert_equal(self.is_element_visible(mover_type_list[i]), True)
        self.assert_equal(self.is_element_visible(marker), True)
        self.click(top_gainer)
        self.sleep(2)
        self.assert_equal(self.is_element_visible(top_gainer_on_homepage), True)
        self.launch_app_again()
        self.login_and_verify_homepage_for_non_kyc_user(number)
        self.scroll_up()
        self.assert_equal(self.is_element_visible(top_gainer_on_homepage), False)
        self.verify_top_frequency_presention()
        self.click_on_TF_down_arrow()
        self.go_back()
        self.verify_top_frequency_presention()

    @allure.step("login and verify homepage for rg user")
    def login_and_verify_homepage_for_non_kyc_user(self, phone_number):
        self.sleep(4)
        self.click_mulai_sekarang()
        self.type_mobile_no(phone_number)
        self.click_selanjutnya()
        self.enter_otp('1234')
        self.enter_pin()
        #self.close_home_page_banner()
        self.verify_home_page()

    @allure.step("Compare the stock details with mover page")
    def compare_the_stock_details_with_mover_page(self):
        stock_name_lst = []
        mover_page_stock_name = []
        for i in range(3):
            stock_name = self.get_attribute(f'//android.view.ViewGroup[@content-desc="HomepageTFStock{i}"]/android.view.ViewGroup/android.widget.TextView[1]', 'text')
            stock_name_lst.append(stock_name)
        self.click(see_more_btn)
        self.verify_mover_page()
        for i in range(3):
            stock_name = self.get_attribute(f'MoverPageEntry{i}Code', 'text')
            mover_page_stock_name.append(stock_name)
        self.assert_equal(mover_page_stock_name,mover_page_stock_name)

    @allure.step("Scroll up and scroll down validation")
    def scroll_up_and_scroll_down_validation(self):
        self.scroll_up()
        self.scroll_down()
        self.assert_equal(self.is_element_visible(mover_page_entry_1), True)

    @allure.step("stock value not change according to mover change")
    def stock_value_not_change_according_to_mover_change(self):
        top_frequency_code = self.get_attribute(mover_stock_code, 'text')
        self.click(top_frequency_down_arrow)
        self.click(top_gainer)
        self.sleep(3)
        top_gainer_stock = self.get_attribute(mover_stock_code_1, 'text')
        self.assert_not_equal(top_frequency_code, top_gainer_stock)
        self.go_back()
        self.verify_top_frequency_presention()
        stock_code_home_page = self.get_attribute(f'//android.view.ViewGroup[@content-desc="HomepageTFStock0"]/android.view.ViewGroup/android.widget.TextView[1]','text')
        self.assert_equal(top_frequency_code, stock_code_home_page)

    @allure.step("Validate Urutkan half card")
    def validate_urutkan_half_card(self):
        self.click(see_more_btn)
        self.click(top_frequency_down_arrow)
        for i in range(len(mover_type_list)):
            self.assert_equal(self.is_element_visible(mover_type_list[i]), True)
        self.assert_equal(self.is_element_visible(marker), True)
        self.go_back()
        self.verify_mover_page()

    @allure.step("Collect all value from mover page")
    def collect_all_value_from_mover_page(self):
        stock_code = []
        stock_name = []
        stock_last_price = []
        for i in range(10):
            if i == 10:
                stock_codes = self.get_attribute(f'MoverPageEntry{i}Code', 'text')
                self.assert_equal(self.is_element_visible(f'MoverPageEntry{i}Code'), True)
                stock_code.append(stock_codes)
                stock_names = self.get_attribute(f'MoverPageEntry{i}Name', 'text')
                self.assert_equal(self.is_element_visible(f'MoverPageEntry{i}Name'), True)
                stock_name.append(stock_names)
                stock_lastprices = self.get_attribute(f'MoverPageEntry{i}LastPrice', 'text')
                self.assert_equal(self.is_element_visible(f'MoverPageEntry{i}LastPrice'), True)
                stock_last_price.append(stock_lastprices)
                self.scroll_up()
                self.scroll_up()
                self.sleep(5)
            #logger.info(f'MoverPageEntry{i}Code')
            self.sleep(1)
            stock_codes = self.get_attribute(f'MoverPageEntry{i}Code', 'text')
            self.assert_equal(self.is_element_visible(f'MoverPageEntry{i}Code'), True)
            stock_code.append(stock_codes)
            stock_names = self.get_attribute(f'MoverPageEntry{i}Name', 'text')
            self.assert_equal(self.is_element_visible(f'MoverPageEntry{i}Name'), True)
            stock_name.append(stock_names)
            stock_lastprices = self.get_attribute(f'MoverPageEntry{i}LastPrice', 'text')
            self.assert_equal(self.is_element_visible(f'MoverPageEntry{i}LastPrice'), True)
            stock_last_price.append(stock_lastprices)
            #self.scroll_down()
            #logger.info(stock_code)
            #logger.info(stock_name)
            #logger.info(stock_last_price)
        return stock_code, stock_name, stock_last_price

    @allure.step("Click to mover dropDown")
    def click_mover_dropDown_btn(self):
        self.click(mover_page_down)
        self.sleep(2)

    @allure.step("Verfiy Stock on mover page with api")
    def verify_stock_on_mover_page_with_api_for_top_frequency(self):
        top_frequency = []
        top_top_gainer=[]
        top_gainer_percent =[]
        top_gainer_value=[]
        top_gainer_volume = []
        top_loser_price = []
        top_loser_percent=[]
        getAccelerationBoardList=[]
        token_value = self.login()
        token = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJpWlYzdUJkTkJyTDA4dVIzQUR2bmg4akdTdHNkSHpQVSIsInN1YiI6IlNpbWFzSW52ZXN0In0.Kj31bgBrbc94NaUDKWgbx-N4ZBQNFsrZBmF7xtZ4hNo"}
        token['Authorization'] = 'Bearer ' + token_value
        top_frequency_rs = request_utilities.get(base_url='https://stg-api.siminvest.co.id/api/mds/v1/stock/category', endpoint='/top-gainer-frequency',headers=token, expected_status_code=200)
        top_top_gainer_rs = request_utilities.get(base_url='https://stg-api.siminvest.co.id/api/mds/v1/stock/category', endpoint='/top-gainer-price',headers=token, expected_status_code=200)
        top_gainer_percent_rs = request_utilities.get(base_url='https://stg-api.siminvest.co.id/api/mds/v1/stock/category', endpoint='/top-gainer-percent',headers=token, expected_status_code=200)
        top_gainer_value_rs = request_utilities.get(base_url='https://stg-api.siminvest.co.id/api/mds/v1/stock/category', endpoint='/top-gainer-value',headers=token, expected_status_code=200)
        top_gainer_volume_rs = request_utilities.get(base_url='https://stg-api.siminvest.co.id/api/mds/v1/stock/category', endpoint='/top-gainer-volume',headers=token, expected_status_code=200)
        top_loser_price_rs = request_utilities.get(base_url='https://stg-api.siminvest.co.id/api/mds/v1/stock/category', endpoint='/top-loser-price',headers=token, expected_status_code=200)
        top_loser_percent_rs = request_utilities.get(base_url='https://stg-api.siminvest.co.id/api/mds/v1/stock/category', endpoint='/top-loser-percent',headers=token, expected_status_code=200)
        getAccelerationBoardList_rs = request_utilities.get(base_url='https://stg-api.siminvest.co.id', endpoint='/emerson/v1/stock?board_id=3&sort_by=code&is_asc=true&limit=50',headers=token, expected_status_code=200)
        #logger.info(type(top_frequency_rs))
        #logger.info(top_frequency_rs[0])
        for i in range(10):
            top_frequency.append(top_frequency_rs[i]['code'])
            top_top_gainer.append(top_top_gainer_rs[i]['code'])
            top_gainer_percent.append(top_gainer_percent_rs[i]['code'])
            top_gainer_value.append(top_gainer_value_rs[i]['code'])
            top_gainer_volume.append(top_gainer_volume_rs[i]['code'])
            top_loser_price.append(top_loser_price_rs[i]['code'])
            top_loser_percent.append(top_loser_percent_rs[i]['code'])
            getAccelerationBoardList.append(getAccelerationBoardList_rs['data'][i]['code'])
        return top_frequency,top_gainer_percent, top_gainer_value, top_gainer_volume, top_loser_price, top_loser_percent, top_top_gainer,getAccelerationBoardList

    @allure.step("Click on search Btn")
    def click_on_mover_search_btn(self):
        self.click(search_btn_mover)

    @allure.step("Click on stock in mover")
    def click_on_stock_in_mver(self):
        self.click(mover_page_entry_1)
        self.sleep(3)

    @allure.step("verify stock page after back")
    def verify_sdp_page_after_back(self):
        self.assert_equal(self.is_element_visible(stock_name), True)
        self.sleep(1)

    @allure.step("scroll for with two component")
    def scroll_with_two_element(self, first, second):
        self.sleep(1)
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
        self.scroll_screen(start_x=sec_x, start_y=sec_y, end_x=fist_x, end_y=fist_y, duration=9000)
        self.sleep(1)

    @allure.step("verify sheild tracker when click tidak and setuju")
    def verify_sheild_tracker_tidak(self):
        self.sleep(1)
        self.click(Tidak_Setuju)
        Sheildtracker_header = self.get_attribute(Syarat_dan_ketentuan, "text")
        self.assert_equal(Sheildtracker_header, "Syarat dan ketentuan")
        self.sleep(2)
    @allure.step("scroll on sheild tracker")
    def scroll_up_on_sheild(self):
        self.scroll_screen(start_x=544, start_y=1616, end_x=533, end_y=667, duration=10000)
        self.sleep(2)
    @allure.step("scroll on sheild tracker")
    def scroll_down_on_sheild(self):
        self.scroll_screen(start_x=540, start_y=689, end_x=540, end_y=1639, duration=10000)
        self.sleep(2)
    @allure.step("verify sheild tracker when click setuju")
    def verify_sheild_tracker_setuju(self):
        self.sleep(1)
        self.click(Saya_Setuju)
        self.sleep(2)

    @allure.step("verify eye button is default close mode and visible when click")
    def verify_eye_defaultmode(self):
        self.sleep(1)
        self.assert_equal(self.is_element_visible(home_rdn_value), True)
        self.assert_equal(self.is_element_visible(homepage_starpoint_value), True)
        self.assert_equal(self.is_element_visible(today), True)
        self.assert_equal(self.is_element_visible(homepage_rp), True)
        self.assert_equal(self.is_element_visible(Buying_Power), True)
        eye_home_rdn_value = self.get_attribute(home_rdn_value, "text")
        self.assert_equal(eye_home_rdn_value, "******")
        eye_homepage_starpoint_value = self.get_attribute(homepage_starpoint_value, "text")
        self.assert_equal(eye_homepage_starpoint_value, "******")
        eye_homepage_rp = self.get_attribute(homepage_rp, "text")
        self.assert_equal(eye_homepage_rp, "******")
        eye_today = self.get_attribute(today, "text")
        self.assert_equal(eye_today, "****** (**%) Today")
        eye_Buying_Power = self.get_attribute(Buying_Power, "text")
        self.assert_equal(eye_Buying_Power, "Buying power ******")
        self.sleep(2)
        self.click(btn_reksadana)
        self.assert_equal(self.is_element_visible(reksadana_header), True)
        self.assert_equal(self.is_element_visible(reksadana_today), True)
        self.assert_equal(self.is_element_visible(reksadana_value), True)
        eye_reksadana_today = self.get_attribute(reksadana_today, "text")
        self.assert_equal(eye_reksadana_today, "******(**%) Today")
        eye_reksadana_value = self.get_attribute(reksadana_value, "text")
        self.assert_equal(eye_reksadana_value, "******")
        self.sleep(2)
        self.click(tampilkan)
        self.sleep(2)
        self.assert_equal(self.is_element_visible(home_rdn_value), True)
        home_rdn_rp = self.get_attribute(home_rdn_value, 'text')
        home_rdn_rp_value = home_rdn_rp[3:]
        self.assert_in(',', home_rdn_rp_value)
        self.sleep(1)
    
    @allure.step("kill apss")
    def Validate_kill_app(self):
      self.launch_app_again()
      self.login_and_verify_homepage_for_reg_user(user_data['reg_no_6'])











