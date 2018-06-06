from flask import Flask, Response, request
import requests
import hashlib

app = Flask(__name__)
salt = "UNIQUE_SALT"
def_name = 'Horse'


@app.route('/', methods=['GET', 'POST'])
def mainpage():
	name = def_name

	if request.method == 'POST':
        	name = request.form['name']

	salted_name = salt + name
	name_hash = hashlib.sha256(salted_name.encode()).hexdigest()

	header = '<html><head><title>Identidock</title></head><body>'
	body = '''<form method="POST">
		  Hello <input type="text" name="name" value="{0}">
		  <input type="submit" value="submit">
		  </form>
		  <p>You look like a:
		  <img src="/monster/{1}"/>
		  '''.format(name, name_hash)
	footer = '</body></html>'
	return header + body + footer

@app.route('/monster/<name>')
def get_identicon(name):
	req = requests.get('http://dnmonster:8080/monster/' + name + '?size=80')
	image = req.content

	return Response(image, mimetype='image/png')

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
