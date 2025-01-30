import requests
import time
from plyer import notification
import datetime

def send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=10  
    )

# Define counter as a global variable
counter = 0

def check_api_availability():
    global counter  # Use the global counter variable
    api_url = "https://platform.deepseek.com/api_keys"
    redirect_url = "https://chat.deepseek.com/503/"
    current_time = datetime.datetime.now()
    
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            print("API is available." + " Current time: ", current_time, counter + 1)
            counter += 1
        else:
            print(f"API returned status code: {response.status_code}. Redirecting to {redirect_url}")
            send_notification("API Unavailable", f"API returned status code: {response.status_code}. Redirecting to {redirect_url}")
            print("Try again later. Current time: ", current_time, counter + 1)
            counter += 1
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}. Redirecting to {redirect_url}")
        send_notification("API Error", f"Error occurred: {e}. Redirecting to {redirect_url}")

def main():
    while True:
        check_api_availability()
        time.sleep(1800)

if __name__ == "__main__":
    main()