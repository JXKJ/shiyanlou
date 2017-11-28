from flask import Flask ,render_template,abort
import json

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD']=True
def _read_title(paths):
	titel_list = list()
	for path in paths:
		with open(path,'r') as file:
			jsonStr=json.loads(file.read())
			titel_list.append(jsonStr['title'])
	return titel_list

def _read_file(path):
	with open(path,'r') as file:
		jsonStr=json.loads(file.read())
	return jsonStr

@app.route('/')
def index():
	paths=['../files/helloworld.json','../files/helloshiyanlou.json']
	title_list = _read_title(paths)
	return render_template('index.html',title_list=title_list)

@app.route('/files/<filename>')
def file(filename):
	try:
		filename = str(filename)
	except ValueError:
		abort(404)
	try:
		path = '../files/'+filename+'.json'
		fileinof=_read_file(path)
	except:
		abort(404)
	return render_template('file.html',fileinof=fileinof)

@app.errorhandler(404)
def not_found(error):
	return render_template('404.html'),404

if __name__=='main':
	app.run(port=3000)