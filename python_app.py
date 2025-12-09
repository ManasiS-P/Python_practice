
###############Conversion of weight################

weight_lbs = input("Enter weight in pounds:")
weight_kg = int(weight_lbs) * 0.45
print(f"Weight in kg: {weight_kg}")

################Strings in Python###############

course = '''
Hi John,

Here is the outline for the "Python" course
Regards,
Manasi
'''
print(course)

################String indexing in Python###############

course = "Python for Beginners"
print(course[0])
#Positive indexing starts from left to right, negative indexing starts from right to left
print(course[-1])
#2 number in square brackets is used to return the characters from indexing
print(course[0:3])
print(course[0:])#will return whole string
print(course[:5])#will return first 5 characters
print(course[:])#will return whole string   
another = course[:]#returns the string in course variable, another is the another variable which returns contents of course variable
print(another)
#example
name = "Jennifer"
print(name[1:-1])

################Formatted Strings###############

first_name = "John"
last_name = "Smith"
message = first_name + ' [' + last_name + '] is a coder' #without formatted string
print(message)
msg = f'{first_name} [{last_name}] is a coder'#with formatted string that is use f'everything you want to print goes inside this'
print(msg)

###############String methods###############

course = "Python for Beginners"
print(len(course))#length of string
if len(course)>18:
 {
  print("String should have length less than 18")
  }
else:
 {print ("String length is exceptable")}

################  When a function specific belongs to an object, it is called method.  ##############

print(course)#original string remains unchanged
print(course.upper())#converts everything to uppercase
print(course.lower())#converts everything to lowercase
print(course.title())#converts first letter of each word to uppercase
print(course.strip())#removes any whitespace in the beginning or end of the string
print(course.find('B'))#returns index of B(first occurrence of B) find method is case sensitive
print(course.replace('B','b'))#replaces the first parameter with second parameter this is also case sensitive method
print('Python'in course)#return boolean value that is true if present else false' this is also case sensitive

################Arithmetic operations###############
print(10 + 5)#addition
print(10 - 5)#subtraction
print(10 * 5)#multiplication
print(10 / 3)#division
print(10 // 3)#floor division - removes decimal part
print(10 % 3)#modulus - returns remainder after division
print(10 ** 3)#exponentiation

x = 10
x = x + 3 #is similar to x += 3 this is called augmented assigment operator
print(x)

################ Operator Precedence###############
x = 10 + 3 * 2
print(x)#multiplication has higher precedence than addition so it is calculated first
#Order of Precedence: Parentheses, Exponents, Multiplication/Division, Addition/Subtraction
y = (10 + 3) * 2
print(y)#parentheses have highest precedence so addition is calculated first

################Math functions###############
x = 2.9
print(round(x))#rounds to nearest integer
print(abs(-2.9))#returns absolute value

#Module in python is a file containing python code. This code can be functions, classes, or variables. We can reuse the code in other python files by importing the module.
import math


################If statements###############
is_hot = False
is_cold = True
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")  
else:
    print("Enjoy your day")

#Example
price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
    print(f"Down payment = ${down_payment}")
else:
    down_payment = 0.2 * price
    print(f"Down payment = ${down_payment}")


################Logical Operator###############
has_high_income = True
has_good_credit = False

if has_high_income or has_good_credit:
    print("Eligible for loan")
else:
    print("Not eligible for loan")


################Comparison Operator###############
temp = 30

if temp > 30:
   print("It is a hot day")
elif temp < 10:
    print("It is a cold day")
else:
    print("It is neither a hot day nor a cold day")

#Example
name = "Manasi"
len_name = len(name)

if(len_name) < 3:
    print("Name must be at least 3 characters")
elif(len_name) > 50:
    print("Name must be less than 50 characters")
else:
    print("Name has proper length of characters")


################Project Weight Converter###############
weight = input("Enter weight: ")
unit = input("(L)bs or (K)g: ")

if unit == "L":
    converted_weight = int(weight) * 0.45
else:
    converted_weight = int(weight) / 0.45
print(f"Converted weight is: {converted_weight}")

################While Loops###############

i = 1

while i <= 6:
    print('*' * i)
    i = i + 1
print("Completed while loop")

################Guessing Game###############

secret_number = 10
user_guess = 0


while user_guess < 3:
    guess = int(input("Guess: "))
    user_guess = user_guess + 1
    if guess == secret_number:
        print("You win")
        break
else:
    print("You failed")

################Car Game###############
command = ""
started = False

while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started")
        else:
            started = True
            print("Car started...Ready to go!")
    elif command == "stop":
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print("Car stopped.")
    elif command == "help":
        print("start - to start the Car")
        print("stop - to stop the Car")
        print("quit - to exit")
    elif command == "quit":
        break
    else:
        print("I don't understand that command.")

################For loops###############
prices = [10,20,30]
total = 0

for price in prices:
    total = total + price
print(f"Total price : {total}")

################Nested loops###############
for x in range(4):
   for y in range(4):
      print(f"({x}, {y})")

#Example
numbers = [5,2,5,2,2]

for number in numbers:
   output = ''
   for count in range(number):
     output = output +'*'
   print(output)

#Alternative approach
numbers = [5,2,5,2,2]

for number in numbers:
    print('*' * number)


################Lists###############
#Example to find largest number out of list
numbers = [3,6,12,8,4,10,2]

max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(f"Largest number is: {max}")

############List methods###############
#List are represented in square bracket
x = [5,2,1,7,4]
x.append(20)#adds 20 to the end of the list
print(x)
x.insert(0,10)#inserts 10 at index 0
print(x)
x.remove(5)#removes 5 from the list
print(x)
x.clear()#clears all from the list
print(x)
x.pop()
print(x)

#Example - remove the duplicate from list

x = [1,2,3,4,5,5,6]
num = []

for item in x:
    if item not in num:
        num.append(item)
print(num)

#Alternative approach
x = [1, 2, 2, 3, 4, 4]
print(list(set(x)))


###################Tuples################
#Tuples are immutable - we cannot change them represented in round brackets
x = (1,2,3)
print(x)

##############Unpacking in Python#############
coordinates = (1,2,3)
x,y,z = coordinates
print(x)

##################Dictionaries####################
#We use it when we want to store information in key value pair
#The keys in dictionaries should be unique, and are case sensitive

#Example to print numbers in words
x = input("Phone: ")
#print (x)

numbers = {
    "1":"one",
    "2": "two",
    "3":"three",
    "4":"four"
}

output = "" 
for ch in x:
    output = output + numbers.get(ch,"!") + " "
print(output)

#Example to convert emojis
message = input(">")
words = message.split(' ')
emojis = {
    ":)": "😊",
    ":(": "😞"
}
output = ""
for word in words:
    output = output + emojis.get(word, word) + " "
print(output) 

##Converting integer into decimal

import decimal
x = 10
print(decimal.Decimal(x))
print(type(decimal.Decimal(x)))

##Converting string of integer into decimal

import decimal
x = '12345'
print(decimal.Decimal(x))
print(type(decimal.Decimal(x)))


## Reversing a string in Python

text = input("Start your text: ")
reverse_text = text[::-1]
print(f"Reversed string: {reverse_text}")

#Another approach
s = input("Enter string: ")
rev = ""
for ch in s:
    rev = ch + rev
print(rev)


##Counting vowels in given string

vowels = ['a','e','i','o','u']
word = "Programming"
count = 0
for v in word:
    if v in vowels:
        count += 1
print(count)

##Counting consonants in given string

vowels = ['a','e','i','o','u']
word = "Programming"
count = 0
for v in word:
    if v not in vowels:
        count += 1
print(count)

##Counting number of occurences of character in a string

word = "nipani"
character = "n"
count = 0

for ch in word:
    if ch == character:
        count += 1
print(count)

##Counting fibonacci series
n = int(input("Enter how many fibonacci numbers you want: "))

a = 0
b = 1

print("Fibonacci series : ")

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

##Finding max number from the given list

x = [1,2,3,4,5,9]
print(max(x))
print(min(x))

maxNum = x[0]
for num in x:
    if maxNum < num:
        maxNum = num
print(maxNum)

minNum = x[0]
for num in x:
    if minNum > num:
        maxNum = num
print(maxNum) 


##Check if number is odd or even
n = int(input("Enter number: "))
if n % 2 == 0:
    print("Even")
else:
    print("Odd")

##Sum of digits of numbers
n = input("Enter number: ")
total = 0
for digit in n:
    total += int(digit)
print(total)

##Check if Palindrome
s = input("Enter string: ")
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")


##Print multiplication table
n = int(input("Enter number: "))
for i in range(1, 11):
    print(n, "x", i, "=", n*i)

##Factorial of a number
n = int(input("Enter number: "))
fact = 1
for i in range(1, n+1):
    fact *= i
print("Factorial =", fact)

##count words in a sentence
s = input("Enter sentence: ")
words = s.split()
print(len(words))


#second largest number in a list
x = [10, 4, 9, 1]
x.sort()
print("Second largest:", x[-2])


##Check if number is prime
n = int(input("Enter number: "))
isPrime = True

if n < 2:
    isPrime = False
else:
    for i in range(2, n):
        if n % i == 0:
            isPrime = False
            break

if isPrime:
    print("Prime")
else:
    print("Not Prime")


##Swapping two numbers
a = int(input())
b = int(input())

a, b = b, a
print(a, b)


##Print all even numbers in a range
n = int(input())
for i in range(1, n+1):
    if i % 2 == 0:
        print(i)


##Calculate simple interest

p = float(input("Principal: "))
r = float(input("Rate: "))
t = float(input("Time: "))

si = (p * r * t) / 100
print("Simple Interest =", si)


##covert Celsius to Fahrenheit
c = float(input("Celsius: "))
f = (c * 9/5) + 32
print("Fahrenheit:", f)

#Print prime numbers in a range
n = int(input("Enter limit: "))
for i in range(2, n+1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i, end=" ")
#Find common elements in two lists
a = [1,2,3,4]
b = [3,4,5,6]
common = list(set(a) & set(b))
print(common)


#Print number from 1 to N
n = int(input("Enter N: "))
for i in range(1, n+1):
    print(i)


#Print even number from 1 to N
n = int(input())
for i in range(1, n+1):
    if i % 2 == 0:
        print(i)


#Sum of first N numbers
n = int(input())

total = 0
for i in range(1, n+1):
    total += i

print(total)


#Find area of circle
r = float(input("Enter radius: "))
area = 3.14 * r * r
print("Area =", area)

#Multiply all items in list
x = [2, 3, 4]
product = 1
for i in x:
    product *= i
print(product)

#Alternate approach
import math
x = [2, 3, 4]
print(math.prod(x))
# print(f"Total price : {total}")








 
















