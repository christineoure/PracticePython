# clearing a python list
List_x = [1,2,3,4,5,6,7,8,9]
List_x.clear()
print(List_x)

#reversing a python list

# def reversed():
#      List_x = [1,2,3,4,5,6,7,8,9]
#      reversed_list =List_x[::-1]
#      print(reversed_list)
# reversed()

List_x = [1,2,3,4,5,6,7,8,9]
def reverselist(list):
   list= list.reverse()
   return list
print(reverselist(list))

# def Reverse(lst):
#     lst.reverse()
#     return lst
     
# lst = [1,2,3,4,5,6,7,8,9]
# print(Reverse(lst))