from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


import time
import subprocess
import sys

def start_application():
    # Function to start application
    return subprocess.Popen([sys.executable,'WebDriverEra1.py'])

def monitor_application():
    # Restart if Stops
    while True:
        app_process = start_application()
        print(f"Application Started")
    
        app_process.wait()
        print(f"Application Paused")

        time.sleep(10)


if __name__ == "__main__":
    monitor_application()