# This is a single line comment

"""
This
is
multiline
comment
"""

# Line Continuation

Total = 1 + 2 + 3 + 4 + 5 \
        + 6 + 7 + 8 + 9 + 0
print("Total = ", Total)

# Multiple statements on a single line.

x = 5
y = 10
z = x + y
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
#
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
# Nested FOR loop

for i in range(3):
    for j in range(2):
        print(f"i : {i} and j : {j}")
        print("j++")
    print("i++")
print("EOWL")

print("----------------------------------------------------------------")
# Example of FOR & WHILE loop
# Calculate the sum of first n natural number

n = 10
sum = 0
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

# List in Python.

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

indexMango = fruits.index("Mango")  # returns the first index position of the element passed
print("Index of Mango : ", indexMango)

fruits.insert(1, "Apple")  # add the passed element at the index passed.
print("Total Apple in the list are ", fruits.count("Apple"))  # counts the number element passed

fruits.sort()  # sorts the list in ascending order.
print("Sorted Fruits : ", fruits)

fruits.reverse()  # it reverses the list
print("Reversed List : ", fruits)

fruits.clear()  # clears the list
print(fruits)

# Slicing the list.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("nums[2:5] =", nums[2:5])
print("nums[:5]=", nums[:5])
print("nums[5:]=", nums[5:])
print("nums[::2]=", nums[::2])
print("nums[::-1]=", nums[::-1])
print("nums[::-2]=", nums[::-2])

# List Comprehension
print("----------------------------------------------------------------")
lst = []
for x in range(10):
    lst.append(x ** 2)
print(lst)

even = [z ** 2 for z in range(20) if z % 2 == 0]
print("Even List : ", even)
print("--------------------------------------------------------------- -")

# Dictionary In Python
Dic1 = {}
dic1 = dict()
print(type(Dic1))
print(type(dic1))

emp = {"Name": "Akshit", "Age": "24", "Gender": "Male"}
print(emp)
print(emp.keys())
print(emp.values())
print(emp.items())

# to make a copy of a dictionary
emp1 = emp
print("EMP", emp)
print("EMP1", emp1)

emp["Age"] = 10

print("EMP", emp)
print("EMP1", emp1)

# Copy a dict
emp_new = emp.copy()
emp["Age"] = 25
print("EMP", emp)
print("EMP_NEW", emp_new)

# LAMBDA FUNCTIONS
print("-----------------------LAMBDA FUNCTIONS-----------------------")

'''
Syntax to define the lambda function 

fun_name = lambda args : expressions
example : 
sq_num = lambda x : x**2 

'''


def add(num1, num2):
    return num1 + num2


print("Using add function ", add(10, 20))

add_1 = lambda num1, num2: num1 + num2
print("Using the Lambda function ", add_1(50, 30))

print("-----------------------MAP FUNCTIONS-----------------------")
'''
Syntax to define the map function without lambda 
map (fun_name,iterables)
Example is shown below
'''


def sqr(sq):
    return sq ** 2


sqr(10)

sqrs = [1, 2, 3, 4, 5, 6, 7, 8]
print(list(map(sqr, sqrs)))

print("-----------------------MAP FUNCTIONS WITH LAMBDA-----------------------")
'''
Syntax to define the map function with lambda 
map (lambda args:expression ,iterables)
Example is shown below
'''
n1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(list(map(lambda x: x ** 2, n1)))

print("-----------------------FILTER FUNCTION-----------------------")
'''
Syntax to define filer function 
    filer(fun_name,iterables) --> Regular Function
    filer(lambda args:expression,iterables) --> Lambda function 
    filer(lambda args:expression and expression, iterables) --> Lambda function with multiple expression 
examples shown below 
'''
n1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


def even(num):
    if num % 2 == 0:
        return True


even_n1 = list(filter(even, n1))
print("EVEN N1: ", even_n1)

odd_n1 = list(filter(lambda x: x % 2 != 0, n1))
print("ODD N1 : ", odd_n1)

even_gt_n1 = list(filter(lambda x: x % 2 == 0 and x > 5, n1))
print("Even & GT 5 :", even_gt_n1)

print("-----------------------INBUILT os FUNCTIONS-----------------------")

import os

print(os.getcwd()) # --> returns the current working directory
os.mkdir("mkdir",mode=0o777) # --> makes a new folder with the passed name from the current working directory
print(os.listdir(os.getcwd())) # --> lists all the files & folder in the current working directory
os.removedirs("mkdir") # --> removes the folder with the passed name from the current working directory
print(os.listdir(os.getcwd()))

print("-----------------------INBUILT csv FUNCTIONS-----------------------")

import csv

with open("Mycsv.csv",mode='w+',newline="") as file :
    writer=csv.writer(file)
    writer.writerow(["Name" , "Place" ,"Animal","Thing"])
    writer.writerow(["Ajay", "Agra","Ant","Aeroplane"])

with open("Mycsv.csv",mode='r')as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)

print("-----------------------INBUILT shutil FUNCTIONS-----------------------")
import shutil

print("Files before copy : ",os.listdir(os.getcwd()))
shutil.copyfile("PythonHelp.py","PythonHelp_bkp_26AUG.py")
print("Files after copy : ",os.listdir(os.getcwd()))


print("-----------------------INBUILT datetime FUNCTIONS-----------------------")
import datetime as dt
today = dt.datetime.now()
print("today is : ",today)
yesterday = today - dt.timedelta(days=1)
print("yesterday was : ",yesterday)

print("-----------------------INBUILT time FUNCTIONS-----------------------")
import time
print(time.time())
time.sleep(5)
print(time.time())