from AppiumFramework.Base.BasePage import BasePage
from AppiumFramework.Pages.loginpage import Login


class Logout(BasePage):
    """constructors of the class"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """ locators"""
    text = "ACCOUNT"
    Logout = "LOGOUT"
    ok_text = "android:id/button2"
    cancel_text = "android:id/button1"




    """actions on the page"""
    def click_logout(self):
        self.scroll_in_view(self.text, "text")
        self.click_Element(self.text, "text")
        self.click_Element(self.Logout, "text")

    def confirmation_popup_ok(self):
        self.click_Element(self.ok_text,"id")
        self.log.info("sucesfully clicked on the OK button")

    def confirmation_popup_cancel(self):
        self.click_Element(self.cancel_text,"id")
        self.log.info("sucesfully clicked on the cancel button")


