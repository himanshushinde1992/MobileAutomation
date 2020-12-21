from AppiumFramework.Base.BasePage import BasePage
import AppiumFramework.Utilities.Custom_logger as cl


class SelectionPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locator values in selectionPage
    country_selection_dropdown = "com.androidsample.generalstore:id/spinnerCountry"  # id
    text = "India"
    index = "3"
    enter_name_field = "com.androidsample.generalstore:id/nameField"
    gender_selection = "com.androidsample.generalstore:id/radioFemale"
    let_shop_button = "com.androidsample.generalstore:id/btnLetsShop"

    def country_selection(self):
        self.click_Element(self.country_selection_dropdown, "id")
        self.scroll_in_view(self.text, "text")

        self.click_Element(self.text, "text")

    def enter_name(self):
        self.enterText("himanshu shinde", self.enter_name_field, "id")

    def gender_select(self):
        self.click_Element(self.gender_selection, "id")

    def click_let_shop(self):
        self.click_Element(self.let_shop_button, "id")
