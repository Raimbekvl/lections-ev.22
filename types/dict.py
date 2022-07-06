#dictionary () - Словарь -> это упорядочная колеция элементов  (python3.7-> стал упорядочным (ordered) ). 
# каждый элемент  в словаре содержится в паре ключ : значение .


# ключи должны быть уникальными и не изменяемым типом данных (str, int,tuple etc.) Когда как значениеями могут выступать любые типы данных.





# thisdict = {
#     'brand': 'Ford', 
#     'model': 'Mustang',
#     'year' : 1964
#     }
# print(thisdict)
# print(type(thisdict))

# Hash tables , фссоцивтивный массив  , dictionary , object(Js)== dictionary(py)




# some_tuple = (1,2,3) класс tuple , литераллом тюпла является запятые 
# print(type(some_tuple))


#  способы создания 
# some_dict = {}
# print(type(some_dict))

# key_values = {'key': 'value', 'key1': 'Value1'}
# print(type(key_values))
# dict_created_with_function =  dict()
# print(type(dict_created_with_function))

# dict_ = dict((('key', 'value'), ('key2', 'value2')))
# print(dict_)
# print(type(dict_))



# --------------------------------------------------------------------
# from curses import use_default_colors
# from optparse import Values


# user_info = {
#     'First_name':'John',
#     'last_name': 'Snow',
#     'age': 24,
#     'email': 'johnsnow24@gmail.com',
#     'role': 'moderator',
#     'list': [1,2,3],
#     # [1,2,3]: 'list' error
#     'first_name': 'Raychel,'
# }
# print(user_info['First_name'])
# print(user_info.get('age'))
# print(dir(dict))
# print(user_info.items())
# for items in user_info.items():
#     print(items)

# print(user_info.keys())   #before changes

# user_info['height'] = 185 #after changes
# print(user_info.keys())  
# print (user_info)

# for keys in user_info.keys():
#     print(keys)

# for values in user_info.values():
#     print(values)

# pop() - удаляет элемент по определенному ключу 

# popitem() - Удаляет последнию пару в словаре


# print(user_info)

# user_info.pop('list')
# user_info.pop('email')
# user_info.popitem()
# user_info.popitem() 
# print(user_info)

# aetdefault(key, [default_value]) -  Рфботает так же как и гет (), но еслим такого ключа нет  то он создаст новую пару ключей

# # 1 способ применение получение значений
# dict_={'name': 'John', 'age': 23}
# result = dict_.setdefault('age')
# # print(result)


# 2 способ применение получение значений
# dict_={'name': 'John', 'age': 23}
# result = dict_.setdefault('address', )
# print(dict_)



# print(user_info)
# user_info.updatee({'First_name', 'Raychel'})
# user_info.update({'height': 185})

# print(user_info)


# user_info['First_name'] = 'Raychel'
# user_info['height'] = 185
# print(user_info)










# # ====================================================================================
# roles = {
#     0: 'Admin',
#     1: 'Moderator',
#     2: 'Vendor',
#     3: 'Customer',
#     4: 'Guest',

# }


# users = [
#     {
#         'id': 0,
#         'name': 'John',
#         'role': roles[0],
#     },
#     {
#         'id': 1,
#         'name': 'Raychel',
#         'role': roles[3],
#     },  
#     {
#         'id': 2,
#         'name': 'Aibek',
#         'role': roles[4],
#     }
    
# ]

# product = {
#     'id': 1,
#     'title': 'Samsung Galaxy S20', 
#     'discription': 'Loren Ipsum',
#     'price': 1000 
# }

# print(users)
# print(product)

# user_id=int(input('Enter your id:'))
# if users[user_id]['role'] == roles[0]:
#     product['discription'] = input('Enter new opisanie product:')
# else:
#     raise Exception('U vas ne dostatochno prav!!!')
# print(product)





# information = {'Name' : 'Misha', 'Age': 21, 'Email': 'misha21@gmail.com'}
# information.update ({'Name':'Andrei'})
# information.update ({'height': 172})
# print(information)




# information1 = {'Name' : 'Misha', 'Age': 21, 'Email': 'misha21@gmail.com'}
# information2 = information1.copy()
# print(information2)

# print(dir(dict))



