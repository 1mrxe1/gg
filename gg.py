import telebot
from telebot import types

API_TOKEN = "6208795820:AAEF_NcBlSVdc-hj16WyWSXsNL9TPQUc0xs"
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    btn = telebot.types.InlineKeyboardButton("🔗", url="https://t.me/finalv1")
    markup.add(btn)    
    bot.send_message(message.chat.id, "- أهلا عزيزي في بوت حذف اشعارات الإنضمام في المجموعات .", reply_markup=markup)
        
@bot.message_handler(content_types=['new_chat_members'])
def delete_join_message(message):
    try:
        bot.delete_message(message.chat.id, message.message_id)
    except Exception as e:
        print(f"Error: {e}")
bot.infinity_polling()
