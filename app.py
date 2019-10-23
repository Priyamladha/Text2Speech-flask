from flask import Flask, render_template, request, jsonify
import tts

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')

def download_file():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text1 = request.form['text1']
    tts.changetoaudio(text1)
    return render_template("audio.html")

if __name__ == "__main__":
    app.run(debug=True)