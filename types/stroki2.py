# Методы строк

# dir() -  функция которая вытаскивает методы типов данных


# print(dir(str))

# '<соединитель>'.join(<массив который нужно соединить>) - Соединяет массив из строк по соединителю в одну строку.
# ls = ['milk', 'bread', 'water', 'Apple']
# joined = '!'.join(ls)
# print(joined)


# split(разделитель) ->  Дробит строку по разделителю и возвращает тип данных list.
# text = 'Milk, water, Apple'
# splited = text.split(', ')
# print (splited)
# joined = ', '.join(splited)
# print (joined)



# replace (<old value>, <new value>, [count]) -> Меняет в строке значение олд на ню value  если вы 
# укажите count он заменит count раз


# text = 'ha ha ha ha '
# result = text.replace('h', 'la')
# print(result)



# text = '#makers#bootcamp#программирование#it#курсы'
# result = text.replace('#', " ")
# print (result)




# strip() - убирает пробельные символы в начале и в конце  строки.

# rstrip() в конце удаляет
# lstrip()- В начале удаляет

# text = input('Ведите ФИО: ')

# print(text.lstrip())
# result = (text.lstrip())
#  print(text)

# count('simbol') -> считает колтчество вхождений <simbol> в строку


# text = 'Hello world! I\'m from Earth!'
# result = text.count('o')
# print(result) 




# index('< value>'. [start], [end]) -> выводит индекс значение value в нашей строке .
# text = 'Hello world! This is Makers!'




# year = int(input('Ведите число :'))
# if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
#     print('YES')
# else:
#     print('NO')

# num = int(input ('chislo :'))
# choice = input('Vsh vybor B/KB')
# if choice.lower == 'b':
#   print ('result:', num*8)
# elif choice.lower() =='kb':
#   print('result:',num / 8 / 1024)
# else :
#   print('Nekorektnyi Vybor')

# a = input ('Ведите текст :')
# b = "Hi"
# if a == b:
#     print('Привет !')
# else:
#     print('No')

# a = int(input('Первое число'))
# b = int(input( 'Второе число '))
# if a%b == 0:
#     print("%d делится на %d" % (a,b))
# else:
#     print("%d не делится на %d" % (a,b))
#     print("Остаток: %d" % (a%b))
# print("Частное: %d" % (a//b))





