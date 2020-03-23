from selenium import webdriver
import time
import math

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element_by_id("input_value")
    x = x.text
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    print(x)
    z = calc(x)
    print("Найдено1")
    answer = browser.find_element_by_id("answer")
    answer.send_keys(z)
    print("Вставлено")
    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()
    print("Выбрано1")
    radiobutton = browser.find_element_by_id("robotsRule")
    radiobutton.click()
    print("Выбрано2")   
    #button = driver.find_element_by_css_selector("button.btn")
	#browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
finally:
	time.sleep(10)
	browser.quit()	