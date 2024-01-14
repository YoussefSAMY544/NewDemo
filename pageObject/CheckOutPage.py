from selenium.webdriver.common.by import By
#self.driver.find_elements(By.CSS_SELECTOR, ".card-title a")
#self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()


class CheckOutPage:
    def __init__(self, driver):
          self.driver = driver

    cardTitle = (By.CSS_SELECTOR, ".card-title a")

    cardfooter = (By.CSS_SELECTOR, ".card-footer button")
    checkout = (By.CSS_SELECTOR, ".nav-link.btn.btn-primary")
    def getcardTitles(self):

         return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getcardfooter(self):

         return self.driver.find_elements(*CheckOutPage.cardfooter)

    def clickcheckout(self):
        return self.driver.find_element(*CheckOutPage.checkout)