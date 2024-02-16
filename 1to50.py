from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("https://zzzscore.com/1to50/en/")
driver.execute_script("window.scrollBy(0,300)", "")

for i in range(1, 51):
    try:
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@style='opacity: 1;' and text() ='{}']".format(str(i))))
        )
        button = driver.find_element(By.XPATH, "//div[@style='opacity: 1;' and text() ='{}']".format(str(i)))
        button.click()

    except:
        logging.warning("Element Not Found!")
        exit()

score = driver.find_element(By.XPATH, "//div[@id='time']").text
print("Time to complete: {}s".format(score))
