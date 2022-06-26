# def swapList(newList):
#     newList[0],  newList[-1] = newList[-1],  newList[0]
#     return newList

# newList = [1, 2, 3, 4, 5]


# print(swapList(newList))

# def swapList(list_x):
#     list_x[0], list_x[-1] = list_x[-1], list_x[0]

#     return list_x

# list_x = [10, 20, 30, 40, 50]

# print(swapList(list_x))

# # test_list = [good, better, best]

# # def replace_string():

# list_y =[1, 2, 3, 4, 5, 6, 7, 8]
# print(len(list_y))


# # def nums(a,b):
# #     for n in nums:
# #      print(n.max)

# # n= 3,6

# # def nums (a,b):
# #     if a>b:
# #         print(a)
# #     else:
# #         print(b)
# # nums(15, 30)




# list_c =[1, 2, 3, 4, 5, 6, 7, 8,9]
# print(len(list_c))
# list_c[3]=14
# list_c[0:2]=10, 20, 30
# print(list_c)
# list_c.append(10)
# print(list_c)
# list_c.extend([11,12,13])
# print(list_c)
  

# # listOdd=[1,2,3,4]


# #removing duplicates from  string


# word="He is a good boy"
# x=word.split()
# print(x)

# listx = [1,2,3,4,5,1,2,3,4,5]
# listy=[]
# for i in listx:
#     if i not in listy:
#         listy.append(i)
# print(listy)


# listz = [1,2,3,4,4,5,2,4]
# newList=[]
# for i in listz:
#     if i not in newList:
#         newList.append(i)
# print(newList)

# del listz[1:3]
# print(listz)


# for i in range(10,55):
#     if i%2==0:
#      print(i)
     
#     a= range.count(i)
#     print(a)



# contacts = [1,2,3,4,5,6,7,8,9]
# for i in range (1,9):
#         if i %2 == 0:
#             print(i)
# i
#             # x=contacts.count(i)
#             # print(x)

# from tkinter import N


# num1 = int(input("enter starting range"))
# num2 = int(input("enter ending range"))

# eve_count=0
# edd_count=0

# for i in range (num1, num2):
#     if i%2 == 0:    
#         eve_count += 1
#     else: 
#         edd_count += 1
# print(f"even number count is {eve_count}")
# print(f"even number count is {edd_count}")


#Removing letters
# from math import prod
# from optparse import Values


# a=['a','b','b','c','b','b','e','f','g','b','h','h','h','h']
 

# while 'b' in a:
#     a.remove('b')
# print(a)
    

    #write a python program to countthe occurrences osf a specific number in a list.
# int(input(enter a number)):
# num= int(input("enter a number"))
# list_x=[1,2,34,2,56,2,78,2,97,2,99,2]
# count=0
# for i in range(len(list_x)):
#     if list_x[i] == num:
#         count+=1
# print(count)

#write a python program to check the first and the last elements of the list is the same or not. if same Print True else false.

# list_p =[10,54,65,83,10]
# # for i in list_p:
# if list_p[0] == list_p[-1]:
#         print(True)
# else:
#         print(False)

#Given two integrers return their product if the product is greater than 500, then return their sum

# def nums(a,b):
#     product=a*b
#     sum=a+b
#     if product>500:
#         print(True)
#     else:
#         print(sum)

# nums( 5 ,20)

#write a python program that counts the number of occurrences of a specific word in a string

# from re import A


from ctypes import pointer


word = "Adam is a boy and Adam loves to play cricket"
# a=input("Enter a word")
x=word.split(" ")
print(x)
# count=0
# for i in range(len(x)):
#     if x[i]==a:
#         count+=1
# print(count)



# pointer = 0
# array = [10,30,,50,70,100]
# print