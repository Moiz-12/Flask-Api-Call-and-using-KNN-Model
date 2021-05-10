from flask import Flask
from flask_restplus import Api, Resource, reqparse
import pickle
import pandas as pd

app=Flask(__name__)
api=Api(app)
parser=reqparse.RequestParser()


with open ('knn_model.pkl','rb') as f:
    my_knn_model=pickle.load(f)

@api.route('/say_hello/')
class HelloWorld(Resource):
    def get(self):
        return "Hellow World"

@api.route('/iris/<string:sepal_length>/<string:sepal_width>/<string:petal_length>/<string:petal_width>')
class HelloWorld(Resource):
    def post(self,sepal_length,sepal_width,petal_length,petal_width):
        prediction=predict_specie(sepal_length,sepal_width,petal_length,petal_width)
        return list(prediction)

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


@api.route('/my_name/<string:username>/<string:password>')
class HelloWorld(Resource):
    def post(self,username,password):
        if username=="qwe" and password=="123":
            return "sucess"
        else:
            return "tryagain"


if __name__ == "__main__":
    app.run(host="localhost", port=3459, debug=True)