"""
17.Print the first 100 odd numbers
"""
n=input("enter up to which range do you required odd numbers:")
lt=(i for i in range(1,n) if i%2!=0)
for i in lt:
    print i
