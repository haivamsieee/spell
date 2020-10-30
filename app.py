from flask import Flask, render_template, request
import enchant
import sys


app = Flask(__name__)
 
 
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():
 
    if request.method == 'POST':
 
        input_name = request.form['input_name']
        data=input_name
        ss='test.txt'
        reason_dict = enchant.PyPWL(ss)
        word_exists = reason_dict.check(data)
        if not word_exists:
    #get suggestions for the input word if the word doesn't exist in the dictionary
            suggestions = reason_dict.suggest(data)
        else:
            suggestions= "no suggestions"
    return render_template('index.html', prediction=suggestions)
if __name__ == '__main__':
    app.run()
    
 