"""
16.Take the input from the user for(Total number of people, toatl number of busses, Number of seats for bus). Based on the input
Deside whether there is su
fficient busses or not and give solution for how many extra busses required.
"""
import math
tp=input("Enter total number of people:")
tb=input("Enter total number of buses:")
ns=input("Enter number of seats in one bus:")
def sufbus(tp,tb,ns):
    if tp==tb*ns:
        print "sufficient bus are avaliable"
    else:
        br=(float(tp)/float(ns))-tb
        print "Number of bus required is ", math.ceil(br)
sufbus(tp,tb,ns)
