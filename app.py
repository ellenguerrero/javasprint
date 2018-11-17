from sqlalchemy import func

from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


#database stuff ###################

###################################

@app.route('/')
def home():

    return render_template("index.html")

@app.route('/contact')
def contact():

    return render_template("contact.html")


@app.route('/field')
def fieldpage():

    return render_template("field.html")

@app.route('/track')
def trackpage():

    return render_template("track.html")

@app.route('/data')
def datapage():

    return render_template("data.html")




@app.route("/api/v1.0/field")
def fieldapi ():
    #tasks
    
    all = db.session.query().all()

    return jsonify(all)



@app.route("/api/v1.0/trackdiff")
def trackdiffapi ():
    #tasks
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db/olympic_sprint_differences_sql"
    db = SQLAlchemy(app)
    all = db.session.query().all()

    return jsonify(all)


@app.route("/api/v1.0/tracktimes")
def tracktimesapi ():
    #tasks
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db/olympic_sprint_times_sql"
    db = SQLAlchemy(app)
    all = db.session.query().all()

    return jsonify(all)







if __name__ == '__main__':
#     Bind to PORT if defined, otherwise default to 5000.
#     port = int(os.environ.get('PORT', 5000))
#     app.run(host='0.0.0.0', port=port)
    app.run(debug=True)