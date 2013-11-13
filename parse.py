from icalendar import Calendar, Event
import os

def pretty_course_name(course):
    course = course[:-3]
    if course[-4] == " ":
        return course
    else:
        return course[0:4] + " " + course[4:7]

all_list = []
classtimes = {}
classdays = {}    

def findTimes(name, schedule):
    schedule = Calendar.from_ical(schedule.read())
    return schedule

#test is a dict in the format {class:[ppl in class]}
test = {}
for course_list in all_list:
    for course in course_list[1:]:
        test.setdefault(course, []).append(course_list[0])

#prints classes with more than one person in them
for course in test:
    if len(test[course]) > 1:
        print pretty_course_name(course), test[course], classtimes[course], classdays[course]
