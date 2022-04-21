import pytest
from SiminvestAppQa.src.pages.Android_pages.stock_detail_page import StockDetailPage
from SiminvestAppQa.src.pages.Android_pages.buy_process import BuyProcess
from SiminvestAppQa.src.data.userData import user_data


@pytest.mark.usefixtures("unittest_setUpClass_fixture_SDP_test")
class SDP_test(StockDetailPage, BuyProcess):

    # Validate user is able to star mark the stock/ Validate user is able to un-mark the star.
    @pytest.mark.SDP_SMMA_001_002
    @pytest.mark.Android
    @pytest.mark.SDP
    def test_validate_star_mark_on_sdp(self):
        self.open_sdp_page_with_kyc_user(user_data['reg_no'], 'ACES')
        self.scroll_down()
        self.tap_on_star()
        self.click_on_watchlist()
        self.sleep(2)
        self.go_back()
        self.go_back()
        self.sleep(2)
        self.scroll_up()
        self.verify_stock_on_watchlist(True)
        self.click_on_stock()
        self.tap_on_star()
        self.click_on_watchlist()
        self.go_back()
        self.scroll_ups()
        self.verify_stock_on_watchlist(False)

    # Validate search option on sdp page
    @pytest.mark.SDP_SMMA_003_004
    @pytest.mark.Android
    @pytest.mark.SDP
    def test_validate_star_mark_on_sdp(self):
        self.open_sdp_page_with_kyc_user(user_data['reg_no'], 'ACES')
        self.click_on_search_btn()
        self.enter_stock_code('ACES')
        self.click_on_stocks()
        self.verify_sdp_page()
        self.go_back()
        self.go_back()
        self.verify_home_page_reg_user()


