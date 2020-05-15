#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def hello():
    #return "Hello World!"
    return render_template("index.html")

@app.route("/1006")
def newPage1006():
    return "1006 page"

@app.route("/pigeons")
def newPagePigeons():
    return render_template("pigeons.html")
    
#start the server
if __name__ == "__main__":
    app.run()