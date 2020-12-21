from AppiumFramework.Base.BasePage import BasePage
from AppiumFramework.Base.Driver import Driver
import AppiumFramework.Utilities.Custom_logger as cl
from AppiumFramework.Pages.SelectionPage import SelectionPage
import time
driver1 = Driver()
log =cl.customLogger()

driver = driver1.getDriver()
pageBase = BasePage(driver)
log.info("Launch app")

sel = SelectionPage(driver)
pageBase.screenshot("app")
sel.country_selection()

time.sleep(40)
sel.enter_name()
sel.gender_select()
sel.click_let_shop()

