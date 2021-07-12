from flask import Flask
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

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)

