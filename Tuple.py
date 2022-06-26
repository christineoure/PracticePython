mytuple = ('bears', 'lions', 'girraffes', 'ostrich')
print(mytuple)

atuple = ('fruits',)
print(atuple)

thistuple = ('seconds', 2007, True, 3.0)
print(type(thistuple))

#accessing items in a tuple using indexing
Mytuple = tuple(('apples', 'corriander', 'spinach'))
print(Mytuple[0])
print(Mytuple[1])
print(Mytuple[-1])

#negative indexing

Mytuple = ('apples', 'corriander', 'spinach','carrot', 'Kiwi', 'brocolli')
print(Mytuple[2:5])
print(Mytuple[0:-1])
print(Mytuple[0: ])
print(Mytuple[ :-1])
print(Mytuple[-5:-1])
print(Mytuple[-2:-1])
print(Mytuple[0:100])

#checking if an item exists in a tuple

if 'apples'  or'paper' in Mytuple:
    print(True)
else:
    print(False)

    #changing tuple into a list and adding items then converting it back to a tuple.
x = list(Mytuple)
print(x)
    #adding an item to the list
x.append('pawpaw')
print(x)
x[-1] = 'tomatoes'
x[1] = 'tangerines'
print(x)

#converting the list back into a tuple
Mytuple = tuple(x)
print(Mytuple)
  
#adding atuple to a tuple.

thistuple = ('seconds', 2007, True, 3.0)
atuple = ('fruits',)

thistuple += atuple
print(thistuple)

#when removing items from a tuple , you convert it into al list then remove the items
#and return the list into a tuple.

print(Mytuple)
a = list(Mytuple)
print(a)
a.remove('brocolli')
print(a)
a.remove('spinach')
print(a)

newtuple = tuple(a)
print(newtuple)

#deleting a tuple you use del keyword before the tuple.

del atuple


#Unpcking a tuple by convertig the items into variables.

fruits = ('oranges', 'bananas', 'mangoes')
(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)


#Using saterisk*
fruits = ('oranges', 'bananas', 'mangoes','strawberry')

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

#looping through a tuple
fruits = ('oranges', 'bananas', 'mangoes','strawberry')
for i in fruits:
    print(i)

thetuple = ('apples', 'corriander', 'spinach','carrot', 'Kiwi', 'brocolli')
for i in thetuple:
    print(i)

#looping through using indexes
fruits = ('oranges', 'bananas', 'mangoes','strawberry')
for i in range(len(fruits)):
    print(fruits[i])

thetuple = ('apples', 'corriander', 'spinach','carrot', 'Kiwi', 'brocolli')
for i in range(len(thetuple)):
    print(thetuple[i])

#Using a while loop.



sentence = "TheLordismyshepderdIshallnotwant"

half=len(sentence)//2
sentence1=(sentence[0:half]).upper()
sentence2=(sentence[half:]).lower()
print(sentence1 + sentence2)


