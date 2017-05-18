from flask import Flask
    
app = Flask(__name__)



@app.route('/')
def home():
    return "Home Page"

@app.route('/home')
def home2():
    return "Home Page"


app.run(debug=True)