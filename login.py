from selenium import webdriver
import time
from config.settings import *

driver = webdriver.Chrome(executable_path=CHROME_PATH)

class TestingLogin():

    def LoginNOK(self, username, parola, testcase):

        driver.get(URL)

        user = driver.find_element_by_xpath("//input[@name='uid']")
        user.send_keys(username)

        password = driver.find_element_by_name("password")
        password.send_keys(parola)

        button = driver.find_element_by_name("btnLogin")
        button.click()

        time.sleep(5)

        try:
            actualTitle = driver.title
            print(actualTitle)
            if (actualTitle == "Guru99 Bank Manager HomePage"):
                print("TEST CASE LOGIN " + testcase + " NOK FAILED")
            else:
                print("TEST CASE LOGIN " + testcase + " NOK PASS")
        except:
            print("TEST CASE LOGIN " + testcase + " NOK PASS")



    def LoginOk(self, username, parola):

        driver.get("http://www.demo.guru99.com/V4/")

        #user = driver.find_element_by_name("uid")
        user = driver.find_element_by_xpath("//input[@name='uid']")
        user.send_keys(username)
        #//input[@name='uid']

        password = driver.find_element_by_name("password")
        password.send_keys(parola)

        button = driver.find_element_by_name("btnLogin")
        button.click()



        try:
            actualTitle = driver.title
            print(actualTitle)
            if (actualTitle == "Guru99 Bank Manager HomePage"):
                print("TEST CASE LOGIN PASS")
            else:
                print("TEST CASE LOGIN FAILED")
        except:
            print("TEST CASE LOGIN FAILED")




        time.sleep(5)



test = TestingLogin()
test.LoginOk(USERNAME, PASSWORD)

#username = "mngr327236"
#parola = "rehavAsNOK"
#test.LoginNOK(username, parola)

test.LoginNOK(USERNAME, "parolaNOK", "user ok, password nok")
test.LoginNOK("userNOK", PASSWORD, "user nok, password ok")
test.LoginNOK("userNOK", "parolaNOK", "user nok, password nok")
test.LoginNOK("", PASSWORD, "user empty, password ok")
test.LoginNOK(USERNAME, "", "user ok, password empty")

driver.quit()