__author__ = 'vinnyfiore'
# Built upon algorithm originally found at http://pythango.blogspot.in/2014/07/python-multiplication-la-russe.html
# Then modified to work.


import time
from mpmath import *

mp.dps = 1000
mp.prec = 1000


def alarusse(m, n):
    result = 0
    while m >= 1:  # Loop Until the multiplier becomes "1"
        if m % 2 != 0:  # check if odd or not
            result = (result + n)  # if yes add the value of n to result
        m = int(m * .5)  # Divide Multiplier by 2 (yes until it becomes "1")
        n = n * 2  # Double the value of Multiplicand
    return result


def classicMult(m, n):
    num = m
    counter = 1
    while counter<n:
        m = m+num
        counter += 1
    return m

print("Note: At current time, the calculations are not correct past 15 digits due to Python limits.")
num1 = int(input("Enter the first number to multiply: "))
num2 = int(input("Enter the second number to multiply: "))

start1 = time.time()
result1 = mp.mpf(num1 * num2)
end1 = time.time()
print("Using built in multiplication:")
print("RESULT:", result1)
print("It took", end1 - start1, "seconds")
print("")

print("Using classic multiplication")
start2 = time.time()
result2 = classicMult(num1, num2)
end2 = time.time()
print("RESULT:", result2)
print("It took", end2 - start2, "seconds")
#print(result1)
#print(result2)
#print(result1 - result2)
print("")

print("Using A La Russe")
start3 = time.time()
result3 = alarusse(num1, num2)
end3 = time.time()
print("RESULT:", result3)
print("It took", end3 - start3, "seconds")
#print (pi)
