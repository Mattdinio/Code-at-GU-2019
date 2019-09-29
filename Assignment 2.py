# Scaffold for solution to DIT 852, Programming task 1
#
from GDPvsLE import *

def quartiles(l):
    # Compute Q1, Q2 (the median), Q3 for a list
    # Insert your code below
    l.sort()
    tempList = findMiddle(l)
    Q2 = tempList[0]
    for i in range(1,3):
        tempList.append(findMiddle(tempList[i])[0])
    del tempList[2]
    del tempList[1]
    Q3 = tempList[2]
    Q1 = tempList[1]
    return Q1, Q2, Q3

def findMiddle(l):
    indexNum = (len(l) // 2)
    if len(l) % 2 == 0:
        num1 = l[(indexNum)]
        num2 = l[(indexNum + 1)]
        number = (num1 + num2) / 2
        list1 = l[:indexNum]
        list2 = l[indexNum:]
    else:
        list1 = l[0:indexNum+1]
        list2 = l[indexNum:]
        number = l[indexNum]
    return [number, list1, list2]

# The following is called if you execute the script from the commandline
# e.g. with python solution.py
if __name__ == "__main__":
    assert quartiles([1,1,2,2,2,3,3,4,4]) == (2., 2., 3.)



