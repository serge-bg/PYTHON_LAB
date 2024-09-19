#Topic:
#Your task is to write a python program that displays a custom banner using the 
#"#" symbol and escape characters for formatting. The banner should include the message
# WELCOME TO STREET FIGHTER: YOUR NAME  

#Submission: Write the code in a file calles banner.py
#Display the result to the screen (print)
#Show the code
#Submit in a word or pdf
#Submit it in your github account in a forlder called py_project

# SOLUTION
# I define the message with your name
name = "SERGE"  # This name will display in the output. 
message = f"WELCOME TO STREET FIGHTER: {name}"

# Display the banner
print("#" * 38)
print(f"#  {message}  #")
print("#" * 38)

