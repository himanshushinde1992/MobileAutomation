import unittest
import pytest

from AppiumFramework.Base.BasePage import BasePage
from AppiumFramework.Base.Driver import Driver
import AppiumFramework.Utilities.Custom_logger as cl
from AppiumFramework.Pages.SelectionPage import SelectionPage
import time


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class selection_form_Test(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.sel = SelectionPage(self.driver)

    def test_selection_method(self):
        log = cl.customLogger()

        log.info("Launch app")

        self.sel.screenshot("app")
        self.sel.country_selection()
        time.sleep(30)
        self.sel.enter_name()
        self.sel.gender_select()
        self.click_let_shop()
        self.sel.screenshot("cart page")
