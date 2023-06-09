from flask import Flask,jsonify,request
from classifier import getPrediction

app=Flask(__name__)
@app.route('/'  ,methods=['GET'])
def homePage():
    return "Welcome to alphabet detection page"

@app.route("/predict-alphabet",methods=['POST'])
def predict_digit():
    image=request.files.get("digit")
    prediction=getPrediction(image)
    return jsonify({
        "prediction":prediction
    }), 200

if __name__=="__main__":
    app.run(debug=True)