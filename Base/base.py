import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

class BaseTest(unittest.TestCase):

    def setUp(self):
        browser = 'firefox'  # Change this value to 'firefox' or 'edge' to switch browsers
        if browser == 'chrome':
            chrome_driver_path = "C:\\Users\\Mallem Kondaiah\\OneDrive\\Desktop\\SDET\\Browsers\\chromedriver.exe"
            serv_obj = ChromeService(chrome_driver_path)
            self.driver = webdriver.Chrome(service=serv_obj)

        elif browser == 'firefox':
            firefox_driver_path = "C:\\Users\\Mallem Kondaiah\\OneDrive\\Desktop\\SDET\\Browsers\\geckodriver.exe"
            serv_obj = FirefoxService(firefox_driver_path)
            self.driver = webdriver.Firefox(service=serv_obj)

        elif browser == 'edge':
            edge_driver_path = "C:\\Users\\Mallem Kondaiah\\OneDrive\\Desktop\\SDET\\Browsers\\msedgedriver.exe"
            serv_obj = EdgeService(edge_driver_path)
            self.driver = webdriver.Edge(service=serv_obj)

        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()
