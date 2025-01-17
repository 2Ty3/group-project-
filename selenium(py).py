# -*- coding: utf-8 -*-
"""「爬蟲」的副本

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1D1WbUi3Cs9OmsI-Nr39meAF7ju2zoxVX
"""

# Update package list and install necessary dependencies
!apt-get update
!apt-get install -y wget unzip libvulkan1

# Download and install Google Chrome
!wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
!dpkg -i google-chrome-stable_current_amd64.deb
!apt-get install -f -y

# Install xvfb for virtual framebuffer support
!apt-get install -y xvfb

# Install selenium and chromedriver-autoinstaller
!pip install selenium chromedriver-autoinstaller

# Automatically install the correct version of ChromeDriver
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()

# Configure Selenium with Chrome options
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Open Google and print the title of the page
driver.get('https://google.com')
print(driver.title)
driver.quit()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service # Import the Service class
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)

url = "https://www.pet.gov.tw/AnimalApp/ShelterMap.aspx"
driver.get(url)
time.sleep(3)  # 等待網頁加載
html = driver.page_source  # 获取网页源代码
soup = BeautifulSoup(html, "lxml")  # 使用 BeautifulSoup 解析 HTML

print(len(soup.find_all("table")))  # 打印表格数量
print(soup.find("table", {"id": "tab2-1"}))  # 打印指定 ID 的表格

driver.close()  # 關閉瀏覽器視窗
driver.quit()  # 結束瀏覽器進程

df.loc[:, ['收容所', '(犬)留容最大值', '(犬)在養數']]