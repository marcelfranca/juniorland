from flask import Flask, render_template, request, redirect
import speech_recognition as sr

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    transcript = ''
    if request.method == 'POST':
        print('Form data received')

        if 'file' not in request.files:
            return redirect(request.url)

        file = request.files['file']


