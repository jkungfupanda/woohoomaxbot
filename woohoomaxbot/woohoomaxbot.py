from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import date
import os
from selenium.webdriver.common.keys import Keys

PATH = "C:/Users/james/Desktop/msedgedriver.exe"  #will be wherever you have your microsoft edge driver downloaded
driver = webdriver.Edge(PATH)

email = "email@email12.com"  #put your email address in here
passwrd = "asdfasdfa"  #put your password in here

url = "https://www.facebook.com/" #input the the url where you are going to download the excel file

driver.get(url)


try:
    element = WebDriverWait(driver, 10).until(
         EC.presence_of_element_located( (By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input" ) ) and   #paste the FULL xpath of the login box
        EC.presence_of_element_located( (By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/input") )  #paste the FULL xpath of the password box
       
    )
    login = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input")  #paste the FULLxpath of the login box
    login.send_keys(email)
    password = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/input") #paste the FULL xpath of the password box
    password.send_keys(passwrd)
    password.send_keys(Keys.RETURN)  #this clicks enter after it has entered your email and password for you

except:
    print("could not click login or password button")
    time.sleep(10)

time.sleep(5) #wait to login



# first checkbox
# try:
#     element=WebDriverWait(driver,10).until(
#        EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/main/div[2]/div[1]/a"))     #paste the FULL xpath of the first checkbox
#    )
#     element.click()
# except:
#    print("could not click")
#    time.sleep(10)


# #second checkbox
# try:
#     element=WebDriverWait(driver,10).until(
#        EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/main/div[2]/div[1]/a"))    #paste the FULL xpath of the 2nd checkbox
#    )
#     element.click()
# except:
#    print("could not click")
#    time.sleep(10)


# #third checkbox
# try:
#     element=WebDriverWait(driver,10).until(
#        EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/main/div[2]/div[1]/a"))    #paste the FULL xpath of the 3rd checkbox
#    )
#     element.click()
# except:
#    print("could not click")
#    time.sleep(10)


# download excel file
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[1]/main/div[2]/div[1]/a")    #paste the FULL xpath of the button to download the excel file
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