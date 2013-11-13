import os, freeTime, sharedclass
from flask import Flask, render_template, redirect, request, url_for, send_from_directory
from werkzeug.utils import secure_filename
from icalendar import Calendar, Event

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# @app.route('/')
# def home():
#     return render_template('index.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/schedule')
def schedule():
    return render_template('schedule.html')

@app.route('/humans')
def humans():
    return render_template('humans.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/render')
@app.route('/render/<shared>/<free>')
def render(shared=None, free=None):
    return render_template('render.html', shared=shared, free=free)

@app.route('/help')
def help_page():
    return render_template('help.html')

@app.errorhandler(500)
def too_few(e):
    return render_template('too_few.html'), 500

UPLOAD_FOLDER = r'C:\Users\David\Documents\GitHub\PennScheduler\static\img\schedules'
ALLOWED_EXTENSIONS = set(['txt', 'ics'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
           
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        numEntries = request.form['id']
                    
        d = {}
#         name = []
#         schedule = []
        for i in range(0, int(numEntries)):
#            name.append(request.form["fullname-" + str(i+1)])
#            schedule.append((request.files['file-' + str(i+1)]).stream.read())
            d[request.form["fullname-" + str(i+1)]] = (request.files['file-' + str(i+1)]).stream.read()
        shared = sharedclass.shared(d)
        free = freeTime.freeFormat(freeTime.generalFreetime(freeTime.free_time_parse(d)))
#         fur = sharedclass.shared(d)
#         return fur
        return redirect(url_for('render', shared=shared, free=free))
        # return freeTime.freeFormat(freeTime.generalFreetime(freeTime.free_time_parse(d)))
#         name1 = request.form['name1']
#         schedule1 = request.files['file1']
#         name2 = request.form['name2']
#         schedule2 = request.files['file2']
        # if schedule1 and allowed_file(schedule1.filename):
            # filename = secure_filename(schedule1.filename)
            # print "David is awesome"
        # schedule1.stream.seek(0)
#             i = 1;
#     print 'fullname-'+i;
#     if request.method == 'POST':
#         numEntries = request.form['id']
#         name = [];
#         schedule = [];
#         for i in range(1,numEntries):
#             name[i] = request.form['fullname-'+i]
#             schedule[i] = request.form['file-'+i]
#             schedule[i] = schedule[i].stream.read()
#             print name[i]
#         schedule1 = schedule1.stream.read()
#         schedule2 = schedule2.stream.read()
#         schedule1 = Calendar.from_ical(schedule1)
#         schedule2 = Calendar.from_ical(schedule2)
#         
#         schedule_courses = [name1]
#         
#         for component in schedule1.walk():
#             if component.name == "VEVENT":
#                 course_name = component.get("SUMMARY")
#                 course_name = str(course_name)
#                 if course_name not in schedule_courses:
#                     schedule_courses.append(course_name)
#         
#                 day_of_week = component.get("RRULE")
#                 day_of_week = dict(day_of_week)
#                 day_of_week = str(day_of_week["WKST"])[3:5]
#         
#                 start_time = component.get('DTSTART').dt
#                 start_time = str(start_time)[11:16]
#                 end_time = component.get('DTEND').dt
#                 end_time = str(end_time)[11:16]
# 
#         schedule_courses1 = [name2]
#         
#         for component in schedule2.walk():
#             if component.name == "VEVENT":
#                 course_name = component.get("SUMMARY")
#                 course_name = str(course_name)
#                 if course_name not in schedule_courses1:
#                     schedule_courses1.append(course_name)
#         
#                 day_of_week = component.get("RRULE")
#                 day_of_week = dict(day_of_week)
#                 day_of_week = str(day_of_week["WKST"])[3:5]
#         
#                 start_time = component.get('DTSTART').dt
#                 start_time = str(start_time)[11:16]
#                 end_time = component.get('DTEND').dt
#                 end_time = str(end_time)[11:16]
#         return " ".join(schedule_courses) + "<br>" + " ".join(schedule_courses1)        
#             # return redirect(url_for('printDavid', f=schedule1))
#             # return redirect(url_for('uploaded_file', filename=filename))
#             # return redirect(url_for('printDavid', f=schedule1))
    return render_template('upload.html')

@app.route('/david/<f>')
def printDavid(f):
    print "Adel is awesome"
    return f.read()

@app.route('/upload/<f>')
def printFilenameOld(f):
    return secure_filename(schedule.filename)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)
    
if __name__ == '__main__':
    app.run()
