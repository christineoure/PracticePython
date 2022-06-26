#Finding the length of a string without using in-built functions
# from fcntl import LOCK_WRITE
# import string


# word ="My name is Oure"
# words="I'm famous"
# count1 = 0
# count2 = 0  

# for i in word :
#     count1=count1+1

# for j in words :
#     count2=count2+1

# if(count1<count2):
#     print("larger string is:")
#     print(words)

# elif(count1==count2):
#     print("both strings are equal")

# else:
#     print("larger string is:")
#     print(word)  

# Python3 program to count upper and
# lower case characters without using
# inbuilt functions

# def upperlower(string):

#     upper = 0
#     lower = 0

#     for i in range (len(string)):
#         if (ord (string[i])>=97 and
#             ord(string[i])<=122):
#             lower += 1

#         elif(ord (string[i])>=65 and
#              ord (string[i])<=90):
#              upper += 1

#     print('Lower characters = %s' % lower, 
#           'Upper characters = %s' % upper)

# string = "I love My School Activities"
# upperlower(string)

#alternativey you can do this

import re
import string


s = 'The husband is a Lion'
l,u = 0,0
for i in s:
    if (i>='a' and i<='z'):
        l=l+1 
    if (i>'A' and i<='Z'):    
        u=u+1

print('Lower case characters:',l)
print('Upper case characters:',u)
    
#write a python program to find sequence of one upper 
#case letter followed by a lower case letters


def match(text):
    pattern ='[A-Z]+[a-z]+$'
    if re.search(pattern, text):
        return True
    else: 
        return False

print(match('Oure'))
print(match('codeHive'))
print(match('mangoes'))
