from AppiumFramework.Base.BasePage import BasePage
import time
from AppiumFramework.Pages.MenuPage import menu


class Login(BasePage):
    """constructors of the class"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """ locators of the page"""
    Email = "com.assetpanda:id/LoginEmailAdressET"
    Password = "com.assetpanda:id/LoginPasswordET"
    Login = "com.assetpanda:id/LoginBtn"
    text = "ACCOUNT"
    Logout = "LOGOUT"

    """"page Actions"""

    """ this method will be used to enter the username and password"""

    def account_details(self):
        self.enterText("ui-test@assetpanda.com", self.Email, "id")
        self.enterText("panda123", self.Password, "id")
        self.hide_keyboard()

    """ this method will be used to click on login button"""

    def click_login_button(self):
        self.click_Element(self.Login, "id")
        self.log.info("login Successful")

    def click_group(self):
        self.click_Element(self.index, "index")

    def do_login(self):
        self.account_details()
        self.click_login_button()
        time.sleep(25)
        menu_page = menu(self.driver)
        return menu_page
