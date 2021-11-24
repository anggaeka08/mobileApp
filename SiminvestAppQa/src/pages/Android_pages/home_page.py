from appiumbase import BaseCase

# Locators
top_up = "Top Up"


class HomePage(BaseCase):

    def verify_top_up(self):
        self.assert_element_present(top_up)