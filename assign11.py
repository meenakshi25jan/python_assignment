"""
11.take a string from the user and check contains atleast one digit or not?
"""
s=raw_input("Enter a string:")
for i in s:
    if i.isdigit():
        print "string contains digits"
        break
else:
    print "string doesnot contains digits"
