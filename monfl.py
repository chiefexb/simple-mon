from flask import Flask
from flask import render_template
from flask import render_template
import os

app=Flask (__name__)


    
@app.route("/")
def hello():
    return render_template("base.html",status="badge badge-danger",
        title = 'Home')
def main ():
    app.run(debug = True)
if __name__ == "__main__":
    main()