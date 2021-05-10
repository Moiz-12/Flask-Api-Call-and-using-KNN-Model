from flask import Flask, render_template, request,jsonify
application = Flask(__name__)
@application.route("/ab")
# def index():
#     return jsonify({
#         "moiz":"12"
#     })
    #return render_template('index.html')

# @application.route("/my_name/", methods=['POST'])
# def my_name():
#     first_number = request.form['fnum']
#     second_number = request.form['snum']
#     third_number = request.form['snum']


    # sum= int(first_number)+int(second_number)/int(third_number)
    # return render_template('index.html', results=sum)
@application.route("/a")
def encode():
    import pandas as pd
    df=pd.read_csv('C:/Users/user/Desktop/Ai/Iris.csv')
    from sklearn import preprocessing
    label_encoder = preprocessing.LabelEncoder()
    y= label_encoder.fit_transform(df['species'])
    return jsonify ({
        "moiz":list(y)
    })

@application.route("/b")
def preprocessing_and_traning_saving():
    import pandas as pd
    import os
    import numpy as np
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.metrics import confusion_matrix,accuracy_score
    from sklearn.model_selection import cross_val_score
    import pickle

    df=pd.read_csv('C:/Users/user/Desktop/Ai/Iris.csv')
    df.replace('Iris-setosa',1,inplace=True)
    df.replace('Iris-versicolor',2,inplace=True)
    X=df.drop('species',axis=1)
    y=df['species']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=424)
    knn=KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train, y_train)
    predicted= knn.predict(X_test)
    print(predicted)
    accuracy_score(y_test, predicted)*100
    with open ('knn_model.pkl','wb') as f:
        pickle.dump(knn,f)
    return jsonify ({"Path":os.getcwd()})

@application.route("/c")
def loading_model():
    import pickle
    import pandas as pd
    with open ('knn_model.pkl','rb') as f:
        my_knn_model=pickle.load(f)
    df=pd.DataFrame(columns=["sepal length","sepal width","petal length","petal width"])
    new_row={'sepal length':9,'sepal width':8,'petal length':5,'petal width':4}
    df=df.append(new_row,ignore_index=True)
    result=my_knn_model.predict(df)
    return jsonify ({"Path":list(result)})

@application.route("/abc")
def log():
    return render_template('login.html')


@application.route("/", methods=["POST"])
def login():
    username = request.form['uname']
    password = request.form['psw']
    if username=="qwe" and password=="123":
        return render_template('sucess.html')
    else:
        return render_template('tryagain.html')

if __name__ == "__main__":
    application.run(host="localhost", port=3459, debug=True)