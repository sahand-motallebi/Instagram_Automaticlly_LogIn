from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime
import time
import random

class instagram_Bot:

    # open webdriver(chrome)
    def __init__(self):
        self.driver = webdriver.Chrome()

    #save your record
    def save_Login_Account(self,username, password):
        time_recording = datetime.now().strftime("%Y-%m-%d | %H:%M:%S")
        with open('LoginAccount.txt', 'a') as f:
            f.write(f"{time_recording}\n username: {username}\nPassword: {password}\n")

    #get your username, password to login
    def get_Account(self):
        username = input("Enter your Instagram username: ")
        password = input("Enter your Instagram password: ")
        self.save_Login_Account(username, password)
        return username, password

    #Executive function
    def Login(self, bot, username, password):
        time_delay = random.randint(4,8)
        bot.get('https://www.instagram.com/accounts/login/')
        time.sleep(time_delay)

        try:
            element = self.driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[3]/div[2]/button")
            element.click()
        except NoSuchElementException:
            print("[INFO] - Bot not found element.")

        print("[INFO] - Logging in...")
        username_input = WebDriverWait(bot,time_delay).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
        password_input = WebDriverWait(bot,time_delay).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

        username_input.clear()
        username_input.send_keys(username)
        password_input.clear()
        password_input.send_keys(password)

        login_button = WebDriverWait(bot,time_delay).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
        login_button.click()
        
def main():

    bot = instagram_Bot()
    driver = bot.driver
    username, password = bot.get_Account()
    bot.Login(driver,username, password)
    time.sleep(10)

if __name__ == "__main__":
    main()