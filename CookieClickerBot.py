# place your imports here
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
driver = webdriver.Chrome('C:\WinPython-64bit-3.6.3.0Qt5\chromedriver.exe')
driver.get('http://orteil.dashnet.org/cookieclicker/')
time.sleep(3)


cookie = driver.find_element_by_id("bigCookie")
cursor = driver.find_element_by_id("product0")
grandma = driver.find_element_by_id("product1")
farm = driver.find_element_by_id("product2")
mine = driver.find_element_by_id("product3")
factory = driver.find_element_by_id("product4")

classUpgrade0 = ''
classUpgrade1 = ''


while True:
    cookie.click()
    try:
        classCursor = cursor.get_attribute("class")
        classGrandma = grandma.get_attribute("class")
        classFarm = farm.get_attribute("class")
        classMine = mine.get_attribute("class")
        classFactory = factory.get_attribute("class")
        upgrade0 = driver.find_element_by_id("upgrade0")
        classUpgrade0 = upgrade0.get_attribute("class")
    except NoSuchElementException:
        pass
    
    if classCursor == "product unlocked enabled":
        cursor.click()
    elif classGrandma == "product unlocked enabled":
        grandma.click()
    elif classFarm == "product unlocked enabled":
        farm.click()
    elif classMine == "product unlocked enabled":
        mine.click()
    elif classFactory == "product unlocked enabled":
        factory.click()
    elif classUpgrade0 == "crate upgrade enabled":
        upgrade0.click()
