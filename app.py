import os, parse, sharedClasses, freeTime
from flask import Flask, render_template, redirect, request, url_for, send_from_directory
from werkzeug.utils import secure_filename
from icalendar import Calendar

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/schedule.html')
def schedule():
    return render_template('schedule.html')

@app.route('/humans.html')
def humans():
    return render_template('humans.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/help.html')
def help_page():
    return render_template('help.html')

UPLOAD_FOLDER = r'C:\Users\David\Documents\GitHub\PennScheduler\static\img\schedules'
ALLOWED_EXTENSIONS = set(['txt', 'png', 'jpg', 'jpeg', 'gif', 'ics'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
           
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        name1 = request.form['name1']
        schedule1 = request.files['file1']
        name2 = request.form['name2']
        schedule2 = request.files['file2']
        # if schedule1 and allowed_file(schedule1.filename):
            # filename = secure_filename(schedule1.filename)
            # print "David is awesome"
        # schedule1.stream.seek(0)
        
        def pretty_course_name(course):
            course = course[:-3]
            if course[-4] == " ":
                return course
            else:
                return course[0:4] + " " + course[4:7]
        
        schedule1 = schedule1.stream.read()
        schedule2 = schedule2.stream.read()
        
        schedule1 = Calendar.from_ical(schedule1)
        schedule2 = Calendar.from_ical(schedule2)
        
        path = "C:\Users\David\Documents\GitHub\PennScheduler\static\img\schedules"
        list_of_all_ics_files = []
        for filename in os.listdir(path):
            if not filename.endswith('.ics'):
                continue
            # filename is in the format adel.ics
            first_name = filename[:-4]
            file_dir = os.path.join(path, filename)
            if file_dir not in list_of_all_ics_files:
                list_of_all_ics_files.append([first_name, file_dir])
        
        all_list = []
        classtimes = {}
        classdays = {}
        for pair in list_of_all_ics_files:
            name = pair[0]
            filepath = pair[1]
            vars()[name] = open(filepath)
            name = vars()[name]
            temp_list = [pair[0]]()
        
        
            name = Calendar.from_ical(name.read())
            for component in name.walk():
                if component.name == "VEVENT":
                    course_name = component.get("SUMMARY")
                    course_name = str(course_name)
                    if course_name not in temp_list and "PREC" not in course_name:
                        temp_list.append(course_name)
        
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
            all_list.append(temp_list)
        
        for course in classdays:
            t = classdays[course]
            t = list(set(t))
            classdays[course] = t
        
        #------------------------------------------------------------
        print all_list
        
        
        #test is a dict in the format {class:[ppl in class]}
        test = {}
        for course_list in all_list:
            for course in course_list[1:]:
                test.setdefault(course, []).append(course_list[0])
        
        #prints classes with more than one person in them
        classListFinal = ""
        for course in test:
            if len(test[course]) > 1:
                classListFinal += pretty_course_name(course), test[course], classtimes[course], classdays[course]
                classListFinal += "<br>"
        return classListFinal       
            # return redirect(url_for('printDavid', f=schedule1))
            # return redirect(url_for('uploaded_file', filename=filename))
            # return redirect(url_for('printDavid', f=schedule1))
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
