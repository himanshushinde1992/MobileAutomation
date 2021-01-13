import unittest
import pytest
import AppiumFramework.Utilities.Custom_logger as cl
from AppiumFramework.Base.BasePage import BasePage
from AppiumFramework.Pages.Itemspage import products
from AppiumFramework.ConfigurationFiles import conftest
import time


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class product_page_Test(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classObject(self):
        self.bp = BasePage(self.driver)
        self.item = products(self.driver)

    def test_product_to_cart(self):
        self.log = cl.customLogger()

        self.log.info("This is produt to car method")
        cl.allureLogs("Adding item")
        self.item.Add_item()
        self.item.cart()
