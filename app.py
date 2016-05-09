import csv
csv_path = './static/incendios.csv'
csv_obj = csv.DictReader(open(csv_path, 'r'))
csv_list = list(csv_obj)
csv_dict = dict([[o['IDPIF'], o] for o in csv_list])

import os
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def index():
	return render_template('index.html',
	object_list=csv_list)

def detail(number):
	return render_template('detail.html',
	object=csv_dict[number],)

app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))
if __name__ == '__main__':
								    app.run(
								        host="0.0.0.0",
								        port=8000,
								        use_reloader=True,
								        debug=True,
								    )
'</number>'