from flask import Flask, render_template
from dbhelper import *

	

app = Flask(__name__)

head:list = ["ID", "ID NO" , "LAST NAME", "FIRST NAME", "COURSE", "LEVEL"]


@app.route("/")

def main()->None:
	
	studentlist = getrecord("students")
	return render_template("index.html", title = "student List", slist= studentlist, header = head)
	
	
if __name__ == "__main__":
	app.run(debug=True)