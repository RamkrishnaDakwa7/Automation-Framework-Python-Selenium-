import pytest
from selenium import webdriver
from Utility.ReadYaml import YamlUtility


@pytest.fixture(autouse=True)
def load_driver(browser):
    if browser=='chrome':
        driver=webdriver.Chrome()
    elif browser=='firefox':
        driver=webdriver.Firefox()
    else:
        driver=webdriver.Chrome()
    return driver

@pytest.fixture(autouse=True)
def loading_yaml_url():
    lpy=YamlUtility("..\Configurrations\config.yaml")
    return lpy.read_yaml_td('baseurl')

@pytest.fixture(autouse=True)
def loading_yaml_userName():
    lpy=YamlUtility("..\Configurrations\config.yaml")
    return lpy.read_yaml_td('Username')

@pytest.fixture(autouse=True)
def loading_yaml_userPassword():
    lpy=YamlUtility("..\Configurrations\config.yaml")
    return lpy.read_yaml_td('Password')

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(autouse=True)
def browser(request):
    return request.config.getoption("--browser")

