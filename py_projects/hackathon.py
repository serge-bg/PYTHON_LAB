# Exercise: 
# You are given both messages
# message1= ” welcome to aws python 101 class: strings”
# message2= ” The instructor here is Claudio”
# Write python program that will:
#  1- Capitalize all first character of each word of msg1
#  2- Reverse msg2
#  3- Write msg1 in lower case
#  4- Write msg2 in upper case
#  5- Find how many “e’’ character was use in msg2
#  6- Replace “python” by “java” in msg1
#  7- Create a new message “python is great” using msg1 characters.
#  8- Create a new message “Java is well done” using msg1 characters

# Operation/code writting
# 0. Writting down the messages given
message1 = "welcome to aws python 101 class: strings"
message2 = "The instructor here is Claudio"

# Capitalize the first character of each word in msg1
message1_with_1st_word_capitalized_per_word = message1.title()

    # Printing the result
print(message1_with_1st_word_capitalized_per_word)

# 2- Reversing message2
message2_in_reverse_mode = message2[::-1]
   # printing the result
print(message2_in_reverse_mode)

# 3. Write message1 in lower case
message1_in_lowercase = message1.lower()
   # printing the result
print(message1_in_lowercase)

# 4. Write message2 in upper case
message2_in_uppercase = message2.upper()
   # printing the result
print(message2_in_uppercase)

# 5. Finding how many “e” characters were used in message2
count_e_in_message2 = message2.count("e")                        
   # printing the result
print(count_e_in_message2)

# 6. Replacing “python” by “java” in message1
java_in_lieu_of_python_in_message1 = message1.replace("python", "java")
    # printing the result
print(java_in_lieu_of_python_in_message1)

# 7. Writting a new message “python is great” using message1 characters
new_message1 = message1[15:21] + " " + message1[-4]+message1[-7]+ " " + message1[-2] + message1[-5] + message1[6] + message1[-12] + message1[-6]
   # printing the result
print(new_message1)

# 8. Writting new message “Java is well done” using message1 characters
replace_message1 = "welcome to aws java 101 class: strings"
   # Constructing the new message "Java is well done"
new_message2 = replace_message1[-23:-19] + " " + replace_message1[-4] + replace_message1[-1] + " " + replace_message1[0:3] + replace_message1[2] + " " + "d" + replace_message1[4] + replace_message1[-3] + replace_message1[1]
   # Printing the result
print(new_message2)