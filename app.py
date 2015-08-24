#flask-app-backbone

from flask import Flask

#create the application object
app = Flask(__name__)

app.config["DEBUG"] = True

#use decorators to link the function to a url
@app.route("/")
@app.route("/hello")

#define the view using a function
def hello_world():
	return "Hll wrldasdasd!"

#dynamic routes
@app.route("/test/<search_query>")
def search(search_query):
	if search_query.lower() == "vikram":
		return "Hello, {}".format(search_query), 200
	else:
		return "404, not found", 404

@app.route("/test/<int:int_value>")
def return_int(int_value):
	return "The int value is {} and its added to 22 to get: {}".format(int_value, int_value + 22)

@app.route("/test/<float:float_value>")
def return_float(float_value):
	return "The float value is {} and its added to 22 to get: {}".format(float_value, float_value + 22)

@app.route("/test/<path:path_value>")
def return_path(path_value):
	return path_value

#start the development server
if __name__ == "__main__":
	app.run()

