#!/usr/bin/python3

import undetected_chromedriver as uc 
import time
from selenium.webdriver.common.by import By 
import json

# @Table
# export class RealEstate extends Model {
#   @Column
#   title: string;
#   @Column
#   creation_date: Date;
#   @Column
#   last_modification_date: Date;
#   @Column
#   area: number;
#   @Column
#   area_living: number;
#   @Column
#   area_commercial: number;
#   @Column
#   num_units: number;
#   @Column
#   num_carports: number;
#   @Column
#   num_garages: number;
#   @Column
#   thousandsth: number;
#   @Column
#   ground_value: number;
# }


def scrapeImmoscoutId(immoscoutUrl):
    driver = uc.Chrome(browser_executable_path="/snap/bin/chromium") 
    driver.get(immoscoutUrl)
    
    time.sleep(10)
    
    realEstate = {
        'title': 'NAN',
        'creation_date': None,
        'last_modification_date': None,
        'area': "",
        'area_living': 0,
        'area_commercial': 0,
        'num_units': 0,
        'num_carports': 0,
        'num_garages': 0,
        'thousandsth': 0,
        'ground_value': 0
    }
    
    realEstate['title'] = driver.find_element(By.ID, "expose-title").text
    
    areaSize = driver.find_element(By.XPATH, "//div[@class='is24qa-flaeche-main is24-value font-semibold']")
    priceValue = driver.find_element(By.CLASS_NAME, "is24-preis-value")
    
    print('values')
    print(areaSize)
    print(areaSize.text)
    print(len(areaSize.text))
    
    print(priceValue)
    print(priceValue.text)
    priceValue.text
    
    print('values')
    realEstate['area'] = areaSize.text
    print(driver.current_url) # https://www.nowsecure.nl/ 
    
    realEstateJson = json.dumps(realEstate)
    print(realEstateJson)
    
scrapeImmoscoutId("https://www.immobilienscout24.de/expose/144521476")