import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome(executable_path=".\\Driver\\chromedriver.exe")
        print("Launching Chrome Browser")
        driver.maximize_window()
    elif browser=="firefox":
        driver = webdriver.Chrome(executable_path=".\\Driver\\chromedriver.exe")
        print("Launching Firefox Browser")
        driver.maximize_window()
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


########### Pytest HTML Report ###############

#Hook for adding environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name']='nop Commerce'
    config._metadata['Module Name']='Customers'
    config._metadata['Tester']='Sai'

#Hook for delete/modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("plugins",None)
    


