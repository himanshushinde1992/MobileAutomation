from AppiumFramework.Base.BasePage import BasePage


class menu(BasePage):
    """constructors of the class"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """ locators"""
    audit_button = "com.assetpanda:id/add_audit"
    create_audit = "com.assetpanda:id/createAudit"
    Text = "NOTIFICATIONS"
    fab_icon = "com.assetpanda:id/fab_add_img"
    index = "2"

    def click_notification(self):
        self.scroll_in_view(self.Text, "text")
        self.click_Element()



