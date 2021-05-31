from selenium import webdriver
import time
from config.settings import *
from selenium.webdriver import ActionChains


driver = webdriver.Chrome(executable_path=CHROME_PATH)




class DgraAndDrop():
    def testingDragAndDrop(self):
        driver.get("https://jqueryui.com/droppable/")

        pathIframe = driver.find_element_by_xpath("//iframe[@class='demo-frame']")
        driver.switch_to.frame(pathIframe)

        fromElement = driver.find_element_by_xpath("//div[@id='draggable']")
        toElement = driver.find_element_by_xpath("//div[@id='droppable']")

        action = ActionChains(driver)
        action.drag_and_drop(fromElement, toElement)
        action.perform()

        time.sleep(5)

dragAndDrop = DgraAndDrop();
dragAndDrop.testingDragAndDrop();

driver.quit()