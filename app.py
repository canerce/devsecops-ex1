from flask import Flask, render_template, request
import yaml

app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def upload():
	if request.method == 'GET':
		return render_template("index.html")
	elif request.method == 'POST':
		file = request.files.get('file')
		data = yaml.load(file.read())
		return render_template("index.html",data=data)

if __name__ == "__main__":
    app.run('0.0.0.0',5000)
