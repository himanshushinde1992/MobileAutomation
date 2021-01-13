from AppiumFramework.Base.BasePage import BasePage
import AppiumFramework.Utilities.Custom_logger as cl


class products(BasePage):
    def __init__(self, driver):
        super.__init__(driver)
        self.driver = driver

    log = cl.customLogger()

    # locator values in product page
    add_to_cart_text = "com.androidsample.generalstore:id/productAddCart"
    add_to_cart_icon = "com.androidsample.generalstore:id/appbar_btn_cart"
    page_title = "Products"

    def verify_page_title(self):
        Title = self.is_displayed(self.page_title, "text")
        print(Title)
        assert Title == True

    def Add_item(self):
        self.click_Element(self.add_to_cart_text, "id")
        self.log.info("user clicked on the item")

    def cart(self):
        self.click_Element(self.add_to_cart_icon, "id")
        self.log.info("cart icon clicked")
