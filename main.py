from flask import Flask
import os

# TODO: Create FS/PhotoDump


app = Flask(__name__)

@app.route('/')
def index():
    # TODO: parse first fs system (album)
    pass

@app.route('/<name>')
def name():
    # TODO: Pass layer 1 FS system -> photos for now
    pass

