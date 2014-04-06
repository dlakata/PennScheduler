from icalendar import Calendar

def prettyCourseName(course):
	course = course[:-3]
	if course[-4] == " ":
		return course
	else:
		return course[0:4] + " " + course[4:7]

def weekdays(day):
	daylist = {'MO':'02', 'TU':'03', 'WE':'04', 'TH':'05', 'FR':'06', 'SA':'07', 'SU':'08'}
	return daylist[day]

def shared(dictionary):
	all_list = []
	classtimes = {}
	classdays = {}

	for name in iter(dictionary):
		temp_list = [name]
		cal = dictionary[name]
		cal = Calendar.from_ical(cal)
		for component in cal.walk():
			if component.name == "VEVENT":
				course_name = component.get("SUMMARY")
				course_name = str(course_name)
				if course_name not in temp_list and "PREC" not in course_name:
					temp_list.append(course_name)

				day_of_week = component.get("RRULE")
				day_of_week = dict(day_of_week)
				day_of_week = str(day_of_week["WKST"])[2:4]

				start_time = component.get('DTSTART').dt
				start_time = str(start_time)[11:16]
				end_time = component.get('DTEND').dt
				end_time = str(end_time)[11:16]

				if course_name not in classtimes:
					classtimes[course_name] = [start_time, end_time]
				classdays.setdefault(course_name, []).append(day_of_week)
		all_list.append(temp_list)

	for course in classdays:
		t = classdays[course]
		t = list(set(t))
		classdays[course] = t

	students = {}
	for course_list in all_list:
		for course in course_list[1:]:
			students.setdefault(course, []).append(course_list[0])

	final = ""
	for course in students:
		if len(students[course]) > 1:
			for day in classdays[course]:
				final += "{ title: '%s (%s)', start:'2013-09-%s %s:00', end:'2013-09-%s %s:00', allDay: false},\n" % (prettyCourseName(course), ", ".join(students[course]), weekdays(day), classtimes[course][0], weekdays(day), classtimes[course][1])
	return final[:-2]
