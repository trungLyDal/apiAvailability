import requests
import time
from plyer import notification

def send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=10  # Notification will disappear after 10 seconds
    )

def check_api_availability():
    api_url = "https://platform.deepseek.com/api_keys"
    redirect_url = "https://chat.deepseek.com/503/"
    
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            print("API is available.")
        else:
            print(f"API returned status code: {response.status_code}. Redirecting to {redirect_url}")
            send_notification("API Unavailable", f"API returned status code: {response.status_code}. Redirecting to {redirect_url}")
            print("Try again later")
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}. Redirecting to {redirect_url}")
        send_notification("API Error", f"Error occurred: {e}. Redirecting to {redirect_url}")
        

def main():
    while True:
        check_api_availability()
        time.sleep(3600)

if __name__ == "__main__":
    main()