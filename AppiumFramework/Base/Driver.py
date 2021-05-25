from appium import webdriver


class Driver:

    def getDriver(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['automationName'] = 'UiAutomator2'
        desired_caps['platformVersion'] = '7.0'
        desired_caps['deviceName'] = 'WK8DWSMJAASGLREM'
        desired_caps['app'] = ("J:\\copied docus\\")
        desired_caps['appPackage'] = 'com.assetpanda'
        desired_caps['appActivity'] = 'com.assetpanda.activities.LoginRegisterActivity'
        # desired_caps['FullReset'] = True


        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        driver.hide_keyboard()
        return driver
