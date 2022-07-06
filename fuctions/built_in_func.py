# 1 #Встроенные функции 
# input()
# print()
# str()
# sum()
# list()
# len()
# divmod()
# globals()
# locals()
# min()
# max() etc.



# map()
# filter()
# lambda
# enumerate
 


#  Анонимные функции - lamda ( такие же функции только без названия )
#  lamda функции могут принимать сколько угодно аргументов но всегда возвращают только одно выражение
 

# def sum_args(a, b):
#     result = a + b
#     return result

# def sum_args(a, b): return a + b

# print(sum_args(1,2))
# print(sum_args(1,2))

# sum_args = lambda a, b: a + b
# print(sum_args(1,2))


# x = lambda a, b, c: a + b + c
# print(x(1,2,3))



# def myFunc(n):
#     return lambda a: a * n
# my_doubler = myFunc(2)
# my_tripler = myFunc(3)
# print(my_doubler(11))
# print(my_doubler(22))
# print(my_tripler(11))
# print(my_tripler(22))


# ls = ['def', 'makers', 'john', '', ' ']
# new_list = sorted(ls, key=len)
# print(new_list)


#--------------------------------------------------------------------------------------------



# map(function, Iterable) -> применяет функцию к каждому элементу последовательности и возвращает  mapobject(итератор) с реузльтами 

# например с помощью map можно выполнять преобразавание элементов. Перевести все строки в верхний регистр:
# list_of_words = ['one', 'two', 'three', 'dict']
# result = list(map(str.upper, list_of_words))
# print(result)
# result2 = list(map(len, list_of_words))
# print(result2)

# ls = ['1', '2', '3', '4']
# result = list(map(int, ls))
# print(result)

# names = ['John', 'Jamie', 'Sansa', 'Tirion', 'Aibek']
# #['Hello mr/mrs John', 'Hello mr/mrs Jamie]

# result = list(map(lambda x:f'Hello mr/mrs {x}', names))
# print(result)
# nums = [1,2,3,4,5]
# num2 = [100, 200,300,400,500]
# result = list(map(lambda y,x: x*y, nums, num2))
# print(result)

# dict_ = {1:2, 3: 4, 5: 6}
# result = dict(map(lambda items: (items[0], str(items[1],)), dict_.items()))
# print(result)


#---------------------------------




# filter (function, Iterable) - применяет ко всем элементам  iterable функцию  которую мы передаем и возвращает filtreobject (итератор) с теми обьектами для которых функция вернула True.   


# list_of_str = ['one', 'two', 'list', '', '100', '1', '50', 'john99']
# result = filter(str.isdigit, list_of_str)
# print(list(result))
# for x in result:
#     print(x)

# ls =[10,11,102,213,314,515]
# result = list(filter(lambda x: x % 2 !=0, ls))
# print(result)


# list_of_words = ['John', 'One', 'two', 'list', 'makers', 'ev.22', 'ono']
# result = list(filter(lambda x:len(x) >=4, list_of_words))
# print(result)


#--------------------------------------------
# enumerate(iterable) 
# ls = ['str1', 'str2', 'str3']
# i = 0
# for x in ls:
#     print(f'elment: {x}, index{i}')
#     i+=1

# for i, x in enumerate (ls):
#      print(f'elment: {x}, index{i}')

# new_list = list(enumerate(ls))
# print(new_list)
 

#-----------------------------------------
# zip (iterable) - она соеденяет каждый элемент интериуруемых обьектов между собой в тип данных tuple и возвращает это
# list1 = [1,2,3]
# list2 = [100,200,300]
# result = list(zip(list1,list2))
# print(result)

# a = [1, 2, 3, 4, 5]
# b = [10, 20, 30, 40]
# c = [100, 200, 300]
# result = list(zip(a, b, c))
# print(result)

# zip - для создания словарей

# d_keys = ['hostname', 'locatio', 'vendor', 'model', 'IOS', 'IP']
# d_values = ['London_r1', '21 New Blobe Walk', 'Cisgo', '4451', '15.4', '10.255.01']
# d_r1 = dict(zip(d_keys, d_values))
# print(d_r1)


# d_keys = ['hostname', 'locatio', 'vendor', 'model', 'IOS', 'IP']
# data = {
#     'r1':['London_r1', '21 New Blobe Walk', 'Cisgo', '4451', '15.4', '10.255.01'],
#     'r2':['London_r2', '21 New Blobe Walk', 'Cisgo', '4451', '15.4', '10.255.02'],
#     'sw1':['London_sw1', '21 New Glob Walk', 'Cisgo', '3850', '3.6.XE', '10.255.101']
# }
# london_data = {}
# for key in data.keys():
#     london_data[key] = dict(zip(d_keys, data[key]))
# print(london_data)

#-------------------------------------------------------------
# all и any 

# all -> возвращает true если все элементы обьекта истинна или обьект пустой

# ls =[[1,2],False, 1, 'stroka', True]

# print(all(ls))

# ip = '10.255.0.0.1 '
# result = all(i.isdigit() for i in ip.split('.'))
# print(result)


# any - > возвращает True, если есть хоть один True


# ls = [0, 0, 0, '', 1 , False]
# print(any(ls))



# def ignor_command(comannd):
#     """
#     Функция проверяет есть ли в команде слово из списка  igonore. True - если есть, False - если нет такого слова .
#     """
#     ignore = ['rm - rd', 'alias', 'reset']
#     for word in ignore:
#         if word in comannd:
#             return True
#     return False

# print(ignor_command('sudo root user'))
# comannd = ''
# if ignor_command(comannd):
#     raise Exception('Invalid comannd')
# print('Vse OK')


# ignore = ['rm -rf', 'alias', 'reset']
# command = 'sudo rm -rf nano configurations'
# if any([word in command for word in ignore]):
#     raise Exception ('Invalid command')
# print('Vse ok')

#----------------------------------------------------------
# from random import choices
# from string import ascii_letters, digits
# from itertools import repeat


# quantity = int(input('Ведите количество паролей: '))
# print({
#     f(choices(ascii_letters, k=10), choices(digits, k=7)) for f in repeat(lambda x, y: ''.join(set(x+y)), quantity )
# })





def func_str(str_):
    vowels = 0
    consonants = 0
    symbols = 0
    
    for i in str_.lower():
        if i in "йуеыаоэяиюё":
            vowels += 1 
        elif i in "цкнгшщзмчвфжрлдтсп":
            consonants += 1
        else:
            symbols += 1
    return f'Количество гласных: {vowels}, согласных: {consonants}, символы: {symbols}'

print(func_str('Мэйкерс буткэмп !!!'))