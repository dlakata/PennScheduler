import colors
from itertools import combinations, groupby
from operator import itemgetter
from icalendar import Calendar

JSON_EVENT = "{{ title: '{}', start:'{}', end:'{}', allDay: false, backgroundColor:'{}'}},\n"

def time_analyze(time):
	"""
	Time documentation
	7:00 - 7:05 = 0
	7:05 - 7:10 = 1
	7:10 - 7:15 = 2
	7:15 - 7:20 = 3
	7:20 - 7:25 = 4
			.
			.
			.
	23:55 - 00:00 = 203
	"""
	if time == "00:00":
		return 204
	hour = int(time[0:2])
	hour = (hour - 7) * 12
	minutes = int(time[-2:]) // 5
	return hour + minutes

def two_times(time1,time2):
	time_range = []
	time1 = time_analyze(time1)
	time2 = time_analyze(time2)
	for i in range(time1,time2):
		time_range.append(i)
	return time_range

def final_time_conversion(time,day):
	"""
	Final_time documentation
	Creates a system to put all times in one list
	monday = 1000
	tuesday = 2000
		.
		.
		.
	sunday = 7000
	"""
	day_dict = {"MO":1000, "TU":2000,
	"WE":3000, "TH":4000, "FR":5000,
	"SA":6000, "SU":7000}
	return day_dict[day] + time_analyze(time)

def final_time_range(time1,time2,day):
	time_range = []
	time1 = final_time_conversion(time1, day)
	time2 = final_time_conversion(time2, day)
	for i in range(time1,time2):
		time_range.append(i)
	return time_range

def rev_time_analyze(numb):
	if numb == 204:
		return "22:00:00"
	hour = (numb // 12) + 7
	minutes = (numb % 12) * 5
	if len(str(hour)) == 1:
		hour = "0" + str(hour)
	if len(str(minutes)) == 1:
		minutes = "0" + str(minutes)
	return str(hour) + ":" + str(minutes) + ":" + "00"

def rev_day(listy):
	"""
	this inputs listy, which is in the format [2072,2077]
	and outputs in the format ["2013-09-02 13:15:00", "2013-09-02 13:15:00"]
	"""

	day_dict = {1:"2013-09-02", 2:"2013-09-03", 3:"2013-09-04",
	4:"2013-09-05", 5:"2013-09-06", 6:"2013-09-07", 7:"2013-09-08"}

	start = listy[0]
	end = listy[-1]
	start_day = day_dict[int(str(start)[0])]
	end_day = day_dict[int(str(end)[0])]

	start_time = rev_time_analyze(int(str(start)[1:]))
	end_time = rev_time_analyze(int(str(end)[1:])+1)

	start_final = str(start_day) + " " + str(start_time)
	end_final =  str(end_day) + " " + str(end_time)

	return [start_final, end_final]

def firstTuple(dictionaryTuple):
	setList = []
	for i in range(len(dictionaryTuple)):
		setList.append(dictionaryTuple[i][0])
	return setList

def secondTuple(dictionaryTuple):
	setList = []
	for i in range(len(dictionaryTuple)):
		setList.append(dictionaryTuple[i][1])
	return setList

def rangeMaker(timeRange):
	timeRange = list(timeRange)
	timeRange.sort()

	timeRangesList = []
	for k, g in groupby(enumerate(timeRange), lambda i_x:i_x[0]-i_x[1]):
		ranges = list(map(itemgetter(1), g))
		timeRangesList.append([ranges[0],ranges[-1]])
	return timeRangesList


def free_time_parse(dictionary):
	all_list = {}
	all_free_time = [i for i in range(1000,7204)]

	for name in iter(dictionary):
		all_free_time = [i for i in range(1000,7204)]
		
		cal = dictionary[name]
		cal = Calendar.from_ical(cal)
		for component in cal.walk():
			if component.name == "VEVENT":
				course_name = component.get("SUMMARY")
				course_name = str(course_name)

				day_of_week = str(component.get("RRULE")['BYDAY'][0])

				start_time = component.get('DTSTART').dt
				start_time = str(start_time)[11:16]
				end_time = component.get('DTEND').dt
				end_time = str(end_time)[11:16]

				class_time_range = final_time_range(start_time,end_time,day_of_week)
				for time in class_time_range:
					if time in all_free_time:
						all_free_time.remove(time)
		all_list[name] = all_free_time
	return all_list

def generalFreetime(freetimeDict):
	"""
	Takes dictionary of freetimes, keys are full names and values are lists of
	integers with the times that are available for that person.
	"""
	everybody = ", ".join(freetimeDict.keys())
	blacklistedSets = []
	freetimeDatabase = []

	for value in freetimeDict:
		freetimeDict[value] = set(freetimeDict[value])

	fullSet = set.intersection(*freetimeDict.values())
	blacklistedSets.append(fullSet)
	fullSet = rangeMaker(fullSet)
	# Add to database
	for i in fullSet:
		freetimeDatabase.append([everybody, rev_day(i),everybody.count(',')+1])

	for numComparing in range(len(freetimeDict.items()) - 1, 1, -1):
		for combination in combinations(freetimeDict.items(), numComparing):
			# Take shared elements of 2 sets without including prior elements
			subsetLists = set.intersection(*secondTuple(combination)).difference(*blacklistedSets)
			# Add shared elements to blacklist to avoid being included later
			blacklistedSets.append(subsetLists)
			partialset = rangeMaker(subsetLists)
			# Add partial items to database
			for i in partialset:
				freetimeDatabase.append([", ".join(firstTuple(combination)),rev_day(i),everybody.count(',')+1])
	return freetimeDatabase

def freeFormat(listlist):
	"""
	Return list of times as JSON
	Compatible with fullCalendar.js
	"""
	final = ""
	for block in listlist:
		final += JSON_EVENT.format(
			block[0],
			block[1][0],
			block[1][1],
			colors.choose_color(block[0].count(',')+1,block[2]))
	return final[:-2]
