import email.headerregistry

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains

import os
from dotenv import load_dotenv

load_dotenv()


EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')
URL = "https://www.linkedin.com/jobs/search/?currentJobId=3348204152&f_AL=true&f_E=2&f_WT=2&geoId=102257491&keywords=" \
      "python%20developer&location=London%2C%20England%2C%20United%20Kingdom&refresh=true"


def main():
    chrome_driver_path = "C:\Developement\chromedriver.exe"
    service = Service(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=service)
    driver.get(url=URL)
    driver.maximize_window()
    sign_in_button = driver.find_element(By.CLASS_NAME, "nav__button-secondary")
    sign_in_button.click()
    sign_in_email = driver.find_element(By.NAME, "session_key")
    sign_in_email.send_keys(EMAIL)
    sign_in_password = driver.find_element(By.ID, "password")
    sign_in_password.send_keys(PASSWORD)
    login = driver.find_element(By.CSS_SELECTOR, ".login__form_action_container button")
    login.click()
    time.sleep(10)

    id= []
    ids = driver.find_elements(By.CSS_SELECTOR, ".scaffold-layout__list-container li")
    for i in ids:
        id.append(i.get_attribute("id"))
    id_list = [x for x in id if x != ""]
    print(id_list)
    for n in id_list:
        try:
            element_id = driver.find_element(By.ID, n)
        except NoSuchElementException:
            pass
        else:
            element_id.click()
            time.sleep(1)

        try:
            apply_button = driver.find_element(By.CLASS_NAME, "jobs-apply-button")
        except NoSuchElementException:
            pass
        else:
            driver.implicitly_wait(10)
            ActionChains(driver).move_to_element(apply_button).click(apply_button).perform()
            for x in range(2):
                next_button = driver.find_element(By.CLASS_NAME, "artdeco-button--primary")
                driver.implicitly_wait(10)
                ActionChains(driver).move_to_element(next_button).click(next_button).perform()
                # next_button.click()
                # time.sleep(5)

            review_button = driver.find_element(By.CLASS_NAME, "artdeco-button--primary")
            if review_button.text != "Review":
                cancel = driver.find_element(By.CLASS_NAME, "artdeco-button__icon")
                driver.implicitly_wait(10)
                ActionChains(driver).move_to_element(cancel).click(cancel).perform()
                # cancel.click()
                discard = driver.find_element(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")
                driver.implicitly_wait(10)
                ActionChains(driver).move_to_element(cancel).click(cancel).perform()
                # discard.click()
            else:
                review_button.click()

            submit_button = driver.find_element(By.CLASS_NAME, "artdeco-button--primary")
            if submit_button.text != "Submit application":
                cancel = driver.find_element(By.CLASS_NAME, "artdeco-button__icon")
                cancel.click()
                discard = driver.find_element(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")
                discard.click()
            else:
                submit_button.click()
        time.sleep(1)
    time.sleep(500)


if __name__ == "__main__":
    main()

