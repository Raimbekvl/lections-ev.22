# list()(список массивь) - изменяемый тип данных ,который представляет собой колекцию каких либо обьектов .

# my_list = [1, 'string', False, None, [1,2,3]]

# print(my_list)
# print(type(my_list))

# 1. -> list(<iterable>)
# my_list = list('Hello world')
#  print (my_list)


# tuple_ = ("banana", 'apple', 'cherry' )
# print (tuple_)
# print(type(tuple_))

# my_list = list()
# print (my_list)
# print(type(my_list))

# 2. range() -> возвращает последовательность элементов (числа)
# a = list(range (0, 100, 2))
# print(a)

# 3. -> []

# my_list = [2,3,4434,1]
# print(type(my_list))

# print(dir(list))

# append(element) - добовляет элемент в конец списка
# list_ = [1,2,3]
# print (list_)
# list_.append(5)
# list_.append([1,2,3,4])
# print(list_)

# extend(element[interable]) -> расширяет список добовляет элемент в конец списка. 
# list_ = [1,2,3 ]
# list_.extend([1,2,3])
# print(list_)


# insert(<index>, <element>) -> берет и добовляет element по указонному индексу
# list_ = ['string', 2, 3, False]
# list_.insert(1, [1,2,3,None])
# print(list_)
# list_.insert(2,1)
# print(list_)
# print(list_[-1])
# print(list_[1][3])
# print(list_[2:5])
# print(len(list_))


# index(element, [star], [end])- возвращает индекс элемента
# ls = [1,2,33,3,4,5,5,7,2, 'hello']
# print(ls.index(5, 6))
# if 'hello' in ls:
    # print(f'"hello" is in list:{ls.index("hello")}')

# count (element ) - возвращает количество вхождений element в списке 
# ls = [1,2,3,4,5,5,5,5,5,1]
# result = ls.count(1)
# print (result)



# remove (element) -> удаляет эелемент , но если нет такого элемента в списке то выводит ошибку
# pop([index]) -  удаляет и возвращает элемент по индексу, но елси индекс не указан , то удаляет последний эелемент 


# list_ = [5,1,2,3,4,5]
# # list_.remove(5)
# # list_.remove(5)
# deleted = list_.pop(1)
# d = list_.remove(4)
# print(list_)


# print(deleted)


# sort([reverse=True/False], [key=<>])-> сортирует список.
# Если передан reverce = True то список будет отсортирован в убывающему порядке.

# ls = [5, 0, -2, -101, 102, 23, 1]
# print(ls)
# ls.sort(reverse=True)
# print(ls)

# ls = ['Hello', 'john', 'London', 'a']
# ls.sort(key=len, reverse=True)
# print(ls)

# ls = [1, 'h', 3]
# ls[1] = 2
# print (ls)
# del ls[-1]
# print(ls)






















