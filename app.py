
import numpy as np
from flask import Flask,request,app,render_template
from xgboost import XGBClassifier

def predciton(x):
    XGB=XGBClassifier()
   
   
    XGB.load_model("XGBOOST.json")
    
    y_pred=XGB.predict(x)
    pred={0:'Good', 1:'Poor', 2:'Standard'}
    return pred[y_pred[0]]


def parse_request_form_values(form_values):
    parsed_values = np.empty(len(form_values), dtype=object)
    for i, value in enumerate(form_values):


        try:
            parsed_values[i] = float(value)
        except TypeError:
            try:
                parsed_values[i] = int(value)
            except TypeError:
                parsed_values[i] = str(value)
            except ValueError:
                parsed_values[i] = str(value)                
        except ValueError:
            try:
                parsed_values[i] = int(value) 
            except ValueError:
                parsed_values[i] = str(value)
            except TypeError:
                parsed_values[i] = str(value)
    return parsed_values

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict",methods=["POST"])
def predict():

 
    data=list(request.form.values())
    data=parse_request_form_values(data)
    predict=predciton([data[6:]])

    return render_template("result.html",var=predict)

if __name__ == '__main__':
    app.run()
