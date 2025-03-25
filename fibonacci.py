# # Function to print Fibonacci sequence up to n terms
# def fibonacci(n):
#     # First Fibonacci number
#     a = 0  
#     # Second Fibonacci number
#     b = 1  
#      # Repeat n times
#     for i in range(n): 
#          # Print the current number
#         print(a) 
#         # Calculate the next number
#         next_num = a + b  
#          # Move to the next number in sequence
#         a = b 
#          # Update b to the new number
#         b = next_num 

# # Ask the user for the number of Fibonacci numbers to generate
# n = input("How many Fibonacci numbers do you want? ")

# # Check if the input is a number and greater than zero
# # n.isdigit() checks if the input is a number
# if n.isdigit():
#     # int(n) converts the input to an integer
#     n = int(n)
#     # n > 0 checks if the number is greater than zero
#     if n > 0:
#         fibonacci(n)
#     else:
#         print("Please enter a number greater than zero.")
# else:
#     print("Invalid input. Please enter a positive number.")
# var = 0
# while var < 6:
#     var += 1
#     if var % 2 == 0:
#         continue
#     print("#")



my_list = [3, 1, -2]
print(my_list[my_list[-2]])
 