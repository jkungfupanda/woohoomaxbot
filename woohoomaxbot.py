from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time
import datetime  
from datetime import date
from tkinter import *
from tkinter import ttk
import os



PATH = "C:\Program Files (x86)\chromedriver.exe" #will be wherever you have your microsoft edge driver downloaded
driver=webdriver.Chrome(PATH)


url = ""
# input your url in this string above ^^

driver.get(url)
# print(driver.title)








#first checkbox
try:
    element=WebDriverWait(driver,10).until(
       EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/main/div[2]/div[1]/a"))
   )
    element.click()
except:
   print("could not click")
   time.sleep(10)



#second checkbox
try:
    element=WebDriverWait(driver,10).until(
       EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/main/div[2]/div[1]/a"))
   )
    element.click()
except:
   print("could not click")
   time.sleep(10)



#third checkbox
try:
    element=WebDriverWait(driver,10).until(
       EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/main/div[2]/div[1]/a"))
   )
    element.click()
except:
   print("could not click")
   time.sleep(10)




#download excel file
try:
    element=WebDriverWait(driver,10).until(
       EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/main/div[2]/div[1]/a"))
   )
    element.click()
except:
   print("could not click")
   time.sleep(10)
















today = date.today()


currentDirectory = os.getcwd() #<< replace os.getcwd with the file path that you would like the folders downloaded to (will be in Users unless you change it)
dir = f"{currentDirectory}/{str(today)}"
# os.makedirs(str(today))

print(currentDirectory)

if not os.path.exists(dir):
    #os.mkdir(dir)
    
    print("directory created")

print(str(today))
