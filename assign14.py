"""
14. take a string from the user and check contains atleast one capital letter or not?
"""
s=raw_input("Enter a string:")
for i in s:
    if i==i.capitalize():
        print "string contains capital letters"
        break
else:
    print "string does not capital letters"
