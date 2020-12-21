import pytest

from AppiumFramework.Base.Driver import Driver


@pytest.yield_fixture(scope='class')
def beforeClass(Request):
    print("before class")
    driver1 =Driver()
    driver = driver1.getDriver()