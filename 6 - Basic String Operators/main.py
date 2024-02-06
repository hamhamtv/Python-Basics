# Strings are bits of text. They can be defined as anything between quotes:
astring = "Hello World!"

print(astring.index("o")) # This shows where the first occurence of o is -- Letter casing does matter
# Output: 4

print(astring.count("o")) # This counts the o's in my string
# Output: 2


print(astring[3:7]) # Prints out the content of index 3 to 7
# Output: lo W

print(astring[::-1]) # This will just reverse the string
# Output: !dlroW olleH


print(astring.upper()) # Upercase output
# Output: HELLO WORLD!

print(astring.lower()) # Lowercase output
# Output: hello world!


print(astring.startswith("Hello")) # It does start in Hello
# Output: True

print(astring.endswith("abcdefg")) # It does not end in abcdefg
# Output: False

afewwords = astring.split(" ") # Splits astring into two entries of a list at the here defined position(This time at space)

print(afewwords)

# Output: ['Hello', 'World!']


# The len() function returns the number of items (length) in an object.
languages = ['Python', 'Java', 'JavaScript']
objectnumber = len(languages)

print("\nThe number of Codinglanguages in my list is %d. \nMy list consists of following coding languages: %s" % (objectnumber, languages))

# Output: 3


js = "javascript"
length = len(js) # lenght of the word "javascript"

print("\nThe length of the word %s is %d" % (js, length))

# Output: 10