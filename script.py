import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time




def get_data(URL:str, XPATH:str, XPATH_CLICK:str, XPATH_TABLE:str)->str:
    driver = webdriver.Chrome("./chromedriver")
    driver.get(URL)
    field = driver.find_element_by_xpath(XPATH)
    field.click()
    for _ in range(12):
        field.send_keys(Keys.BACKSPACE)
    field.send_keys("03-01-1989")
    field.send_keys(Keys.ENTER)
    field2 = driver.find_element_by_xpath(XPATH_CLICK)
    field2.click()
    time.sleep(5)
    table_field = driver.find_element_by_xpath(XPATH_TABLE)
    return table_field.get_attribute('innerHTML')



def parser(table_element:str)-> dict:
    table = BeautifulSoup(table_element, 'lxml')
    for rows in table.find_all('tr'):
        finder = lambda x: rows.find_all(x)
        if finder('th'):
            headers=[nodo.get_text() for nodo in finder('th')]
            data = {header:[] for header in headers }
        else: 
            row=[nodo.get_text() for nodo in finder('td')]
            for i,v in enumerate(data.values()):
                v.append(row[i])
    return data

def make_dataframe(data:dict) -> pd.DataFrame:
    dataframe = pd.DataFrame(data=data).replace(r",",'.', regex=True)
    dataframe.iloc[:,1:3] = dataframe.iloc[:,1:3].replace(',', '.').astype(float)
    dataframe.iloc[:,0]=pd.to_datetime(dataframe.iloc[:,0], dayfirst=True)
    return dataframe


def main()-> pd.DataFrame:

    XPATH = "/html/body/main/div[6]/div/div/div[1]/input"
    XPATH_TABLE = '/html/body/main/div[6]/div/div/table'
    XPATH_CLICK = "/html/body/main/div[6]/div/div/button"
    URL = "https://www.ambito.com/contenidos/dolar-informal-historico.html"
    raw_data = get_data(URL,XPATH,XPATH_CLICK,XPATH_TABLE)
    data = parser(raw_data)
    dataframe = make_dataframe(data)
    return dataframe



if __name__=="__main__":
    data = main()
    data.to_csv('datos_ambito.csv')



