from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.get('/')
def index():
    root_dir = os.path.dirname(os.path.realpath(__file__))
    return send_from_directory(root_dir, 'index.html')

if __name__ == "__main__":
    app.run()