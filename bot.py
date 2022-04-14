import pip
import telebot

from telebot import types

svao = 'СВАО'
yvao = 'ЮВАО'
yzao ='ЮЗАО'
szao ='СЗАО'
sao = 'САО'
zao = 'ЗАО'
vao = 'ВАО'
yao = 'ЮАО'
tsao ='ЦАО'
zelao = 'Зеленоградский АО'
nomao = 'Новомосковский АО'
troao = 'Троицкий АО'

bot = telebot.TeleBot('5207964829:AAGqzMZOAr3mVQJ1qOhPjyhaDWgXyN4Uiao')



@bot.message_handler(content_types=['text'])

def get_text_messages(message):
    if message.text == '/reg':
        keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
        key_1 = types.InlineKeyboardButton(text='Просвещение', callback_data='1'); #кнопка «1»
        keyboard.add(key_1); #добавляем кнопку в клавиатуру
        key_2= types.InlineKeyboardButton(text='Творчество', callback_data='2');
        keyboard.add(key_2);
        key_3 = types.InlineKeyboardButton(text='Просто отдых', callback_data='3');
        keyboard.add(key_3);
        question = 'Какой вид досуга вы бы хотели?';
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: 1)
def callback_worker(call):
    if call.data == "1":  # call.data это callback_data, которую мы указали при объявлении кнопки  код сохранения данных, или их обработки
        bot.send_message(call.message.chat.id, "Выберите из нижепредложенных   ЦАО    САО    СВАО    ВАО     ЮВАО    ЮАО    ЮЗАО    ЗАО    СЗАО  Зеленоградский АО Новомосковский АО Троицкий АО")
        def get_text_messages1(message):
            if message.text == "СВАО" or "свао":
                bot.send_message(message.from_user.id, "Вот доступные вам центры досуговой деятельности")
            elif message.text == "ЮВАО" or "ювао":
                bot.send_message(message.from_user.id, "Напиши привет")
            else:
                bot.send_message(message.from_user.id, "-.");
    elif call.data == "2":
         bot.send_message(call.message.chat.id, "Выберите из нижепредложенных  ЦАО    САО    СВАО    ВАО     ЮВАО    ЮАО    ЮЗАО    ЗАО    СЗАО  Зеленоградский АО Новомосковский АО Троицкий АО" );
    elif call.data == "3":
         bot.send_message(call.message.chat.id, 'Выберите из нижепредложенных  ЦАО    САО    СВАО    ВАО     ЮВАО    ЮАО    ЮЗАО    ЗАО    СЗАО  Зеленоградский АО Новомосковский АО Троицкий АО' );
    else:
                bot.send_message(call.message.chat.id, 'Напиши /reg')


bot.polling(none_stop=True, interval=0)