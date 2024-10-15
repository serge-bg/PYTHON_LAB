# EXERCISE
'''
Lab cake 2: Reversing a List @channel
Objective: Practice reversing a list and transferring its elements into a new list using loops.
Task: Write a Python program that works with the list called laura_things containing the following items:
•	"sewing machine"
•	"scissor"
•	"cutting mat"
•	"television"
Your program should do the following:
1.	Create a list called laura_things with the items listed above.
2.	Reverse the order of the items in laura_things.
3.	Transfer each item from the reversed list into a new list called reversed_things.
4.	Print out the new list reversed_things to show that it contains the items in reverse order.
Requirements:
•	You must reverse the list using slicing or a loop (do not use Python's built-in reverse methods like reverse() ).
•	The final output should look like this:
•	['television', 'cutting mat', 'scissor', 'sewing machine']
Bonus Challenge:
•	After reversing the list and creating reversed_things, print a message that says: "The list has been successfully reversed!"
Submission
Please submit your code by [insert due date here] in a file named reverse_list_assignment.py. Make sure to test your code to ensure it produces the correct output (edited) 
'''
# OPERATION

# List called laura_things with these specified items
laura_things = ["sewing machine", "scissor", "cutting mat", "television"]

# empty list to store the reversed items
reversed_things = []

# Manually reversing the list using a loop
for i in range(len(laura_things) - 1, -1, -1):
    reversed_things.append(laura_things[i])

# Printing the new list reversed_things 
print(reversed_things)

# Bonus Challenge: message after the list is reversed
print("The list has been successfully reversed!")
 