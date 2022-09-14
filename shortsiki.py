# ������ �� �����������: �� ���������� ����� ��������� �������������� �������� ��� ����� �������
import operator as op
def arithmetic_operation(s):
    dic = {'+': (lambda x, y: op.add(x,y)), '-': (lambda x, y: op.sub(x, y)), '*': (lambda x, y: op.mul(x, y)), '/': (lambda x, y: op.truediv(x, y))}
    return dic[s]

add = arithmetic_operation('+')
div = arithmetic_operation('/')
print(add(10, 20))
print(div(20, 5))

# ���������� �� ���������� ����� ��������� ���� �������� ������ ��������������� �����, � ������� - ����� �� 5 ����, ���������� �������� ������������ ���������� �������
import string # ����� ��� �����, ����� ���������� � ������ ������ ���������� - ������� ������ ������ � �������� �� ������
with open('English.txt','r') as readfile:  # ���� � �������� ������� ���������� ������ ���������� ����
    with open('exampleY.txt','w') as writefile:
        for line in readfile:
                writefile.write(line)  # ��� ������������ ������� � ����� ����, ����� �������� ���

with open('exampleY.txt') as text:
    t = text.read()  # ������ ��������� ���������� � �������� �������
f_del ='�' + string.punctuation + '�' + '�' + '�' # � �������������� ������ ���������� ������ ������-�� �� ��� ����� �����, ��������, ��� ������������� �������
for i in f_del:
    if i in t:
        t = t.replace(i, '')        # ������ �� ��������� ���������� ��� ����������, ����� ��� �� ������ �� ����� ����    
t = t.lower().split()  # �������� ��������� ���������� �� ����� � ��������� �� � ��������� ����������

maska ='aeiouy' # ��� ����� ������ ������������ ������� �����
num = 5  # ����� �������� �����
t = {i: sum((j in i) for j in maska) for i in t if len(i) == num}  # ���� ��������� ���: sum((j in i) for j in maska) - ��������� True ������ ���������� � ����� ������ ���� �� ����� 

m = max(t.values())
out = list({i: j for i, j in t.items() if j == m}.keys())  # ��� ����� ������ ����� � ������� ����������� ������������ ������������ ����� �� �����
out = sorted(out)  # �������� �������� ������ ���� �� ��������

with open('exampleY.txt','w') as writefile:
    for i in "\n".join(out):      # ������ ���, ��� ��������� � join, �������� ������ ���� ������-�� ������������ � ��������� ���� �������� �������
        writefile.write(i)
print('��������������� �� �������� ��������� ��', len(out), '���� �', num, '���� ����������� ������������� ��', maska, '�������� � ���� exampleY.txt')

# �������� � �������������� ���������� ����� https://istories.media/workshops/2021/01/29/vvedenie-v-python-chast-11-rabota-s-failami/
with open('C:\\Users\\PS\\Desktop\\Eesti.txt') as f:
    #data = f.readlines() - ���������� ���� ����� � ������ �����, ���� ������������, �� ���������� ���������� ������ read() ����������� �����������
    #data = f.readline()  - ���������� ������: ����� �������� �� (������� ����� ������  - ����� ������, �� �� �����, �� ��������, ���� ��� �� � ��������), ���� ��������� � ������� ������������� �����, ������� ����� ������ �� ����� �������� ������ �������� ������ ����� �����, � ��������� ������ � ������ ���� �������� ������ � ������� ���������� �������, ���� ����� ��������� ������ ����� ������, �������� ��� ����� ������ �� �����.
    d_ata = f.read()  # ���������� ����� ������ ������� ������ � ������� ������� � ���� �������
    
# data[0] = data[0].replace('�','�') - ������������ ������� ������ �� �������� � �� ��������

with open('text_test.txt', 'w') as tf:
    tf.write(d_ata[d_ata.find('� ������'):].strip())
with open('text_test.txt', 'a') as tf:
    tf.write('\n������� �� ��������!\n')

with open('C:\\Users\\PS\\Desktop\\Eesti.txt') as f:
    data = f.readlines()    
with open('text_test.txt', 'a') as tf:
    tf.writelines(i for i in data[8:12])
with open('text_test.txt') as tf:
        print(tf.read())

# ������� ������ �������� ������ �� ��������� ��������

def generate_index():
    import string
    import random
    a = 'LetterLetterNumber_NumberLetterLetter' # �������� ������ � ������
    s = {'Letter': (string.ascii_uppercase), 'Number': range(0, 100)}  # ������� ���������� ��������
    for k, v in s.items():
        while k in a:                      
            a = a.replace(k, str(random.choice(v)), 1)  # ������� ����� ����� �������: ���� ��� ���, �� ��� ��������� ������ � ���� �� ����� ������� � ������ ��������� ����� � ��� �� ��������������� ���������, � �� �������
    return a
print(generate_index())

# ������ ������ � �������� (���������� ����� ����������) ��������� �� �����������
s = {}
for i in range(int(input())):
    a, b, c = input().split() # �� �������� ������ �� ����� ������ "���������� ����� ����������"
    s.setdefault(a, {})  # ������������� ���� (��� ���� �����������) �� ��������� ������� (��� �������� �������)
    s[a].setdefault(b, int()) # ������������� ���� �� ��������� ����� ����� (��� ���������� �������)
    s[a][b] += int(c) # �������� �� ����� �� ��������� ������ ����� (���������� �������)

for k, v in sorted(s.items()):  # �� �������� ������ ������� ��������� ���������� �� ��������� ������� ������ � �� �����������
    print(f'{k}:')
    a = sorted(v.items())
    for j in a:
        print(*j)

# �������� � ���� ������� ���� �������� ������
def merge(lst):
    a = {}
    for i in lst:
        for k, v in i.items():
            a.setdefault(k, set())
            a[k].add(v)
    return a

# ����� ������ �����
s = input('����� �����: ').split() 

s = {i: s.count(i) for i in s}
print(f'���� ����� �����������, � ���������� �������, ����� "{min([i for i in s if s[i] == max(s.values())])}"')

# ��������� ������� ������ � ������� ��������� ���������
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
s.extend(['0', ' ']) # ������ ������ ��� �������
ss = {s[i]: s[i+1] for i in range(0, len(s), 2)} # ������� � ������� �� ������
ss.update({s[i+1][j]: s[i] for i in range(0, len(s), 2) for j in range(len(s[i+1]))})  # ������� �������� �������� � ������� �� �������� (������)

n = list(input('����� ����� ��� ������ �� ��������� �������� ���������: ').upper()) 
res = ''
for i in n:
    if i in ss:
        res += ss[i] * (ss[ss[i]].find(i) + 1)  # ���� � ������� �� ����� ����� ����� �������� (��������� �����) � ������� �������� �� �� ������ ����� � ������� �� ����� (���� ����)

print(res)


# ��������� �������� ������ � ���������� (��������������� �� �����������) ��������� �����
n = int(input('����� ���������� ����� � ������� ��� �����: '))  
print('��� ����� ��������� ������ ����� ����� ������')
n = [frozenset([int(j) for j in input().split()])for i in range(n)]  # ������, ��� ����� ��������� ������ frozenset, ����� �������� � ����� � ��� �� ������� ����� � ��� �� �������� 
m_inion = set()
for i in n:
    m_inion |= i

index_ = int(input('''����� ������ (����� ������ � ����) ������, 
� ������� ����� �������� ������ ���������� ��������, 
�� ������������� � ��������� �������: '''))

m_dif = []
for i in n:
    m_dif.append(i)
m_dif[0], m_dif[index_] = m_dif[index_], n[0]
for i in range(1, len(m_dif)):
    m_dif[0] -= m_dif[i]

m_inter = n[0]

for i in n:
    m_inter &= i

print('��� �������� ������ ��������: ', n)   
print('��� ��������� ���� �����: ', *sorted(m_inion))
print('��� ��������� ���� ����� �����: ', *sorted(m_inter))
print(f'��� ��������� ���� ���������� ����� ������ � �������� {index_}: ', *sorted(m_dif[0])) 


# �������� �� ���� � ������ ������ ������ �� � �� ���� ������� ���������� ������ ���� 
n = input().lower().split()
for_del = list('.,;:-?!)(')  # ��� ������ ������, ������� ����� ������� �� ������
s = set()
for i in range(len(n)):
    for j in for_del:
        while j in n[i]:
            n[i] = n[i].replace(j, '')
    s.add(n[i])
print(*n)  # ���� � ����, ��� ��� ����� ����� �������� � ������ ��������
print(len(s))  # ���������� ������ ���� � ������

# ����� � ��������� ���������� �������
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
print(f'������� ��������: {total_up}', f'������ ��������: {total_r}', f'������ ��������: {total_low}', f'����� ��������: {total_l}', sep='\n')            

# ������ � ����� �����������
n, m, k, x, y, z, t, aa = int(input('�������� ������� ���������: ')), int(input('�������� ������� ���������: ')), int(input('�������� �������� ���������: ')), int(input('�������� ������������� OR �������-������� ��������: ')), int(input('�������� ������������� OR �������-�������� ��������: ')), int(input('�������� ������������� OR �������-�������� ��������: ')), int(input('�������� ������� AND ������� AND �������� ��������: ')), int(input('�������� �������������� ���������: '))
a = n + m - x - t
b = m + k - y - t
c = n + k - z - t
n_ = n - a - t - c
m_ = m - a - t - b
k_ = k - b - t - c
s = (a, b, c, n_, m_, k_, t)
s = sum(s)
print(f'�������� ��������� ��������� ������ � �����-�� ����� �� �������� �������� (����������� ������ 1 �� 3� ����): {n_ + m_ + k_}')
print(f'�������� ��������� ��������� ����� � ���� �� �������� �������� (����������� �� 2-� �� 3� ����): {a + b + c}')
print(f'�������� ��������� ��������� �� �� �������� �� � ���� �� �������� �������� (�� ����������� ����): {aa - s}') 

# ������ ������ ��������� - "����� ����������"
n = int(input())
a, b, c = 1, 1, 1  # ������� ��� ���������� �������� � ������
for i in range(n):
    print(a, end=' ')
    a, b, c = b, c, a + b + c
print()
f = 1, 1, 1  # ������� � ����������� �������� � ������
for i in range(n):   
    print(f[i], end=' ')
    f += sum(f[i:i+3]),
print()
print(f)

# ������� ���� ����� 
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

# ������� ���� �����
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

# �������� ���������� ������� �� ��������� �������
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


# ��������� �������������� ������� ������������ �������������� ���������
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

# ������ ��������
n = int(input())
s = [['.' for i in range(n)] for j in range(n)]

for i in range(n):
    for j in range(n):
        if i == j or i == n - j - 1 or i == n // 2 or j == n // 2:
            s[i][j] = '*'
for i in s:
    print(*i)


# ������������� ���������� �������
n = int(input())
s = [[int(i) for i in input().split()] for j in range(n)]

for i in range(n):
    for j in range(n):
        print(s[j][i], end=' ')
    print()   

# �������� �������� ������ � ��������� � ����� n
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

# �������� ���� ������
n, m = [int(i) for i in input('����� ���������� ����� � ����� ������ ��������').split()]
mat1 = [input('����� ����� ������ ������ ������ �������').split() for i in range(n)]
input('enter')
mat2 = [input('����� ����� ������ ������ ������ �������').split() for i in range(n)]

res_mat = [['0' for i in range(m)] for j in range(n)]
for i in range(n):
    for j in range(m):
        res_mat[i][j] = int(mat1[i][j]) + int(mat2[i][j])
for i in res_mat:
    print(*i)


# ���������� ������� � �������
stepen = int(input('����� �����, � ����� ������� ���� �������� �������: '))
n1 = []
while input('������ ������� ������ ��� n1 ') != 'n':
    n1.append(input('����� ������ ��� n1 ').split())
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

# ������������ ���� ������
n1 = []
while input('n ���� �� ������ ������� ������ ��� ������ ������� ') != 'n':
    n1.append(input('����� ������ ��� n1 ').split())
n2 = []
while input('n ���� �� ������ ������� ������ ��� ������ ������� ') != 'n':
    n2.append(input('����� ������ ��� n2 ').split())
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

# ��������� ������� ���������
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

# ������ ������������������ �� 1 �� n �������� �� m �������������
n, m = [int(i) for i in input().split()]
s = [str(i).ljust(3) for i in range(1, n * m + 1)]
for i in range(0, len(s), m):
    print(*s[i:(i + m)])
# ������ ������������������ �� 1 �� n �������� �� m �����������
n, m = [int(i) for i in input().split()]
s = [str(i).ljust(3) for i in range(1, n * m + 1)]
for i in range(n):
    print(*s[i:len(s):n])

# ������ ������������������ �� 1 �� n �������� �������������
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
             
# ������ ������������������ �� 1 �� n �������� �������� �����������
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


# �������� ������� �� ���������� ������� - ��������� ���� ������ �� �����, ��������, ���������� ������� �� ���� �� 1 �� ����������� � ��������
def magic_sq():
    n = int(input()) # ����������� ���������� �������
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


# ������������ ���������� ������� ������ �� 90 ��������
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

# ������� ������ ���� ��������� ����������
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

# ������������� ���������� ������ ���������� ������ �������� ��� �������
m = 0  # ����� �������
n = 10  # ������� ��� ���������
tup = tuple([i[:] for i in [[m] * n]])

# ��� ��������� ����������� ����� ������ � ������������ ������� ��������� �������
list1 = [[1, 2, 3], [4, 5]]
list2 = [i[:] for i in list1]  # ��� ���!
list3 = []  # ��� ��� ���!
for i in list1: 
    list3.append(i.copy())

list1[0].append(7) # ��� �������� �������������
list2[0].append(100)
print(list3)
print(list2)
print(list1)

list1 = [1, 2, 3]  # � ��� �� �����������
list2 = list(list1)       # ������ ������ �����������
list3 = list1[:]          # ������ ������ �����������
list4 = list1.copy()      # ������ ������ ���������� - ������ � Python 3.3+


# ���� ������-���-���-��-����
s_Timur, s_Ruslan = input('�����: '), input('������: ')
s = [s_Timur, s_Ruslan]
result = ['�����', '������', '�����']
def k_n_b(s):
    if s[0] == s[1]:
        return -1
    if '�������' in s:
        if '������' in s:
            return s.index('�������')
        elif '������' in s:
            return s.index('������')
        elif '�������' in s:
            return s.index('�������')
        elif '����' in s:
            return s.index('����')
        
    if '������' in s:
        if '������' in s:
            return s.index('������')
        elif '�������' in s:
            return s.index('�������')
        elif '����' in s:
            return s.index('������')
        
    if '������' in s:
        if '�������' in s:
            return s.index('������')
        elif '����' in s:
            return s.index('����')
    
    if '�������' in s:
        if '����' in s:
            return s.index('�������')
            

print(result[k_n_b(s)])



def flaviy(n, k):  # ������� ����������� ����������� � ������ ������ ������
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
print(flaviy(int(input('����� ���������� ������: ')), int(input('����� ������� �������: '))))

total_g = 0
total_s = 0
g = '�����������������ި�'
sog = '������������������������������������������'
for i in range(len(s)):
    if s[i] in g:
        total_g += 1
    if s[i] in sog:
        total_s += 1
print('���������� ������� ���� �����', total_g)
print('���������� ��������� ���� �����', total_s)

def convert_to_tenth():  # ������������ ����� ��������� ������� ��������� � ����������
    num = input('������ ����� ��� �������� � ���������� �������: ')
    system = int(input('������ �����-��������� �������, �� ������� ��� �����: '))
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

# ���������� � "�����" ������� ���������
n = int(input('������ ����� ������������� ����� ��� ��� ����������� � ������� ��������� '))
systema = int(input('����� ��������� ������� ������� ���������: '))
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

# ����� ����������� ��������
s = input('������ ������� ���������� ������� � ��������� unicod, press y ')
if s == 'y':
    for i in range(ord('a'), ord('z') + 1):
        print(chr(i), ord(chr(i)))    

# ������ ����� ������� ������
def number_to_words(num):  # ������� ������ ����� �� 1 �� 99 ������� ������
    l1 = ['','����', '���', '���', '������', '����', '�����', '����', '������', '������']
    l10 = ['������', '�����������', '����������', '����������', '������������', '����������', '�����������', '����������', '������������', '������������']
    l00 = ['��������', '��������', '�����', '���������', '����������', '���������', '�����������', '���������']
    ll = []
    for i in range(len(l00)):
        for j in range(len(l1)):
            ll.append(l00[i] + ' ' + l1[j])
    ll[0:0] = l10
    ll[0:0] = l1
    
    return ll[num]
    
print(number_to_words(int(input('����� ����� �� 1 �� 99 ��� �������� �� �������: ')))) # �������� �������

# ������� �������� �������� ������ �� ��� ������
def get_month(language, number):  
    ru = ['', '������','�������','����','������','���','����','����','������','��������','�������','������','�������']
    en = ['', 'january','february','march','april','may','june','july','august','september','october','november','december']
    if language == 'ru':
        return ru[number]
    if language == 'en':
        return en[number] 
    else:
        return False
print(get_month(input('����� ru ��� en ��� ������ ����� �������� �������: '), int(input('����� ����� �� 1 �� 12, ����� ������ �������� ������: '))))  # �������� �������

# ������ ������� (���� � ���) ����� � ������
l = '10 9 8 7 6 5 4 3 2 1'.split()  # � ���� ������ ��������� ����� ����� �������
for i in range(len(l)):  # ���� �������� ��������, ��� � ���� ������
    if l[i].isdigit() == True:
        l[i] = int(l[i])
print(l)
b = l.index(max(l))
a = l.index(min(l))

l[a], l[b] = l[b], l[a]  # ����������, ����� �������
print(l)
for i in range(len(l)):  # ��� ���� ����� ����� � ��� �� ����, ��� � ���� ���, ����� �������
    if str(l[i]).isdigit() == True:
        l[i] = str(l[i])
print(' '.join(l))

# ��������� �������
# ��������� ��� ����������
# digit = '123456789' if input('�������� �� �����:').lower() == 'y' else ''

from string import ascii_lowercase, ascii_uppercase, digits, punctuation
import random
print('����� ���������� � ��������� �������!')
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
		if add_digits.lower() == '�':
			password += random.choice(digits)
			chars += digits
		if add_lower.lower() == '�':
			password += random.choice(ascii_lowercase)
			chars += ascii_lowercase
		if add_upper.lower() == '�':
			password += random.choice(ascii_uppercase)
			chars += ascii_uppercase
		if add_punctuation.lower() == '�':
			password += random.choice(punctuation)
			chars += punctuation
		print(generat_pass(lenght))

lenght = int(input('������� ����� ������... '))
add_digits = input('����� � ������ (� - �� � - ���) ').strip()
add_lower = input('�������� ����� � ������ (� - �� � - ���) ').strip()
add_upper = input('��������� ����� � ������ (� - �� � - ���) ').strip()
add_punctuation = input('������� � ������ (� - �� � - ���)' ).strip()
count = int(input('������� ���-�� �������... '))
more_pass(lenght, count)


# ������������ �� �������
s = []  # ������ ���������� �� ��������� ������ ������
s [:] = '45b'  # ���������� ���� ��������� ������� ������ �������� � �������� - 
                # � ��� �������� ����� ��������� ������� ����� ��������! 
s[-10:0] = '�123'  # ���� ��������� �������� ����� �� ��������, ��������� �� ����� ������
                  # ������ ������������ �� ���������� ��������� ������ ���������� ��������
                  # ��������� �� ����� ������! ��: ����� ���� ������ ���� ������ ������ ��������, ����� ������ ������ �������
                  # ���� ������� ���� � �������������� �� ����, �� �������� ���������� � ������ ������
print(s)
sum_s = 0 # ��������� ����� �� ������� �� ��������������� �������� ��� �����
for i in range(len(s)): # ���������� ���� ������ ������� �� ��������, � ����� ��� �� �����
    if s[i].isdigit() == True:  
        s[i] = int(s[i])  # ��������� ��� ������� ���� � ����� . � �����: s = [int(x) for x in s]
print(s)
s[3:5] = '�'  # ���� ��������� �������� � ���� ������ ����� ������, ��� � ���� ������
              # ������ �������� �� ��������������� ���������� "������" ���������
print(s)
s[2] = 'aaaaa'  # ���� �������� ����� ���������� �������� ������ � ���� ������, ��� ����� ���� �������, 
                # ������� ��������� ������� � ��������������� ������� ������
print(s)
s[2:3] = 'aaaaa'  # �� ���� �������� ����� ���������� �������� �������� ������ � ��� ���� �������, 
                # ����� ����� ������, � ������ ��� � �������� ��������������� ���������� ���������!
print(s)
s[1:1] = '222'  # ���� ��������� ������ ������� ����� ���������, 
               # �������� �������� � ������ ������� � ������ ����� �������
print(s)

fruits = ['apple', 'apricot', 'banana', 'cherry', 'kiwi', 'lemon', 'mango']
fruits[(len(fruits) + 1):(len(fruits) + 1)] = ['�����', '�����', '����']

print(fruits)
fruits[0:1] = []  # ������ ��������������� �������� (del)
print(fruits)

# ������ �� ����� �����������
n = int(input())  # ������, �� �������� ������ ����� �����������
m = int(input())  # �������
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
                            print(ab) # ����� �����������
                            print(a, b, c, d)  # ��������� ����� �����
                            print()
ss.sort()
print()
print(ss)  # ������������� �� ����������� ����� �����������