from flask import Flask, render_template, request, redirect, url_for, render_template_string
from werkzeug.utils import secure_filename
from validators.file_upload_validation import validate_extension, has_duplicates
from track.configs import UPLOAD_DIR, ALLOWED_EXTENSIONS
from track.generate_track import GenerateTrack
import os

app = Flask(__name__)
app.config["UPLOAD_DIR"] = UPLOAD_DIR
app.config["ALLOWED_EXTENSIONS"] = ALLOWED_EXTENSIONS
IS_VALID = False


@app.route("/", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        if request.files:
            midi_file = request.files["midi"]
            filename = secure_filename(midi_file.filename)
            IS_VALID = validate_extension(filename)
            filename = has_duplicates(filename)
            if IS_VALID:
                midi_file.save(os.path.join(app.config["UPLOAD_DIR"], filename))
                return redirect(url_for('generate_text', filename=filename), code=307)
            else:
                return render_template('invalid_file_extension.html')
    return render_template('upload_midi.html')


@app.route("/generate", methods=["POST", "GET"])
def generate_text():
    if request.method == "POST":
        filename = request.args['filename']
        track = GenerateTrack(filename)
        generated_track = track.play_song()
        return render_template("play_song.html", generated_track=generated_track)
    return render_template('invalid_file_extension.html')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
