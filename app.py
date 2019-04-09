import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)

            #add mongo db name and the url linking to that database
app.config["MONGO_DBNAME"] = 'project3-gaa-players'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')


    
mongo = PyMongo(app)                                #create instance of pymongo. add app into it with method called constructor method

@app.route('/')
@app.route('/get_tasks')
def get_tasks():
    return render_template("player_profile.html", tasks=mongo.db.player_profile.find())
    
    
    
if __name__ == "__main__":          
    app.run(host=os.getenv('IP', '0.0.0.0'), 
            port=int(os.getenv('PORT', 8080)), 
            debug=True) 