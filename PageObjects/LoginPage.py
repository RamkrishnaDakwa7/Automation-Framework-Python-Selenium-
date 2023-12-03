import selenium.webdriver.chrome.options
import selenium.webdriver.chrome.webdriver
from selenium.webdriver.common.by import By


class Login:
    testbox_username_id="Email"
    textbox_password_id="Password"
    button_login_class= "//button[@class='button-1 login-button']"
    button_logout_ref="//a[@href='/logout']"

    def __init__(self,driver):
        self.driver=driver

    def setUsername(self,Username):
        self.driver.find_element(By.ID,self.testbox_username_id).clear()
        self.driver.find_element(By.ID,self.testbox_username_id).send_keys(Username)

    def setPassword(self,Password):
        self.driver.find_element(By.ID,self.textbox_password_id).clear()
        self.driver.find_element(By.ID,self.textbox_password_id).send_keys(Password)

    def clickLoginButton(self):
        self.driver.find_element(By.XPATH, self.button_login_class).click()

    def clicklogoutButton(self):
        self.driver.find_element(By.XPATH,self.button_logout_ref).click()




