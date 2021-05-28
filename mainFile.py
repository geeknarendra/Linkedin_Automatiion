from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def get_in_to_account(user_name,user_pwd,no_of_request):
    #webdriver of firefox is being used, downlaod and use proper driver
    driver = webdriver.Firefox(executable_path="D:\Projects\Selinum\Driver\Mozilla\geckodriver-v0.29.1-win64\geckodriver.exe")

    #open Linkdin
    driver.get("https://in.linkedin.com/")

    #id login
    email = driver.find_element_by_id("session_key")        #email element
    time.sleep(5)
    email.send_keys(user_name)

    pwd = driver.find_element_by_id("session_password")     #password element
    time.sleep(5)
    pwd.send_keys(user_pwd)

    driver.find_element_by_xpath("/html/body/main/section[1]/div[2]/form/button").click()

    # close messages tab
    driver.find_elements_by_css_selector('.msg-overlay-bubble-header__controls.display-flex > *')[2].click()
    time.sleep(2)

    #My network
    driver.get("https://www.linkedin.com/mynetwork/")
    time.sleep(5)

    # Accept all incoming
    accept_buttons = driver.find_elements_by_css_selector('[aria-label^="Accept"]')
    for accept_button in accept_buttons:
        accept_button.click()
        time.sleep(3)

    #send request
    request_send=0
    # connect_buttons=driver.find_elements_by_css_selector("[aria-label^='Invite']")              #Invite send
    connect_buttons=driver.find_elements_by_css_selector("[aria-label^='Follow company']")      #follow company
    for connect_button in connect_buttons:
        connect_button.click()
        print("You are here")
        request_send+=1
        time.sleep(5)
        if request_send>=no_of_request:
            break

    driver.close()
    driver.quit()




if __name__=="__main__":

    username=input("Enter Username ")
    password=input("Enter Password ")
    no_of_connection=int(input("Enter number of Request you want to send "))

    if not username or not password or not no_of_connection:
        print(" Something is missing")

    #calling funtion
    get_in_to_account(username,password,no_of_connection)
    print("task Done")







