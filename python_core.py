#Real original, i know
print("Hello world")
#print first character
print("Hello"[0])
#removes leading and tailing characters, blank for whitespace removal
print(("l Hello l").strip())
#uppercase
print(("hello").upper())
#replace
print(("hello").replace("l","r"))
#compare
telling_the_truth = True
telling_a_lie = False
print(telling_the_truth == telling_a_lie)

#data structures, their differences
#lists are ordered, mutable and allow repetations
list_example = ["rollerblades", "longboards", "windsurfs","rollerblades"]
print(list_example)
#lists can become a stack o follow lifo logic
stack_example = list_example
stack_example.pop()
stack_example.append("snowboards")
stack_example.append("skis")
print(stack_example)
#lists can also become queues to follow fifo logic, seems to be the fastest way to handle lists with fifo logic
from collections import deque
queue_example = deque(list_example)
queue_example.append("ice-skates")
queue_example.popleft()
queue_example.popleft()
queue_example.popleft()
print(queue_example)
#tuple are immutable
tuple_example = ("Pancake", "Sausage", "Apple")
print(tuple_example)
#empty = () empty tuple
#singleton = 'hello', tuple with one element, useful if you wanna combine tuples? or multiply them with each other?
#tuple packing and unpacking
t = 1234,4321,'hello'
print(t)
x,y,z = t
print(x)
#sets
set_example = {'nut','wulnut','corn','nut'}
print(set_example)
print('nut' in set_example)
char_set_example = set('abracadabra')
print(char_set_example)
#dictionaries
dict_example = {'Sonic':15,'Knuckles':16}
dict_example['Tails'] = 12
print(dict_example)

#branches
if 2<1:
    print("Won't happen")
elif 2>1:
    print("True, so gets printed")
else:
    print("wont even be considered since elif is True")
#branch_tricks
#print("Bazooka") if 1>0 elif 1<0 print("what?!") else print("Rocket") Ternary operators dont work with elif
print("Bazooka") if 1>0 else print("Rocket")
#better example, thx w3Schools
a = 330
b = 330
#this is how elif works here, the else ... if would be elif a==b:print("="), so the next line is an if a>b:.....elif a==b:....else Ternary operator
print("A") if a>b else print("=") if a==b else print("B")
#not wasting time for logical operators and, not, or

#loop, their differences
x = 0
while x< 10:
    print(x)
    x+=1 
    if x>5:
        break
for item in list_example:
    print(item)
#get type of variable
print(type(x))

#functions
#hello_function() wont work here, reads up-down
def write_function(word):
    print(word)
write_function("Yo")
#give a function a tuple
def give_me_tuple(*games):
    print(games)
give_me_tuple("Sonic_The_Hedgehog","Sonic_The_Hedgehog2","Sonic_The_Hedgehog3")
#give function a buch of keyword arguments
def give_me_keyword_arguments(game1,game2,game3):
    print("The best console ever: " + game3)
    print(type(game3))
give_me_keyword_arguments(game1 = "PS2", game2 = "NES", game3 = "Switch")
#give functio a dict
def give_me_a_big_fat_dict(**names):
    print("Name of our daughter will be: " + names["lname"])
give_me_a_big_fat_dict(fname = "Anna", lname = "Horváth")
#default def value
def my_favourite_milkshake_is(milkshake = "Strawberry"):
    print("My fave milkshake is "+ milkshake)
my_favourite_milkshake_is("Vanilla")
my_favourite_milkshake_is()
#return from function
def add_5_to_it(number_to_be_added_five_to):
    return number_to_be_added_five_to + 5
print(add_5_to_it(3))
#main difference of recursion and iteration: call frames
def recursion_example(k):
    #print("step-by-step "+str(k))
    if k>0 :
        result = k+recursion_example(k-1)
        #print("step-by-step "+str(k))
        #print("step-by-step "+str(recursion_example(k-1)))
        print(result)
    else:
        result = 0
    return result
recursion_example(6)
def recursion_example2(m):
    if m<10:
        #print(m)
        result = m+recursion_example2(m+2)
        print(result)
    else:
        result = 0
    return result
recursion_example2(0)

#Classes (lambda other day)
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return round(math.pi * self.radius ** 2,2)

circle_1 = Circle(2)
print(circle_1.radius)
print(circle_1.calculate_area())

#git reminder for remote origin master setting: just add .git at the end of the hyperlink


