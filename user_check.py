from telegram import Update
from telegram.ext import Application, CallbackContext, CommandHandler, MessageHandler, ChatJoinRequestHandler, ChatMemberHandler, filters
import logging
import asyncio
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

import telebot



# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Your bot token
TOKEN = '7084909006:AAH4GzuOkuNVDcVroXt-4pm6gXAoVLJU7Qc'
bot = telebot.TeleBot(TOKEN)

# Dictionary to store kicked users and their respective channels
kick_members = {}
with open("kick_member_list.txt", "r") as file:
        kick_members = file.readlines()
channel_list = {}
with open("channel_list.txt", "r") as file:
        channel_list = file.readlines()
print(channel_list)
# Function to kick user from specified channels
def handle_special_channel_kick(update: Update, context: CallbackContext) -> None:
    # Check if the kick happened in the special channel
    bot.send_message('@my_test_group_kk', 'nice')
    if update.effective_chat.id in channel_list:
        kicked_user_id = update.effective_user.id
        print(kicked_user_id + 'kicked')
        # Iterate through other special channels and kick the user
        for channel_id in channel_list:
            bot.kick_chat_member(channel_id, kicked_user_id)
        # Add the user to the kick member list
        with open("kick_member_list.txt", "a") as file:
            file.write(str(kicked_user_id) + "\n")

# Function to reject user when kicked someone rejoin
def reject_rejoined_users(update: Update, context: CallbackContext) -> None:
    bot.send_message('@my_test_screenshot', 'nice')
    rejoined_user_id = update.effective_user.id
    # Check if the rejoined user is in the kick member list
    with open("kick_member_list.txt", "r") as file:
        kick_members = file.readlines()
        if str(rejoined_user_id) + "\n" in kick_members:
            bot.kick_chat_member(update.effective_chat.id, rejoined_user_id)

async def error(update: Update, context: CallbackContext):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    application = Application.builder().token("7084909006:AAH4GzuOkuNVDcVroXt-4pm6gXAoVLJU7Qc").build()
    
    application.add_handler(ChatMemberHandler(handle_special_channel_kick, ChatMemberHandler.MY_CHAT_MEMBER))
    application.add_handler(ChatJoinRequestHandler(reject_rejoined_users))
    # application.add_handler(CommandHandler('nice', bot.send_message('@my_test_screenshot', 'nice')))
    application.run_polling()

if __name__ == '__main__':
    main()
