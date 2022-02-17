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

def pytest_configure(config):
    config._metadata["Project Name"] = "Airlines-Yatra"
    config._metadata["Tester"] = "Priya"

@pytest.mark.optionalhook
def pytest_configure(config):
    config._metadata.pop("JAVA_HOME", None)
    config._metadata.pop("Plugins", None)

def pytest_html_report_title(report):
    report.title= "Automation Report by Priya Shah"


