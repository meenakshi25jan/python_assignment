
u_i=raw_input("Enter input to check given input is alphabates only or not")
jk="""~ ` ! @ # $ % ^ & * ( ) _ - + = [ ] { } | \ : ; " < > ? / . ,'"""
l=list(u_i)
for i in u_i:
    if i in jk:
        print "All are special chars"
        break
    else:
        print "Not All are special chars"
        break

