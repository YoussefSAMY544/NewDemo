import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObject.CheckOutPage import CheckOutPage
from pageObject.ConfirmPage import ConfirmPage
from pageObject.Homepage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self):
        homePage = HomePage(self.driver)
        homePage.shopItems().click
        checkoutpage =homePage.shopItems().click()
        cards = CheckOutPage.getcardTitles(self)

        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            print(cardText)
            if cardText == "Blackberry":

             CheckOutPage.getcardfooter(self)[i].click()

        CheckOutPage.clickcheckout(self).click()

        ConfirmPage.getcheckoutbutton(self).click()

        ConfirmPage.getcountryfiled(self).send_keys("ind")

        # Delay using WebDriverWait
        element = ConfirmPage.getresultindia(self)
        element.click()

        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

        # Delay using WebDriverWait
        textMatch = WebDriverWait(self.driver, 20).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[class*='alert-success']"), "Success! Thank you!")
        )

        assert textMatch