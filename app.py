import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)

            #add mongo db name and the url linking to that database
app.config["MONGO_DBNAME"] = 'project3-gaa-players'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')


    
mongo = PyMongo(app)                                #create instance of pymongo. add app into it with method called constructor method

@app.route('/')
@app.route('/get_tasks')
def get_tasks():
    return render_template("player_profile.html", tasks=mongo.db.player_profile.find())
    
"""    
@app.route('/add_profile_data')
def add_profile_data():
    
    heights = []
    weights = []
    
    for types in mongo.db.height.find():
        height = types.get("player_height")
        for item in height:
            heights.append(item)


    for types in mongo.db.weight.find():
        weight = types.get("weight_in_kg")
        for item in weight:
            weights.append(item)
            
    return render_template('add_profile_data.html',county_name=mongo.db.county_name.find(), height = height, weight = weight)
"""   

"""            
@app.route('/add_profile_data')
def add_profile_data():
    return render_template('add_profile_data.html',
    county_name=mongo.db.county_name.find(),
    club_name=mongo.db.club_name.find(),
    height=mongo.db.height.find(),
    weight=mongo.db.weight.find(),
    player_profile = mongo.db.player_profile.find())
    
    
@app.route('/insert_player_profile', methods= ['POST'])
def insert_player_profile():
    player_profile = mongo.db.player_profile
    player_profile.insert_one(request.form.to_dict())
    return redirect(url_for('get_tasks'))
"""    
@app.route('/add_profile_data')
def add_profile_data():
    """route for adding profile data"""
    county_name=mongo.db.county_name.find()    #having var names better here
    height=mongo.db.height.find()              #as we can now see whats inside each var
    weight=mongo.db.weight.find()
    player_profile = mongo.db.player_profile.find()
    club_name=mongo.db.club_name.find()
    print(height)  #this shows what data is inside the var height
    print(weight)
    
    return render_template('add_profile_data.html', county_name=county_name, playerprofile=player_profile, weight=weight, height=height, club_name=club_name)
    
@app.route('/insert_player_profile', methods= ['GET','POST'])
def insert_player_profile():
    """function to insert player profile into db"""
    player_profile = mongo.db.player_profile
    player_profile.insert_one(request.form.to_dict())
    return redirect(url_for('get_tasks'))               #get tasks
    


@app.route('/edit_profile/<task_id>')
def edit_profile(task_id):
    the_task = mongo.db.task.find_one({"_id": ObjectId(task_id)})
    all_categories = mongo.db.categories.find()
    return render_template('edit_profile.html', task=the_task, categories=all_categories, county_name=mongo.db.county_name.find())
    
    

    
if __name__ == "__main__":          
    app.run(host=os.getenv('IP', '0.0.0.0'), 
            port=int(os.getenv('PORT', 8080)), 
            debug=True) 