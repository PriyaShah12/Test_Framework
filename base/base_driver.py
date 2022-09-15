import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseDriver:

    def __init__(self,driver):
        self.driver=driver
        #self.wait=wait

    def page_scroll(self):
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        while True:  # Scroll down to bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # Wait to load page
            time.sleep(5)
        # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        time.sleep(5)

    def wait_until_all_elements_present(self, locatortype, locator):
        wait=WebDriverWait(self.driver,10)
        list_of_elements=wait.until(EC.presence_of_all_elements_located((locatortype, locator)))
        return list_of_elements

    def wait_until_an_element_present(self,locatortype,locator):
        wait = WebDriverWait(self.driver, 10)
        element=wait.until(EC.element_to_be_clickable((locatortype, locator)))
        return element
