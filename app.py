from flask import Flask, render_template, request
from werkzeug import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER']	= '/uploaded_images'

@app.route("/")
def hello():
    return "Ploder App!"

@app.route('/upload')
def upload_file():
   return render_template('upload.html')


@app.route("/uploader", methods = ['GET', 'POST'])
def uploader():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename('image'))
        return 'File uploaded sucessully'

if __name__ == "__main__":
    app.run()
