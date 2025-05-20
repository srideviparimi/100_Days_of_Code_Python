from flask import Flask,render_template,request
import requests
from datetime import datetime as dt
import smtplib
import os
from dotenv import load_dotenv
app=Flask(__name__)
load_dotenv()
EMAIL=os.getenv("MY_EMAIL")
PASSWORD=os.getenv("PASSPORT")
def get_date():
    date_obj=dt.now()
    current_year=date_obj.strftime('%Y')
    return current_year

def get_blogs():
    resp = requests.get("https://api.npoint.io/6c2a802db718b4c1d515")
    blogs = resp.json()
    return blogs

@app.route('/')
def home():
    return render_template("index.html",blogs=get_blogs(),year=get_date())
@app.route('/about.html')
def about():
    return render_template("about.html",year=get_date())
@app.route('/post.html')
def first_post():
    return render_template("post.html",year=get_date(),blog=get_blogs()[0])
@app.route('/post.html/<int:id>')
def post(id):
    blogs=get_blogs()
    selected_blog=blogs[id]
    return render_template("post.html",year=get_date(),blog=selected_blog)
@app.route('/contact.html',methods=["GET","POST"])
def contact():
    if request.method=="POST":
        name = request.form['name']
        email = request.form['email_id']
        phone = request.form['phone_number']
        mess = request.form['message']
        message=(f"Subject: You got a new message from the contact form\n"
                 f"Name: {name}\n"
                 f"Email: {email}\n"
                 f"Phone Number: {phone}\n"
                 f"Message: {mess}")
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL,password=PASSWORD)
            connection.sendmail(from_addr=EMAIL,
                                to_addrs=EMAIL,
                                msg=message)
        print("email sent")

    return render_template("contact.html",year=get_date())


if __name__=="__main__":
    app.run(debug=True)