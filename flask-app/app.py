from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient


app = Flask(__name__)

client = MongoClient('mongodb://mongo_db:27017/')
db = client.user_profiles
collection = db.profiles


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    user_name = request.form.get('name')
    user_email = request.form.get('email')
    user_age = request.form.get('age')

    user_data = {
        'name': user_name,
        'email': user_email,
        'age': user_age
    }

    collection.insert_one(user_data)
    return redirect(url_for('thank_you'))

@app.route('/thank_you')
def thank_you():
    return "<h1>Thank you! Your profile has been created successfully</h1>"

if __name__=="__main__":
    app.run(host = "0.0.0.0", port = 5000, debug = True)