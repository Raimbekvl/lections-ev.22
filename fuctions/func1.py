# def <name_of_function>(<a, b> #параметры ):
#     <body>  #некий код, некая логика
#     <return #возвращаем что то>
# <name_of_function>(<5, 6>#аргументы)


# параметры функциии - переменные которые будут принимаеть наша функция,для того что бы мы смогли работать с данными которые передаются в эту функцию

# аргументы это данные которые мы передаем для параметров при вызове функции

# return нужен для того что бы функция что то возвращала , и для того что бы  мы могли работать с рузультатом действия функции, return является не обязательным оператором
# (то есть он возвращает None если не казать return)

# ls = []
# result = ls.append(1)
# print(ls)
# print('результат действия: ', result)

# result1 = ls.pop()
# print(ls)
# print('результат действия: ', result1)

# def sumTwoNums(num1, num2): #параметры
#     result = num1 + num2
#     # print(result)
#     return result

# sumTwoNums(5, 5) #аргументы

# def isEven(num):
#     if  num % 2 == 0:
#         return True
#     else:
#         return False

# a = 10
# b = int(input('Enter num:'))

# print(isEven(5))
# print(isEven(a))
# print(isEven(b))

#Анотации ##############################################################################################

# def isEven1(num:int) -> bool :
#     """
#     Наша функция проверяет является ли число ти int четным.
#     """
#     if num % 2 == 0 :
#         return True
#     return False
# isEven()
# isEven1()


# Anna, Ded, Kabak, Kazak  полиндромы
# from typing import List
# def get_polindrom(words: List[str]) -> List[str]:
#     '''функция фозвращает список из полиндромов'''
#     result = []
#     for word in words:
#         if word.lower() == word[::-1].lower():
#             result.append(word)
#     return result

# # a = input('Enter:')
# # print (get_polindrom(a))

# Some_words  = ['John', 'Ded', 'Ono', 'Kazak', 'Piter', 'Dovod', 'Julia', 'Mama']

# print(get_polindrom(Some_words))


# def func():
#     print('Hello World!')

# func()

#_________________-___________________________________________________
# default params(дефолтные параметры)

# def print_welcome(name:str = 'User123') -> str:
#     print(f'Welcome, {name} !')

# print_welcome()

'''Напишите функцию которая будет возвращать ваш депозит через определенное время с процентом 10 %, возвращать финально количество денег  минимальная ставка 30000'''

# def procent (num1) :
#     result = num1


# p,x,y=int(input('Проценты')),int(input('Сумма ')),int(input('')); from math import floor
# print((100*x+y+p/100*(100*x+y))//100, floor((100*x+y+p/100*(100*x+y))%100))


# def get_percentage (money: float, period : int) -> float:
#     '''Return final amount of money !'''
#     if money < 30000 :
#         raise Exception ('Вы вели некоректное количество денег, минимальная ставка денег 30000 сом!')
#     if period <3:
#         raise Exception('Вы вели некоректный срок для депозита, минимальный период вложения 3 года!')
#     i = 0
#     while i < period:
#         money = money +(money * 0.1)
#         #money * 1.1 / money+(money/100) * 10
#         i += 1 # i = i + 1
#     return money  

# money = float(input('Ведите  сумму :'))
# year = int(input('Срок вашего депозита :'))
# print(get_percentage(money,year))


# 'Hello world! My name is John, last name is Snow. Nice  to meet you'
# from unittest import result


# a = 'Hello world! My name is John, last name is Snow. Nice  to meet you'
# print(john(a))




# def get_reverse_string(text:str) -> str:
#     '''return reversed string*'''
#     spisok = text.split(' ')
#     result = '' .join(spisok[::-1])
#     print(result)
#     return result

# get_reverse_string('Hello world! My name is John, last name is Snow. Nice  to meet you')





# def numbers (num1,num2) :
#   result = num1 + num2 
#   return result
# num1= 10
# num2= 5
# print(numbers)
# def sumTwoNums(num1, num2): #параметры
#     result = num1 + num2
#     print(result)
#     # print(result)
#     return result

# print(sumTwoNums(5,10))


# from defer import return_value


# def stroki(a):
#     return len(a)
# print(stroki('Makers bootcamp it is cool !!!'))



# def numbers (num1:int, num2:int):
#   result =  num1 / num2 
# #   print(result)
#   return (result)
    
  

# num1 = int(input('Ведите число:'))
# num2 = int(input('Ведите число:'))
# print(numbers(num1,num2))

# print(dir(dict))
# def dict_(dict1):
#   for key in dict1.keys():
#     print(key)
    
      

# dict1 = {'one': 1, 'two': 2, 'thee': 3, 'four': 4}
# print(dict_(dict1))



# def numbers(a):
#     for i in a:



# a = [1,2,3,4,5,6,7,8]
# print(numbers(a))


####################################################
""""
def name_of_finction():
    some_code
    return variable
"""


# def function():
#     print('The funcrion is called')
#     return'Makers'

# print(function())

# def substract ():
#     num1 = 20
#     num2 = 5
#     print(num1+num2)
#     return num1 - num2

# print(substract())


# variable = substract ()
# print(variable)

# list_ = [1,2,3,4,5,6,7,8,9,10,11,12,13,14, substract()]
# print(list_)


# def substract ():
#     num1 = 20
#     num2 = 5
#     print(num1+num2)
#     return num1 - num2

# def function():
#     print("I'm calling substract function")
#     print(substract())

# print(function())


# def interval(a:int, b:int)->list:
#   list_=[str(x) for x in range(a,b) if x%2==0]
#   return list_
# a = int(input('Enter initial: '))
# b = int(input('Enter finally: '))
# print(interval(a,b))



# def walks(naprav):
#     res = False
#     x, y = 0, 0
#     if len(naprav) == 10:
#         for i in naprav:
#             if i == 'С': y += 1
#             if i == 'В': x += 1
#             if i == 'Ю': y -= 1
#             if i == 'З': x -= 1
#         res = True if x + y == 0 else False
#     return res
# dannye = ['С', 'Ю','В','З']
# import random
# naprav= []
# for i in random.randint(1,10):
#   naprav.append(random.choice(dannye))
# print(walks(naprav))

# or 

# def func(nap):
#     res = False
#     x, y = 0, 0
#     if len(nap) == 10:
#         for i in nap:
#             if i == 'С': y += 1
#             if i == 'В': x += 1
#             if i == 'Ю': y -= 1
#             if i == 'З': x -= 1
#         res = True if x + y == 0 else False
#     return res
# dannye = ['С', 'Ю','В','З']
# import random
# nap= []
# list=[]
# for i in range (10):
#     list.append(i)
# for i in list:
#   nap.append(random.choice(dannye))
# print(nap)
# print(func(nap))

# def func(num):
#     if num % 2 == 0:
#         return num // 2
#     return num * 3
 
 
# print('Четное-нечетное')
# for i in range(1, 11):
#     print(f'{i} -> {func(i)}')

# def numbers(num1:int,num2:int):
#     if  num1 > num2:
#         return('Num1 , bolshe')
#     else:
#         return('Num2, bolshe')

# num1 = int(input('Chislo 1 :'))
# num2 = int(input('chislo 2 :'))
# print(numbers(num1,num2))

# def even_or_odd(num:int)->str:
#   if num%2==0:
#     return 'It\'s even number'
#   return 'It\'s odd number'
# num = int(input('Enter number: '))
# print(even_or_odd(num))



# def get_polindrom(words):
 
#   for word in words:
#     if word.lower() == word[::-1].lower():
#       return  True
#     return False
# some_words = ["кок", "топот", "комок"]
# print(get_polindrom(some_words))




