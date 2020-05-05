from flask import Flask, render_template, send_file, request

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/index.html')
def index1():
	return render_template("index.html")

@app.route('/projects-grid-cards.html')
def index2():
	return render_template("projects-grid-cards.html")

@app.route('/cv.html')
def index3():
	return render_template("cv.html")

@app.route('/hire-me.html')
def index4():
	return render_template("hire-me.html")

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')

