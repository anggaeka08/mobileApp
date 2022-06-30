import pytest
from SiminvestAppQa.src.data.userData import user_data
from SiminvestAppQa.src.pages.Android_pages.transaction import Transaction


@pytest.mark.usefixtures("unittest_setUpClass_fixture_Portfolio_test")
class Portfolio_test(Transaction):

    # Cover all 5 test cases in single test
    @pytest.mark.T_SMMA_001_to_005
    @pytest.mark.Android
    @pytest.mark.transaction
    def test_validate_transaction_btn_redirection_saham_reksadana_tab(self):
        self.open_trans_page_with_reg_user(user_data['reg_no'])
        self.verify_last_transaction_orderlist()
