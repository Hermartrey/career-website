from flask import Flask

app = Flask(__name__)
@app.route("/")
def hello_world():
    return "<h1>hello hermart</h1>"

@app.route("/about")
def about():
  return "<h1>You are in the about section</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
