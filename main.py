from flask import Flask ,render_template,request
from app.utils import Prediction
import CONFIG

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route('/predict', methods = ["POST","GET"])
def predict_price():
    data = request.form
    pred_obj = Prediction()
    predicted_price = pred_obj.predict_price(data)
    print(predicted_price)
    
    return render_template("index.html" ,value = predicted_price)


if __name__ == "__main__":
    app.run(host=CONFIG.HOST,port=CONFIG.PORT,debug=CONFIG.DEBUG)