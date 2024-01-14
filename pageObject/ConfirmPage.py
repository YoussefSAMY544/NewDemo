#self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
#self.driver.find_element(By.ID, "country").send_keys("ind")
#presence_of_element_located((By.PARTIAL_LINK_TEXT, "India")
#element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "India")))
from telnetlib import EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    checkoutbutton = (By.XPATH, "//button[@class='btn btn-success']")

    def getcheckoutbutton(self):

         return self.driver.find_element(*ConfirmPage.checkoutbutton)


    countryfiled = (By.ID, "country")

    def getcountryfiled(self):

        return self.driver.find_element(*ConfirmPage.countryfiled)



    resultindia = (By.PARTIAL_LINK_TEXT, "India")



    def getresultindia(self):

            return WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(ConfirmPage.resultindia))









