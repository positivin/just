# (украденное) 

#из двух файлов строк (имена first_name.txt и фамилии last_names.txt) составляет (три) случайные имя-фамилия. заметь в частности зведочку перед map - без нее возвращаются пара списков, а не набор имен-фамилий
import random
[print(*p) for p in zip(*map(lambda f: random.sample(open(f + 'st_names.txt').read().split(), 3), ['fir', 'la']))]

#проверка что хотя бы по одному элементу в каждом подсписке соответствует признаку (среди k учеников класса есть отличник в каждом из n классов). замечательно использование 'k'* и 'n'* вместо range() и решение без сплита
print(('NO', 'YES')[all([any(['5' in input() for _ in 'k'*int(input())]) for _ in 'n'*int(input())])])

# проверка строки на содержание как минимум по одному символу каждого нужного вида (и длины не менее 7)
#зацени идею передачи в map кортежа функций!
(lambda p: print(('NO','YES')[len(p)>6 and all(map(lambda f: any(map(f, p)), (str.isdigit, str.islower, str.isupper)))]))(input())
# и вот такой вариант еще, чуть менее изощренный, тут интересно применение any() от противного:
(lambda s: print(('YES', 'NO')[any([len(s) < 7, s.islower(), s.isupper(),s.isalpha(), s.isdigit(), not s.isalnum()])]))(input())


#  присвоение вводимым через пробел данным строки целочисленных значений
c = [*map(int, input().split())]


# перемешивание матрицы
import random as rnd
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

n, m, lst = len(matrix), len(matrix[0]), sum(matrix, [])  # обрати внимание на применение функции sum - превращает двумерное в одномерное!
rnd.shuffle(lst)
matrix = [[lst[i * m + j] for j in range(m)] for i in range(n)] #  а вот так собирают одномерное в двумерное!


# enumerate
list_a = [-2, -1, 0, 1, 2, 3, 4, 5]
list_e = [x for i, x in enumerate(list_a) if i % 3 == 0]
print(list_e)   # NB [-2, 1, 4] при enumerate(list_a) и [0, 3] при enumerate(list_a, 1) - 1 задает старт, а так как единица на 3 не делится, то она не проходит фильтр, а 0 проходит

# перевод списка в строку
list_a = [-2, -1, 0, 1, 2, 3, 4, 5]
my_str = ''.join(str(x) for x in list_a)  # используем генератор прямо в .join() одновременно приводя элементы к строковому типу
print(my_str)  # -2-1012345


# сортировка списка кортежей по убыванию-возрастанию элементов в них
shop = [('каретка', 1200), ('шатун', 1000), ('седло', 300),
        ('педаль', 100), ('седло', 1500), ('рама', 12000),
        ('обод', 2000), ('шатун', 200), ('седло', 2700)]

def prepare_item(item):
    return (item[0], -item[1]) # NB если item[1], то возвращает кортежи с одним и тем же первым элементом по возрастанию значения второго элемента, а если -item[1] - то по убыванию! 

shop.sort(key=prepare_item)  # вместо своей функции того же эффекта можно добиться с использованием лямбда-функции: shop.sort(key=lambda x: (x[0], -x[1]))
print(shop)

# шаблон генератора: {(some_key1 if condition else some_key2):(something1  if condition else something2) for key, value in dict_.items()}

# создание словаря из взаимообратных пар задаваемого количества синонимов.
print({w[i]: w[not i] for _ in range(int(input())) for w in [input().split()] for i in (0, 1)})  # если требуется нечто найти в словаре, добавь перед закрывающейся скобкой [input()]

# задача по введенным строкам со странами на первом месте и городами за ними вывести заданное количество стран по городам
# вариант 1
d = {}
for _ in range(int(input())):
    country, *cities = input()
    d.update(dict.fromkeys(cities, country))
# [print(d[input()]) for _ in range(int(input()))] 
for _ in range(int(input())):    
    print(d[input()])

# вариант 2
d = {i : j for _ in range(int(input())) for i, *j in  [input().split()]}
[print(k) for _ in range(int(input())) for i in [input()] for k, v in d.items() if i in v] # тут поиск города идет по значениям словаря стран

# вариант 3
d={}
for _ in range(int(input())):
    a = input().split()
    for c in a[1:]: # интересный вариант замены fromkeys
        d[c]=a[0]
for _ in range(int(input())):
    print(d[input()])

# мой вариант (я сразу создаю словарь по городам)
s = {i[j]: i[0] for i in [input().split() for _ in range(int(input()))] for j in range(1, len(i))}
print(*[s.get(i, 'Нет данных') for i in [input() for _ in range(int(input()))]], sep='\n')

# (украдено https://habr.com/ru/post/319200/) Можно менять части последовательности — это применение выглядит наиболее интересным, так как решает задачу просто и наглядно.
my_list = [1, 2, 3, 4, 5]
my_list[1:3] = [20, 30]
print(my_list)          # [1, 20, 30, 4, 5]
my_list[1:3] = [0]      # нет проблем заменить два элемента на один
print(my_list)          # [1, 0, 4, 5]
my_list[2:] = [40, 50, 60]   # или два элемента на три
print(my_list)               # [1, 0, 40, 50, 60]
my_list = [1, 2, 3, 4, 5]
my_list[:2] = []    # или del my_list[:2]
print(my_list)      # [3, 4, 5]

