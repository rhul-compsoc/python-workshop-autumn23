from flask import Flask, request
from flask import Response


app = Flask(__name__)


# Example of just a regular GET endpoint.
@app.route('/ping', methods=['GET'])
def get_ping():
    return 'ping'


# Example of a POST endpoint using the body to determine the response.
@app.route('/ping', methods=['POST'])
def post_ping():
    # Get the request data
    request_data = request.get_data(as_text=True)

    # Response varies on the request data
    if "ping" in request_data:
        return "pong"
    else:
        return Response(status=400)


# Example of a GET request using a parameter.
@app.route('/greet/<name>', methods=['GET'])
def get_greet(name):
    # Use parameter in resonse
    return f'Hello, {name}!'


# Example of a GET request using parameters and arguments.
@app.route('/math/<one>/<two>', methods=['GET'])
def get_result(one, two):
    # Get argument
    operation = request.args.get('operation')

    # Convert to ints
    one, two = int(one), int(two)

    # Argument determines response
    if operation == 'add':
        return str(one + two)
    elif operation == 'minus':
        return str(one - two)
    elif operation == 'divide':
        return str(one / two)
    elif operation == 'times':
        return str(one * two)
    else:
        # If an unrecognised argument we want to status 400
        return Response(status=400)


# A better example of a GET request using parameters and arguments.
@app.route('/echo/<str>', methods=['GET'])
def get_echo(str):
    # Get flip argument
    flip = request.args.get('flip')

    # If flip is true then return reversed.
    if flip == 'true':
        return reversed(str)
    else:
        return str


def run():
    app.run()
