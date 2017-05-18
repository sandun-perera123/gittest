from flask import Flask, render_template
from controller.engagement_controller import EngagementController
from controller.home_controller import HomeController
    
app = Flask(__name__)

#app.add_url_rule('/home',None, HomeController.home)

#app.add_url_rule('/engagement/get',None, EngagementController.getEngagements)


app.run(debug=True)
