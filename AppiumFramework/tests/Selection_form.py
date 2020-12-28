import unittest
import pytest

from AppiumFramework.Base.BasePage import BasePage
from AppiumFramework.Base.Driver import Driver
import AppiumFramework.Utilities.Custom_logger as cl
from AppiumFramework.Pages.SelectionPage import SelectionPage
import time


@pytest.yield_fixture("beforeClass", "beforeMethod")
class selection_form(unittest.TestCase):
    def selection_method(self):
        log = cl.customLogger()

        pageBase = BasePage(driver)
        log.info("Launch app")

        sel = SelectionPage(driver)
        pageBase.screenshot("app")
        sel.country_selection()
        time.sleep(30)
        sel.enter_name()
        sel.gender_select()
        sel.click_let_shop()
        pageBase.screenshot("cart page")
