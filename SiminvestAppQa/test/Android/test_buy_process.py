import pytest
from SiminvestAppQa.src.pages.Android_pages.login_page import LoginPage
from SiminvestAppQa.src.pages.Android_pages.home_page import HomePage
from SiminvestAppQa.src.utilities.genericUtilities import generate_random_integer
from SiminvestAppQa.src.pages.Android_pages.buy_process import BuyProcess
from SiminvestAppQa.src.data.userData import user_data

class BuyProcess_test(BuyProcess):

    #Validate that user can see buy button on stock detail page
    @pytest.mark.BP_SMMA_301
    @pytest.mark.Homepage
    @pytest.mark.Android
    def test_validate_buy_btn_on_sdp_page(self):
        self.open_sdp_page_with_user(user_data['reg_no'], 'ACES')