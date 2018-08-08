import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True


my_response = [
    {"response" : "Hello World"}
]

#routing the app towards the required link
@app.route('/nxchallenge/astarisborn', methods=['GET'])
def api_all():
    return jsonify(my_response)

# Define main() function to host the application on provided port
def main():
    app.run(host='0.0.0.0', port=5000, debug=True)


#Call the main function
if __name__ == '__main__':
    main()


