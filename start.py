from flask import Flask,render_template,request
import json
import apitest

with open('config.json', 'r') as c:
    params = json.load(c)["params"]

app=Flask(__name__)
@app.route("/")
@app.route("/ShaurydeepSaxena")
def home():
    leetc=apitest.leet()
    gfgc=apitest.gfg()
    hrank=apitest.hrank()
    codechef=apitest.codechef()

    return render_template("index.html",params=params,leetc=leetc,gfgc=gfgc,hrank=hrank,codechef=codechef)



# @app.route("/contact",methods=['GET', 'POST'])
# def contact():
#     if (request.method == 'POST'):
#         '''Fetch data and add it to the database'''
#         '''Fetch data->add entry to database through names of elements whose data has to be fetched'''
#         name = request.form.get('name')
#         email = request.form.get('email')
#         # subject = request.form.get('phone')
#         message = request.form.get('message')
#         Mail.send_message('New message from' + name, sender=email, recipents=params['gmail_user'], body=message + "\n")
#         return render_template("index.html")

app.run(debug=True)
