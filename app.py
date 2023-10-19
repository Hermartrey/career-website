from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    "id": 1,
    "title": "Python Developer",
    "location": "philippines",
    "salary": "100k",
  },
  {
    "id": 2,
    "title": "frontend engineer",
    "location": "singapore",
    "salary": "150k",
  },
  {
    "id": 3,
    "title": "backend engineer",
    "location": "japan",
    "salary": "180k",
  },
  {
    "id": 4,
    "title": "full stack developer",
    "location": "united states",
    "salary": "220k",
  }
]
company_name = "Hr"

@app.route("/")
def hello_world():
    return render_template("home.html",jobs=JOBS, company_name = company_name)

@app.route("/api/jobs")
def api_jobs():
  return jsonify(JOBS)
  
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)


