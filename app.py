# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 00:11:52 2024

@author: mohdk
"""

# app
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# List of all drink names
drinks = [

    "Cola Zero Can", "Cola Can ", "Cola Zero Can", 
    "Fanta Can", "7up can zero","7up Regular Can",
    "Club Orange", "Lucozade Can","Energise can",
    "Starbucks 3 can","Starbucks Coffee","Vit-Hit can 1","Vit-Hit can 2",
    "Schweppes Tonic Water", "Schweppes Ginger Ale",
    "Vit-Hit Green", "Vit-Hit Orange", "Vit-Hit Pink","Vit-Hit Mango",
    "Volic Water Small", "Ballygowan Big", "Ballygowan small water",
    "Circle k tip water", "Circle K Water", "Circle K Green Water",
    "Fanta Bottle","Club orange Bottle","Club White Bottle",
    "Sprite Bottle","Cola White Bottle","Cola Black Bottle",
    "Cola Red Bottle","Red Bull (M)","Red bull (L)","Red Bull Blue (M)",
    "Red bull (S)",
    "Cosmic","Peach Vibe","Red Bull Blue (S)",
    "Monster original","Mon original Red",
    "Mon Peach","Mon Navy Blue","Mon Blue",
    "Mon punch","Mon Biege","Mon Dark Blue",
    "Mon White","Mon Light Pink","Mon Red",
    "Mon Pink","Mon Teal",
    "Celsus 1","Celsus 2","Celsus 3", "Celsus 4",
    "Lucozade Orange big", "Lucozade Sport Raspberry",
    "Lucozade Wild Berry", "Lucozade Orange Samll",
    "Lucozade Original small","Lucozade Original Big",
    "lucozade Mango","Energise Bottle","Water green",
    "Water Blue","Vital Green","Vital Mango","Lipona 1",
    "Lipona 2","Ribena","Blue Juice","Energise orange",
    "Circle k Water Big","Evian","Volic Yellow",
    "Volic red","Sparkling Orange","Sparkling Green",
    "Capri","Pepsi Small","7up big","Club Big",
    "Pepsi Big","Cola Red big","Cola Black Big"

]


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Collect form data
        quantities = request.form.getlist("quantity")
        extras = request.form.getlist("extra")
        stock_list = []

        # Combine data into a structured list
        for drink, quantity, extra in zip(drinks, quantities, extras):
            stock_list.append({"drink": drink, "quantity": quantity, "extra": extra})

        # Redirect to summary page with data
        return render_template("summarys.html", stock_list=stock_list)

    # If GET request, just render the form
    return render_template("indexs.html", drinks=drinks)


@app.route("/reset", methods=["GET"])
def reset():
    # Redirect to the main page
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug= False,host='0.0.0.0')
