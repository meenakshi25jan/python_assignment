"""
21.Given an age, figure out whether someone's a baby, toddler, child, teenager, adult or older
"""
year=input("Enter no of years:")
if year<=1:
    print "baby"
elif year in (2,4):
    print "toddler"
elif year in range(5,12):
    print "child"
elif year in range(13,18):
    print "teenager"
elif year in range(19,50):
    print "adult"
else:
    print "older"
