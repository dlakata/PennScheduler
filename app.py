import freeTime
import sharedclass
from flask import Flask, render_template, redirect, request, url_for, send_from_directory, session
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.secret_key = "P+zg!FH[KfxWk6e.2MT_"


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


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
def render():
    return render_template('render.html', shared=session['shared'], free=session['free'])


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
        for i in range(0, int(numEntries)):
            d[request.form[
                "fullname-" + str(i + 1)]] = (request.files['file-' + str(i + 1)]).stream.read()
        shared = sharedclass.shared(d)
        free = freeTime.freeFormat(
            freeTime.generalFreetime(freeTime.free_time_parse(d)))
        session['shared'] = shared
        session['free'] = free
        return redirect(url_for('render'))
    return render_template('upload.html')


@app.route('/upload/<f>')
def printFilenameOld(f):
    return secure_filename(schedule.filename)


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

if __name__ == '__main__':
    app.run()
