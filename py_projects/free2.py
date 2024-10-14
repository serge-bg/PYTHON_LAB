# trying to understand PEMDAS ( please, Excuse My Dear Aunt Sidi )
calculation = 8 / 2 * (2 + 2)
print (calculation)
calculation2 = 8*2/(2+2)
print(calculation2)
a = 2>3
b = 2>=2
print(a)
print (b)
c = (a+b)>0
print(c)
d=1!=1
print(d)
bottle="water"
print (bottle)
_bag = "chips"
print(_bag)
myvar = "MYVAR"  # Assign the value "MYVAR" to myvar

# Compare myvar to the string "MYVAR"
if myvar == "MYVAR":
    print("myvar is equal to 'MYVAR'")
else:
    print("myvar is not equal to 'MYVAR'")
if myvar.lower() == "myvar":
    print("myvar is equal to 'MYVAR' (case insensitive)")

greeting = "hello friend"
print(greeting)

#special or escape character
my_store_name = 'oumou\'s store'
print(my_store_name)

first_string = "I"
second_string = "love"
third_string = "you"
print(first_string + " " + second_string + " " + third_string)

my_user_name = "serge007"
print("welcome to street3107 "+ my_user_name)

#Place horders help to put the the variables where you want them. different ways to do that
# .format() and f format
name = "saka"
color1 = "blue"
color2 = "black"
place = "home"

sentence = "{} car is {}".format(name,color1)
print (sentence)

sentence2 = f"{name} car is {color1} and the rims are {color2}"
print(sentence2)
sentence3 = f"My {place} as you know is become the parking of {name} where he keeps its {color1} car with {color2} rims"
print(sentence3)

#Let's try with number
num1 = 20
num2 = 35
result = f"the addition of {num1} and {num2} is: {num1 + num2}"
print (result)

#slicing string
sentence = "hello world"
print (len(sentence))
#finding the position of character
position = sentence.find("o")  # Finds the first occurrence of 'o'. You can also use the code position = sentence.index("0")
print(f"The position of 'o' is: {position}")

position = sentence.index("w")
print(f"The position of 'w' is: {position}")

my_string = "hello word"
print(my_string[0:5])
print(my_string[-5:-1])

#reversing string
arn = "1234567890"
print (arn[::1])

print(my_string[0:5:2])

print(my_string.upper())

type ('5')
print(type)