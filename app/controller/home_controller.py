from flask import render_template

class HomeController:
    
    def home():
       return render_template('index.html')