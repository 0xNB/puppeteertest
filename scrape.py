import undetected_chromedriver as uc 
import time
from selenium.webdriver.common.by import By 
 
driver = uc.Chrome() 
driver.get("https://www.immobilienscout24.de/expose/143404064")
 
time.sleep(5)
 
print(driver.current_url) # https://www.nowsecure.nl/ 
print(driver.title) # nowSecure

driver.save_screenshot('nowsecure.png')

print(driver.find_element(By.ID, "is24-expose-about-realtor-box-tablet"))