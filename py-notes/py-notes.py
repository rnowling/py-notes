import json

from flask import Flask
from flask import request

from models import Note

app = Flask(__name__)

notes = [Note(1, "Jogging in park"), Note(2, "Pick-up posters from post-office")]
created_notes = 2

@app.route("/")
def index():
	return "<h1>Hello World</h1>"

@app.route("/notes", methods=["GET"])
def get_notes():
	#note = Note(5, "some title")
	note_lst = [note.to_dict() for note in notes]
	return json.dumps(note_lst) + "\n"

@app.route("/notes", methods=["POST"])
def create_note():
	body = json.loads(request.data)
	created_notes += 1
	new_note = Note(created_notes, body["title"])
	notes.append(new_note)
	return json.dumps(new_note.to_dict()), 201



@app.route("/hello/<name>")
def hello(name):
	return "<h1>Hello, %s!</h1>" % name

if __name__ == "__main__":
	app.run(debug=True)
