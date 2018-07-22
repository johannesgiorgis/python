from flask import flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	"""Print 'Hello world!' as the response body."""
	return 'Hello world!'