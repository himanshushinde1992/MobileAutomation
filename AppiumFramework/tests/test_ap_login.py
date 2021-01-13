import unittest

import pytest

from AppiumFramework.Pages.MenuPage import menu
from AppiumFramework.Pages.loginpage import Login


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class test_user_login(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classObject(self):
        self.log = Login(self.driver)

    @pytest.mark.run(order=1)
    def test_login(self):
        menu_page = self.log.do_login()
        menu_page.click_notification()

