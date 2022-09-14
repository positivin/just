# задача из контрольной: по введенному знаку исполнить соответствущую операцию над двумя числами
import operator as op
def arithmetic_operation(s):
    dic = {'+': (lambda x, y: op.add(x,y)), '-': (lambda x, y: op.sub(x, y)), '*': (lambda x, y: op.mul(x, y)), '/': (lambda x, y: op.truediv(x, y))}
    return dic[s]

add = arithmetic_operation('+')
div = arithmetic_operation('/')
print(add(10, 20))
print(div(20, 5))

# экстракция из текстового файла множества слов наиболее близко соответствующих маске, в примере - слова из 5 букв, содержащих максимум разнообразия английских гласных
import string # здесь мне нужен, чтобы обратиться к списку знаков пунктуации - готовый список знаков к удалению из текста
with open('English.txt','r') as readfile:  # файл с исходным текстом содержащим списки английских слов
    with open('exampleY.txt','w') as writefile:
        for line in readfile:
                writefile.write(line)  # для подстраховки копирую в новый файл, чтобы курочить там

with open('exampleY.txt') as text:
    t = text.read()  # создаю строковую переменную с исходным текстом
f_del ='»' + string.punctuation + '«' + '‘' + '’' # в пунктуационном списке библиотеки стринг почему-то не все такие знаки, например, нет кириллических кавычек
for i in f_del:
    if i in t:
        t = t.replace(i, '')        # удаляю из строковой переменной всю пунктуацию, чтобы она не влияла на дилну слов    
t = t.lower().split()  # разбиваю строковую переменную на слова и превращаю ее в списочную переменную

maska ='aeiouy' # эти буквы должны сформировать целевое слово
num = 5  # длина целевого слова
t = {i: sum((j in i) for j in maska) for i in t if len(i) == num}  # суть алгоритма тут: sum((j in i) for j in maska) - подсчетом True выдает количество в слове разных букв из маски 

m = max(t.values())
out = list({i: j for i, j in t.items() if j == m}.keys())  # мне нужны только слова в которых максимально разнообразно представлены буквы из маски
out = sorted(out)  # формирую итоговый список слов по алфавиту

with open('exampleY.txt','w') as writefile:
    for i in "\n".join(out):      # просто так, без ухищрения с join, итоговый список слов почему-то записывается в текстовый файл сплошной строкой
        writefile.write(i)
print('отсортированное по алфавиту множество из', len(out), 'слов в', num, 'букв максимально разнообразных по', maska, 'сохранен в файл exampleY.txt')

# открытие и редактирование текстового файла https://istories.media/workshops/2021/01/29/vvedenie-v-python-chast-11-rabota-s-failami/
with open('C:\\Users\\PS\\Desktop\\Eesti.txt') as f:
    #data = f.readlines() - превращает весь текст в список строк, если активировать, то дальнейшее применение метода read() оказывается невозможным
    #data = f.readline()  - возвращает строку: набор символов до (символа конца строки  - пишет степик, но до точки, на практике, если она не в кавычках), если поставить в скобках положительное число, меньшее длины строки то длина выданной строка окажется равной этому числу, а следующая строка в выдаче этой функцией пойдет с позиции следующего символа, если число поставить больше длины строки, вернется все равно строка до точки.
    d_ata = f.read()  # возвращает текст единой строкой дальше в примере работаю с этой строкой
    
# data[0] = data[0].replace('Д','К') - демонстрирую обычную работу со списками и со строками

with open('text_test.txt', 'w') as tf:
    tf.write(d_ata[d_ata.find('В случае'):].strip())
with open('text_test.txt', 'a') as tf:
    tf.write('\nСпасибо за внимание!\n')

with open('C:\\Users\\PS\\Desktop\\Eesti.txt') as f:
    data = f.readlines()    
with open('text_test.txt', 'a') as tf:
    tf.writelines(i for i in data[8:12])
with open('text_test.txt') as tf:
        print(tf.read())

# функция замены подстрок строки на случайные элементы

def generate_index():
    import string
    import random
    a = 'LetterLetterNumber_NumberLetterLetter' # входящая строка к замене
    s = {'Letter': (string.ascii_uppercase), 'Number': range(0, 100)}  # словарь заменяемых подстрок
    for k, v in s.items():
        while k in a:                      
            a = a.replace(k, str(random.choice(v)), 1)  # единица здесь самая мякотка: если без нее, то все вхождения одного и того же ключа словаря в строке заменятся одним и тем же сгенерированным значением, а не разными
    return a
print(generate_index())

# массив данных о покупках (покупатель товар количество) выводится по покупателям
s = {}
for i in range(int(input())):
    a, b, c = input().split() # по условиям задачи на входе строки "покупатель товар количество"
    s.setdefault(a, {})  # инициализирую ключ (для имен покупателей) со значением словарь (для названий товаров)
    s[a].setdefault(b, int()) # инициализирую ключ со значением целое число (для количества товаров)
    s[a][b] += int(c) # суммирую по ключу со значением целого числа (количества товаров)

for k, v in sorted(s.items()):  # по условиям задачи сначала выводится покупатель на следующих строках товары с их количеством
    print(f'{k}:')
    a = sorted(v.items())
    for j in a:
        print(*j)

# собрание в один словарь всех словарей списка
def merge(lst):
    a = {}
    for i in lst:
        for k, v in i.items():
            a.setdefault(k, set())
            a[k].add(v)
    return a

# самое частое слово
s = input('введи текст: ').split() 

s = {i: s.count(i) for i in s}
print(f'чаще всего встречается, в алфавитном порядке, слово "{min([i for i in s if s[i] == max(s.values())])}"')

# перевести символы строки в нажатия кнопочным телефоном
s = ('''1	.,?!:
2	ABC
3	DEF
4	GHI
5	JKL
6	MNO
7	PQRS
8	TUV
9	WXYZ''').split()
ss = []
s.extend(['0', ' ']) # создан список для словаря
ss = {s[i]: s[i+1] for i in range(0, len(s), 2)} # словарь с ключами по цифрам
ss.update({s[i+1][j]: s[i] for i in range(0, len(s), 2) for j in range(len(s[i+1]))})  # словарь дополнен словарем с ключами по символам (буквам)

n = list(input('введи текст для набора на кнопочном телефоне латиницей: ').upper()) 
res = ''
for i in n:
    if i in ss:
        res += ss[i] * (ss[ss[i]].find(i) + 1)  # ищет в словаре по букве какую цифру нажимать (строковая цифра) и строчно умножает ее на индекс буквы в словаре по цифре (плюс один)

print(res)


# принимает числовые строки и возвращает (отсортированные по возрастанию) множества чисел
n = int(input('укажи количество строк с числами для ввода: '))  
print('при вводе ожидаются строки чисел через пробел')
n = [frozenset([int(j) for j in input().split()])for i in range(n)]  # заметь, что здесь необходим именно frozenset, чтобы работать с одним и тем же списком одних и тех же множеств 
m_inion = set()
for i in n:
    m_inion |= i

index_ = int(input('''укажи индекс (номер считая с нуля) строки, 
в которой нужно оставить только уникальные элементы, 
не встречающиеся в остальных строках: '''))

m_dif = []
for i in n:
    m_dif.append(i)
m_dif[0], m_dif[index_] = m_dif[index_], n[0]
for i in range(1, len(m_dif)):
    m_dif[0] -= m_dif[i]

m_inter = n[0]

for i in n:
    m_inter &= i

print('вот исходный список множеств: ', n)   
print('вот множество всех чисел: ', *sorted(m_inion))
print('вот множество всех общих чисел: ', *sorted(m_inter))
print(f'вот множество всех уникальных чисел строки с индексом {index_}: ', *sorted(m_dif[0])) 


# удаление из слов в тексте разных знаков ну и до кучи подсчет количества разных слов 
n = input().lower().split()
for_del = list('.,;:-?!)(')  # это список знаков, которые нужно удалить из текста
s = set()
for i in range(len(n)):
    for j in for_del:
        while j in n[i]:
            n[i] = n[i].replace(j, '')
    s.add(n[i])
print(*n)  # имей в виду, что все слова будут выведены в нижнем регистре
print(len(s))  # количество разных слов в тексте

# суммы в сегментах диагоналей матрицы
n = int(input())
m = []
for i in range(n):
    m.append([int(x) for x in input().split()])
total_up = 0
total_r = 0
total_low = 0
total_l = 0

for i in range(n):
    for j in range(n):
        if i < j and i < n - j - 1:
            total_up += m[i][j]
        elif i < j and i > n - j - 1:
            total_r += m[i][j] 
        elif i > j and i > n - j - 1:
            total_low += m[i][j]  
        elif i > j and i < n - j - 1:
            total_l += m[i][j]         
print(f'Верхняя четверть: {total_up}', f'Правая четверть: {total_r}', f'Нижняя четверть: {total_low}', f'Левая четверть: {total_l}', sep='\n')            

# пример с тремя множествами
n, m, k, x, y, z, t, aa = int(input('мощность первого множества: ')), int(input('мощность второго множества: ')), int(input('мощность третьего множества: ')), int(input('мощность объединенного OR первого-второго множеств: ')), int(input('мощность объединенного OR второго-третьего множеств: ')), int(input('мощность объединенного OR первого-третьего множеств: ')), int(input('мощность первого AND второго AND третьего множеств: ')), int(input('мощность универсального множества: '))
a = n + m - x - t
b = m + k - y - t
c = n + k - z - t
n_ = n - a - t - c
m_ = m - a - t - b
k_ = k - b - t - c
s = (a, b, c, n_, m_, k_, t)
s = sum(s)
print(f'мощность множества состоящих только в каком-то одном из исходных множеств (прочитавших только 1 из 3х книг): {n_ + m_ + k_}')
print(f'мощность множества состоящих сразу в двух из исходных множеств (прочитавших по 2-е из 3х книг): {a + b + c}')
print(f'мощность множества состоящих из не входящих ни в одно из исходных множеств (не прочитавших книг): {aa - s}') 

# пример работы кортежами - "числа трибоначчи"
n = int(input())
a, b, c = 1, 1, 1  # вариант без накопления значений в кортеж
for i in range(n):
    print(a, end=' ')
    a, b, c = b, c, a + b + c
print()
f = 1, 1, 1  # вариант с накоплением значений в кортеж
for i in range(n):   
    print(f[i], end=' ')
    f += sum(f[i:i+3]),
print()
print(f)

# шахматы ходы ферзя 
n = 8
s = []
for i in range(n):   
    s.append(['0'] * n)
lugar = input()
b = 'abcdefgh'.find(lugar[0])
a = n - '12345678'.find(lugar[1]) - 1
s[a][b]= 'Q'
for i in range(n):
    for j in range(n):
        if s[i][j] == '0':
            if abs(i - a) == abs(j - b) or a == i or b == j:
                s[i][j] = '*'
            else:
                s[i][j] = '.'
for i in s:
    print(*i)

# шахматы ходы конем
n = 8
s = []
for i in range(n):   
    s.append(['0'] * n)
lugar = input()
b = 'abcdefgh'.find(lugar[0])
a = n - '12345678'.find(lugar[1]) - 1
s[a][b]= 'N'
for i in range(n):
    for j in range(n):
        if s[i][j] == '0':
            if abs(i - a) == 2 and abs(j - b) == 1 or abs(i - a) == 1 and abs(j - b) == 2:
                s[i][j] = '*'
            else:
                s[i][j] = '.'
for i in s:
    print(*i)

# проверка квадратной матрицы на латинский квадрат
n = int(input())
s = [[i for i in input().split()] for j in range(n)]
num = list(range(1, n + 1))
flag = 'YES'

for i in range(n):      
    
    if flag != 'YES':
        break
    for j in range(n):
        if str(num[j]) not in s[i]:
            flag = 'NO'
            break
else:
    for j in range(n):
        if flag != 'YES':
            break
        p = []
        for i in range(n):
            p.append(s[i][j])
        for ii in range(n):
            if str(num[ii]) not in p:
                flag = 'NO'
                break
print(flag)


# проверяем симметричность матрицы относительно дополнительной диагонали
n = int(input())
s = [[i for i in input().split()] for j in range(n)]
flag = 'YES'
for i in range(n):
    if flag != 'YES':
        break
    for j in range(n):
        if s[i][n - j - 1] != s[j][n - i - 1]:
            flag = 'NO'
            break
print(flag)

# рисуем снежинку
n = int(input())
s = [['.' for i in range(n)] for j in range(n)]

for i in range(n):
    for j in range(n):
        if i == j or i == n - j - 1 or i == n // 2 or j == n // 2:
            s[i][j] = '*'
for i in s:
    print(*i)


# транспонируем квадратную матрицу
n = int(input())
s = [[int(i) for i in input().split()] for j in range(n)]

for i in range(n):
    for j in range(n):
        print(s[j][i], end=' ')
    print()   

# собирает элементы списка в подсписки с шагом n
s = input().split()
n = int(input())
i = 0
res = []
for j in range(n):
    res_ = []
    for i in range(j, len(s), n):
        res_.append(s[i])
    res.append(res_)

print(res)

# сложение двух матриц
n, m = [int(i) for i in input('введи количество строк и через пробел столбцов').split()]
mat1 = [input('введи через пробел строку первой матрицы').split() for i in range(n)]
input('enter')
mat2 = [input('введи через пробел строку второй матрицы').split() for i in range(n)]

res_mat = [['0' for i in range(m)] for j in range(n)]
for i in range(n):
    for j in range(m):
        res_mat[i][j] = int(mat1[i][j]) + int(mat2[i][j])
for i in res_mat:
    print(*i)


# возведение матрицы в степень
stepen = int(input('введи число, в какую степень надо возвести матрицу: '))
n1 = []
while input('будешь вводить строку для n1 ') != 'n':
    n1.append(input('введи строку для n1 ').split())
n2 = [i[:] for i in n1]
print(n2)
counter = 1
while counter < stepen:
    mult = []
    mult_res = []    
    for i in range(len(n1)):
            count_sum = 0
            for j in range(len(n2[0])):
                    count_sum = 0
                    for ii in range(len(n2)):
                            count_sum += int(n2[ii][j]) * int(n1[i][ii])
                    mult.append(count_sum)
    
    for x in range(0, len(mult), len(n1)):
        mult_res.append(mult[x:(x + len(n1))])
    
    n2 = [_[:] for _ in mult_res]
    counter += 1    
    
for i in mult_res:
    print(*i)

# перемножение двух матриц
n1 = []
while input('n если не будешь вводить строку для первой матрицы ') != 'n':
    n1.append(input('введи строку для n1 ').split())
n2 = []
while input('n если не будешь вводить строку для второй матрицы ') != 'n':
    n2.append(input('введи строку для n2 ').split())
mult = []
for i in range(len(n1)):
        count_sum = 0
        for j in range(len(n2[0])):
                count_sum = 0
                for ii in range(len(n2)):
                        count_sum += int(n2[ii][j]) * int(n1[i][ii])
                mult.append(count_sum)

mult_res = []
for i in range(0, len(mult), len(n1)):
        mult_res.append(mult[i:(i + len(n1))])
    
for i in mult_res:
    print(*i)

# заполняем матрицу спирально
n, m = [int(i) for i in input().split()]
numbers = [str(i) for i in range(1, n * m + 1)]
s = [['0' for i in range(m)] for j in range(n)]

k = 0
counter1 = 0
counter2 = 0
counter3 = 0
counter4 = 0
i = 0
j = 0
while 1:
    while j < m - counter1:
        s[i][j] = numbers[k].ljust(3)
        k += 1
        j += 1
    counter1 += 1
    j -= 1
    i += 1
    if k >= len(numbers):
        break
    while i < n - counter2:
        s[i][j] = numbers[k].ljust(3)
        k += 1
        i += 1

    counter2 += 1
    i -= 1
    j -= 1
    if k >= len(numbers):
        break
    while j >= 0 + counter3:
        s[i][j] = numbers[k].ljust(3)
        k += 1
        j -= 1
    counter3 += 1
    j += 1
    i -= 1

    if k >= len(numbers):
        break
    while i > 0 + counter4:
        s[i][j] = numbers[k].ljust(3)
        k += 1
        i -=1
    counter4 += 1
    i += 1
    j += 1

    if k >= len(numbers):
        break    
for i in s:
    print(*i)   

# печать последовательности от 1 до n строками по m горизонтально
n, m = [int(i) for i in input().split()]
s = [str(i).ljust(3) for i in range(1, n * m + 1)]
for i in range(0, len(s), m):
    print(*s[i:(i + m)])
# печать последовательности от 1 до n строками по m вертикально
n, m = [int(i) for i in input().split()]
s = [str(i).ljust(3) for i in range(1, n * m + 1)]
for i in range(n):
    print(*s[i:len(s):n])

# печать последовательности от 1 до n строками бустрофедоном
n, m = [int(i) for i in input().split()]
s_ = [str(i).ljust(3) for i in range(1, n * m + 1)]
s = []
for i in range(0, len(s_), m):
    s.append(s_[i:(i + m)])
for i in range(len(s)):
    if i % 2 == 0:
        print(*s[i][:])
    else:
        print(*s[i][::-1])
             
# печать последовательности от 1 до n строками заполняя диагонально
n, m = [int(i) for i in input().split()]
s_ = [str(i) for i in range(1, n * m + 1)]
s = [['0' for i in range(m)] for j in range(n)]
k = 0
while k < len(s):
    for i in range(n):
        for j in range(m):
            if s[i][j] =='0':
                s_sum = i + j
                for ii in range(n):
                    for jj in range(m):
                        if ii + jj == s_sum:    
                            s[ii][jj] = s_[k].ljust(3)
                            k += 1                            
                        
for i in s:
    print(*i)   


# проверка матрицы на магический квадрат - равенства сумм каждой из строк, столбцов, диагоналей матрицы из цифр от 1 до размерность в квадрате
def magic_sq():
    n = int(input()) # размерность квадратной матрицы
    numbers = list(range(1, n ** 2 + 1))
    s = []
    s_ext = []
    for i in range(n):
        ss = [int(x) for x in input().split()]
        s.append(ss)
        s_ext.extend(ss)
    for i in numbers:
        if i not in s_ext:
            return 'NO'
    s_ = []
    for i in range(n):
        if sum(s[i]) not in s_:
            s_.append(sum(s[i]))
    if len(s_) > 1:
        return 'NO'
    else:
        row_sum = s_[0]
    total_main = 0
    total_sub = 0
    for i in range(n):
        total_main += s[i][i]
        total_sub += s[i][n - i -1]
    if total_main != total_sub:
        return 'NO'
    s_ = []
    for j in range(n):
        total_col = 0
        for i in range(n):
            total_col += s[i][j]
        if total_col not in s_:
            s_.append(total_col)
        if len(s_) > 1:
            return 'NO'            
    if total_col == row_sum and row_sum == total_main:
        return 'YES'    
    else:
        return 'NO'
print(magic_sq())


# поворачивает квадратную матрицу вправо на 90 градусов
n = int(input())
s = []
for i in range(n):
    s.append([int(x) for x in input().split()])
s_ = []
for i in range(n):   
    s_.append([0] * n)
for i in range(n):
    for j in range(n):
        s_[j][n - i - 1] = s[i][j]
for i in s_:
    print(*i)

# возврат списка всех возможных подсписков
s = input().split()
res = [[]]
i = 0
k = 1
while len(res[-1]) < len(s):
    while i <= len(s) - k:
        res.append(s[i:(i + k)])
        i += 1
    i = 0
    k += 1

print(res)

# сгенерировать изменяемый список повторения одного элемента для кортежа
m = 0  # какой элемент
n = 10  # сколько раз повторить
tup = tuple([i[:] for i in [[m] * n]])

# как создавать независимую копию списка с независимыми копиями вложенных списков
list1 = [[1, 2, 3], [4, 5]]
list2 = [i[:] for i in list1]  # ВОТ ТАК!
list3 = []  # ИЛИ ЕЩЕ ТАК!
for i in list1: 
    list3.append(i.copy())

list1[0].append(7) # для проверки независимости
list2[0].append(100)
print(list3)
print(list2)
print(list1)

list1 = [1, 2, 3]  # а вот из украденного
list2 = list(list1)       # Первый способ копирования
list3 = list1[:]          # Второй способ копирования
list4 = list1.copy()      # Третий способ копировани - только в Python 3.3+


# игра камень-нож-бум-ящ-Спок
s_Timur, s_Ruslan = input('Тимур: '), input('Руслан: ')
s = [s_Timur, s_Ruslan]
result = ['Тимур', 'Руслан', 'ничья']
def k_n_b(s):
    if s[0] == s[1]:
        return -1
    if 'ножницы' in s:
        if 'бумага' in s:
            return s.index('ножницы')
        elif 'камень' in s:
            return s.index('камень')
        elif 'ящерица' in s:
            return s.index('ножницы')
        elif 'Спок' in s:
            return s.index('Спок')
        
    if 'бумага' in s:
        if 'камень' in s:
            return s.index('бумага')
        elif 'ящерица' in s:
            return s.index('ящерица')
        elif 'Спок' in s:
            return s.index('бумага')
        
    if 'камень' in s:
        if 'ящерица' in s:
            return s.index('камень')
        elif 'Спок' in s:
            return s.index('Спок')
    
    if 'ящерица' in s:
        if 'Спок' in s:
            return s.index('ящерица')
            

print(result[k_n_b(s)])



def flaviy(n, k):  # функция определения выживающего в задаче Иосифа Флавия
    a = [int('1') for i in range(n)]
    counter = 0
    i = 0
    while sum(a) > 1:
        if a[i % n] == 1:
            counter += 1
            if counter == k:
                a[i % n] = 0
                counter = 0
        i += 1
    return a.index(1) + 1
print(flaviy(int(input('введи количество воинов: ')), int(input('введи порядок смертей: '))))

total_g = 0
total_s = 0
g = 'ауоыиэяюёеАУОЫИЭЯЮЁЕ'
sog = 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ'
for i in range(len(s)):
    if s[i] in g:
        total_g += 1
    if s[i] in sog:
        total_s += 1
print('Количество гласных букв равно', total_g)
print('Количество согласных букв равно', total_s)

def convert_to_tenth():  # конвертирует цифру указанной системы счисления в десятичную
    num = input('ввести цифру для перевода в десятичную систему: ')
    system = int(input('ввести число-основание системы, из которой эта цифра: '))
    num = [str(i) for i in num]
    number = 0
    if system == 16:
        for i in range(len(num)):
            if num[i] == 'A':
                num[i] = '10'
            elif num[i] == 'B':
                num[i] = '11'
            elif num[i] == 'C':
                num[i] = '12'
            elif num[i] == 'D':
                num[i] = '13'
            elif num[i] == 'E':
                num[i] = '14'
            elif num[i] == 'F':
                num[i] = '15'            
    for i in range(len(num)):
        a = int(num[i]) * system ** (len(num) - 1 - i)
        number += a
    return number

# ковертация в "любую" систему счисления
n = int(input('ввести целое положительное число для его конвертации в систему счисления '))
systema = int(input('укажи основание целевой системы счисления: '))
t = ''
while n > 0:
    a = n % systema
    if systema == 16:
        if a == 10:
            a = 'A'
        elif a == 11:
            a = 'B'
        elif a == 12:
            a = 'C'
        elif a == 13:
            a = 'D'
        elif a == 14:
            a = 'E'
        elif a == 15:
            a = 'F'          
    t = str(a) + t
    n //= systema
print(t)

# вывод английского алфавита
s = input('хочешь вывести английский алфавит в кодировке unicod, press y ')
if s == 'y':
    for i in range(ord('a'), ord('z') + 1):
        print(chr(i), ord(chr(i)))    

# запись числа русским языком
def number_to_words(num):  # функция записи числа от 1 до 99 русским языком
    l1 = ['','один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
    l10 = ['десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
    l00 = ['двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
    ll = []
    for i in range(len(l00)):
        for j in range(len(l1)):
            ll.append(l00[i] + ' ' + l1[j])
    ll[0:0] = l10
    ll[0:0] = l1
    
    return ll[num]
    
print(number_to_words(int(input('введи число от 1 до 99 для перевода на русский: ')))) # вызываем функцию

# функция возврата названия месяца по его номеру
def get_month(language, number):  
    ru = ['', 'январь','февраль','март','апрель','май','июнь','июль','август','сентябрь','октябрь','ноябрь','декабрь']
    en = ['', 'january','february','march','april','may','june','july','august','september','october','november','december']
    if language == 'ru':
        return ru[number]
    if language == 'en':
        return en[number] 
    else:
        return False
print(get_month(input('введи ru или en для выбора языка названий месяцев: '), int(input('введи номер от 1 до 12, чтобы узнать название месяца: '))))  # вызываем функцию

# меняем местами (макс и мин) числа в списке
l = '10 9 8 7 6 5 4 3 2 1'.split()  # в этой задаче вводились цифры через пробелы
for i in range(len(l)):  # если строчные значения, мин и макс поедут
    if l[i].isdigit() == True:
        l[i] = int(l[i])
print(l)
b = l.index(max(l))
a = l.index(min(l))

l[a], l[b] = l[b], l[a]  # собственно, обмен местами
print(l)
for i in range(len(l)):  # это если нужен вывод в том же виде, что и ввод был, через пробелы
    if str(l[i]).isdigit() == True:
        l[i] = str(l[i])
print(' '.join(l))

# генератор паролей
# прикольно так записывать
# digit = '123456789' if input('Включать ли цифры:').lower() == 'y' else ''

from string import ascii_lowercase, ascii_uppercase, digits, punctuation
import random
print('Добро пожаловать в генератор паролей!')
chars = ''
password = ''

def generat_pass(lenght):
	global password
	global chars
	while len(password) < lenght:
		password += random.choice(chars)
	pass_list = list(password)
	random.shuffle(pass_list)
	password = ''.join(pass_list)
	return password 

def more_pass(lenght, count):
	global password
	global chars
	for _ in range(count):
		password = ''
		chars = ''
		if add_digits.lower() == 'д':
			password += random.choice(digits)
			chars += digits
		if add_lower.lower() == 'д':
			password += random.choice(ascii_lowercase)
			chars += ascii_lowercase
		if add_upper.lower() == 'д':
			password += random.choice(ascii_uppercase)
			chars += ascii_uppercase
		if add_punctuation.lower() == 'д':
			password += random.choice(punctuation)
			chars += punctuation
		print(generat_pass(lenght))

lenght = int(input('Введите длину пароля... '))
add_digits = input('Цифры в пароле (д - да н - нет) ').strip()
add_lower = input('Строчные буквы в пароле (д - да н - нет) ').strip()
add_upper = input('Прописные буквы в пароле (д - да н - нет) ').strip()
add_punctuation = input('Символы в пароле (д - да н - нет)' ).strip()
count = int(input('Введите кол-во паролей... '))
more_pass(lenght, count)


# эксперименты со срезами
s = []  # создаю переменную со значением пустой список
s [:] = '45b'  # присваиваю всем элементам пустого списка значение в кавычках - 
                # и это значение сразу запишется набором своих символов! 
s[-10:0] = 'о123'  # если присвоить значение срезу по индексам, выходящим за рамки списка
                  # список продлевается на количество элементов равное количеству символов
                  # выходящее за длину списка! НО: такой срез должен быть больше одного элемента, иначе просто ошибка индекса
                  # если указать срез с отрицательного до нуля, то элементы приклеются в начало списка
print(s)
sum_s = 0 # посчитать сумму не удастся не инициализировав элементы как цифры
for i in range(len(s)): # полученный выше список состоит из символов, и цифры там не цифры
    if s[i].isdigit() == True:  
        s[i] = int(s[i])  # переведем все символы цифр в цифры . а проще: s = [int(x) for x in s]
print(s)
s[3:5] = 'э'  # если присвоить значение в один символ срезу больше, чем в один индекс
              # список сожмется на соответствующее количество "лишних" элементов
print(s)
s[2] = 'aaaaa'  # если вставить любое количество символов срезом в один индекс, это будет один элемент, 
                # которым заменится элемент в соответствующей позиции списка
print(s)
s[2:3] = 'aaaaa'  # но если вставить любое количество символов отрезком длиной в эту одну позицию, 
                # кроме одной замены, в список еще и вклеится соответствующее количество элементов!
print(s)
s[1:1] = '222'  # если повторить индекс позиции через двоеточие, 
               # элементы вклеются в список начиная с номера этого индекса
print(s)

fruits = ['apple', 'apricot', 'banana', 'cherry', 'kiwi', 'lemon', 'mango']
fruits[(len(fruits) + 1):(len(fruits) + 1)] = ['банан', 'вишня', 'киви']

print(fruits)
fruits[0:1] = []  # стираю соответствующий диапазон (del)
print(fruits)

# задача на числа рамануджана
n = int(input())  # предел, до которого ищутся числа Рамануджана
m = int(input())  # степень
ss=[]
for a in range(1, n):
    for b in range(1, n):
        if a !=b:
            ab = a **m + b ** m
            for c in range(1, n):
                for d in range(1, n):
                    if c != d:
                        cd = c ** m + d ** m
                        if ab == cd and a + b != c + d and ab not in ss:
                            ss.append(ab)
                            print(ab) # число Рамануджана
                            print(a, b, c, d)  # слагаемые этого числа
                            print()
ss.sort()
print()
print(ss)  # упорядоченные по возрастанию числа Рамануджана