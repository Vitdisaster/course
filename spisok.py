from selenium import webdriver
import time 
import math


try:
    link = "http://suninjuly.github.io/selects2.html"
    driver = webdriver.Chrome()
    driver.get(link)

    x = driver.find_element_by_id("num1")
    x = x.text
    x=int(x)
    #print(x)
    
    y = driver.find_element_by_id("num2")
    y = y.text
    y=int(y)
    #print(y)
    z = x+y
    #print(z)
    z = str(z)
    from selenium.webdriver.support.ui import Select
    select = Select(driver.find_element_by_tag_name("select"))
    select.select_by_visible_text(z)
    button = driver.find_element_by_css_selector("button.btn")
    button.click()
	
finally:
	time.sleep(10)
	driver.quit()	