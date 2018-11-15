from flask import Flask, render_template,request,redirect,url_for,jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import  func
import os


data = "./Olympic sqlite and csv files/        "
data = "./Olympic sqlite and csv files/        "
data = "./Olympic sqlite and csv files/        "




app = Flask(__name__)


@app.route('/')
def home():

    return redirect("http://www.example.com", code=302)

@app.route('/sprint')
def sprintpage():

    return redirect("http://www.example.com", code=302)


@app.route('/field')
def fieldpage():

    return redirect("http://www.example.com", code=302)


@app.route("/api/v1.0/field")
def fieldapi ():
    #tasks
     all = session.query().all()

   return jsonify()



@app.route("/api/v1.0/track")
def trackapi ():
    #tasks
    all = session.query().all()

   return jsonify()



@app.route("/remove")
def remove ():
    #Deleting a Task with various references
   
    return redirect("/")



if __name__ == '__main__':
#     Bind to PORT if defined, otherwise default to 5000.
#     port = int(os.environ.get('PORT', 5000))
#     app.run(host='0.0.0.0', port=port)
    app.run(debug=True)