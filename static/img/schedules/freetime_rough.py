from icalendar import Calendar, Event


def time_analyze(time):
	hour = int(time[0:2])
	hour = (hour - 6) * 60
	minutes = int(time[-2:])
	return hour + minutes

def two_times(time1, time2):
	time_range = []
	time1 = time_analyze(time1)
	time2 = time_analyze(time2)
	for i in range(time1,time2, 5):
		time_range.append(i)
	return time_range

all_times = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200, 205, 210, 215, 220, 225, 230, 235, 240, 245, 250, 255, 260, 265, 270, 275, 280, 285, 290, 295, 300, 305, 310, 315, 320, 325, 330, 335, 340, 345, 350, 355, 360, 365, 370, 375, 380, 385, 390, 395, 400, 405, 410, 415, 420, 425, 430, 435, 440, 445, 450, 455, 460, 465, 470, 475, 480, 485, 490, 495, 500, 505, 510, 515, 520, 525, 530, 535, 540, 545, 550, 555, 560, 565, 570, 575, 580, 585, 590, 595, 600, 605, 610, 615, 620, 625, 630, 635, 640, 645, 650, 655, 660, 665, 670, 675, 680, 685, 690, 695, 700, 705, 710, 715, 720, 725, 730, 735, 740, 745, 750, 755, 760, 765, 770, 775, 780, 785, 790, 795, 800, 805, 810, 815, 820, 825, 830, 835, 840, 845, 850, 855, 860, 865, 870, 875, 880, 885, 890, 895, 900, 905, 910, 915, 920, 925, 930, 935, 940, 945, 950, 955, 960, 965, 970, 975, 980, 985, 990, 995, 1000, 1005, 1010, 1015, 1020, 1025, 1030, 1035, 1040, 1045, 1050, 1055, 1060, 1065, 1070, 1075]

prakhar = open("prakhar.ics")
cal_prakhar = Calendar.from_ical(prakhar.read())
prakhar_courses = ["prakhar"]

monday = ["prakhar"]
tuesday = ["prakhar"]
wednesday = ["prakhar"]
thursday = ["prakhar"]
friday = ["prakhar"]
saturday = ["prakhar"]
sunday = ["prakhar"]

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

		if day_of_week == "MO":
			monday.append([start_time,end_time])
		if day_of_week == "TU":
			tuesday.append([start_time,end_time])
		if day_of_week == "WE":
			wednesday.append([start_time,end_time])
		if day_of_week == "TH":
			thursday.append([start_time,end_time])
		if day_of_week == "FR":
			friday.append([start_time,end_time])
		if day_of_week == "SA":
			saturday.append([start_time,end_time])
		if day_of_week == "SU":
			sunday.append([start_time,end_time])

		print course_name, day_of_week, start_time, end_time

print monday
print tuesday
print friday
print sunday
print wednesday
# 		listy = two_times(start_time, end_time)
# 		all_times = list(set(all_times) - set(listy))
# all_times.sort()
# print all_times