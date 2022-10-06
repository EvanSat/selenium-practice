from selenium import webdriver
from selenium.webdriver.chrome.service import Service

PATH = "C:\Program Files (x86)\chromedriver.exe"
s = Service(PATH)
browser = webdriver.Chrome(service=s)

url = "https://www.google.com"
browser.get(url)
