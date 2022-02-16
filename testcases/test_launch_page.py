import logging
import time
import softest
from selenium import webdriver
from base.base_driver import BaseDriver
from pages.searchflights_result_page import SearchFlightResult
from pages.yatra_launch_page import launchpage
#from selenium.common.exceptions import ElementClickInterceptedException,StaleElementReferenceException, ElementNotSelectableException
import pytest
from utilities.read_properties import configRead
from utilities.utils import Utils
import softest
from ddt import ddt, data, file_data, unpack


@ddt
@pytest.mark.usefixtures("setup")
class Test_LaunchPg(softest.TestCase):
    base_url =configRead.ReadUrl()
    log= Utils.custom_logger()

    def test_home_page_title(self):
        lp = launchpage(self.driver)
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        time.sleep(5)
        act_title=self.driver.title

        if act_title=="Flight, Cheap Air Tickets , Hotels, Holiday, Trains Package Booking - Yatra.com":

            assert True
            print("Title Match")
            self.log.info("Title match")
        else:
            assert False
            print("Title does not match")
            self.log.info("Title does not match")

    #@data(("Ahmedabad", "Chennai", "28/04/2022", "1 Stop"),("Mumbai", "Goa", "20/08/2022", "2 Stop"))
    #@unpack
    #@file_data("../testData/datajson.json")
    #@file_data("../testData/datayaml.yaml")

    #@data(*Utils.read_data_from_excel("C:\\Users\\prsha\\PycharmProjects\\TestFramework\\testData\\tdata1.xlsx","Sheet1"))
    #@unpack

    @data(*Utils.read_data_from_csv("C:\\Users\\prsha\\PycharmProjects\\TestFramework\\testData\\datacsv.csv"))
    @unpack
    def test_launch_pg(self, goingfrom, goingto, date, stop):

        lp=launchpage(self.driver)
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        time.sleep(5)
        lp.departfrom(goingfrom)
        lp.goingto(goingto)
        lp.selectdate(date)
        lp.clicksearch()
        lp.page_scroll()
        sf=SearchFlightResult(self.driver)
        all_stops=sf.filter_nonstop_flights_list()
        sf.select_stops(stop)
        ut=Utils()

        ut.assert_list_item_text(all_stops,"1 Stop")










