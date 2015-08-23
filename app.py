#flask-app-backbone

from flask import Flask

#create the application object
app = Flask(__name__)

#use decorators to link the function to a url
@app.route("/")
@app.route("/hello")

#define the view using a function
def hello_world():
	return "Hll wrld!"

#start the development server
if __name__ == "__main__":
	app.run()

