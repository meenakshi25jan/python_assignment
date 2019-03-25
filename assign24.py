"""
24.Write a program to findout biggest number in the given numbers
"""
def highest_num(n):
        l=[]
        for i in range(n):
                num=input("Enter number:")
                l.append(num)
        max1=l[0]
        for i in l:
                if max1 < i:
                        max1=i
        return max1
n=input("Enter number the total numbers:")
x=highest_num(n)
print "The highest number of given numbers:",x
