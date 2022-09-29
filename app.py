from flask import Flask, redirect, render_template, request, flash
from logiccode import makerequest, getids
import csv
app = Flask(__name__)
app.secret_key = "abcdef"
@app.route('/', methods = ['POST', 'GET'])

def main():
    if request.method == "GET":
        return render_template("index.html")
    else:
        studentid = request.form['id']
        jsonstuff = makerequest(studentid)
        if jsonstuff['name'] == "Invalid ID":
            flash("Invalid ID")
        elif jsonstuff['seniorPriv'] == False:
            flash("No Senior Privilege")
        else:
            flash("ID Accepted")
        return redirect("/")
if __name__ == "__main__":
    app.run(debug = True, port = 1234)