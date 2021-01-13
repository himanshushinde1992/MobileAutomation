import time

import pytest

from AppiumFramework.Base.Driver import Driver


@pytest.yield_fixture(scope='class')
def beforeClass(request):
    global driver
    print("before class")
    driver1 = Driver()
    driver = driver1.getDriver()
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    time.sleep(5)
    driver.quit()