from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
  data = {
    "title":"Flask Basic",
    "user":"Jun",
    "admin":True,
    "item_list":["I", "LOVE", "PYTHON"]
  }

  return render_template("index.html", data=data)

if __name__ == "__main__":
  app.run(debug=True, host="127.0.0.1", port=3000)