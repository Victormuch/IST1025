# this is a first_name input 
# first_name = input("Please enter your first name: ")
# last_name = input("Please enter your last name: ")
# age = int(input("Please enter your age: "))  
# this is a under age function checking if the person is underaged 
# def underage():
#     # this a a if checking if the persons age is less than 18 or not 
#     if age < 18:
#         print("You are under age.")
#     else:
#         print("You are of age.")

# # print(f"Hello {first_name} {last_name}")  
# # we call the function
# underage()  

# a= 3/4 * 2/6
# print(a)

# b= 10.5
# print("Type of b:", type(b))

# c= 2+3j 
# print("Type of c:", type(c))

# string1= "Hello "
# string2= "World"
# string3= """ 
#                 It can 
#                 take 
#                 multiple lines
# """
# print(string1 + string2 + string3)
# print(string1 * 3)
# # learning about index where 0 is the first character while -1 represents the last character  
# print("First character of string1:", string1[0])
# print("First character of string2:", string2[-1])

# # Creating Lists  
# List = []
# print(List)
# List1 = ["Geeks", "For", "That"]
# List1.reverse()
# print(List1)

# Tuple they are immutable. This means they cannot be changed.use the paranthesis
# Tuple = (2, 1, 4, 3, 5)
# tuple = sorted(Tuple)
# print(tuple) 
# # Sets are unordered, and unchangeable. It can be initiated with curly brackets or the set() class constructor. The set() class constructor takes a list or tuple as its only argument (remember those brackets and parentheses!) The elements of a set are unique:
# set1 = ([1, 2, 3, 4, 5, 'a', 'b', 'c'])
# set1.append(1)
# print(set1)


#  IF and else 
# num = int(input("Enter a number: "))

# if num % 2 == 0:
#     print("The number is even.")
# else:
#     print("The number is odd.")
    
    
# Loops  
 
# sum = 0
# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in list:
#     sum = sum + i # u can also say sum += i
# print(sum)# Output: 55

# The use of range. The demostration of range function is shown below:
# range starts from 0 by default and increments by 1 until it reaches the specified number.
# range does not store values, we have to store it in a variable.

# print(list(range(10)))
# print(list(range(1, 11)))

# # Range can actually take 3 parameters 
# listb = list(range(1, 21, 2))
# print("Print the whole listb :" ,listb)
# for i in range(1, 21, 2):
#     print(i)    
    
# listb.reverse()
# print("Print the reversed listb :" ,listb)

# A simple python program to demonstrate iteration through a list using an index 
music = ["pop", "rock", "Jazz", "Classical" , "Country"]
# iterate over the list using index
for i in range(len(music)):
    print( "Index:", i, "I like", music[i], )
# output 
# Index: 0 I like pop
# Index: 1 I like rock
# Index: 2 I like Jazz
# Index: 3 I like Classical
# Index: 4 I like Country

# Programm to demonstrate while loop by adding natural numbers the user specifies 
# n = int(input("Enter  how many natural numbers you want "))
# sum = 0 
# i = 1 
# # while loop to add natural numbers 
# while i <= n:
#     print("The sum of the first", n , "natural number is:", sum)
#     sum += 1 
#     i+= 1 
   

# for val in " string":
#     print("in the for loop", val)
#     if val =="i":
#         break

# print(" out of loop")

# for char in "string":
#     print("in for loop", char)
#     if char == "i":
#         print("i found i")
#         continue


for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)# prints odd numbers from 1 to 10