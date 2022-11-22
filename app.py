from flask import Flask, render_template, request, flash

app= Flask(__name__)
app.secret_key="manbearpig_MUDMAN888"

@app.route("/hello")
def index():
    flash("Whats is your names ?")
    return render_template("index.html")


@app.route("/greet", methods=["POST","GET"])
def greet():
    flash ("Hi "+ str ( request.form['name_input'])+", greate to see you" ) 
    return render_template("index.html")
   