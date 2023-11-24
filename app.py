from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename

import sys, os, json, cv2
from xla import xuly

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = "uploads"
app.config['XLA'] = "xla_done"
DIR_ROOT = os.path.dirname(os.path.abspath(__file__))
# Phần mở rộng tệp cho phép
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    try:
        # Lấy file ảnh từ form
        image_file = request.files['image']

        # Lấy giá trị từ dropdown
        selected_option = request.form['options']

        # Xử lý ảnh ở đây (lưu vào thư mục, xử lý, ...)
        # Ví dụ: Lưu ảnh vào thư mục uploads
        image_path = os.path.join(DIR_ROOT, "uploads", image_file.filename)
        image_file.save(image_path)

        # Thực hiện các thao tác cần thiết với dữ liệu
        # image_path = os.path.join(DIR_ROOT, "uploads", image_file.filename)
        image_path = "uploads/Screenshot from 2023-11-02 09-01-02.png"
        return render_template('results.html', image_path=image_path, selected_option=selected_option)
    except Exception as e:
        return f"Error: {str(e)}"



if __name__ == '__main__':
    app.run(debug=True)