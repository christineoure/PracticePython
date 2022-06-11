#dictionaries in Python 
# class MyClass:
#     x = 5
# print(MyClass)

# p1 = MyClass()
# print(p1.x)
#dictionaries in Python 

def dictionary():
    given_dict = {'0':1, '1':2, '2':3}
    print(given_dict.keys())
    for a in given_dict.keys():
        return f"Value of key 0 is ,{given_dict['0']}"

dictionary()

dict={'0':"value 1", '1':"value 2"}
print(f"value key 0 is {dict['0']}")
print(f"value key 0 is {dict.get('0')}")


user_input = input("")
user_input()
split_user = user_input.split()