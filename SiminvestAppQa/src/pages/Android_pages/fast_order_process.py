from selenium.common.exceptions import InvalidElementStateException
from datetime import datetime
from SiminvestAppQa.src.data.userData import user_data
from SiminvestAppQa.src.pages.Android_pages.buy_process import BuyProcess
from SiminvestAppQa.src.pages.Android_pages.home_page import HomePage
import time
import allure
from datetime import timedelta
from datetime import date
import logging as logger
from  numerize import numerize


class FastOrder(BuyProcess):

    @allure.step("Verify last transaction in orderlist")
    def verify_last_transaction_orderlist(self):
        pass
