from flask import Flask, render_template, request, send_file
import os
import tempfile

app = Flask(__name__)

# You'll replace this with your real genre-changing function
def change_genre(genre_file, source_file, output_path):
    # For now, just copy source_file as a dummy example
    with open(output_path, 'wb') as out:
        out.write(source_file.read())

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    genre_file = request.files['genreFile']
    source_file = request.files['sourceFile']
    
    output_path = tempfile.NamedTemporaryFile(suffix='.mp3', delete=False).name
    change_genre(genre_file, source_file, output_path)

    return send_file(output_path, as_attachment=True, download_name='converted_output.mp3')

import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Use the port provided by Render
    app.run(host='0.0.0.0', port=port)

