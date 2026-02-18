from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    rainfall = float(request.form["rainfall"])
    river = float(request.form["river"])
    drainage = float(request.form["drainage"])

    # Simple logic (you can change later)
    if rainfall > 100 and river > 50:
        result = "High Flood Risk"
    else:
        result = "Low Flood Risk"

    return render_template("index.html", prediction=result)

if __name__ == "__main__":
    app.run(debug=True)