# LAB 1
# Write a program that will ask for two numbers (integer or float) and calculate the sum of those two numbers.
# Display on the screen: the sum of number1 and numberz2 is: sum.

#solution

#choosing the 2 numbers: 
number1 = float(input("Enter the first number: \n"))
number2 = float(input("Enter the second number: \n"))

# Calculate the sum of the two numbers
result = number1 + number2

# Display the result
print(f"The sum of {number1} and {number2} is: {result}")