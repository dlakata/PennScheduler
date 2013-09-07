import os
from flask import Flask, render_template, redirect, request, url_for, send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

'''@app.route('/')
def home():
    return render_template('index.html')'''

UPLOAD_FOLDER = r'C:\Users\David\workspace\Test\begin'
ALLOWED_EXTENSIONS = set(['txt', 'png', 'jpg', 'jpeg', 'gif', 'ics'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
           
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        schedule = request.files['file']
        if schedule and allowed_file(schedule.filename):
            filename = secure_filename(schedule.filename)
            schedule.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method="post" enctype="multipart/form-data">
      <p><input type="file" name="file">
         <input type=submit value=Upload>
    </form>
    '''

@app.route('/upload', methods=['GET', 'POST'])
def up_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(UPLOAD_FOLDER)
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method="post" enctype="multipart/form-data">
      <p><input type="file" name="file">
         <input type=submit value=Upload>
    </form>
    '''

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)
    
if __name__ == '__main__':
    app.run()