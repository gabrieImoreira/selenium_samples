from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from util.seleniumUtil import SeleniumUtil
import re

class WebScraper:

    def scrapeEmailAddresses(driver, pageUrl):
        list_emails = []
        page_source = WebScraper.get(pageUrl, driver)
        table = driver.find_element(By.TAG_NAME, "table")
        for element in table.find_elements(By.XPATH, ".//*"):
            if "@" in element.text:
                emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", element.text)
                for email in emails:
                    if email not in list_emails:
                        list_emails.append(email)
        return list_emails

    def scrapeMobileNumbers(driver, pageUrl):
        list_tels = []
        page_source = WebScraper.get(pageUrl, driver)
        table = driver.find_element(By.TAG_NAME, "table")
        for element in table.find_elements(By.XPATH, ".//*"):
            tels = re.findall(r"\b\d{10}\b", element.text)
            for tel in tels:
                if tel not in list_tels:
                    list_tels.append(tel)
        return list_tels
    
    # do not modify
    def get(url, driver):
        driver.get(url)
        return driver.page_source
