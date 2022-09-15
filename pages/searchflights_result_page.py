import logging
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_driver import BaseDriver
from utilities.utils import Utils


class SearchFlightResult(BaseDriver):
    non_stop_button="//p[@class='font-lightgrey bold'][contains(text(),'0')]"
    one_stop_button="//p[@class='font-lightgrey bold'][contains(text(),'1')]"
    two_stop_button="//p[@class='font-lightgrey bold'][contains(text(),'2')]"
    all_flight_result_elements="//span[contains(text(),'Non Stop')\
         or contains(text(),'1 Stop') or contains(text(),'2 Stop')]"

    log=Utils.custom_logger(loglevel= logging.WARNING)

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
        #self.wait=wait

    def select_stops(self, stop):
        if stop == "Non Stop":
            self.driver.find_element(By.XPATH,self.non_stop_button).click()
            #print("Selected non stop flights")
            self.log.warning("Selected non stop flights")
            time.sleep(2)
        elif stop == "1 Stop":
            self.driver.find_element(By.XPATH,self.one_stop_button).click()
            #print("Selected flights with one stop")
            self.log.warning("Selected flights with one stop")
            time.sleep(2)
        elif stop == "2 Stop":
            self.driver.find_element(By.XPATH,self.two_stop_button).click()
            #print("Selected flights with two stop")
            self.log.warning("Selected flights with two stop")
            time.sleep(2)
        else:
            print("Enter correct value")

    def filter_nonstop_flights_list(self):
        list_flights= self.wait_until_all_elements_present(By.XPATH,self.all_flight_result_elements)
        return list_flights







