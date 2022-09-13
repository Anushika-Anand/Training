from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello_world():
    return "<h2> This is the first web app by anushika</h2>"
if __name__ == "__main__":
    app.run()
