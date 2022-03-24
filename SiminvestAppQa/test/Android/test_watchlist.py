import pytest
from SiminvestAppQa.src.pages.Android_pages.watchlist import Watchlist
from SiminvestAppQa.src.data.userData import user_data

@pytest.mark.usefixtures("unittest_setUpClass_fixture_Watchlist_test")
class Watchlist_test(Watchlist):

    #Validate user will able to create watchlist.
    @pytest.mark.Wat_SMMA_001
    @pytest.mark.Android
    @pytest.mark.watchlist
    def test_validate_user_able_create_watchlist(self):
        self.go_to_watchlist_option_after_login(user_data['reg_no'])
        self.click_on_defaults_btn()
        self.click_on_plus_btn()
        self.enter_watchlist_name('test')
        self.validate_watchlist_entry('test')


    #Validate user will able to edit watchlist name.
    @pytest.mark.Wat_SMMA_002
    @pytest.mark.Android
    @pytest.mark.watchlist
    def test_validate_user_able_edit_watchlist_name(self):
        self.go_to_watchlist_option_after_login(user_data['reg_no'])
        self.click_on_defaults_btn()
        self.click_on_edit_btn()
        self.edit_watchlist_name()
        self.click_on_simpan()
        self.validate_watchlist_entry('testtest')



