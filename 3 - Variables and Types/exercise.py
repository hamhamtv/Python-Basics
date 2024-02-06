# Exercise

myint = 20
myfloat = float(10.0) # I could also only write 10
mystring = "hello"

# testing code
# Do not need to understand this yet since this is just a check to see if I got it right
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)
