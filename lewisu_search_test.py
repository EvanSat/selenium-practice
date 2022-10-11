import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time


class SeleniumSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_about_us_exists(self):
        self.driver.get('https://lewisu.edu/index.htm')
        self.driver.maximize_window()
        assert "About Us" in self.driver.page_source

    def test_academics_exists(self):
        self.driver.get('https://lewisu.edu/index.htm')
        assert "Academics" in self.driver.page_source
        self.driver.quit()

    def test_admission_aid_exists(self):
        self.driver.get('https://lewisu.edu/index.htm')
        time.sleep(1)
        print(time.localtime())
        assert "Admission & Aid" in self.driver.page_source
        self.driver.quit()

    def test_Athletics_exists(self):
        self.driver.get('https://lewisu.edu/index.htm')
        assert "Athletics" in self.driver.page_source
        self.driver.quit()

    def test_student_life_exists(self):
        self.driver.get('https://lewisu.edu/index.htm')
        assert "Student Life" in self.driver.page_source
        self.driver.quit()

    def test_locations_exists(self):
        self.driver.get('https://lewisu.edu/index.htm')
        assert "Locations" in self.driver.page_source
        self.driver.quit()

    def test_faculty_staff_search(self):
        self.driver.get('https://lewisu.edu/index.htm')
        self.driver.maximize_window()
        self.driver.find_element(By.LINK_TEXT, 'Fac/Staff').click()
        time.sleep(1)
        self.driver.find_element(By.LINK_TEXT, 'Faculty/Staff Directory').click()
        time.sleep(1)
        last_name_search = self.driver.find_element(By.NAME, 'last')
        last_name_search.send_keys('Omari')
        self.driver.find_element(By.NAME, 'submit').click()
        assert "Omari, Dr. Safwan" in self.driver.page_source
        self.driver.quit()

    def test_search_in_python_org(self):
        self.driver.get("http://www.python.org")
        self.assertIn("Python", self.driver.title)
        elem = self.driver.find_element(By.NAME, 'q')
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in self.driver.page_source
        self.driver.quit()

    def tear_down(self):
        self.driver.close()
