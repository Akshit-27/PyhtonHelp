##This is a single line comment

"""
This
is
multiline
comment
"""

##Line Continuation

Total = 1 + 2 + 3 + 4 + 5 \
        + 6 + 7 + 8 + 9 + 0
print("Total = ", Total)

# Multiple statements on a single line.

x = 5;
y = 10;
z = x + y;
print("z = ", z)

# Type Interface

var = 10
print(type(var))
var = "Hello World"
print(type(var))
var = 3.14
print(type(var))

# declaring a variable & assigning value

name = "Jack"
age = 25
height = 6.1
isAdult = True

print("Name is ", name)
print("Age is ", age)
print("Height is ", height)
print("isAdult is ", isAdult)

# age = input("Enter You Age: ")
# print("Your Entered : ",age)

print("----------------------------------------------------------------")
Num_1 = 15
Num_2 = 23

add = Num_1 + Num_2
sub = Num_1 - Num_2
mul = Num_1 * Num_2
div = Num_2 / Num_1
floor_div = Num_2 // Num_1
mod = Num_2 % Num_1
expo = Num_1 ** 2

print("Addition : ", add)
print("Subtraction  : ", sub)
print("Multiplication : ", mul)
print("Division : ", div)
print("Floor Division : ", floor_div)
print("Modulus : ", mod)
print("Exponential : ", expo)
print("----------------------------------------------------------------")
age = 10
if age < 12:
    print("You are a kid")
elif age < 18:
    print("You are a teenager")
else:
    print("You are adult")
print("----------------------------------------------------------------")
number = 12
if number > 0:
    print("Positive Number")
    if number % 2 == 0:
        print("Even")
    else:
        print("odd")
else:
    print("Negative Number")
print("----------------------------------------------------------------")
# Assignment for Operators & Conditional Statements

# num1= float(input("Enter num1"))
# num2= float(input("Enter num2"))
# operation = input("Enter + or - or * or / or // or % or **")
#
# if operation == "+":
#         print(num1+num2)
# elif operation == "-":
#         print(num1-num2)
# elif operation == "*":
#         print(num1*num2)
# elif operation == "/":
#         print(num1/num2)
# elif operation == "//":
#         print(num1//num2)
# elif operation == "%":
#         print(num1%num2)
# elif operation == "**":
#         print(num1**num2)
# else:
#         print("Invalid Operation")
#
print("----------------------------------------------------------------")
# for loops

for i in range(10, 0, -1):
    print("i = ", i)
print("----------------------------------------------------------------")
# While loops
count = 0
while count < 6:
    print(count)
    count = count + 1

print("----------------------------------------------------------------")
# break & continue statements

for i in range(20):
    if i == 10:
        break
    print("Loop Number :", i)
print("----------------------------------------------------------------")
for i in range(10):
    if i % 2 == 0:
        continue
    print("Odd Numbers are", i)
print("----------------------------------------------------------------")
##Netsed FOR loop

for i in range(3):
    for j in range(2):
        print(f"i : {i} and j : {j}")
        print("j++")
    print("i++")
print("EOWL")

print("----------------------------------------------------------------")
# Example of FOR & WHILE loop
##Calculate the sum of first n natural number

n = 10;
sum = 0;
count = 1
while count <= n:
    sum = sum + count
    count = count + 1
print("Sum of first ", n, "numbers is = ", sum)
print("----------------------------------------------------------------")
res = 0
for i in range(20):
    res = res + i
print(res)
print("EOFL")
print("----------------------------------------------------------------")

### List in Python.

myList = []
print(type(myList))
fruits = ["Apple", "Banana", "Chiku", "Mango", "Cherry"]
print(fruits)
print(fruits[2])
print(fruits[1:4])
print(fruits[1:])
print(fruits[-1])

fruits.append("Kivi")  # add the passed element at the end of the list
print(fruits)

fruits.insert(1, "Grapes")  # add the passed element at the index 1st
print(fruits)

fruits.remove("Chiku")  # removes the first occurrence of the passed element
print(fruits)

popped_fruit = fruits.pop()  # removes & returns the last element of the list.
print(popped_fruit)
print(fruits)

indexMango=fruits.index("Mango") # returns the first index position of the element passed
print("Index of Mango : ",indexMango)

fruits.insert(1,"Apple") #add the passed element at the index passed.
print("Total Apple in the list are ",fruits.count("Apple")) #counts the number element passed

fruits.sort()#sorts the list in accesding order.
print("Sorted Fruits : ",fruits)

fruits.reverse()#it reverses the list
print("Reversed List : ",fruits)

fruits.clear() #clears the list
print(fruits)


## Slicing the list.
nums = [1,2,3,4,5,6,7,8,9,10]
print("nums[2:5] =",nums[2:5])
print("nums[:5]=",nums[:5])
print("nums[5:]=",nums[5:])
print("nums[::2]=",nums[::2])
print("nums[::-1]=",nums[::-1])
print("nums[::-2]=",nums[::-2])


##List Comprehension
print("----------------------------------------------------------------")
lst= []
for x in range(10):
    lst.append(x**2)
print(lst)

even = [z**2 for z in range(20) if z%2==0 ]
print("Even List : " ,even)
print("----------------------------------------------------------------")