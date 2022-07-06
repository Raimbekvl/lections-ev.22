# """
# tuple- это структура данных
# неизменяемый 
# индексируемый
# упорядочный

# """


# string1 = str('Hello AttackPython')
# string2 = 'hello world'
# list1 = list(i for i in range (5))
# list2 = [1,2,3,4,5]
# set1 = {1,2}
# dict1 =  {"key": "value"}


# tuple1 = (1,2)
# print(type(tuple1))





# tuple1 = 1,2
# print(tuple1[1])
# print (type(tuple1))
# tuple1 [0] = 3
# print(tuple1[0])



# tupl1 = 1,2
# tuple2 = (1,)
# tuplr3 = tuple([1,2,3])
# tuple4 = tuple(range(5))
# print(range(5))

# emails = ["Python@gmail.com", "Tima@mail.ru"]

# emails1 = ("Python@gmail.com", "Tima@mail.ru", 3, 5, ["potato", 'arbuz', 'apple'])
# print(type(emails1[-1]))
# last_object = emails1[-1] # list
# last_object.append("Tomato")
# print(last_object)
# print(len(emails1))




# print(dir(tuple)) #имеет 2 метода



# #
# tuple_sequance_first = (2, 2, 3, 4)
# tuple_sequance = tuple(range(5))
# tuple_sequance += tuple_sequance_first
# print(tuple_sequance.count(2))


# tuple_sequance_first = (2, 2, 3, 4)
# tuple_sequance = tuple(range(5))
# # print(tuple_sequance)
# # indx = tuple_sequance.index(3)
# # print(tuple_sequance[indx])


# for value in tuple_sequance:
#     print(value)


# names = ("Tima", "Zhanylai", "Aidana", "Bermet", "ermek")
# names_enter = ["Bermet", "Ermek"]
# # print(names [0] + " Hello!")
# for name in names:
#     if name in names_enter:
#         print(f'hello{name.capitalize}')
#     else:
#         print(f"{name} go home!!!")
#     print(f'hello {name.capitalize()}!!!' )
    


# names = input ('Enter names :').split(" ")

# print(names)

# 
# first_step_names = []
# names = input ('Enter names :').split(" ")

# for name in names :
#     if len(name) > 4:
#         first_step_names.append(name)
#         print(first_step_names)


        
# print('start for')
# for i in range(10):
#     print(i)
# print('stop for')

# i = 0

# while 3 > 2:
#     print(f'{i} i work')
#     i +=1


# i =0
# num = 3 
# while num > i:
#     print(' i work')
#     i +=1

# # Ряд Фибоначчи от 1 до 100
# Max = 100
# x1 = 1
# x2 = 1
# x3 = x1+x2
# A = [x1,x2,x3] # создать список из чисел

# while x3<=Max:
#     x1=x2
#     x2=x3
#     A+=[x2]
#     x3=x1+x2
# print("A = ",A)


# a = list(range (0, 100, 2))
# b = list(range (1, 100, 2))
# a.append (b)
# print ('Updated list:',a )


# a = []
# for i in range(1,11):
#     a.append(i)
# print(a)

# a = list(range(29))

# for i in a:
#     if i <7:
#         print(i)

# a = list(range(29))
# for elem in a:
#     if elem < 28:
#         print(elem)    


# my_lst1 =['абажур', 'люстра', 'компьютер']
# my_lst2 = []
# letters = ['б', 'к']
# x = str
# for i in range(0, len(my_lst1)):
#     x = my_lst1[i]
#     for k in range(0, len(x)):
#         for s in range(0, len(letters)):
#             if x[k] == letters[s]:
#                 my_lst2.append(x)
#         if len(my_lst2) > 0:
#             for q in range(0, len(my_lst2) - 1):
#                 if my_lst2[q] == my_lst2[q+1]:
#                     my_lst2.remove(my_lst2[q])
# print(my_lst2)








# a = [1,2,3,4,5,6,7,8,9,10]
# for i in a:
#     print(i*2)


#списки лист list
# numbers1 = []
# numbers2 = list()


# print(type(numbers1))
# print(type(numbers2))



# numbers4 = [1,2,3,4]
# numbers5 = list(numbers4)
# print((numbers5))


# numbers = [ 7,7,7,7,7,7]
# numbers2 =[7] * 6
# print(numbers)
# print(numbers2)

# функция range
#1. range(end)
# numbers = list(range(10))
# print(numbers)

# #2. range (start, end)
# numbers = list(range(1,10))
# print(numbers)


# #3. range(strart, end step )(начало , конец , шаг)
# numbers = list(range(2, 10, 2)) # четные , нечетные с шагом
# print(numbers)
# numbers = list(range(1,10, 2))
# print (numbers)


# #циклы for
# for i in range(1, 11): #-> 1,2,3,4,5,6,7,8,9,10
#     print (i**2) #возводит в степеьн цикл 

#операции над списком 
"""сравнение списко"""

# numbers1 = [1, 2, 3, 4 ,5, 9] # до 9 идет сравнение 
# numbers2 = [1, 2, 3, 4, 5, 9, 100, 34, 10000]
# print(numbers1 < numbers2)


# numbers = [1, True, 'Makers', 'hello', 8.9, ]
# print(numbers)

#индексация
# numbers = [1, True, 'Makers', 'hello', 8.9, ]
# numbers[3] = 'Bootcamp'
# numbers[-1] = {-1:'a'}
# print (numbers) можно изменять по индексу кроме не существуюещего



# print(numbers[0])
# print(numbers[2])
# print(numbers[1])
# print(numbers[4])




# users = ['Alice', 'Sam', 'Carly']

# for user in users :
#     print(f'Hello {user}')
# for letter in 'Makers':
#     print(letter.upper())

#методы списков

#append(добовляет элемент в конеу списка)
# users = ['Alice', 'Cat', 'Billy']
# user = 'Tom'
# users.append(user)
# users.append(100)
# print(users)
# print(users[-1])

# guests = []
# list_length = int(input('Enter number of guests '))
#                 #5
# for i in range(list_length):
#     guest = input('Enter guest name:')
#     guests.append (guest)

# print(guests)


# name = []
# list_= 'Raim', 'John'
# for i in (list_):
#     name.append(list_)
# print(name)


# # extend (list) (расширает список за счет другого списка)
# users1 = ['Alice', 'Sam']
# users2 = ['Bob', 'Tom']
# users1.extend (users2)
# print(users1)
# print(users2)


# users2.extend(['John', 'Aibek'])
# print(users2)


#insert добовляет по индексу(index, element)
# users = ['John', 'Lenny', 'Andy', 'Anna']
# users.insert(1, 'Raychel') #добовляет между не удаляя
# print(users)

# numbers1 =[1,2,3,4,5,6,9]
# numbers2 = []
# numbers2.extend(numbers1)
# print(numbers2)

# a = []
# b = list(range(29))
# for i in (b):
#     a.append (b)

# print(a)

# a = [1,2,3,4,5,6,7,8,9]
# print(a[0])
# print(a[-1])



























