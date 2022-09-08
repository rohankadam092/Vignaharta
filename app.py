from flask import *
from dbm import view,viewcity
app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index1.html")

@app.route("/ganpatiinfo")
def info():
    data=view()
    return render_template("ganpatiproject.html",i=data)

@app.route("/ganpatiinfo",methods=["post"])
def info1():
    city = request.form["City"]
    if city=="All":
        data=view()
        return render_template("ganpatiproject.html",i=data)
    else:
        data=viewcity(city)
        return render_template("ganpatiproject.html",i=data)
    
@app.route("/aboutus")
def about():
    return render_template("aboutus.html")


@app.route("/maps")
def map():
    return render_template("map.html")


if __name__=="__main__":
    app.run(debug=True)