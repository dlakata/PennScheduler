from icalendar import Calendar, Event
import os

def pretty_course_name(course):
    course = course[:-3]
    if course[-4] == " ":
        return course
    else:
        return course[0:4] + " " + course[4:7]

#---------------------------------------------------------------
    #this chunk creates a list of lists that have the format [name, filepath]
#   path = "C:\Users\David\Documents\GitHub\PennScheduler\static\img\schedules"
#   list_of_all_ics_files = []
# for filename in os.listdir(path):
#     if not filename.endswith('.ics'):
#         continue
#     #filename is in the format adel.ics
#     first_name = filename[:-4]
#     file_dir = os.path.join(path, filename)
#     if file_dir not in list_of_all_ics_files:
#         list_of_all_ics_files.append([first_name, file_dir])
#---------------------------------------------------------------

#---------------------------------------------------------------------
    #this inputs lists into all_list in the format [name, class1, class2,..]
    #classtimes is a dictionary with {"class":["start", "end"]}
    #classdays is a dictionary with {"class": [mon, tues, wed]}
all_list = []
classtimes = {}
classdays = {}
# for pair in list_of_all_ics_files:
#     name = pair[0]
#     filepath = pair[1]
#     vars()[name] = open(filepath)
#     name = vars()[name]
#     

def findTimes(name, schedule):
    schedule = Calendar.from_ical(schedule.read())
    course_list = []
    for component in schedule.walk():
        if component.name == "VEVENT":
            course_name = component.get("SUMMARY")
            course_name = str(course_name)
            if course_name not in course_list and "PREC" not in course_name:
                course_list.append(course_name)

            day_of_week = component.get("RRULE")
            day_of_week = dict(day_of_week)
            day_of_week = str(day_of_week["WKST"])[3:5]

            start_time = component.get('DTSTART').dt
            start_time = str(start_time)[11:16]
            end_time = component.get('DTEND').dt
            end_time = str(end_time)[11:16]

            if course_name not in classtimes:
                classtimes[course_name] = [start_time, end_time]
            classdays.setdefault(course_name, []).append(day_of_week)
    all_list.append(course_list)
    for course in classdays:
        t = classdays[course]
        t = list(set(t))
        classdays[course] = t
    all_dictionary = {name : all_list}
    return all_dictionary


#test is a dict in the format {class:[ppl in class]}
test = {}
for course_list in all_list:
    for course in course_list[1:]:
        test.setdefault(course, []).append(course_list[0])

#prints classes with more than one person in them
for course in test:
    if len(test[course]) > 1:
        print pretty_course_name(course), test[course], classtimes[course], classdays[course]
