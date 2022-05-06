import pytest
from SiminvestAppQa.src.pages.Android_pages.portfolio_page import Portfolio
from SiminvestAppQa.src.utilities.genericUtilities import generate_random_string
from SiminvestAppQa.src.data.userData import user_data
import logging as logger

@pytest.mark.usefixtures("unittest_setUpClass_fixture_Portfolio_test")
class Portfolio_test(Portfolio):

    # Cover all 5 test cases in single test
    @pytest.mark.Port_SMMA_001_to_005
    @pytest.mark.Android
    @pytest.mark.portfolio
    def test_validate_portfolio_btn_position_clickable_redirection_rakshdana_saham_btn_clickable(self):
        self.login_and_verify_homepage_for_reg_user(user_data['reg_no'])
        self.verify_portfolio_on_homepage()
        self.click_on_portfolio_btn()
        self.verify_portfolio_for_kyc_user()
        self.verify_saham_tab_clickable()
        self.verify_reksadhana_tab_clickable()

