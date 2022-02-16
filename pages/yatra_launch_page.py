import logging
import time

from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from base.base_driver import BaseDriver
from utilities.utils import Utils


class launchpage(BaseDriver):

    depart_from_xpath = "//input[@id='BE_flight_origin_city']"
    going_to_xpath="//input[@id='BE_flight_arrival_city']"
    departure_date_xpath="//input[@id='BE_flight_origin_date']"
    date_list_xpath="//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']"
    search_flights="//input[@value='Search Flights']"
    all_location_list_xpath="//div[@class='viewport']//li"

    log = Utils.custom_logger()



    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        #self.wait = wait

    def departfrom(self,departlocation):
        #depart_from=self.wait.until(EC.element_to_be_clickable((By.XPATH,self.depart_from_xpath)))
        depart_from = self.wait_until_an_element_present(By.XPATH,self.depart_from_xpath)
        time.sleep(5)

        depart_from.click()
        time.sleep(5)
        depart_from.clear()
        time.sleep(5)
        depart_from.send_keys(departlocation)
        time.sleep(5)
        depart_from.send_keys(Keys.ENTER)
        time.sleep(2)
        self.log.info("******Depart location entered************")

    def goingto(self,goingtolocation):
        #going_to=self.wait.until(EC.element_to_be_clickable((By.XPATH,self.going_to_xpath)))
        going_to = self.wait_until_an_element_present(By.XPATH, self.going_to_xpath)
        time.sleep(5)
        going_to.click()
        time.sleep(5)
        going_to.clear()
        time.sleep(5)
        going_to.send_keys(goingtolocation)
        time.sleep(5)
        going_to.send_keys(Keys.ENTER)
        time.sleep(2)
        self.log.info("******Going to location entered************")
        # search_flight=self.wait.until(EC.presence_of_all_elements_located((By.XPATH,self.all_location_list_xpath)))
        # for result in search_flight:
        #     if "goingtolocation" in result.text:
        #         result.click()
        #         break

    def selectdate(self,departuredate):
        time.sleep(5)
        #self.wait.until(EC.element_to_be_clickable((By.XPATH,self.departure_date_xpath))).click()
        depdt = self.wait_until_an_element_present(By.XPATH,self.departure_date_xpath )
        time.sleep(3)
        depdt.click()
        time.sleep(5)
        # all_dates = self.wait.until(
        #     EC.element_to_be_clickable((By.XPATH,self.date_list_xpath))) \
        #     .find_elements(By.XPATH,self.date_list_xpath)
        all_dates=self.wait_until_an_element_present(By.XPATH,self.date_list_xpath).find_elements(By.XPATH,self.date_list_xpath)
        for date in all_dates:
            if date.get_attribute("data-date") == departuredate:
                date.click()
                break
        self.log.info("******Date selected******")

    def clicksearch(self):
        self.driver.find_element(By.XPATH, self.search_flights).click()
        time.sleep(5 )



