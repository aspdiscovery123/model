from flask import Flask
app = Flask(__name__)
import json
import joblib

@app.route("/",methods=["POST"])


def main():
    model=joblib.load('ccpp-model.pkl')
    data=json.loads(data)['data']
    out=model.predict(data)
    out=out.tolist()
    return {"output":out}

if __name__=="__main__":
    app.run(debug=True)
    
