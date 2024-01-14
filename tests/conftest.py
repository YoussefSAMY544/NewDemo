#python -m pytest --browser_name firefox
#C:\Users\YoussefAbourabeh\PycharmProjects\pythonProject1 - path project
#c+sh+R

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome")


@pytest.fixture(scope="class")
def setup(request):
    browser_name= request.config.getoption("browser_name")
    if browser_name == "chrome":
        service = Service()
        driver = webdriver.Chrome()
        driver.get("https://rahulshettyacademy.com/angularpractice/")
        driver.maximize_window()
    elif browser_name == "firefox":
        service = Service()
        driver = webdriver.Firefox()
        driver.get("https://rahulshettyacademy.com/angularpractice/")
        driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()


