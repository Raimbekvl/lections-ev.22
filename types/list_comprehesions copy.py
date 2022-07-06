
# 1 
# list_ = list(range (0,200))
# list_1 = list_[::2]
# list_2 = []

# for i in list_1:
#     list_2.append(i)
# print(list_2)

# 2 task
# ls = [x for x in range(0,200) if x % 2==0 and x % 3 ==0]
# print(ls)

# 3 task

# ls = []
# for i in range(0,100):
#     if i%2==0:
#         i.append(i**2)
#     elif i%2!=0:
#         ls.append(i)
# print(ls)

# ls = [x**2 if x%2==0 else x**3 for x in range(0,100) ]
# print(ls)



#####################################################################################################################################################################
# Генераторы списков (list comprehenssions)



# newlist  = [expression for item in  iterable <if condittion==True>]
# list - comprehenssion - это упрощенный подход к созданию списка который задействует цикл for , а также конструкции if - else для определения того , что в итоге добавлено в наш список.


# ls = []
# for i in range (0,100, 2):
#     ls.append(i)
# print(ls)

# new_list = [i for i in range(0,100,2)]
# print(new_list)



# ls = [i**2 for i in range(0,11)]
# print(ls)



# fruits = ['apple', 'banana', 'kiwi', 'mango', 'limon']
# ls = [x.capitalize() for x in fruits]
# print(ls)

# ls = [x for x in fruits if x == 'cherry']
# print(ls)

# ls = [x for x in  fruits if x != 'apple'] 
# print(ls)


# list_ = [[1,2,3], [4,5,6], [7,8,9]]
# ls = []
# ls = [1,2,3,4,5,6,7,8,9]
# for inner_list in list_:
#     for num in inner_list:
#             ls.append(num)
# print(ls)

# ls = [x for inner_list in list_ for x in inner_list]
# print(ls)

import datetime
from random import random


# start = datetime.datetime.now()
# ls = [x for x in range(1,1000_000)]
# ls = []
# # for x in range(1,1000_000):
# #     ls.append(x)
# finish = datetime.datetime.now()
# print(finish-start)


# ls = [x+10 if x ==8 else x+1 for x in range(0,10)]
# print(ls)

# ls = [x**2 for x in range(0,25)]
# print(ls)
# str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# ls = [int(x) for x in str_list]
# print(ls)


# import random

# list1 = [1,2,3,4,5,6,7,8,9,10,True, 'Makers', 'Bootcamp', 'E.v. 22']
# rand_items1 =random.sample(list1, 10)
# rand_items2 = random.sample(list1, 10)

# set1 = {x for x in random.sample(list1, 10)}
# set2 = {x for x in random.sample(list1, 10)}
# print(set2)
# print(set1)
# new_set= set1.union(set2)
# print(new_set)

# if len(new_set)<20:
#     print(f'в этом сете было {20-len[new_set]} повторения длинна  состовляет 17')
# else:
#     print('Ваше обьедененное множество было уникальным !')

# names = ['Raim', 'Igor','Ermek','John', 'Sanjar','Temirlan', 'Raychel', 'Ivan', 'Pasha', 'Julia']
# ls = ['shorter 'if len(name)<=4 else 'longer' for name in names]
# print(ls)



# my_dict = {'first': {'a': 1}, 'second': {'b':2}}
# result = {key: value for key, v in my_dict.items() for value in v.values()}
# print(result)




# text = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
# ls = [x for x in text if x.isdigit()]
# print (ls)