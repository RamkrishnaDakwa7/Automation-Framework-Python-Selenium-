import pytest
from selenium import webdriver
from PageObjects.LoginPage import Login
from Utility.ReadYaml import YamlUtility

class TestCaseLogin:

  #  baseurl= "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
   # Username="admin@yourstore.com"
    #Password="admin"

   # def using_yaml_utility(self):
   #    self.lpy=YamlUtility("config.yaml")
    #    self.lpy.read_yaml_td("baseurl") # self.lp.read_yaml_td


    def test_browser_login(self,load_driver,loading_yaml_url):
        self.driver=load_driver
        self.driver.get(loading_yaml_url)
        act_title=self.driver.title
        self.driver.close()
        if act_title=="Your store. Login":
            assert True
        else:
            self.driver.close()

    def test_userlogin(self,load_driver,loading_yaml_url,loading_yaml_userName,loading_yaml_userPassword):
        self.driver=load_driver
        self.driver.get(loading_yaml_url)
        self.lp=Login(load_driver)
        self.lp.setUsername(loading_yaml_userName)
        self.lp.setPassword(loading_yaml_userPassword)
        self.lp.clickLoginButton()
        act_title=self.driver.title
        if act_title=="Dashboard / nopCommerce administration":
            assert True
        else:
            assert False


#bj1=TestCaseLogin()
#obj1.using_yaml_utility()