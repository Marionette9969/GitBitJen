from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


import time
import requests
import re

#   TELEGRAM TOKEN
TELEGRAM_BOT_TOKEN='bot7378325824:AAGP3baSLxnwYOaWXoBMgUisVwTNkAe1ok8'
CHAT_ID='6024022767'

#   SENDING MESSAGE TO TELEGRAM
def send_telegram_message(message):
    url = f'https://api.telegram.org/bot7378325824:AAGP3baSLxnwYOaWXoBMgUisVwTNkAe1ok8/sendMessage'
    params = {
        'chat_id':CHAT_ID,
        'text': message,
    }
    response = requests.get(url,params=params)
    print(f"Telegram API Response: {response.json()}")
    return response.json()

service = Service(executable_path=r"D:\Programmer Zaman Now\belajar-docker-master\Phyton\chromedriver.exe")
driver = webdriver.Chrome(service=service)

url ="https://spacelog.cygnuss-district8.com/"
driver.get(url)
element_id = "div_kafka"
    
#   RELOAD PAGE
try:
    while True:
        try:
            
            # Find the element by ID
            element = driver.find_element(By.ID, element_id)

            # Extract the text from the element
            element_text = element.text.strip() 

            #Remove non-numeric characters
            cleaned_text = re.sub(r'[^0-9.]', '', element_text)

            try:
                number_value = float(cleaned_text)  # Convert to float
                print(f"Kafka last message log speed : {number_value}")
            except ValueError:
                print(f"Could not convert text '{element_text}' to a number.")
                number_value = None

            # Check Number

            if number_value is not None and number_value > 0.75:
                message = f"Kafka Message {number_value} is greater than Usual, Personal Monitoring Advised"
                send_telegram_message(message)
                print(f"Message sent to Telegram Cronbot {message}")
            
                

        except Exception as e:
            print(f"Error occurred: {e}. Checking again...")

        driver.refresh()
        time.sleep(15)
        
        

except KeyboardInterrupt:
    print("Process interrupted by user.")

finally:
    
    driver.refresh()