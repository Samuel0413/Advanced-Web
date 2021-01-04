from flask import Flask, render_template, send_file, request

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("welcome.html")

@app.route('/index.html')
def index1():
	return render_template("index.html")

@app.route('/cv.html')
def index3():
	return render_template("cv.html")

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')

