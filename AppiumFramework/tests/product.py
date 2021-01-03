import unittest
import pytest
import AppiumFramework.Utilities.Custom_logger as cl
from AppiumFramework.Base.BasePage import BasePage
from AppiumFramework.Pages.Itemspage import products
import time


class product_page(unittest.TestCase):
    @pytest.mark.usefixtures("beforeClass", "beforeMethod")
    def classObject(self):
        self.item = products(self.driver)
        self.bp = BasePage(self.driver)
        self.log = cl.customLogger()

    def test_product_to_cart(self):
        self.log.info("This is produt to car method")
        cl.allureLogs("Adding item")
        self.item.Add_item()
        self.item.cart()
