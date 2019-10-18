"""
Main module of the server file
"""

# 3rd party moudles
from flask import render_template
import connexion
from flask import request
import json

# Create the application instance
app = connexion.App(__name__, specification_dir="./")

# Read the swagger.yml file to configure the endpoints
app.add_api("swagger.yml")


# create a URL route in our application for "/"
@app.route("/")
def home():
    """
    This function just responds to the browser URL
    localhost:5000/

    :return:        the rendered template "home.html"
    """
    return render_template("home.html")


@app.route('/hello')
def hello_world():
    return 'Hello, World!'


@app.route('/post/test', methods=['POST'])
def receive_post():
    headers = request.headers
    return
    auth_token = headers.get('authorization-sha256')
    if not auth_token:
        return 'Unauthorized', 401
        data_string = request.get_data()
        data = json.loads(data_string)

        request_id = data.get('request_id')
        payload = data.get('payload')

        if request_id and payload:
            return 'Ok', 200
        else:
            return 'Bad Request', 400


if __name__ == "__main__":
    app.run(debug=True)
