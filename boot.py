from flask import Flask, request, jsonify
import os
app = Flask(__name__)

@app.route("/")
def home():
    bg = os.getenv('background', 'yellow')
    color = os.getenv('color', 'red')
    text = os.getenv('text', 'This is a sample text')
    html = """
    <html>
        <head>
            <style>
            </style>
        </head>
        <body style='background-color:%s'>
            <h1 style='color: %s'>%s</h1>
        </body>
    </html>
    """
    return html % (bg, color, text)


@app.route("/test")
def test():
    return "This is a test"


@app.route("/json")
def json():
    return {
            "name": "ehsan",
            "age": 36
            }


@app.route("/auth", methods=['POST'])
def auth():
    # content = request.get_json(silent=True)
    params = request.get_json()
    username = params['username']
    password = params['password']
    if username == 'admin' and password == '123':
        return jsonify(isError=False,
                       message="Success",
                       statusCode=200,
                       data={}), 200
    else:
        return jsonify(isError=True,
                       message="Failed",
                       statusCode=401,
                       data={}), 401


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)

