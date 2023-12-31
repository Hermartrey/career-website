from flask import Flask, render_template, jsonify
from dummy import JOBS

app = Flask(__name__)

company_name = "Hr"

@app.route("/")
def hello_world():
    return render_template("home.html",jobs=JOBS, company_name = company_name)

@app.route("/api/jobs")
def api_jobs():
  return jsonify(JOBS)
  
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)


