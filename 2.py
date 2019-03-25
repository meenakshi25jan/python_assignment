a=raw_input("Enter Actual String")
b=raw_input("Enter Sub String")

def string(a,b):
    a.lower()
    b.lower()
    if b in a:
        print "Substring is in actual string"
    else:
        print "Substring not found"
string(a,b)
