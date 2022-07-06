# операторы сравнения 
# условные операторы 
# логические операторы 

# операторы сравнения :
# <,>.=(равно),<=,>=, !=(не равно)


# num1= 29
# num2= 19
# stroka1 = 'A'
# print(ord(stroka1))
# stroka2 = 'a'
# print(ord(stroka2))
# result = stroka1 > stroka2
# print (result)
# print(result)
# print (chr(1080))


# bool - true(1) or false(0)
# условные  операторы
# if 
# elif
# else

# if <conditional>:
#      если в if приходит True 
#      <body> if>
# elif <conditional>:
#      <body>
# else:
#     <body>

# string = input('Enter something: ')
# if string == 'Hello':
#     print('Hello stranger!')
# elif string == 'Mercedez':
#     print ('Mercedez-Benz S class')
# else:
#     print('Совпадений не найдено')

# print('Код закончился')


# sign up 
# email =input('Enter your email:')
# password1 = input('Enter passwor:')
# password2 = input('Enter password confirmation: ')

# if password1 != password2 :
#     raise Exception('password didn\'t match!!!')
# else:
#     print('Successfully signed Up!')


# age =  input ('Enter your age: ')
# print (type(age))
# if age.isdigit():
#     age = int(age)
# else:
#     print('Ведите коректные данные')
#     raise Exception ('Value error!')

# if age< 18: 
#     print(f'Чувак приходи через {18-age} года/лет!')
# else: 
#     print('Вы подходите по возрасту!  ')

#логические операторы
# 1. and -> логическое и 
# 2. or -> лог или 
# 3.not -> лог отрецание 

# my_age = 20
# your_age = 18
# result = (my_age ==20)and (your_age ==18)
# print(result)

# result= my_age > 18 or your_age ==20


# result = not my_age == 20
# print(result)



# is_user_google_user = True
# is_user_github_user = False

# if is_user_google_user and is_user_github_user : 
#     print('You can enter the system mr John Snow')
# else:
#     print('Sorry, you can should have Google and Github accounts!')


# # is_user_google_user = True
# # is_user_github_user = False
# # is_user_age_greater_21 = False
# # user_accounts_coins =8000

# # if is_user_google_user and is_user_github_user and (is_user_age_greater_21 or user_accounts_coins > 5000): 
# #     print('You can enter the system mr John Snow')
# # else:
# #     print('Sorry, you can should have Google and Github accounts!')



# # a = int(input('Ведите число'))
# # if a>5:
# #      print(True)
# # elif a<5:
# #     print(False)


# a = int(input ('ведите число'))
# if a>=90:
#     print('Отлично ваша оценка 5')

# elif a >=80:
#     print('Здорово ваша оценка 4')

# elif a>=70 :
#     print('Хорошо ваша оценка 3')
# elif a >= 60:
#     print('Вам стоит подучить материал')
# elif a <60:
#     print('Вам стоит подучить материал')
 


# a = int(input('Ведите число '))
# if a < 0:
#     print('Negative')
# elif a == 0 :
#     print('Zero')
# elif a > 0:
#     print('Pozitive')


# a = int(input())
# b = int(input())
# if a < b:
#     print(a)

# else:
#     print(b)


# a=int(input('Ведите число !'))
# b=int(input('Ведите число !'))
# c=int(input('Ведите число !'))
# if a>b>c:
#    print(c)
# elif a<b<c:
#     print(a)
# else:
#     print(b)


# a = int(input('Ведите первое число :'))
# b = int(input('Ведите второе число :'))
# c = int(input('Ведите третье число :'))
# if a==b==c:
#     print('3')
# elif a==b or a==c or b==c :
#     print('2')
# else :
#     print ('0')
    


# a = str(input('Ведите слово '))
# if a >=5:
#     print(True)
# elif  a <5:
#     print (False)


# a = int(input())
# b = int(input())
# if a%b == 0:
#     print("%d делится на %d" % (a,b))
# else:
#     print("%d не делится на %d" % (a,b))
#     print("Остаток: %d" % (a%b))
# print("Частное: %d" % (a//b))




# num = int(input('chislo :'))
# choice = input('Vsh vybor B/KB')
# if choice.lower == 'b':
#   print ('result:', num*8)
# elif choice.lower() =='kb':
#   print('result:',num / 8 / 1024)
# else :
#   print('Nekorektnyi Vybor')

# a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6}
# b = {}
# for i,v in a.items() :
#   if v %2 ==0 :
#       b[i] = 2
#   else:
#       b[i]= v
# print(b)



# a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6}
# b = {}

# for k, v in a.items():
#     if v % 2 == 0:
#         b[k] = 2
#     else:
#         b[k] = v

# print(b)


# a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}

# for g, v in list(a.items()):
#     if v == None:
#         a.pop(g)

# print(a)

# a = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}

# for k, v in a.items():
#     a[k] = v / 5

# print(a)


# a = {'Iphone 11':50000, 'Samsung Galaxy S 24ultra+': 900000 , 'Nokia S20 ultra pro edition': 150000}
# for k,v in a.items():
#     a[k] = v / 5
# print (a)




# a = {'Apple': 50, 'Banana': 24, 'Kiwi':32,'Cherry':41,'Orange':33}
# for k,v in list(a.items()):
#   if v% 2 == 0:
#     a.pop(k)
# print(a)
   

# print(dir(dict))

# dict={"a":1,"b":2,"c":3}
# inverse_dic={}
# for key,val in dict.items():
#     inverse_dic[val]=key

# numbers = {'a':2, 'b': 3, 'c': 4, 'd': 12}

# for k, v in list(numbers.items()):
#     del numbers[k]
#     numbers[v] = k

# print(numbers)


# a = {}
# print(type(a))
# b = dict()
# print(type(b))
# c = dict.fromkeys([])
# print(type(c))

# a = input('your name') 
# b = int (input('your age ?\n'))
# c = b +1

# print (f'{a} next birthday you will be{c}')

a = input('Enter your name:')
if len(a) >5 :
  print(a.lower())
else :
  print(a.upper())
