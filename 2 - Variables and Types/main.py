# https://learnpython.org/en/Variables_and_Types

# Python is object oriented. 

# Integers - Real Numbers(7)
myint = 1
print("myint:", myint)

int = 2
print("int:", int)



# Floats - Deciamls(7.3)
# Syntax for float is: float() - When using a decimal number declaring a float is not necessary, it will not break the programm to use a decimal number in a variable without declaring it a float since python will do this itself
# When using a real number in a float python will just output: number.0
myfloat = 1.2
print("myfloat:", myfloat)

thisisafloat = float(2.3)
print("this is a float:", thisisafloat)

thefuckisthis = float(3.1)
print("You can name your float whatever you want:", thefuckisthis)



# Convert integers into floats
int_number = 25
float_number = float(int_number)

print("Here I converted, what originally was a integer into a float:", float_number)
# Output: 25.0



# Strings
mystring = 'Hello'
print("This is a String:", mystring)
# Using double quotes makes it easy to use apostrophes
mystringwhithapostrophes = "Don't worry about apostrophes"
print(mystringwhithapostrophes)


# Extra Stuff
a, b = 3, 4
print(a,b)

# Mixing operators for ints/floats and strings will not work
# This would not work:
# one = 1
# two = 2
# hello = "hello"
# print(one + two + hello)