import numpy as np
import pickle as pkl
import pandas as pd



def make_df(path):
    df = pd.read_csv(path)
    return df

def is_boy(X_test,P_B,P_G):
    pred = np.sum(X_test * np.log(P_B)) - np.sum(X_test * np.log(P_G))
    return 1 if pred>0 else 0

def pred(X_train,P_B,P_G):
    y = np.zeros(len(X_train))
    for i,a in enumerate(X_train):
        y[i] = is_boy(a,P_B,P_G)
    return y


def find_P_B_G(X_train,y):
    P_B = np.zeros(len(X_train[0])) # prob of letter given boy
    P_G = np.zeros(len(X_train[0])) # prob of letter given girl
    n_b = 0
    n_g = 0
    for i,a in enumerate(X_train):
        if y[i]==1:
            P_B += a
            n_b += np.sum(a)
        else:
            P_G += a
            n_g += np.sum(a)

    n_b+=len(P_B)
    n_g+=len(P_G)
    P_B=(P_B+1)/n_b
    P_G=(P_G+1)/n_g
    print(np.sum(P_B),np.sum(P_G))
    return P_B,P_G

def find_error(y_pred,y):
    error = 0
    N = len(y_pred)
    for i,a in enumerate(y_pred):
        if a!=y[i]:
            error+=1
    return error/N*100

def create_feature(name,d):
    x = np.zeros(d)
    for c in name:
        if(ord(c)-97<0) or (ord(c)-97>=26) : continue
        else : x[ord(c)-97] +=1
    last_1 = ord(name[-1])-97
    last_2 = ord(name[-2])-97
    # last 1 character
    if 0<=last_1<26:
        x[26+last_1] +=1
    # last 2 characters
    if 0<=last_1<26 and 0<=last_2<26:
        x[26+last_2*26 +last_1] +=1
    
    return x

def get_train_test(path):
    with open(path,'rb') as f:
        data = pkl.load(f)
        X_train,y_train,X_test,y_test = data['X_train'],data['y_train'],data['X_test'],data['y_test']
    return X_train,y_train,X_test,y_test

if __name__ == '__main__':
    X_train,y_train,X_test,y_test = get_train_test('names_dataset_v2.pkl')
    d = len(X_train[0])
    P_B,P_G = find_P_B_G(X_train,y_train)
    y_pred = pred(X_train,P_B,P_G)
    err = find_error(y_pred,y_train)
    print("Traning Error:",err)

    y_pred = pred(X_test,P_B,P_G)
    err = find_error(y_pred,y_test)
    print("Testing Error:",err)
    iterate = 0
    while(True):
        name = input("Enter name in lower Case letter:")
        name = name.lower()

        if name.isalpha():
            x = create_feature(name,d)
            gender = "Boy" if is_boy(x,P_B,P_G) else "Girl"
            print("You are a good ",gender)
            iterate+=1
            if iterate==5:
                break
    
        

    

