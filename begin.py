import os
from flask import Flask, render_template, redirect, request, url_for, send_from_directory
from werkzeug.utils import secure_filename

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

UPLOAD_FOLDER = r'C:\Users\David\workspace\Test\begin'
ALLOWED_EXTENSIONS = set(['txt', 'png', 'jpg', 'jpeg', 'gif', 'ics'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
           
@app.route('/upload.html', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        schedule = request.files['file']
        if schedule and allowed_file(schedule.filename):
            filename = secure_filename(schedule.filename)
            schedule.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template('index.html')
    return render_template('upload.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)
    
if __name__ == '__main__':
    app.run()