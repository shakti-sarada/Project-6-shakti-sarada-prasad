import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle


app = Flask(__name__)
model0 = pickle.load(open('Logistic-model.pkl','rb'))
model1 = pickle.load(open('Naive_Bayes-model.pkl','rb'))
model2 = pickle.load(open('SVM-model.pkl','rb'))
model3 = pickle.load(open('Random_Forest-model.pkl','rb'))
model4 = pickle.load(open('Decision_Tree-model.pkl','rb'))
model5 = pickle.load(open('KNN-model.pkl','rb'))


@app.route('/')
def home():
  
    return render_template("index.html")
  
@app.route('/predict_Logistic',methods=['GET'])

def predict_Logistic():
    
    Tenth = float(request.args.get('10th'))
    Twelth = float(request.args.get('12th'))
    BTech = float(request.args.get('B.Tech'))
    SeventhSEM = float(request.args.get('7-SEM'))
    SixthSEM = float(request.args.get('6-SEM'))
    FifthSEM = float(request.args.get('5-SEM'))
    FinalPerformance = float(request.args.get('Final Performance'))
    Medium = float(request.args.get('Medium'))
    
    		
    prediction = model0.predict([[Tenth,Twelth,BTech,SeventhSEM,SixthSEM,FifthSEM,FinalPerformance,Medium]])
    
    if prediction == 1:
      text = "Student is Placed"
    else:
      text = "Student is not Placed"

    return render_template('index.html', prediction_text='Logistic Regression Algorithm Prediction: {}'.format(text))

@app.route('/predict_NaiveBayes',methods=['GET'])

def predict_NaiveBayes():
    
    Tenth = float(request.args.get('10th'))
    Twelth = float(request.args.get('12th'))
    BTech = float(request.args.get('B.Tech'))
    SeventhSEM = float(request.args.get('7-SEM'))
    SixthSEM = float(request.args.get('6-SEM'))
    FifthSEM = float(request.args.get('5-SEM'))
    FinalPerformance = float(request.args.get('Final Performance'))
    Medium = float(request.args.get('Medium'))
    
    		
    prediction = model1.predict([[Tenth,Twelth,BTech,SeventhSEM,SixthSEM,FifthSEM,FinalPerformance,Medium]])
    
    if prediction == 1:
      text = "Student is Placed"
    else:
      text = "Student is not Placed"

    return render_template('index.html', prediction_text='Naive Bayes Algorithm: {}'.format(text))

@app.route('/predict_SVM',methods=['GET'])

def predict_SVM():
    
    PTenth = float(request.args.get('10th'))
    Twelth = float(request.args.get('12th'))
    BTech = float(request.args.get('B.Tech'))
    SeventhSEM = float(request.args.get('7-SEM'))
    SixthSEM = float(request.args.get('6-SEM'))
    FifthSEM = float(request.args.get('5-SEM'))
    FinalPerformance = float(request.args.get('Final Performance'))
    Medium = float(request.args.get('Medium'))
    
    		
    prediction = model2.predict([[PTenth,Twelth,BTech,SeventhSEM,SixthSEM,FifthSEM,FinalPerformance,Medium]])
    
    if prediction == 1:
      text = "Student is Placed"
    else:
      text = "Student is not Placed"

    return render_template('index.html', prediction_text='SVM Algorithm Prediction: {}'.format(text))

@app.route('/predict_RandomForest',methods=['GET'])

def predict_RandomForest():
    
    Tenth = float(request.args.get('10th'))
    Twelth = float(request.args.get('12th'))
    BTech = float(request.args.get('B.Tech'))
    SeventhSEM = float(request.args.get('7-SEM'))
    SixthSEM = float(request.args.get('6-SEM'))
    FifthSEM = float(request.args.get('5-SEM'))
    FinalPerformance = float(request.args.get('Final Performance'))
    Medium = float(request.args.get('Medium'))
    
    		
    prediction = model3.predict([[Tenth,Twelth,BTech,SeventhSEM,SixthSEM,FifthSEM,FinalPerformance,Medium]])
    
    if prediction == 1:
      text = "Student is Placed"
    else:
      text = "Student is not Placed"

    return render_template('index.html', prediction_text='Random Forest Algorithm Prediction: {}'.format(text))

@app.route('/predict_DecisionTree',methods=['GET'])

def predict_DecisionTree():
    
    Tenth = float(request.args.get('10th'))
    Twelth = float(request.args.get('12th'))
    BTech = float(request.args.get('B.Tech'))
    SeventhSEM = float(request.args.get('7-SEM'))
    SixthSEM = float(request.args.get('6-SEM'))
    FifthSEM = float(request.args.get('5-SEM'))
    FinalPerformance = float(request.args.get('Final Performance'))
    Medium = float(request.args.get('Medium'))
    
    		
    prediction = model4.predict([[Tenth,Twelth,BTech,SeventhSEM,SixthSEM,FifthSEM,FinalPerformance,Medium]])
    
    if prediction == 1:
      text = "Student is Placed"
    else:
      text = "Student is not Placed"

    return render_template('index.html', prediction_text='Decision Tree Algorithm Prediction : {}'.format(text))

@app.route('/predict_KNN',methods=['GET'])

def predict_KNN():
    
    Tenth = float(request.args.get('10th'))
    Twelth = float(request.args.get('12th'))
    BTech = float(request.args.get('B.Tech'))
    SeventhSEM = float(request.args.get('7-SEM'))
    SixthSEM = float(request.args.get('6-SEM'))
    FifthSEM = float(request.args.get('5-SEM'))
    FinalPerformance = float(request.args.get('Final Performance'))
    Medium = float(request.args.get('Medium'))
    
    		
    prediction = model5.predict([[Tenth,Twelth,BTech,SeventhSEM,SixthSEM,FifthSEM,FinalPerformance,Medium]])
    
    if prediction == 1:
      text = "Student is Placed"
    else:
      text = "Student is not Placed"

    return render_template('index.html', prediction_text='KNN Algorithm Prediction: {}'.format(text))


if __name__ == "__main__":
    app.run(debug=True)