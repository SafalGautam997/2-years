from selenium import webdriver
import pandas as pd
import os
driver = webdriver.Chrome(executable_path=r'C:\webdrivers\chromedriver.exe')
driver.get('https://doko.dwit.edu.np/class/show/1?stream=BSc.CSIT')
name1_element = driver.find_elements_by_xpath('//*[@id="main-content"]/section/section/div[1]/div/a/p')[0]
name1 = name1_element.text
name2_element = driver.find_elements_by_xpath('//*[@id="main-content"]/section/section/div[2]/div/a/p')[0]
name2 = name2_element.text
name3_element = driver.find_elements_by_xpath('//*[@id="main-content"]/section/section/div[3]/div/a/p')[0]
name3 = name3_element.text
name4_element = driver.find_elements_by_xpath('//*[@id="main-content"]/section/section/div[4]/div/a/p')[0]
name4 = name4_element.text
name5_element = driver.find_elements_by_xpath('//*[@id="main-content"]/section/section/div[5]/div/a/p')[0]
name5 = name5_element.text
name6_element = driver.find_elements_by_xpath('//*[@id="main-content"]/section/section/div[6]/div/a/p')[0]
name6 = name6_element.text
Names = [name1, name2, name3, name4, name5, name6]
print(Names)
