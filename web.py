from flask import Flask, render_template, request
import os
from input_test import input_test
app = Flask(__name__)

@app.route("/")
def index():
	subject = request.values.get('subject')
	owner = request.values.get('owner')
	input_test(subject, owner)
	return render_template('index.html')

@app.route("/about")
def about():
	return render_template('about.html')

if __name__ == "__main__":
	port = int(os.environ.get("PORT",5000))
	app.run(host="192.168.61.195", port=port)