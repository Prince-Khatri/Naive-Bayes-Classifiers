from flask import Flask,request,url_for,render_template

from naive_bayes import is_boy,create_feature
import pickle as pkl
import numpy as np


app = Flask(__name__)


path_to_cond_prob  = 'cond_prob.pkl'


def get_cond_prob(path):
    with open(path,'rb') as f:
        data = pkl.load(f)
        P_B,P_G = data['P_B'],data['P_G']
    return P_B,P_G
current = []
@app.route('/',methods=['GET','POST'])
def predict():
    a=None
    
    if request.method=='POST':
        name = request.form['name']
        current.insert(0,[name])
        P_B,P_G = get_cond_prob(path_to_cond_prob)
        x = create_feature(name,len(P_B))
        a = 1 if is_boy(x,P_B,P_G) > 0 else 0
        print(a)
        current[0].append(a)
        print(current)
    
    return render_template('index.html',is_Boy = a,recent=current)

if __name__ == '__main__':
    # For deployment in render
    app.run(host="0.0.0.0",port=5050)
