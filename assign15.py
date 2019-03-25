"""
15. take a string from the user and check contains atleast one small letter or not?
"""
s=raw_input("Enter a string:")
for i in s:
    if i==i.lower() and i.isalpha():
        print "string contains small letter"
        break
else:
    print "string does not small letters"
