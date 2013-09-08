import parse, os

myFile = open('C:\Users\David\Documents\GitHub\PennScheduler\static\img\schedules\\adel.ics','r')

person = parse.findTimes("adel", myFile)

print person