s = "Strings are awesome!"
# Length should be 20
print("Length of the String is: %d" % len(s))

# First occurrence of "a" should be at index 8
print("First occurence of 'a' is at: %d" % s.index("a"))

# Number of a's should be 2
print("How many a's are in this string: %d" % s.count("a"))

# Slicing the string into bits
print("This is now a list: %s" % s.split(" "))

# Convert everything to uppercase
print("I'm fuckin raging: %s" % s.upper())

# Convert everything to lowercase
print("Everything is lowercase: %s" % s.lower())

# Check how a string starts
print("Does the string start with an S? %s" % s.startswith("S"))

# Check how a string ends
print("Does the string end with an S? %s" % s.endswith("S"))

# Split the string into three separate strings,
# each containing only a word
print("I split everything: %s" % s.split(" "))