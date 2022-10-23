import telebot
import random
token = '5648661356:AAE0g0zuglFNYwpSq6tElTBDlZOMsSzJPpg'
bot = telebot.TeleBot(token)
records = []
def compare(n):
    global counter
    counter += 1
    global num
    try:
        n = int(n)
        if n == num:
            records.append(counter)
            num = random.randint(1, 1001)
            #print('продолжает играть после отгадки! загадано:', num)
            return 'Отгадка: ' + str(n) + ' Попыток: ' + str(counter) + ' Рекорд: ' + str(min(records)) + '. Еще раз сыграем? введи /start'
        elif n < num:
            return str('Загаданное число больше, чем ' + str(n))
        else:
            return str('Загаданное число меньше, чем ' + str(n))
    except:
        return 'Хм, какая-то ошибка... попробуй снова /start'

@bot.message_handler(commands=["start"])
def start(m, res=False):
    global num
    global counter
    counter = 0
    num = random.randint(1, 1001)
    global num_first
    num_first = num
    bot.send_message(m.chat.id, 'Привет, загадано число от 1 до 1000. Отгадай, какое - напиши!')
    print('загадано: ' + str(num) + ', количество игр с последней загрузки: ' + str(len(records)) + ', рекордное число попыток:', min(records) if len(records) >= 1 else ' еще не было игр')

@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, compare(message.text))

    print('попытка номер', counter, 'введено:', message.text)
    if num_first != num:
        print('отгадано! если продолжает играть после отгадки, загадано:', num)



bot.polling(none_stop=True, interval=0)