import parse, os

myFile = open('C:\Users\David\Documents\GitHub\PennScheduler\static\img\schedules\\adel.ics','r')

person = parse.findTimes("adel", myFile)

print person

for n in range(2, 10):
     for x in range(2, n):
         if n % x == 0:
             print n, 'equals', x, '*', n/x
             break
     else:
         # loop fell through without finding a factor
         print n, 'is a prime number'