import telebot
import datetime
from telebot import types
import os

# Ваш API токен, который вы получили от BotFather
API_TOKEN = '6501807348:AAHEgCN9TterDizGWO4nr3-FTSTs7Yf1-F4'  # Замените на свой API токен

    
# Создайте объект бота
bot = telebot.TeleBot(API_TOKEN)

# Словарь для отслеживания состояния пользователей
user_state = {}
# Обработчик для команды /start
@bot.message_handler(commands=['start'])
def welcome(message):
    if message.chat.id in user_state and user_state[message.chat.id] == "waiting_for_code":
        bot.send_message(message.chat.id, "You are already in the process of entering the code. Please enter the code.")
        return

    if message.text == "/start":
        welcome_message =  "🔞 18 + ONLY🔞\n"
        welcome_message += "❗ Subcrubing to the Group you Going to get New Sexual Fetishes\n\n"
        welcome_message += " or Feed an existing ones... \n\n"
        welcome_message += "\n\n"
        welcome_message += "🔴1. 200+ minutes of Short (<1 min) Sissy, Cuckold, Goon Captions\n\n"
        welcome_message += "⚫2. 25 long (15>min) Sissy Stories, Trainings, PMVs \n\n"
        welcome_message += "🔴3. Chats on Topics\n\n"
        welcome_message += "⚫4. 30 Categorized Tabs = Comfort Viewing\n\n"
        welcome_message += "🔴5. Constant Updates\n\n"
        welcome_message += "\n\n"
        welcome_message += "❓ ACCESS IS PAID - YOU CAN GET IT BY FOLLOWING THE INSTRUCTIONS BELOW\n\n"
        welcome_message += "❗ACCESS IS VALID AS LONG AS SUBSCRIPTION VALID❗\n\n"
        welcome_message += "❗ You need Mobile, Web or Desktop Telegram App to view❗\n\n"
        welcome_message += "1️⃣ Choose Platform for paying - Ko-Fi or Patreon\n\n"
        welcome_message += "2️⃣ Click the button bellow\n\n"
        welcome_message += "3️⃣ Choose and Buy Tier in Patreon or make a Tip in Ko-Fi\n\n The Prices don't offer any advantages\n\n"
        welcome_message += "4️⃣ After Purchasing Check The Pinned Post in Ko-Fi or Patreon Feeds\n\n" 
        welcome_message += "5️⃣ You will see 4 Digit Code\n\n"
        welcome_message += "6️⃣ Send Message IN THE MESSAGE ENTRY BAR AT THE BOTTOM (just 4 digits, no more) with 4 digit Code from Patreon or Ko-Fi right to this Bot, Bot will Send You invite to the Private Group in answer\n\n"
        welcome_message += "❓IF ANYTHING GOES WRONG, PRESS THE (ASK ME) BUTTON TO DIALOG WITH ME❓"
        welcome_message += "\n\n"
       
                
        # Создаем инлайн-клавиатуру с кнопками
        markup = types.InlineKeyboardMarkup()
        ko_fi_button = types.InlineKeyboardButton("KO-FI", url="https://ko-fi.com/nowaystraight")
        patreon_button = types.InlineKeyboardButton("PATREON", url="https://www.patreon.com/nowaystraight")
        message_me_button = types.InlineKeyboardButton("ASK ME (Answer from 4 A.M. to 4 P.M UTC)", url="t.me/nwsprofile")
        markup.row(ko_fi_button, patreon_button)
        markup.row(message_me_button)

        # Отправляем сообщение с ссылками на Патреон и Ko-Fi
        bot.send_message(message.chat.id, welcome_message)
        bot.send_message(message.chat.id, "😵‍💫🔒😵‍💫IT FEELS MUCH MORE BETTER WHEN YOU PAY😵‍💫🔒😵‍💫\n\n THE BOT SILENCE CAN BE FIXED BY THE BOT RESTARTING", reply_markup=markup)# Создаем инлайн-клавиатуру с кнопками
        
        # Устанавливаем состояние ожидания ввода кода для пользователя
        user_state[message.chat.id] = "waiting_for_code"
    else:
        bot.send_message(message.chat.id, "❌I don't understand this command. Please use the /start command to begin❌")

# Обработка ввода кода
@bot.message_handler(func=lambda message: message.chat.id in user_state and user_state[message.chat.id] == "waiting_for_code")
def check_code(message):
    if message.text == "5646":
        user = message.from_user
        full_name = user.first_name
        if user.last_name:
            full_name += " " + user.last_name

        bot.send_message(message.chat.id, "✅Code Is Correct. Here is the link✅:")
        bot.send_message(message.chat.id, "Group - https://t.me/+oTcfMQBFODViYmNi", disable_web_page_preview=True)
        
        # Сохраняем данные о пользователе в текстовый файл с датой и временем
        current_time = datetime.datetime.now()
        user_data = f"Timestamp: {current_time}, User ID: {user.id}, Name: {full_name}, Username: {user.username}"
        with open('user_mapping.txt', 'a') as file:
            file.write(user_data + '\n')
        
        # Сбрасываем состояние ожидания
        user_state[message.chat.id] = None
    else:
        bot.send_message(message.chat.id, "❌Code Is Incorrect. Please enter the correct code. Maybe the Code Has Been Changed, check the Code in Patreon or Ko-Fi❌")


# Запуск бота
if __name__ == "__main__":
        bot.polling(none_stop=True, timeout=300)