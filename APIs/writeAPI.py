# 1: import flask tools
from flask import Flask, request, jsonify

# 2: create the app (server)
app = Flask(__name__)

# 3: define the routes
@app.route("/") # use a decorator (@) with the app variable

# 4: define a function to the route and build a response
def home():
    return "Home" # returns plain html text : Home

@app.route("/hello")
def say_hello():
    return "Hello" # returns plain html text : Hello

# path parameter: dynamic value that can be passed in the path URL
@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "First Last",
        "email": "first.last@email.com"
    }

    # query parameter: extra value included after the main path
    extra = request.args.get("extra")

    if extra:
        user_data['extra'] = extra

    return jsonify(user_data), 200
    # can be tested with routes:
    #   http://127.0.0.1:5000/get-user/0001
    #   http://127.0.0.1:5000/get-user/0001?extra="hello"

# how to use POST
@app.route("/create-user", methods = ['POST'])
def create_user():
    #if request.method == 'POST':
    # check with if, if using more than one status codes in methods array

    data = request.get_json()
    return jsonify(data), 201


# 5: run the flask app (server)
if __name__ == "__main__":
    app.run(debug = True)