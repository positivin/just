# (����������) 

#�� ���� ������ ����� (����� first_name.txt � ������� last_names.txt) ���������� (���) ��������� ���-�������. ������ � ��������� �������� ����� map - ��� ��� ������������ ���� �������, � �� ����� ����-�������
import random
[print(*p) for p in zip(*map(lambda f: random.sample(open(f + 'st_names.txt').read().split(), 3), ['fir', 'la']))]

#�������� ��� ���� �� �� ������ �������� � ������ ��������� ������������� �������� (����� k �������� ������ ���� �������� � ������ �� n �������). ������������ ������������� 'k'* � 'n'* ������ range() � ������� ��� ������
print(('NO', 'YES')[all([any(['5' in input() for _ in 'k'*int(input())]) for _ in 'n'*int(input())])])

# �������� ������ �� ���������� ��� ������� �� ������ ������� ������� ������� ���� (� ����� �� ����� 7)
#������ ���� �������� � map ������� �������!
(lambda p: print(('NO','YES')[len(p)>6 and all(map(lambda f: any(map(f, p)), (str.isdigit, str.islower, str.isupper)))]))(input())
# � ��� ����� ������� ���, ���� ����� ����������, ��� ��������� ���������� any() �� ����������:
(lambda s: print(('YES', 'NO')[any([len(s) < 7, s.islower(), s.isupper(),s.isalpha(), s.isdigit(), not s.isalnum()])]))(input())


#  ���������� �������� ����� ������ ������ ������ ������������� ��������
c = [*map(int, input().split())]


# ������������� �������
import random as rnd
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

n, m, lst = len(matrix), len(matrix[0]), sum(matrix, [])  # ������ �������� �� ���������� ������� sum - ���������� ��������� � ����������!
rnd.shuffle(lst)
matrix = [[lst[i * m + j] for j in range(m)] for i in range(n)] #  � ��� ��� �������� ���������� � ���������!


# enumerate
list_a = [-2, -1, 0, 1, 2, 3, 4, 5]
list_e = [x for i, x in enumerate(list_a) if i % 3 == 0]
print(list_e)   # NB [-2, 1, 4] ��� enumerate(list_a) � [0, 3] ��� enumerate(list_a, 1) - 1 ������ �����, � ��� ��� ������� �� 3 �� �������, �� ��� �� �������� ������, � 0 ��������

# ������� ������ � ������
list_a = [-2, -1, 0, 1, 2, 3, 4, 5]
my_str = ''.join(str(x) for x in list_a)  # ���������� ��������� ����� � .join() ������������ ������� �������� � ���������� ����
print(my_str)  # -2-1012345


# ���������� ������ �������� �� ��������-����������� ��������� � ���
shop = [('�������', 1200), ('�����', 1000), ('�����', 300),
        ('������', 100), ('�����', 1500), ('����', 12000),
        ('����', 2000), ('�����', 200), ('�����', 2700)]

def prepare_item(item):
    return (item[0], -item[1]) # NB ���� item[1], �� ���������� ������� � ����� � ��� �� ������ ��������� �� ����������� �������� ������� ��������, � ���� -item[1] - �� �� ��������! 

shop.sort(key=prepare_item)  # ������ ����� ������� ���� �� ������� ����� �������� � �������������� ������-�������: shop.sort(key=lambda x: (x[0], -x[1]))
print(shop)

# ������ ����������: {(some_key1 if condition else some_key2):(something1  if condition else something2) for key, value in dict_.items()}

# �������� ������� �� �������������� ��� ����������� ���������� ���������.
print({w[i]: w[not i] for _ in range(int(input())) for w in [input().split()] for i in (0, 1)})  # ���� ��������� ����� ����� � �������, ������ ����� ������������� ������� [input()]

# ������ �� ��������� ������� �� �������� �� ������ ����� � �������� �� ���� ������� �������� ���������� ����� �� �������
# ������� 1
d = {}
for _ in range(int(input())):
    country, *cities = input()
    d.update(dict.fromkeys(cities, country))
# [print(d[input()]) for _ in range(int(input()))] 
for _ in range(int(input())):    
    print(d[input()])

# ������� 2
d = {i : j for _ in range(int(input())) for i, *j in  [input().split()]}
[print(k) for _ in range(int(input())) for i in [input()] for k, v in d.items() if i in v] # ��� ����� ������ ���� �� ��������� ������� �����

# ������� 3
d={}
for _ in range(int(input())):
    a = input().split()
    for c in a[1:]: # ���������� ������� ������ fromkeys
        d[c]=a[0]
for _ in range(int(input())):
    print(d[input()])

# ��� ������� (� ����� ������ ������� �� �������)
s = {i[j]: i[0] for i in [input().split() for _ in range(int(input()))] for j in range(1, len(i))}
print(*[s.get(i, '��� ������') for i in [input() for _ in range(int(input()))]], sep='\n')

# (�������� https://habr.com/ru/post/319200/) ����� ������ ����� ������������������ � ��� ���������� �������� �������� ����������, ��� ��� ������ ������ ������ � ��������.
my_list = [1, 2, 3, 4, 5]
my_list[1:3] = [20, 30]
print(my_list)          # [1, 20, 30, 4, 5]
my_list[1:3] = [0]      # ��� ������� �������� ��� �������� �� ����
print(my_list)          # [1, 0, 4, 5]
my_list[2:] = [40, 50, 60]   # ��� ��� �������� �� ���
print(my_list)               # [1, 0, 40, 50, 60]
my_list = [1, 2, 3, 4, 5]
my_list[:2] = []    # ��� del my_list[:2]
print(my_list)      # [3, 4, 5]

