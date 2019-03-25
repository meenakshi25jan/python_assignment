import logging

while True:
    try:
        usr_inp = int(raw_input("enter a number to check prime or not"))
        break
    except ValueError:
        print "Input must be number,Please re enter correct input"
        continue
    else:
        usr_inp<0:
        
if usr_inp in [0,1] and usr_inp%2==0 and usr_inp%3==0:
    print "Not prime number"
    
else:
    print "prime number"
