# Cake4: reversing a word (FUN)
# Write a program that will ask for a word and reverse the word.
# Display on the screen: your word is: word, and the reverse is:
# Reverse_word.
 # Leverage methods: split, join and reversed

# Operation

# Let's reverse a word using split, join, and reversed methods

# User: Give me a word
word = input("Enter a word: ")

# Splitting the word into a list of characters
word_list = list(word)  # To split each character

# Reversing the list of characters  
reversed_list = list(reversed(word_list))

# Joining the reversed list of characters to make string
reversed_word = ''.join(reversed_list)

# Display the original word and the reversed word
print(f"Your word is: {word}, and the reverse is: {reversed_word}.")
