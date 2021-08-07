from contextlib import closing
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument('log-level=3')

with closing(webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)) as driver:
    driver.get("https://lirarate.org/")
    time.sleep(5)
    src = driver.page_source

soup = BeautifulSoup(src, "lxml")
buy_price = soup.find("p", {"id":"latest-buy"}).text
sell_price = soup.find("p", {"id":"latest-sell"}).text
last_updated = soup.find("div", {"id":"last-updated"}).text
last_updated_datetime = soup.find("div", {"id":"last-updated-datetime"}).text
print("\n.....................................................")
print(buy_price)
print(sell_price)
print(".....................................................")
print(last_updated)
print(last_updated_datetime)
