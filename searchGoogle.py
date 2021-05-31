from selenium import webdriver
import time

class ChromeDriverWindows():

    def searchGoogle(self):
        driver = webdriver.Chrome(executable_path="D:\\Curs QA\\Curs 12\\chromedriver_win32\\chromedriver.exe")
        driver.get("http://google.com")

        element = driver.find_element_by_id("L2AGLb")
        element.click()

        element_search = driver.find_element_by_name("q")
        element_search.send_keys("selenium")
        element_search.submit()

        time.sleep(30)



search = ChromeDriverWindows()
search.searchGoogle()
