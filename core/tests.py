from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


class SeleniumTest(TestCase):
    def test_one(self):
        driver =webdriver.Chrome()
        driver.get('http://localhost:8000/')
        driver.find_element_by_link_text('Создать место').click()
        sleep(5)
        #elem.send_keys('pycon')
        #elem.send_keys(Keys.RETURN)
        #assert "No results found." not in driver.page_source
        driver.close()















