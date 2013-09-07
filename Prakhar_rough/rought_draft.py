from icalendar import Calendar, Event


david = open('david.ics')
prakhar = open("prakhar.ics")
adel = open("adel.ics")
greg = open("greg.ics")
evan = open("evan.ics")
miguel = open("miguel.ics")

cal_david = Calendar.from_ical(david.read())
cal_prakhar = Calendar.from_ical(prakhar.read())
cal_adel = Calendar.from_ical(adel.read())
cal_greg = Calendar.from_ical(greg.read())
cal_evan = Calendar.from_ical(evan.read())
cal_miguel = Calendar.from_ical(miguel.read())

# for component in cal.walk():
# 	if component.name == "VEVENT":
# 		print component.get('RRULE')
# 		bob = component.get("RRULE")
# 		bob = dict(bob)
# 		print str(bob["WKST"])[3:5]
		# print component.get("SUMMARY")


# for component in cal.walk():
# 	if component.name == "VEVENT":
# 		bob = component.get('DTSTART').dt
# 		bob = str(bob)
# 		print bob[11:16]
# 		print component.get('DTSTART').dt
# 		print component.get('DTEND').dt
adel_courses = ["adel"]
david_courses = ["david"]
prakhar_courses = ["prakhar"]
greg_courses = ["greg"]
evan_courses = ["evan"]
miguel_courses = ["miguel"]


for component in cal_david.walk():
	if component.name == "VEVENT":
		course_name = component.get("SUMMARY")
		course_name = str(course_name)
		if course_name not in david_courses:
			david_courses.append(course_name)

		day_of_week = component.get("RRULE")
		day_of_week = dict(day_of_week)
		day_of_week = str(day_of_week["WKST"])[3:5]

		start_time = component.get('DTSTART').dt
		start_time = str(start_time)[11:16]
		end_time = component.get('DTEND').dt
		end_time = str(end_time)[11:16]


		# print course_name, day_of_week, start_time, end_time


for component in cal_prakhar.walk():
	if component.name == "VEVENT":
		course_name = component.get("SUMMARY")
		course_name = str(course_name)
		if course_name not in prakhar_courses:
			prakhar_courses.append(course_name)

		day_of_week = component.get("RRULE")
		day_of_week = dict(day_of_week)
		day_of_week = str(day_of_week["WKST"])[3:5]

		start_time = component.get('DTSTART').dt
		start_time = str(start_time)[11:16]
		end_time = component.get('DTEND').dt
		end_time = str(end_time)[11:16]

		# print course_name, day_of_week, start_time, end_time

for component in cal_adel.walk():
	if component.name == "VEVENT":
		course_name = component.get("SUMMARY")
		course_name = str(course_name)
		if course_name not in adel_courses:
			adel_courses.append(course_name)

		day_of_week = component.get("RRULE")
		day_of_week = dict(day_of_week)
		day_of_week = str(day_of_week["WKST"])[3:5]

		start_time = component.get('DTSTART').dt
		start_time = str(start_time)[11:16]
		end_time = component.get('DTEND').dt
		end_time = str(end_time)[11:16]

		# print course_name, day_of_week, start_time, end_time

for component in cal_greg.walk():
	if component.name == "VEVENT":
		course_name = component.get("SUMMARY")
		course_name = str(course_name)
		if course_name not in greg_courses:
			greg_courses.append(course_name)

		day_of_week = component.get("RRULE")
		day_of_week = dict(day_of_week)
		day_of_week = str(day_of_week["WKST"])[3:5]

		start_time = component.get('DTSTART').dt
		start_time = str(start_time)[11:16]
		end_time = component.get('DTEND').dt
		end_time = str(end_time)[11:16]


		# print course_name, day_of_week, start_time, end_time

for component in cal_evan.walk():
	if component.name == "VEVENT":
		course_name = component.get("SUMMARY")
		course_name = str(course_name)
		if course_name not in evan_courses:
			evan_courses.append(course_name)

		day_of_week = component.get("RRULE")
		day_of_week = dict(day_of_week)
		day_of_week = str(day_of_week["WKST"])[3:5]

		start_time = component.get('DTSTART').dt
		start_time = str(start_time)[11:16]
		end_time = component.get('DTEND').dt
		end_time = str(end_time)[11:16]


		# print course_name, day_of_week, start_time, end_time

for component in cal_miguel.walk():
	if component.name == "VEVENT":
		course_name = component.get("SUMMARY")
		course_name = str(course_name)
		if course_name not in miguel_courses:
			miguel_courses.append(course_name)

		day_of_week = component.get("RRULE")
		day_of_week = dict(day_of_week)
		day_of_week = str(day_of_week["WKST"])[3:5]

		start_time = component.get('DTSTART').dt
		start_time = str(start_time)[11:16]
		end_time = component.get('DTEND').dt
		end_time = str(end_time)[11:16]


		# print course_name, day_of_week, start_time, end_time


# print prakhar_courses
# print adel_courses
# print david_courses
# d.setdefault(key, []).append(val)
test = {}
for course in prakhar_courses[1:]:
	test.setdefault(course, []).append(prakhar_courses[0])

for course in david_courses[1:]:
	test.setdefault(course, []).append(david_courses[0])

for course in adel_courses[1:]:
	test.setdefault(course, []).append(adel_courses[0])

for course in greg_courses[1:]:
	test.setdefault(course, []).append(greg_courses[0])

for course in miguel_courses[1:]:
	test.setdefault(course, []).append(miguel_courses[0])

for course in evan_courses[1:]:
	test.setdefault(course, []).append(evan_courses[0])

print test
for course in test:
	if len(test[course]) > 1:
		print course, test[course]

# common = list(set(prakhar_courses) & set(adel_courses) & set(david_courses))
# print common		
 
