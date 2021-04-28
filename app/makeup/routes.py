from flask import Blueprint, flash, request, redirect, url_for, send_from_directory
from flask import current_app as app
from werkzeug.utils import secure_filename
import os
import subprocess
import datetime

makeup = Blueprint('makeup', __name__)


@makeup.route('/', methods=['GET'])
def index():
    return 'hello makeup world'


@makeup.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@makeup.route('/process', methods=['GET', 'POST'])
def process():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'nomakeup' not in request.files and 'makeup' not in request.files:
            flash('No file part')
            return redirect(request.url)
        nomakeup = request.files['nomakeup']
        makeup = request.files['makeup']
        # file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if nomakeup.filename == '' or makeup.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if makeup and nomakeup:
            makeup_filename = secure_filename(makeup.filename)
            makeup_path = os.path.join(app.config['UPLOAD_FOLDER'], makeup_filename)
            makeup.save(makeup_path)

            nomakeup_filename = secure_filename(nomakeup.filename)
            nomakeup_path = os.path.join(app.config['UPLOAD_FOLDER'], nomakeup_filename)
            nomakeup.save(nomakeup_path)

            # process file
            ts = datetime.datetime.now().timestamp()
            result_filename = f'{ts}.png'
            result_path = os.path.join(app.config['UPLOAD_FOLDER'], result_filename)

            command = f'python3 demo.py --source_path {nomakeup_path} --reference_path {makeup_path} --save_path {result_path}'
            result_success = subprocess.check_output([command], shell=True)
            # return result_success

            return redirect(url_for('makeup.uploaded_file', filename=result_filename))
    return "hey"
