from selenium import webdriver
from selenium.webdriver.common.by import By
import re

browser = webdriver.Chrome(executable_path=r"C:\webdrivers\chromedriver.exe")
URL = 'https://deerwalk.edu.np/'
numbers = []


browser.get(URL)

a_elements = browser.find_elements(By.TAG_NAME, 'a')
links = [element.get_attribute('href') for element in a_elements]

browser.get(links[0])
footer_content = browser.find_element(By.CLASS_NAME, 'footerContent')
text = footer_content.text
all_nums = re.findall('\d+', text)
numbers += all_nums

browser.get(links[1])
top_text = browser.find_element(By.CLASS_NAME, 'top-text')
text = top_text.text
all_nums = re.findall('\d\d-\d+', text)
numbers += all_nums

browser.close()
print(numbers)