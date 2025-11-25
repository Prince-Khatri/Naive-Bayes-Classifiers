import numpy as np
import pickle as pkl
from math import log1p as log
with open('dataset.pkl','rb') as f:
    data = pkl.load(f)
    X,y = data['X'],data['y']

N=400

P_B = np.zeros(26) # prob of letter given boy
P_G = np.zeros(26) # prob of letter given girl


def is_boy(X_test):
    pred = 0
    for i,a in enumerate(X_test):
        # a-> no of times that letter repeated
        # then normal prob ratio of p|b and p|g for that letter
        pred+= a*(log(P_B[i]) - log(P_G[i]))
    
    return 1 if pred>0 else 0

def pred(X_train):
    y = np.zeros(N)
    for i,a in enumerate(X_train):
        y[i] = is_boy(a)
    return y


def find_P_B_G(X_train,y):
    global P_B
    global P_G
    for i,a in enumerate(X_train):
        if y[i]==1:
            P_B += a
        else:
            P_G += a

    P_B/=N/2
    P_G/=N/2

def find_error(y_pred,y):
    error = 0
    for i,a in enumerate(y_pred):
        if a!=y[i]:
            error+=1
    return error/N*100

def create_feature(name):
    x = np.zeros(26)
    for i in name:
        x[ord(i)-97] +=1
    return x

def train(X,y):
    find_P_B_G(X,y)
    y_pred = pred(X)
    err = find_error(y_pred,y)
    print("Error:",err)

if __name__ == '__main__':
    train(X,y)
    iterate = 0
    while(True):
        name = input("Enter name in lower Case letter:")
        name.lower()
        if name.isalpha():
            x = create_feature(name)
            gender = "Boy" if is_boy(x) else "Girl"
            print("You are a good ",gender)
            iterate+=1
            if iterate==5:
                break
        

    

