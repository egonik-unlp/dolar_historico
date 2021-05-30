import pandas as pd
from selenium import webdriver
from selenium.webdriver import ActionChains
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time

XPATH="/html/body/main/div[6]/div/div/div[1]/input"
XPATH_CLICK="/html/body/main/div[6]/div/div/button"
URL="https://www.ambito.com/contenidos/dolar-informal-historico.html"

def main():
    driver=webdriver.Chrome("./chromedriver")
    driver.get(URL)
    field=driver.find_element_by_xpath(XPATH)
    field.click()
    for _ in range(12):
        field.send_keys(Keys.BACKSPACE)
    field.send_keys("03-01-1989")
    field.send_keys(Keys.ENTER)
    field2=driver.find_element_by_xpath(XPATH_CLICK)
    field2.click()
    time.sleep(60)
if __name__=="__main__":
    main()



