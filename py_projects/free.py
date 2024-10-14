message2 =  "my father is top"
message1 = "come to Jesus now"
message3 = "bravo is my brother"
message4 = "OOOOOOOOOOOOOOOOOOOOOO"

message2 = message2[::-1]

print (message2)

message1 = message1.title()
print (message1)

message3 = message3.upper()
print(message3)

message4 = message4.lower()
print(message4)
message4 = message4.count("o")
print(message4)

message5 = "I love it"
character_count = len(message5)
print(character_count)

# Writting a new message using characters fromt message5
new_message = message5[2:6] + " " + message5[-2] + message5[-1]
print(new_message)