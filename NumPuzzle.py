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
            #print('���������� ������ ����� �������! ��������:', num)
            return '�������: ' + str(n) + ' �������: ' + str(counter) + ' ������: ' + str(min(records)) + '. ��� ��� �������? ����� /start'
        elif n < num:
            return str('���������� ����� ������, ��� ' + str(n))
        else:
            return str('���������� ����� ������, ��� ' + str(n))
    except:
        return '��, �����-�� ������... �������� ����� /start'

@bot.message_handler(commands=["start"])
def start(m, res=False):
    global num
    global counter
    counter = 0
    num = random.randint(1, 1001)
    global num_first
    num_first = num
    bot.send_message(m.chat.id, '������, �������� ����� �� 1 �� 1000. �������, ����� - ������!')
    print('��������: ' + str(num) + ', ���������� ��� � ��������� ��������: ' + str(len(records)) + ', ��������� ����� �������:', min(records) if len(records) >= 1 else ' ��� �� ���� ���')

@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, compare(message.text))

    print('������� �����', counter, '�������:', message.text)
    if num_first != num:
        print('��������! ���� ���������� ������ ����� �������, ��������:', num)



bot.polling(none_stop=True, interval=0)