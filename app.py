from sqlalchemy import func

from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
import numpy as np
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db/olympic_sprint_differences_sql"
# db = SQLAlchemy(app)

#database stuff ###################
engine = create_engine("sqlite:///db/field_events.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)
FD = Base.classes.field_events_data_xlsx_Sheet1
# Create our session (link) from Python to the DB
session = Session(engine)
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
    # data = engine.execute("SELECT * FROM discus")
    results = session.query(FD.Sport, FD.Sex, FD.City, FD.Year, FD.G, FD.S, FD.B, FD.avg_medalists, FD.baseline_medalists).all()

    all_results = []
    for passenger in results:
        passenger_dict = {}
        passenger_dict["baseline_medalists"] = passenger.baseline_medalists
        passenger_dict["avg_medalists"] = passenger.avg_medalists
        passenger_dict["B"] = passenger.B
        passenger_dict["S"] = passenger.S
        passenger_dict["G"] = passenger.G
        passenger_dict["Year"] = passenger.Year
        passenger_dict["Sport"] = passenger.Sport
        passenger_dict["Sex"] = passenger.Sex
        passenger_dict["City"] = passenger.City
        all_results.append(passenger_dict)

    # print(data)
    return jsonify(all_results)



# @app.route("/api/v1.0/trackdiff")
# def trackdiffapi ():
#     #tasks
    
#     all = session.query().all()

#     return jsonify(all)


# @app.route("/api/v1.0/tracktimes")
# def tracktimesapi ():
#     #tasks
#     app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db/olympic_sprint_times_sql"
#     db = SQLAlchemy(app)
#     all = db.session.query().all()

#     return jsonify(all)







if __name__ == '__main__':
#     Bind to PORT if defined, otherwise default to 5000.
#     port = int(os.environ.get('PORT', 5000))
#     app.run(host='0.0.0.0', port=port)
    app.run(debug=True)