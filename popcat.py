from selenium import webdriver
import threading
import random
import time

ths=[]

def work(driver):
    while True:
        try:
            driver.find_element_by_xpath("/html/body/div[1]/div").click()
        except:
            i=0
for i in range(0,20):#number of threads
    try:
        driver = webdriver.Firefox()
        driver.get("https://popcat.click/")
        time.sleep(1)
        ths.append(threading.Thread(target=work, args=(driver)))
    except:
        err=1

for th in ths:
    th.start()
