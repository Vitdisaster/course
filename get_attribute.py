from selenium import webdriver
import time 
import math


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    driver = webdriver.Chrome()
    driver.get(link)

    pict = driver.find_element_by_id("treasure")
    x = pict.get_attribute("valuex")
    #x = x.text
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    print(x)
    z = calc(x)
    print("Найдено1")
    answer = driver.find_element_by_id("answer")
    answer.send_keys(z)
    print("Вставлено")
    