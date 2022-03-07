import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

The_URL = "https://tinder.com/app/recs"
chrome_driver_path = Service("C:\\Users\\Mike\\Desktop\\chromedriver_win32\\chromedriver")
driver = webdriver.Chrome(service=chrome_driver_path)
driver.get(The_URL)
base_window= driver.window_handles[0]

time.sleep(3)
#click on the log_in button

the_log_in_button = driver.find_element(By.XPATH, '//*[@id="o-1556761323"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
the_log_in_button.click()
time.sleep(2)
try:
    facebook_login = driver.find_element(By.XPATH, '//*[@id="o-1335420887"]/div/div/div[1]/div/div[3]/span/div[2]/button')
    facebook_login.click()

except:
    time.sleep(3)
    more_options =driver.find_element(By.XPATH, '//*[@id="o-1335420887"]/div/div/div[1]/div/div[3]/span/button')
    more_options.click()
    facebook_login = driver.find_element(By.XPATH, '//*[@id="o-1335420887"]/div/div/div[1]/div/div[3]/span/div[2]/button')
    facebook_login.click()


finally:


    time.sleep(3)
    fb_login_window = driver.window_handles[1]
    driver.switch_to.window(fb_login_window)
    time.sleep(2)
    facebook_num = driver.find_element(By.XPATH, '//*[@id="email"]')
    facebook_num.send_keys("+380660721528")

    facebook_password = driver.find_element(By.ID, 'pass')
    facebook_password.click()
    facebook_password.send_keys("----")
    time.sleep(3)
    login_button = driver.find_element(By.ID, "loginbutton")
    login_button.click()
    time.sleep(2)
    driver.switch_to.window(base_window)
    time.sleep(3)
    accept_cookies = driver.find_element(By.XPATH, '//*[@id="o-1556761323"]/div/div[2]/div/div/div[1]/button')
    accept_cookies.click()
    time.sleep(3)
    allow_location = driver.find_element(By.XPATH, '//*[@id="o-1335420887"]/div/div/div/div/div[3]/button[1]')
    allow_location.click()
    time.sleep(2)
    notification = driver.find_element(By.XPATH, '//*[@id="o-1335420887"]/div/div/div/div/div[3]/button[2]')
    notification.click()
    time.sleep(5)
while True:
    try:
        like_button = driver.find_element(By.XPATH, '//*[@id="Tinder"]/body')
    except:
        pass
    else:
        for i in range(10):
            like_button.send_keys(Keys.ARROW_RIGHT)
            time.sleep(3)
            break





