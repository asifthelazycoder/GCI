from selenium import webdriver
from time import sleep

name = input("Enter Handle/Email for codeforces: ")
passwd = input("Enter password for codeforces: ")

driver = webdriver.Firefox()
driver.get("https://codeforces.com/contests")
driver.find_element_by_xpath("/html/body/div[5]/div[4]/div[1]/div/div[4]/div[1]/a[2]").click()
driver.find_element_by_id("handleOrEmail").send_keys(name)
driver.find_element_by_id("password").send_keys(passwd)
driver.find_element_by_class_name("submit").click()
driver.implicitly_wait(10)
driver.find_element_by_xpath("/html/body/div[5]/div[4]/div[2]/form/table/tbody/tr[3]/td/div/input").click()

