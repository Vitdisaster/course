from selenium import webdriver
import time 
import math

    #def calc(x):
    #return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/math.html"
    driver = webdriver.Chrome()
    driver.get(link)
    #x_element = driver.find_element_by_css_selector("label > span")
    #y = x_element.text
    x = driver.find_element_by_id("input_value")
    x = x.text
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    #x_element = driver.find_element_by_id("input_value")
    #x = x_element.text
    #What is ln(abs(12*sin(x))), where x =  
    print(x)
    z = calc(x)
    print("Найдено1")
    answer = driver.find_element_by_id("answer")
    answer.send_keys(z)
    print("Вставлено")
    checkbox = driver.find_element_by_id("robotCheckbox")
    checkbox.click()
    print("Выбрано1")
    radiobutton = driver.find_element_by_id("robotsRule")
    radiobutton.click()
    print("Выбрано2")   
    button = driver.find_element_by_css_selector("button.btn")
    button.click()
	
finally:
	time.sleep(10)
	driver.quit()	