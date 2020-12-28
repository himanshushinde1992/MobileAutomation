import pytest
import allure


def test_methodA():
    allureLogs("this is test of allure log")
    allure.severity("high")
    print("This is method A")

def test_methodB():
    print("This is method B")


@pytest.mark.skip
def test_methodC():
    print("This is method C")


def test_methodD():
    print("This is method D")
    assert False


def allureLogs(text):
    with allure.step():
        pass
