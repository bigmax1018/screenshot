import telebot
from PIL import ImageGrab, Image
import pyautogui
import time
import io

# Telegram Bot Token
TOKEN = '7042651707:AAFeKArSV9cufcmZD0ZXygha_9g6ZV6pV84'

# Channel ID where you want to send screenshots
CHANNEL_ID = '@my_test_screenshot'

# Initialize the bot
bot = telebot.TeleBot(TOKEN)

# Function to capture screenshot
def capture_screenshot():
    # Use appropriate method to capture screenshot in Android
    # screenshot = pyautogui.screenshot(region=(620, 100, 540, 900))  # Assuming you are running this script on a Windows machine
    screenshot = pyautogui.screenshot(region=(25, 100, 540, 930))
    return screenshot

# Function to send screenshot to Telegram channel
def send_screenshot(screenshot):
    # Save the screenshot locally (optional)
    screenshot.save('screenshot_re.png')
    # Send the screenshot to the Telegram channel
    with open('screenshot_re.png', 'rb') as photo:
        bot.send_photo(CHANNEL_ID, photo)

# Main function to continuously monitor for new posts and send screenshots
def main():
    while True:
        # Check for new posts in 
        # DatChat (You need to implement this part)
        # if new_post_detected():
            # Capture screenshot
            screenshot = capture_screenshot()
            # Send screenshot to Telegram channel
            with open('screenshot_re.png', 'rb') as photo_re:
                 screenshot_bytes = io.BytesIO()
                 screenshot.save(screenshot_bytes, format='PNG')
                 if screenshot_bytes.getvalue() != photo_re.read():
                    send_screenshot(screenshot)
                 else:
                    print("Screenshots are the same.")
            # Wait for some time before checking again
            # time.sleep(1)  # Adjust the time interval as needed

# Entry point of the script
if __name__ == '__main__':
    main()