# обработка исключений 
# операторы try..except

# ошибки -> ссвязанные с кодом:



# IndentationError
# TabError
# SyntaxError




# # исключения - > Invalid values:
# ZeroDivisionError
# ArithmeticError
# NameError
# IndexError
# KeyError
# ValueError
# ImportError
# BaseException  #проподитель всех ошибок



# try ... except
# try :
#     <body try>
# except : 
#     <body except>


# num1 = int(input('Ведите число :'))
# print(num1)
# print('очень важная строчка кода')


# try:
#     num1 = int(input('Ведите число :'))
#     print(num1)
# except:
#     print('Вы вели некоректные данные исправьте  это!!!')

# print('Очень важная строчка кода ')


# 1. import sys
# list_ = [1,2,3,4,5]
# index = int(input('Ведите индекс:'))
# try:
#     res = list_[index]
#     print(res)
# except :
#     import sys
#     print(f'oops , we catched {sys.exc_info()[0]} error!')




# 2. Exception as e
# list_ = [1,2,3,4,5]
# index = int(input('Ведите индекс:'))
# try:
#     res = list_[index]
#     print(res)
# except Exception as e :
#     print(f'oops, we catched {e.__class__} error')



# list_ = [1,2,3,4,5]

# try:
#     index = int(input('Ведите индекс:'))
#     res = list_[index]
#     print(res)
# except (IndexError, ValueError):
#     print('Вы вели некоректный индекс !!')
# except ValueError:
#     print('Вы вели некоректный индекс !!')


# else в trys...except
# finally в try.... except
# try :
#     <body>
# except:
#     <body>
# else:
#     <body>  #Сработает если в операторе трай не случилась ошибка
# finally:
#     <boddy> сработает при любом исходе

# try:
#     num1 = int(input('Enter :'))
#     num2 = int(input('Enter : '))
#     result = num1 / num2
# except ZeroDivisionError:
#     print('На ноль делит нельзя ')
# except ValueError:
#     print('ivalid symbols')
# else:
#     result = num1 / num2
#     print(result)
# finally :
#     print('Код закончился')





###################################################################################

# """"""""""
# try:
#     some code 1
# except:
#     some code 2
# # else: срабатывет если трай и ексепт не сработали
#        some code 3
#     dinally:
#     some code 4 всегда сработает
# """"""""""


# try :
#     num1 = int(input('Ведите число :'))
# except:
#     print('Вы вели не число !')

# try :
#     num1 =int(input('Ведите первое число'))
#     num2 =int(input('Ведите второе число'))
#     result = num1 / num2
# except ZeroDivisionError:           # голое исклюючения
#     print('На ноль делить нельзя')
# except ValueError:
#     print('Вы вели нечисло !')
# else:
#     print(result)
# finally:
#     print('Программа завершена')



# dict_ = dict.fromkeys(('makers', 'bootcamp', 'hello', 'dictionary'), 0)
# dict_ = {key: len(key) for key, val in dict_.items()}
# print(dict_)

# dict_.update({'except': 'Exception'})
# print(dict_)


# while True:
#     try:
#        key = input(' Ведите слово')
#        if key == 'exit':
#            break
#        dict_[key]+= 2
#     except (KeyError, TypeError):
#         print('такого ключа нет либо конкетенацию с числами нельзя')
    
#     else:
#         print(dict_[key])
#     finally:
#         print(dict_)



# list_ = [i for i in range(1, 31)]

# try :
#     index = int(input())
#     list_[index] = 'Makers'
# except IndexError:
#     print('Такого индекса нету')
# except ValueError:
#     print('Вы вели не число')
# else:
#     print('Нет ошибок')
# finally:
#     print(list_)



# try:
#     print(makers)
# except NameError  :
#     print('Вы не создовали переменную makers')




# raise (Вызываем исключение)

# number = int(input('Ведите число от 1 до 70 :'))
# if not number  in  range (1,71):
#     raise Exception ('Вы вели число , которое не находится в данном промежутке')

# print('Okey')
# b = 10
# c = 11
# try :
#      print(a)
# except NameError:
#     print('Вы не создавали переменную а')

# ##################################################


# try :
#     num1 = int(input('Ведите первое число :'))
#     num2 = int(input('Ведите второе число :'))
#     result = num1 / num2 
# except ZeroDivisionError :
#     print ('На ноль делить нельзя !')
# except ValueError:
#     print(' Вы вели не число!')
# else :
#     print(result)


# number = int(input())
# try:
#    a,b=map(int,input(f'Ведите первое число , \n второе через пробел :').split())
#    result = a+b
# except ValueError:
#     print('Вы вели не число либо, вы вели только одно число ')
# else :
#     print(result)



# dict_ = {'Name': 'John', 'Age': 21, 'Height': 182 , 'status': 'Не женат'}
# try:
#     print(dict_['Nam'])
    
# except KeyError:
#         print('Такого ключа нет')



# list_ = [True,1,2,4,5,7,12,'Name','John312']

# try:
#     print(list_[12])
# except IndexError:
#     print (' Такой элемент не существует!')

# try:
#    a,b=map(int,input(f'Ведите первое число , \n второе через пробел :').split())
#    result = a/b
# except (ZeroDivisionError, ValueError):
#     print('Вы вели не число или же на ноль делить нельзя !')
# else:
#     print(result)



# from logging import raiseExceptions


# bumajnik  = int(input ('Ведите сумму которая у вас сейчас есть в бумажнике :'))
# if  bumajnik <0 :
#     raise ValueError ('')


# try:
#     age = int(input('Ведите ваш возраст :'))
#     if age<18:
#         age1 = 18 - age
#         print(f'Увидемся через {age1} лет/ год')
# except ValueError :
#     print('Некоректный возраст')
# else :
#     print('Спасибо')
# finally :
#     print('Adiós amigo!')

# a,b=input('Ведите 1 значение: '),input('Ведите 2 значение: ')
# try: a=int(a); b=int(b)
# except: a=str(a); b=str(b)
# print (a+b)

# a = input('Ведите :').split()

# b = []

# for i in a:
#     try:
#        b.append(int(i))

#     except:

#      print("Данный элемент не является числом")

# print(b)