import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import time

class Test_001_Login:
    base_URL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()

    logger=LogGen.loggen()

    def test_homePageTitle(self,setup):
        Test_001_Login.logger.info("********** Test_001_Login ***********")
        Test_001_Login.logger.info("********** TestCase Started ***********")
        self.driver=setup
        self.driver.get(self.base_URL)
        act_title=self.driver.title
        if act_title=="Your store. Login":
            assert True
            time.sleep(5)
            self.driver.close()
            Test_001_Login.logger.info("********** Home page title test is passed ***********")
            self.driver.quit()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            time.sleep(5)
            Test_001_Login.logger.error("********** Home page title test is failed ***********")
            self.driver.close()
            self.driver.quit()
            assert False


    def test_Login(self,setup):
        self.logger.info("********** Verifying Login Test ***********")
        self.driver = setup
        self.driver.get(self.base_URL)
        self.lp=LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title
        if act_title=="Dashboard / nopCommerce administration":
            assert True
            time.sleep(5)
            self.logger.info("********** Login Test is passed ***********")
            self.driver.close()
            self.driver.quit()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Login.png")
            time.sleep(5)
            self.logger.error("********** Login Test is failed ***********")
            self.driver.close()
            self.driver.quit()
            assert False