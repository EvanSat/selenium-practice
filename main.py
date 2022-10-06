from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


PATH = "C:\\Users\\evans\\Documents\\GitHub\\selenium-practice\\chromedriver.exe"
s = Service(PATH)
browser = webdriver.Chrome(service=s)

url = "https://www.google.com"
browser.get(url)
print(browser.title)

search = browser.find_element(By.NAME, 'q')  # Finds Search Box
search.send_keys("test input")
search.send_keys(Keys.RETURN)

time.sleep(5)

browser.close()     # closes tab |.quit() will close whole browser
