# import random

# ls = ['plov', 'manty', 'kuurdak', 'lagman', 'dymdama']

# p=0
# m=0
# k=0
# l=0
# d=0
# for i in range(0,10000):
#     choice= random.choice(ls)
#     print(choice)
#     if choice.lower() == 'plov':
#         p= p+1#p+=1 инкремент 
#     elif choice.lower() == 'manty':
#         m+=1 
#     elif choice.lower() == 'kuurdak':
#         k+=1
#     elif choice.lower() == 'lagman':
#         l+=1
#     elif choice.lower() == 'dymdama':
#         l+=1

# # print(f'Plov:{p},\nManty:{m},\nKuurdak:{k}.\nLagman:{l}')
# dict_ ={'Plov':p, 'Manty':m, 'lagman':l, 'Dymdama':d}
# # print(dict_)
# res = sorted(dict_.items(), key=lambda x:x[1] )

# winner = res [-1]
# print(f'Побидило блюдо {winner[0]}, оно набрало: {winner[1]}')


#Counting Valleys Haccerrank
# def countingValleys(steps, path):
#     dolina = 0
#     sea_level = 0
#     for x in path :
#         if x  == 'U':
#             sea_level +=1
#              if sea_level == 0:
#                 dolina +=1
#         elif x ==  'D':
#             sea_level -= 1

#     return dolina
      
# # print(countingValleys)
# ls = [1, 2, 3, 4, 6, 7, 8, 9, 10]
# print(list(map(lambda x: x**2, ls)))
# list_ = [-1, 2, 3, 0, 5, -3, 7,]
# print (any(map(lambda x: x>0, list_)))


# list_ = [5, 8, 4, 6, 7]

# result = any(map(lambda num: num < 0, list_))

# print(result)


