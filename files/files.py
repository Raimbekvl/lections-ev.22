#Работа с файлами
# Karetka - указатель
# Hello world

# # open(,Путь до вашего файла)
# file = open('/home/hello/Desktop/ev.22/files') #Абсолютный путь 
# file = open( 'Files.py')  #относительный путь 


# print(file)

# Режимы для работы с файлами 
# 1. r/r+ (read)
# 2. w/w+ (write)
# 3. a/a+ (append)

# t, b, x

# file = open('text.txt', 'r')
# data = file.read()
# data = data.split('\n')
# print(data)
# print(type(data))

# file = open('/home/hello/Desktop/ev.22/files/text.txt')
# data = file.readlines()
# print(data)
# file.close()



# file = open('text.txt', 'w')
# file.write('Hello World!\n My name is John Snow!\n, King!')
# file.close()



# file = open('text.txt', 'a')
# file.write('\nJohn Snow bastard and King')
# file.close()

# file = open('text3.txt', 'x')
# file.close()



# Контекстный менеджер


# with open('text.txt', 'r') as file :
#     data = file.read()
#     print(data)

# print(file) #Owibka

# write 
# writelines

# ls = ['Hello world', 'My name is John', 'I\'m 35 years old']

# with open('text.txt', 'w') as f:
#     f.writelines(line + '\n' for line in ls)
    
#file.tell()-> возвращает индекс где находится каретка (указатель)
# file.seek(<int>) -> Перемещает каретку(указатель) на указанный int(index)


#------------------------___------------------------------------------_______------------
# from PIL import Image
# import pytesseract 
# import re

# def get_imei_codes(list_images):
#     list_of_imei = []
#     for image in list_images:
#         string = pytesseract.image_to_string(image)
#         print(string)
#         list_of_imei.append(re.findall(r'IME.\d.\s\d+', string))
#         print(list_of_imei)
    
#     with open('imeicodes.txt', 'w') as file:
#         for x in list_of_imei:
#             for i in x:
#                 file.write(f'{i}\n')

# list_images = ['imei.jpg']
# get_imei_codes(list_images)









