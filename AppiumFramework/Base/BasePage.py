from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
import AppiumFramework.Utilities.Custom_logger as cl

import time


class BasePage:
    log = cl.customLogger()

    def __init__(self, driver):
        self.driver = driver

    def waitForElement(self, locatorvalue, locatorType):
        locatorType = locatorType.lower()
        element = None
        wait = WebDriverWait(self.driver, 25, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                                 NoSuchElementException])
        if locatorType == "id":
            element = wait.until(lambda x: x.find_element_by_id(locatorvalue))
            return element
        elif locatorType == "class":
            element = wait.until(lambda x: x.find_element_by_class_name(locatorvalue))
            return element
        elif locatorType == "des":
            element = wait.until(
                lambda x: x.find_element_by_android_uiautomator('UiSelector().description("%s")' % (locatorvalue)))
            return element
        elif locatorType == "index":
            element = wait.until(
                lambda x: x.find_element_by_android_uiautomator("UiSelector().index(%d)" % int(locatorvalue)))
            return element
        elif locatorType == "text":
            # element = wait.until(lambda x: x.find_element_by_android_uiautomator('text("%s")' % locatorvalue))
            # return element
            ele = wait.until(lambda x: x.find_element_by_android_uiautomator(
                'new UiScrollable(new UiSelector()).scrollIntoView(text("%s"))' % locatorvalue))
            return ele


        elif locatorType == "xpath":
            element = wait.until(lambda x: x.find_element_by_xpath('%s' % (locatorvalue)))
            return element


        else:
            self.log.info("Locator value " + locatorvalue + "not found")

        return element

    def getElement(self, locatorvalue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorvalue, locatorType)
            self.log.info(
                "Element found with the locator type" + locatorType + "with the locatorvalue: " + locatorvalue)
        except:
            self.log.info(
                "Element not found with the Locatortype :" + locatorType + " with the locator value :" + locatorvalue)

        return element

    def click_Element(self, locatorvalue: object, locatorType: object = "id") -> object:
        element = None
        try:
            locatorType = locatorType.lower()

            element = self.waitForElement(locatorvalue, locatorType)
            element.click()
            self.log.info(
                "Clicked on element with the locator type" + locatorType + "with the locator value : " + locatorvalue)

        except:
            self.log.info(
                "Element not clickable with locator type" + locatorType + "with the locator value" + locatorvalue)

    def enterText(self, text, locatorvalue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()

            element = self.waitForElement(locatorvalue, locatorType="id")
            element.send_keys(text)
            self.log.info(
                "Clicked on element with the locator type" + locatorType + "with the locator value : " + locatorvalue)

        except:
            self.log.info(
                "Element not clickable with locator type" + locatorType + "with the locator value" + locatorvalue)

    def is_displayed(self, locatorvalue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()

            element = self.waitForElement(locatorvalue, locatorType="id")
            element.is_displayed()
            self.log.info(
                "Clicked on element with the locator type" + locatorType + "with the locator value : " + locatorvalue)
            return True
        except:
            self.log.info(
                "Element not clickable with locator type" + locatorType + "with the locator value" + locatorvalue)
            return False

    def is_enabled(self, locatorvalue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()

            element = self.waitForElement(locatorvalue, locatorType="id")
            element.is_enabled()
            self.log.info(
                "Clicked on element with the locator type" + locatorType + "with the locator value : " + locatorvalue)
            return True
        except:
            self.log.info(
                "Element not clickable with locator type" + locatorType + "with the locator value" + locatorvalue)
            return False

    def screenshot(self, screenshotName):
        fileName = screenshotName + "_" + (time.strftime("%d_%m_%y_%H_%M_%S")) + ".png"
        screenshotDirectory = "../screenshots/"
        screenshotPath = screenshotDirectory + fileName
        try:
            self.driver.save_screenshot(screenshotPath)
            self.log.info("Screenshot is saved on " + screenshotPath)

        except:
            self.log.info("Screenshot not saved on " + screenshotPath)

    def scroll_in_view(self, locatorvalue, locatorType):
        element = None
        try:
            locatorType = locatorType.lower()

            element = self.waitForElement(locatorvalue, locatorType="text")
            element.scroll()
            self.log.info(
                "Clicked on element with the locator type" + locatorType + "with the locator value : " + locatorvalue)
            return True
        except:
            self.log.info(
                "Element not clickable with locator type" + locatorType + "with the locator value" + locatorvalue)
            return False

    def hide_keyboard(self):
        try:
            self.driver.hide_keyboard()
        except:
            self.log.info("Hiding keyboard command failed")
