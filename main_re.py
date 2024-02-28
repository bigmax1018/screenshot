import telebot
from PIL import ImageGrab
import pyautogui
import time

# Telegram Bot Token
TOKEN = '7185979392:AAFNf7WyeiCTR5JaSTX07r5UrwWVbksEzbU'

# Channel ID where you want to send screenshots
CHANNEL_ID = '@foreardtester'

# Initialize the bot
bot = telebot.TeleBot(TOKEN)

# Function to capture screenshot
def capture_screenshot():
    # Use appropriate method to capture screenshot in Android
    screenshot = pyautogui.screenshot(region=(610, 100, 510, 900))  # Assuming you are running this script on a Windows machine
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
        # Check for new posts in DatChat (You need to implement this part)
        # if new_post_detected():
            # Capture screenshot
            screenshot = capture_screenshot()
            # Send screenshot to Telegram channel
            send_screenshot(screenshot)
            # Wait for some time before checking again
            time.sleep(60)  # Adjust the time interval as needed

# Entry point of the script
if __name__ == '__main__':
    main()