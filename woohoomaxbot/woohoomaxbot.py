from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import date
import os


PATH = "C:/Users/james/Desktop/msedgedriver.exe"  #will be wherever you have your microsoft edge driver downloaded
driver = webdriver.Edge(PATH)


url = "https://filesamples.com/formats/xls#google_vignette" #input the the url where you are going to download the excel

driver.get(url)


# first checkbox
# try:
#     element=WebDriverWait(driver,10).until(
#        EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/main/div[2]/div[1]/a"))     #paste the xpath of the first checkbox
#    )
#     element.click()
# except:
#    print("could not click")
#    time.sleep(10)


# #second checkbox
# try:
#     element=WebDriverWait(driver,10).until(
#        EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/main/div[2]/div[1]/a"))    #paste the xpath of the 2nd checkbox
#    )
#     element.click()
# except:
#    print("could not click")
#    time.sleep(10)


# #third checkbox
# try:
#     element=WebDriverWait(driver,10).until(
#        EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/main/div[2]/div[1]/a"))    #paste the xpath of the 3rd checkbox
#    )
#     element.click()
# except:
#    print("could not click")
#    time.sleep(10)


# download excel file
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[1]/main/div[2]/div[1]/a")    #paste the xpath of the button to download the excel file
        )
    )
    element.click()
except:
    print("could not click")
    time.sleep(10)


today = date.today()
nameOfFile = str(today)

time.sleep(5)

parentDir = "C:/Users/james/Desktop/fiverr/woohoomaxbot"  # replace with the file path that you would like the folders downloaded to
newDailyDir = f"{parentDir}/{str(today)}"
os.mkdir(newDailyDir)

print("daily folder created")

time.sleep(5)
print("file moved")

old_name = r"C:/Users/james/Downloads/sample3.xls"  #replace with your downloads file path and what the filename normally is when you download it
new_name = rf"{newDailyDir}/{nameOfFile}.xls"
os.rename(old_name, new_name)