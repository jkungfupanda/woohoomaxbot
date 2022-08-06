from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import date
import os


def main():

    # will be wherever you have your microsoft edge driver downloaded
    PATH = "C:/Users/james/Desktop/msedgedriver.exe"  
    driver = webdriver.Edge(PATH)

    # put your email address in here
    login_email = "email@email12.com"  

    # put your password in here
    login_password = "asdfasdfa"  

    # input the the url where you are going to download the excel file
    url = "https://www.facebook.com/" 
    driver.get(url)

    # login to the website
    try:
        # paste the FULL xpath of the login box here
        login_box = "/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input"

        # paste the FULL xpath of the password box here 
        password_box = "/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/input"

        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, login_box) and (By.XPATH, password_box))
        )

        login = driver.find_element(By.XPATH, login_box)
        login.send_keys(login_email)
        password = driver.find_element(By.XPATH, password_box)
        password.send_keys(login_password)

        # this clicks enter after it has entered your email and password for you
        password.send_keys(Keys.RETURN)

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
        xcel_file = "/html/body/div[1]/main/div[2]/div[1]/a"
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, xcel_file)
            )
        )
        element.click()
    except:
        print("could not click on the excel file")
        time.sleep(10)

    today = date.today()
    nameOfFile = str(today)

    time.sleep(5)

    # replace with the file path that you would like the folders downloaded to
    parentDir = "C:/Users/james/Desktop/fiverr/woohoomaxbot"  
    newDailyDir = f"{parentDir}/{str(today)}"
    os.mkdir(newDailyDir)

    print("daily folder created")

    time.sleep(5)
    print("file moved")

    # replace with your downloads file path and what the filename normally is when you download it
    old_name = r"C:/Users/james/Downloads/sample3.xls"
    new_name = rf"{newDailyDir}/{nameOfFile}.xls"
    os.rename(old_name, new_name)


if __name__ == "__main__":
    main()
