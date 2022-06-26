# #Concatenating two strings
# from pickletools import string1


# string1=input("Enter a string")
# string2=input("Enter a string")

# string3=string1+string2
# print(string3)

# #swaping a number

# a=float(input("Please Enter a Number"))
# b=float(input("Please Enter a Number"))
# temp = a
# a = b
# b = temp

# print("After Swapping ")



#string methods using unbuilt functions

# Python code to demonstrate working of
# find() and rfind()

# string = "my name is Oure and Oure is me."
# string2 = "Oure"

# print('The first occurrence of string2 is at:', end="")
# print(string.find(string2, 3))

# print('The last occurrence of string2 is at:', end="")
# print(string.rfind(string2, 3))

# str = "I'm on a ponny and the ponny is mine"
# str2 = "ponny"

# print("The first occurrence of str2 is at:", end="")
# print(str.find(str2,4))

# print("The last occurrence of str2 is at:", end="")
# print(str.rfind(str2,4))

# str1 = "the bike is your's and the car is your's too"
# str11 = "your's"

# print("The first occurrence of str11 is at:", end ="")
# print(str1.find(str11, 3))

# print("The last occurrence of str11 is at:", end ="")
# print(str1.rfind(str11, 3))

# Python code to demonstrate working of
# startswith() and endswith()

str = "The"
strB = "The book is very interesting"

if strB.startswith(str):
    print("strB begins with:" + str)
else:
    print("strB does not begin with:" + str)
#finding whether the string ends with the give prefix
if strB.endswith(str):
    print("strB ends with:" + str)
else:
    print("strB does not end with:" + str)


#checking whether the string is uppercase or lwercase

stringA = "AkiraChix"
stringB = "akirachix"
stringC = "AKIRACHIX"

if stringC.isupper():
    print(True)
else:
    print(False)

if stringC.islower():
    print(True)
else:
    print(False)

#converting strings to lower and upper case.

mystring = "This apple is sweet"

print(mystring.lower())
print(mystring.upper())
print(mystring.swapcase())
print(mystring.title())