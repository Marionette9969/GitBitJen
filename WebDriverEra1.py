from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


import time
import requests
import re
import subprocess
import sys
import os



#   Start Application Process
def start_application():
    return subprocess.Popen([sys.executable,'WebDriverEra1.py'])

#   Restart Application Process
def monitor_application():
    while True:
        app_process = start_application()

        while app_process.poll() is None:
            time.sleep(30)

        print("Application Process stopped unexpected, Restarting Application")
        time.sleep(30)        


#   TELEGRAM TOKEN
TELEGRAM_BOT_TOKEN=os.getenv('TELEGRAM_BOT_TOKEN')

#TELEGRAM_BOT_TOKEN='bot7378325824:AAGP3baSLxnwYOaWXoBMgUisVwTNkAe1ok8'
CHAT_ID='6024022767'

#   SENDING MESSAGE TO TELEGRAM
def send_telegram_message(message):
    url = f'https://api.telegram.org/bot7378325824:AAGP3baSLxnwYOaWXoBMgUisVwTNkAe1ok8/sendMessage'
    params = {
        'chat_id':CHAT_ID,
        'text': message,
    }
    

    try:
        response = requests.get(url,params=params)
        response.raise_for_status()
        
        if response.json().get('ok'):
            print(f"Message sent to Telegram: {message}")
        else:
            print("Failed to send message:", response.json())
    
    except requests.exceptions.RequestException as e:
        print(f"Error sending message to Telegram: {e}")


service = Service(executable_path=r"D:\Programmer Zaman Now\belajar-docker-master\Phyton\chromedriver.exe")
driver = webdriver.Chrome(service=service) #options=chrome_options*//)

url ="https://spacelog.cygnuss-district8.com/"
driver.get(url)
element_id = "div_kafka"
    
#   RELOAD PAGE
try:
    
    while True:
        try:
            
            # Find the element by ID
            element = driver.find_element(By.ID, element_id)

            # Extract Chrome Element
            element_text = element.text.strip() 

            # Remove non-numeric characters
            cleaned_text = re.sub(r'[^0-9.]', '', element_text)  
            try:
                number_value = float(cleaned_text)  # Convert to float
                print(f"Extracted number: {number_value}")
            except ValueError:
                print(f"Could not convert text '{element_text}' to a number.")
            #number_value = None

            # Check Number

            if number_value is not None and number_value >= 0.25:
                message = f"Kafka Message {number_value} Exceed Allowed Point, Immediate Checking Advised"
                send_telegram_message(message)
                print(f"Message sent to Telegram: {message}")
            

        except Exception as e:
            print(f"Error occurred: {e}. Restarting Web Driver...")
         #   driver.close()
            driver.quit()
            break

        driver.refresh()
        time.sleep(15)
        
except KeyboardInterrupt:
    print("Process interrupted by user.")

finally:
    print("Application Stopped")

if  __name__ == "__main__":
    monitor_application()