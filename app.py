#Importing the libraries
from flask import Flask, render_template, request
import pickle

#Global variables
app = Flask(__name__)
crop_damage = pickle.load(open("crop_damage.pkl", "rb"))

#User-defined functions
@app.route("/", methods=["GET"])
def Home():
    return render_template("CROP.html")

@app.route("/prediction", methods=["POST"])
def prediction():
    insect_count = int(request.form['estimated insect count'])
    
    if request.form['crop type'] == 'kharif':
        crop_type = 0
    else:
        crop_type = 1
        
    if request.form['soil type'] == 'Alluvial':
        soil_type = 0
    else:
        soil_type = 1
        
    if request.form['pesticide use category'] == 'Insecticides':
        pesticide = 0
    elif request.form['pesticide use category'] == 'Bactericides':
        pesticide = 1
    else:
        pesticide = 2
        
        
    doses = int(request.form['doses in week'])
    week_used = int(request.form['number of week used'])
    week_quit = int(request.form['number of week quit'])
    
    if request.form['season'] == 'Summer':
        season = 0
    elif request.form['season'] == 'Monsoon':
        season = 1
    else:
        season = 2
    
    prediction = crop_damage.predict([[insect_count,crop_type,soil_type,pesticide,doses,week_used,week_quit,season]])[0]

    
    
    return render_template("CROP.html", prediction_output=prediction)


#Main function
if __name__ == "__main__":
    app.run(debug=True)
