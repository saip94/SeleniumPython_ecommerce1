import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time

class Test_002_DDT_Login:
    base_URL=ReadConfig.getApplicationURL()
    path=".//TestData/LoginData.xlsx"
    # username=ReadConfig.getUseremail()
    # password=ReadConfig.getPassword()
    logger=LogGen.loggen()

    def test_login_ddt(self,setup):
        self.logger.info("********** Test_002_DDT_Login ***********")
        self.logger.info("********** Verifying Login DDT Test ***********")
        self.driver = setup
        self.driver.get(self.base_URL)
        self.lp=LoginPage(self.driver)

        self.rows=XLUtils.getRowCount(self.path,'Sheet1')
        print("Number of rows in excel:",self.rows)

        for r in range(2,self.rows+1):
            self.user=XLUtils.readData(self.path,'Sheet1',r,1)
            self.password=XLUtils.readData(self.path,'Sheet1',r,2)
            self.expected=XLUtils.readData(self.path,'Sheet1',r,3)

            self.lp.setUsername(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce administration"

            lst_status=[]
            if act_title==exp_title:
                if self.expected=="Pass":
                    self.logger.info("Test is passed")
                    print("Test is passed") 
                    self.lp.clickLogout()
                    lst_status.append("Pass")

                elif self.expected=="Fail":
                    self.logger.info("Test is failed")
                    print("Test is failed")
                    # self.lp.clickLogout()
                    lst_status.append("Fail")

            else:
                if self.expected=="Pass":
                    self.logger.info("Test is failed")
                    print("Test is failed")
                    # self.lp.clickLogout()
                    lst_status.append("Fail")

                elif self.expected=="Fail":
                    self.logger.info("Test is passed")
                    print("Test is passed")
                    # self.lp.clickLogout()
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("Login DDT test is passed")
            print("Login DDT test is passed")
            assert True
            self.driver.close()
            self.driver.quit()
        else:
            self.logger.info("Login DDT test is failed")
            print("Login DDT test is failed")
            assert False
            self.driver.close()
            self.driver.quit()






        # self.lp.setUsername(self.username)
        # self.lp.setPassword(self.password)
        # self.lp.clickLogin()
        # act_title=self.driver.title
        # if act_title=="Dashboard / nopCommerce administration":
        #     assert True
        #     time.sleep(5)
        #     self.logger.info("********** Login Test is passed ***********")
        #     self.driver.close()
        #     self.driver.quit()
        # else:
        #     self.driver.save_screenshot(".\\Screenshots\\" + "test_Login.png")
        #     time.sleep(5)
        #     self.logger.error("********** Login Test is failed ***********")
        #     self.driver.close()
        #     self.driver.quit()
        #     assert False