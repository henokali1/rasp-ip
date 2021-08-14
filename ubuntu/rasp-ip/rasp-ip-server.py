from flask import Flask, render_template, send_from_directory, Response, request
import pickle as pickle
from time import time

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret!"


def read_db():
	with open('db.pickle', 'rb') as handle:
		val = pickle.load(handle)
	return val

def write_to_db(val):
	with open('db.pickle', 'wb') as handle:
		pickle.dump(val, handle, protocol=pickle.HIGHEST_PROTOCOL)


@app.route("/")
def dashboard():
	return render_template("dashboard.html")


@app.route('/save_ip')
def save_ip():
	ipts = int(time())
	ip = request.args.get('ip', default = '', type = str)
	name = request.args.get('name', default = '', type = str)
	ident = request.args.get('ident', default = '', type = str)
	od = read_db()
	od['ip']=ip
	od['name']=name
	od['ident']=ident
	od['ipts']=ipts
	write_to_db(od)
	return {'ip': ip, 'ipts': ipts, 'name': name, 'ident': ident}


@app.route('/lattest_data')
def lattest_data():
	d = read_db()
	print(d)
	cts = int(time())
	ipts = d['ipts']
	ip_diff = cts-ipts
	ip_exp = ip_diff > 61
	d['ip_exp']=ip_exp
	return d


if __name__=="__main__":
	# app.run(host=args.host,port=args.port)
	app.run(host='0.0.0.0', port=8001, debug=True)
