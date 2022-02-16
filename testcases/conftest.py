import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.driver import OperaDriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager, IEDriverManager


@pytest.fixture(scope="class")
def setup(request, browser):
    if browser == 'Chrome':
        s = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=s)
    elif browser == 'Firefox':
        s = Service(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=s)
    elif browser == "Edge":
        s = Service(EdgeChromiumDriverManager().install())
        driver = webdriver.Ie(service=s)
    elif browser == "Opera":
        s = Service(executable_path=OperaDriver().install())
        driver = webdriver.Opera(service_args=s)
    else:
        s = Service(IEDriverManager().install())
        driver = webdriver.Chrome(service=s)
    request.cls.driver = driver
    # request.cls.wait=wait
    yield
    driver.close()


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="class")
def browser(request):
    return request.config.getoption("--browser")

@pytest.mark.usefixtures("setup")
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        # always add url to report
        extra.append(pytest_html.extras.url("http://www.yatra.com/"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            report_directory= os.path.dirname(item.config.option.htmlpath)
            file_name=report.nodeid.replace("::","_")+ ".png"
            destinationFile= os.path.join(report_directory, file_name)
            driver.save_screenshot(destinationFile)
            # only add additional html on failure
            extra.append(pytest_html.extras.html("<div>Additional HTML</div>"))
        report.extra = extra

def pytest_html_report_title(report):
    report.title= "Priya Shah Automation Report"


