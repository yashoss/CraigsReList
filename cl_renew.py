import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotVisibleException 
 
def init_driver():
    driver = webdriver.Chrome(r"/PATH/TO/CHROMEDRIVER.EXT")
    driver.wait = WebDriverWait(driver, 10)
    return driver
 
 

def renew(driver, email, pw):
    driver.get("https://accounts.craigslist.org/login/home")
    query = "//form[@class='managebtn' and @value='repost']"
    try:
        user = driver.wait.until(EC.presence_of_element_located(
            (By.NAME, "inputEmailHandle")))
        pfield = driver.wait.until(EC.presence_of_element_located(
            (By.NAME, "inputPassword")))
        user.send_keys(email)
        pfield.send_keys(pw)
        button = driver.wait.until(EC.element_to_be_clickable(
            (By.CLASS_NAME, "accountform-btn")))
        button.click()
        time.sleep(2)
        rep =  driver.wait.until(EC.presence_of_element_located(
            (By.XPATH, query)))
        while(rep):
            rep.submit()
            time.sleep(4)
            driver.back()
            time.sleep(8)
            rep =  driver.wait.until(EC.presence_of_element_located(
                (By.XPATH, query)))
    except TimeoutException:
        print("No more renews")
 
if __name__ == "__main__":
    driver = init_driver()
    renew(driver, "EMAIL", "PASSWORD")
    time.sleep(10)
    driver.quit()
