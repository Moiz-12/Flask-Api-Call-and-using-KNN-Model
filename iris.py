from flask import Flask, render_template, request,jsonify
import pickle
import pandas as pd
application = Flask(__name__)

with open ('knn_model.pkl','rb') as f:
    my_knn_model=pickle.load(f)

@application.route("/")
def Index():
    return render_template('iris.html')

def predict_specie(sepal_l,sepal_w,petal_l,petal_w):
    df=pd.DataFrame(columns=["sepal length","sepal width","petal length","petal width"])
    new_row={'sepal length':sepal_l,'sepal width':sepal_w,'petal length':petal_l,'petal width':petal_w}
    df=df.append(new_row,ignore_index=True)
    result=my_knn_model.predict(df)
    if result[0]==0:
        result='Iris-setosa'
    elif result[0]==1:
        result='Iris-versicolor'
    elif result[0]==2:
        result='Iris-virginica'
    return result


@application.route("/predict", methods=['POST'])
def train_model_fuc():
    sapel_ll = request.form['sl']
    sapel_ww = request.form['sw']
    petal_ll = request.form['pl']
    petal_ww = request.form['pw']
    prediction=predict_specie(sapel_ll,sapel_ww,petal_ll,petal_ww)
    return render_template('iris.html', results=prediction)

if __name__ == "__main__":
    application.run(host="localhost", port=3459, debug=True)