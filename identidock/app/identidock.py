from flask import Flask, Response
import requests

app = Flask(__name__)
def_name = "Horse"

@app.route('/')
def mainpage():
	name = def_name

	header = '<html><head><title>Hello people</title></head><body>'
	body = '''<form method="Post">
		  Hello <input type="text" name="name" value="{}">
		  <input type="submit" value="Enter">
		  </form>
		  <p>You look like a:
		  <img src="/monster/monster.png"/>
		  '''.format(name)
	footer = '</body></html>'
	return header + body + footer

@app.route('/monster/<name>')
def get_identicon(name):
	req = requests.get('http://dnmonster:8080/monster/' + name + '?size=80')
	image = req.content

	return Response(image, mimetype='image/png')

if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0')
