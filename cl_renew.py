import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotVisibleException 
 
def init_driver():
    driver = webdriver.Chrome(r"C:\Users\The Prophet\Desktop\chromedriver.exe")
    driver.wait = WebDriverWait(driver, 10)
    return driver
 
 

def lookup(driver, email, pw):
    driver.get("https://accounts.craigslist.org/login/home")
    #query = "//input[@value='edit' AND @type='submit']"
    query = "//form[@class='manage renew']"
    try:
        user = driver.wait.until(EC.presence_of_element_located(
            (By.NAME, "inputEmailHandle")))
        pfield = driver.wait.until(EC.presence_of_element_located(
            (By.NAME, "inputPassword")))
        button = driver.wait.until(EC.element_to_be_clickable(
            (By.CLASS_NAME, "accountform-btn")))
        user.send_keys(email)
        pfield.send_keys(pw)
        driver.wait
        button.click()
        driver.wait
        rep =  driver.find_elements_by_xpath(query)
        driver.wait
        while(len(rep) > 0):
            rep[0].submit()
            driver.wait
            driver.back()
            driver.wait
            rep =  driver.find_elements_by_xpath(query)
    except TimeoutException:
        print("No more renews")
 
if __name__ == "__main__":
    driver = init_driver()
    lookup(driver, "email", "password")
    time.sleep(10)
    #driver.quit()
