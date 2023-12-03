import pytest
from selenium import webdriver
from Utility.ReadYaml import YamlUtility

@pytest.fixture(autouse=True)
def load_driver():
    driver=webdriver.Chrome()
    return driver

@pytest.fixture(autouse=True)
def loading_yaml_url():
    lpy=YamlUtility("config.yaml")
    return lpy.read_yaml_td('baseurl')

@pytest.fixture(autouse=True)
def loading_yaml_userName():
    lpy=YamlUtility("config.yaml")
    return lpy.read_yaml_td('Username')

@pytest.fixture(autouse=True)
def loading_yaml_userPassword():
    lpy=YamlUtility("config.yaml")
    return lpy.read_yaml_td('Password')


