from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time
import datetime  
from datetime import date
import os
import glob
import os.path



PATH = "C:\Program Files (x86)\chromedriver.exe" #will be wherever you have your microsoft edge driver downloaded

driver=webdriver.Chrome(PATH)



# options = webdriver.ChromeOptions()

# prefs ={"download.default_directory":"C:/Users/james/Desktop/fiverr/woohoomaxbot"}

# options.add_experimental_option("prefs",prefs)

# driver = webdriver.Chrome(executable_path=PATH,chrome_options=options)




url = "https://filesamples.com/formats/xls#google_vignette"
# input your url in this string above ^^

driver.get(url)
# print(driver.title)




# options = webdriver.ChromeOptions()
# prefs = {"download.default_directory" : "C:\Users\james\Desktop\fiverr\woohoomaxbot"};
# #example: prefs = {"download.default_directory" : "C:\Tutorial\down"}
# options.add_experimental_option("prefs",prefs)




#first checkbox
# try:
#     element=WebDriverWait(driver,10).until(
#        EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/main/div[2]/div[1]/a"))
#    )
#     element.click()
# except:
#    print("could not click")
#    time.sleep(10)



# #second checkbox
# try:
#     element=WebDriverWait(driver,10).until(
#        EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/main/div[2]/div[1]/a"))
#    )
#     element.click()
# except:
#    print("could not click")
#    time.sleep(10)



# #third checkbox
# try:
#     element=WebDriverWait(driver,10).until(
#        EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/main/div[2]/div[1]/a"))
#    )
#     element.click()
# except:
#    print("could not click")
#    time.sleep(10)




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

nameOfFile = str(today)


# folder_path = r'path where your files are located'
# file_type = r'*type'
# files = glob.glob(folder_path + file_type)
# max_file = max(files, key=os.path.getctime)

# print(max_file)













time.sleep(5)

parentDir= "C:/Users/james/Desktop/fiverr/woohoomaxbot" #<< replace with the file path that you would like the folders downloaded to
newDailyDir = f"{parentDir}/{str(today)}"
os.mkdir(newDailyDir)

print("daily folder created")


time.sleep(10)

print("file moved")




old_name = r"C:/Users/james/Downloads/sample3.xls"



new_name = rf"{newDailyDir}/{nameOfFile}.xls"

os.rename(old_name, new_name)






#currentDirectory = os.getcwd() #<< replace os.getcwd with the file path that you would like the folders downloaded to (will be in Users unless you change it)
#dir = f"{currentDirectory}/{str(today)}"
# os.makedirs(str(today))

#print(currentDirectory)

# if not os.path.exists(dir):
#     #os.mkdir(dir)
    
#     print("directory created")

# print(str(today))




