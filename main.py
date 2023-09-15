import telebot
import asyncio
import time
from telebot import types
bot = telebot.TeleBot("6229862030:AAFrhAkX4qyYHOxQjDfpBEaHH71Mzixq-iI")

nick = []
money = 1
money_user = []
doxod = 1
aksesuar = []
eda = 0
banan = 10
palka = 200
golden = 15000
palima = 100000
gorila = 5000
samka = 100000

@bot.message_handler(commands = ["start","старт","Старт","Start"])
def zapusk(message):
    bot.send_message(message.chat.id, f'==============\nПривет, я игровой бот Gorilla 😊.'
                                      f'\nЭто развлекательный бот, в котором вы можете "убить свое время", а так же веселится👌.'
                                      f'\nПожалуйста, ознакомтесь с ботом в "Помощь📋".'
                                      f'\nЕсли у вас не появились кнопки, то пропишите "Магазин".'
                                      f'\nЭто не проблема программиста, а самого месседжера.'
                                      f'\nПриятной игры,{message.from_user.username}\n==============')
    bot.register_next_step_handler(message, get_name)

@bot.message_handler(commands = ["start","старт","Старт","Start"])
def menu(message):
    WTC = 0
    FTC = 0
    money = 1
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Магазин') #Кнопка открывает мазагин с аксессуарами
    item2 = types.KeyboardButton('Покормить Гориллу🍽') #Кнопка восстанавливает рейтинг
    item3 = types.KeyboardButton('Поиграть с гориллой⚽') #Кнопка добавляет деньги и рейтинг
    item4 = types.KeyboardButton('Профиль🐵') #Выводит профиль игрока
    item5 = types.KeyboardButton('Помощь') #Выводит функционал бота
    markup.add(item1, item2, item3, item4, item5)
    bot.send_message(message.chat.id,text = 'Выполнено',reply_markup=markup)

@bot.message_handler()
def bot_message(message):
        global money
        global doxod
        global aksesuar
        global eda
        global banan
        global palka
        global gold
        global palima
        global gorila
        global samka
        global money_user

        if message.text == 'Магазин':
            n = open('C:\личное\Bot_Telegram\photo\Магазин.jpg', 'rb')
            bot.send_photo(message.chat.id,photo= n,caption='\n=========================='
                                             '\n'
                                             '\nАксессуары для вашей Гориллы:'
                                              f'\nБанан🍌: Стоимость {banan} монет, увеличивает доход на 1 монеты.\n'
                                               '\nПалка🪵: Стоимость - 200 монет, увеличивает доход на 10 монеты.\n'
                                               '\nЗолотой банан🌙: Стоимсоть - 15000 монет, увеличивает доход на 100 монет.\n'
                                               '\nПальма с бананами🌴🍌: Стоимтость - 100000 монет, увеличивает доход на 1000 монет.\n'
                                               '\nЭнергия гроилы" Стоимость 500 монет, увеличивает доход в 2 раза на 5 минут\n'
                                               '\nСамка горилы: Стоимость 350000 монет, увеличивает доход в 2 раза'
                                               '\n'
                                               '\n=========================='                             )
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Банан🍌')
            item2 = types.KeyboardButton('Палка🪵')
            item3 = types.KeyboardButton('Золотой банан🌙')
            item4 = types.KeyboardButton('Пальма с бананами🌴🍌')
            item5 = types.KeyboardButton('Энергия гориллы')
            item6 = types.KeyboardButton('Самка гориллы')
            back = types.KeyboardButton('назад🔙')
            markup.add(item1, item2, item3,item4,item5,item6, back)
            bot.send_message(message.chat.id,'Успешно',reply_markup=markup)

        if message.text == 'Банан🍌':
            telegram_id = str(message.from_user.id)
            if money >= 10:
                n = open('C:\личное\Bot_Telegram\photo\На покупку банана.jpg','rb')
                bot.send_photo(message.chat.id, photo=n,caption='Банан🍌 успешно приобретена.')
                aksesuar.append('Банан🍌')
                money -= 10
                banan *= 2
                doxod += 1
            else:
                n = open('C:\личное\Bot_Telegram\photo\На покупку банана.jpg','rb')
                bot.send_photo(message.chat.id, photo=n, caption='К сожалению у вас не хватает средств💵 на покупку данного замечательного артефакта😭.')


        if message.text == 'Палка🪵':
            telegram_id = str(message.from_user.id)
            if money >= 200:
                n = open('C:\личное\Bot_Telegram\photo\Палка.jpg', 'rb')
                bot.send_photo(message.chat.id, photo=n, caption='Палка🪵 успешно приобретена.')
                aksesuar.append('Палка🪵')
                money -=200
                doxod += 10
            else:
                n = open('C:\личное\Bot_Telegram\photo\Палка.jpg', 'rb')
                bot.send_photo(message.chat.id, photo=n, caption='К сожалению у вас не хватает средств💵 на покупку данного замечательного артефакта😭.')

        if message.text == 'Золотой банан🌙':
            telegram_id = str(message.from_user.id)
            if money >= 15000:
                n = open('C:\личное\Bot_Telegram\photo\На золотой банан.jpg', 'rb')
                bot.send_photo(message.chat.id, photo=n, caption='Золотой банан🌙 успешно приобретен.')
                aksesuar.append('Золотой банан🌙')
                money -=15000
                doxod += 100
            else:
                n = open('C:\личное\Bot_Telegram\photo\На золотой банан.jpg','rb')
                bot.send_photo(message.chat.id, photo=n, caption='К сожалению у вас не хватает средств💵 на покупку данного замечательного артефакта😭.')

        if message.text == 'Пальма с бананами🌴🍌':
            telegram_id = str(message.from_user.id)
            if money <= 100000:
                n = open('C:\личное\Bot_Telegram\photo\пальма с бананами.jpg',
                         'rb')
                bot.send_photo(message.chat.id, photo=n,caption='Пальма с бананами🌴🍌успешно приобретена.')
                aksesuar.append('Пальма с бананами🌴🍌')
                money += 100000
                doxod += 1000
            else:
                n = open('C:\личное\Bot_Telegram\photo\пальма с бананами.jpg', 'rb')
                bot.send_photo(message.chat.id, photo=n, caption='К сожалению у вас не хватает средств💵 на покупку данного замечательного артефакта😭.')

        if message.text == 'Энергия горилы':
            telegram_id = str(message.from_user.id)
            if money >= 500:
                n = open('C:\личное\Bot_Telegram\photo\Аксессуар кофе.jpg', 'rb')
                bot.send_photo(message.chat.id, photo=n, caption='Вы успешно купили горилу')
                money -= 500
                doxod *= 1.25
            else:
                n = open('C:\личное\Bot_Telegram\photo\Аксессуар кофе.jpg', 'rb')
                bot.send_photo(message.chat.id, photo=n, caption='К сожалению у вас не хватает средств💵 на покупку данного замечательного артефакта😭')

        if message.text == 'Самка горилы':
            telegram_id = str(message.from_user.id)
            if money >= 100000:
                n = open('C:\личное\Bot_Telegram\photo\самка.jpg','rb')
                bot.send_photo(message.chat.id, photo=n, caption='Самка успешно приобретена')
                money -= 100000
                doxod*= 2
            else:
                n = open('C:\личное\Bot_Telegram\photo\самка.jpg', 'rb')
                bot.send_photo(message.chat.id, photo=n, caption='К сожалению у вас не хватает средств💵 на покупку данного замечательного артефакта😭')
        if message.text == 'назад🔙':
            menu(message)

        if message.text == 'Покормить Гориллу🍽':
            n = open('C:\личное\Bot_Telegram\photo\Покормить гориллу.jpg', 'rb')
            bot.send_photo(message.chat.id, photo=n,caption='Ваша горилла теперь сыта🙊.\nВы можете играть с ней!')
            eda = 100000


        if message.text == 'Поиграть с гориллой⚽':
               n = open('C:\личное\Bot_Telegram\photo\Если горилла голодает.jpg','rb')
               bot.send_photo(message.chat.id, photo=n)
               bot.send_message(message.chat.id,'Ваша Горилла голодна🙊, покормите ее!!!') #Вывод ошибки в случае, если энергия закончилась.
               time.sleep(5)
           else:
                n = open('C:\личное\Bot_Telegram\photo\Поиграть с гориллой.jpg','rb')
                bot.send_photo(message.chat.id, photo=n, caption= f'Вы успешно поиграли с Гориллой, она слегка улыбается 🐒\nВам начисленно {doxod}💎, всего у вас {money} 💎')
                money += doxod


        if message.text == 'Профиль🐵':
            dlina = len(aksesuar)
            n = open('C:\личное\Bot_Telegram\photo\На профиль.jpg', 'rb')
            bot.send_photo(message.chat.id, photo=n,caption=f'Ваш рейтинг в игре: {money}\nВаши аксессуары:{dlina}')

        elif message.text == 'Помощь':
            n = open('C:\личное\Bot_Telegram\photo\Помощь.jpg', 'rb')
            bot.send_photo(message.chat.id, photo=n, caption='Информация о боте:\n1.Нажимая на кнопку поиграть с Гориллой⚽ вы получаете рейтинг🏆 и деньги💎.'
                                             '\n\n2.Ваши деньги = вашему рейтингу, чем вы богаче, тем вы успешнее.'
                                             '\n\n3.В профиле вы можете увидеть ваш рейтинг и деньги, а так же аксессуары, которые у вас есть🐵.'
                                             '\n\n4.Для увеличения вашего дохода вы можете купить аксессуары для вашей Гориллы.'
                                             '\n\n5.Для игры с Гориллой вам нужно ее кормить🍽.')

        while time.time() == True:
            eda -= 1


def get_name(message):
    telegram_id = str(message.from_user.id)
    global user_name, nick
    user_name = message.text


while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)
        time.sleep(5)
