#Урок2
print('#задание1')
stor_square = 1
perimetr = stor_square * 4
ploshad = stor_square ** 2
diagonal_square = (stor_square ** 2 + stor_square ** 2)**0.5
print(perimetr, ploshad, diagonal_square)

print('#задание2')
a = 3
b = 13
c = -30
d = b ** 2 - 4 * a * c
x1 = (-1 * b + d ** 0.5) / a * 2
x2 = (-1 * b - 1 * d ** 0.5) / a * 2
print(x1, x2)

print('#задание3')
string1 = 'ПУсть всегда будет солнце,'
string2 = 'пусть всегда будет небо'
string3 = string1 + string2
print(string3)
print(string3.split(' '))
print(string2[0:2] + string1[2:])
print(string1[0:2] + string2[2:])
#или
string4 = string1[0:2]
string5 = string2[0:2]
print(string1.replace(string4, string5))
print(string2.replace(string5, string4))

print('#задание4')
put = 'С:\python\\file.txt'
disc = ((put.split('\\')[0]).split(':')[0])
papka1 = (put.split('\\')[1])
filesname = ((put.split('\\')[-1]).split('.')[0])
print(disc, papka1, filesname)

print('#задание5')
a = 5
b = 3
c = a + b
d = a * b
print("{} + {} = {}".format(a, b, c))
print(f"{a} * {b} = {d}")
print(f"%d * %d = %d" %(a, b, d))

print('#задание6')
string = "ТуТ МоГлА БыТь вАшА РеКлАмА"
string1 = string[0::2]
print(string1)

print('#задание7')
string1 = 'wtf'
string2 = 'brick quz jmpy veldt whangs fox'
a = min(string2.find(string1[0]), string2.find(string1[1]), string2.find(string1[2]))
b = max(string2.find(string1[0]), string2.find(string1[1]), string2.find(string1[2]))
print(string2[a:b+1])
