"""
10.Show the below menu to the user until and until user select quit and display corresponding os message
Menu:
1. windows
2. Linux
3. Mac
4. quit
"""
print "program started"
while True:
    print "1.MAC\n2.WINDOWS\n3.LINUX\nq.to exist"
    a=raw_input("Enter a value")
    if a=="1":
        print "Mac is selected"
    elif a=="2":
        print "Windows is selected"
    elif a=="3":
        print "Linux is selected"
    elif a=="q":
        print " Exited"
        break
    else:
        print "Selected wrong option,Please select right option"
print "program ended"
