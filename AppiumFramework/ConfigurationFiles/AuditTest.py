import unittest
import pytest
import AppiumFramework.Utilities.Custom_logger as cl
from AppiumFramework.Base.BasePage import BasePage
from AppiumFramework.Pages.Itemspage import products
from AppiumFramework.Utilities.Custom_logger import customLogger
import time

from AppiumFramework.Pages.loginpage import Login



@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class test_audit(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classObject(self):
        self.login = Login(self.driver)
        self.ad = audit(self.driver)
        self.log = customLogger()

    def test_audit(self):

        self.log.info("Audit intiated")
        self.ad.click_on_group()
        self.ad.audit_button_click()
        self.ad.create_audit_click()


