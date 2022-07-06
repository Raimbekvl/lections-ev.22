# области видимости и пространсто имен

# built-in (Встроенная )- print, len, max, int
# global (Глобальная) 
# Enclosed (не локальная, nonlocal охватывающая) #внутри функции
# local (Локальная область видимости )

# def print_list(some_list):
#     for element in some_list:
#         print(element)
# element ='q'
# print(element)
# print_list([1,2,3,4,5])




# a = 10 # global
# print #built-in
# def hello(): #global
#     a = 'Hello world' #local
#     print(a, 'local inside at func')

# hello()
# print(a, 'global')

# x = 'Global'
# print(x, '1')  #1 global
 
# def enclosed():
#     x = 'enclosed'
#     def local():
#         x = 'local'
#         print(x,'3') #local
#     print(x, '2')
#     local()
#     print(x, '4')#enclosed

# enclosed()
# print(x, '5')#global



# def func():
#     print(a)
    
# a = 'str'
# func (a)


# num = 10
# def func():
#     def inner_func():
#         print(num)
#     inner_func()

# func()

 
# var = 100 #global variable
# def increment():
#     var = var + 1 #Try to update a global
#     # variable(using increment ->  var+=1)
# increment()


# global -> позволяет менять значение глобальной переменной находясь в локальной области видимости . 
# nonlocal -> позволяет менять значение  не локальной переменной находясь в локальной области видимости 

# var = 100
# def increment():
#     global var
#     var+= 1


# print(var)
# increment()
# increment()
# increment()
# print(var)


# def counter():
#     num = 0
#     def increment():
#         nonlocal num
#         num += 1
#         return num
#     return increment

# c = counter()
# print(c)
# print(c())
# print(c())
# print(c())
# print(c())




# # print(dir(__builtins__))

# print(abs(-15))#стандартный вызов  встроенной функции

# abs = 15 #переопределяет имя fbs в глобальной области
# del abs
# print(abs(-15))



# list_ = [[1,2,3], [3,35]]
# sums = []
# for x in list_:
#     sums.append(sum(x))
# print(sums)
# print(max(sums))


# res = max([sum(x) for x in list_])
# print(res)
#---------------------------------------------------------------------------------

# alice = [13, 15, 38]
# john = [5, 15, 50]
# def func(a,j):
#     score_a = 0
#     score_j= 0
#     for i in range (0, len(a)):
#         if a[i] > j[i]:
#             score_a +=1
#         elif j[i]> a[i]:
#             score_j +=  1
#         else:
#             pass
#         return {'Alice': score_a, 'John': score_j}
# print(func(alice, john))
# print(func[13,15,38],[5,15,30])
 



# str_ = 'Hello'
# list_ = [i.count for i in str_]
# print(list_)


# str_ = 'hello world'
# dict_ = {key: str_.count(key) for key in  in str_}
# print(dict_)


 
 
# counter = 0
 
# def increment():
#     global counter
#     counter = counter + 1

# increment()
# print(counter)

# increment()
# print(counter)

# increment()
# print(counter)


#     bar()
#     print("переменная в foo: ", var)

# foo()
# print("переменная в foo: ", var)


# def foo():
#     var = 'переменная foo'
#     print('переменная в foo: ', var)
     
#     def bar():
#         global var
#         var = 'переменная bar'
        
#     bar()
# foo()
# print('переменная в foo: ', var)
# balance = 0

# def get_salary(amount):
#     global balance
#     balance += amount

# def pay_bills(amount, log_name):
#     global balance
#     balance -= amount
#     print(f'Вы заплатили {amount} сом за {log_name}')

# def get_balance():
#     print(f'У вас на счету {balance} сом')

# get_salary(1000000)
# get_balance()
# pay_bills(450000, 'аренду дома')
# get_balance()