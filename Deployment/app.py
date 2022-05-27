from flask import Flask, render_template, request, url_for
import numpy as np
import pickle

model_RFC = pickle.load(open("model/model_RFC_FP3.pkl", "rb"))
model_RRF = pickle.load(open("model/model_RRF_FP3.pkl", "rb"))

app = Flask(__name__, template_folder="templates")


@app.route('/')
def main():
    return render_template('main.html')

# Redirecting the API to predict the result


@app.route("/predict", methods=['POST'])
def predict():
    """
    For Rendering result on HTML GUI
    """
    int_features = [x for x in request.form.values()]
    final_features = [np.array(int_features)]

    prediction_RRF = model_RRF.predict(final_features)

    output_RRF = round(prediction_RRF[0])
    output_text_RRF = ''

    prediction_RFC = model_RFC.predict(final_features)

    output_RFC = round(prediction_RFC[0])
    output_text_RFC = ''
    
    if output_RFC == 0:
        output_text_RFC = 'pasien belum meninggal'
        if  output_RRF == 0:
            output_text_RRF = 'pasien belum meninggal'
        elif output_RRF == 1:
            output_text_RRF = 'pasien telah meninggal'
    elif output_RFC == 1:
        output_text_RFC = 'pasien telah meninggal'
        if  output_RRF == 0:
            output_text_RRF = 'pasien belum meninggal'
        elif output_RRF == 1:
            output_text_RRF = 'pasien telah meninggal'

    return render_template("main.html", prediction_text_RFC="Berdasarkan Random Forest Classifier, {} sebelum waktu follow-up berikutnya.".format(output_text_RFC), 
    prediction_text_RRF="\n\nBerdasarkan Random Forest Regressor, {} sebelum waktu follow-up berikutnya.".format(output_text_RRF))


if __name__ == '__main__':
    app.run(debug=True)
