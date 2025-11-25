import numpy as np
import pickle as pkl
import pandas as pd

def make_df(path):
    df = pd.read_csv(path)
    return df


def lower_case(X):
    for i,a in enumerate(X):
        X[i] = a.lower()
    return X

def find_X_y(df):
    return df.Name.to_numpy(),df.Gender.to_numpy()

def split(X,y,a):
    n_test = int(len(X) * a)
    rand = np.random.default_rng()
    splitter = rand.integers(low=0,high=len(X),size=n_test)

    X_test = X[splitter]
    y_test = y[splitter]

    mask = np.ones(len(X))
    mask[splitter] = 0
    mask = mask == 1
    X_train =  X[mask]
    y_train = y[mask]

    return X_train,y_train,X_test,y_test


def create_BOL(X):
    _X = np.zeros((len(X),26+26+26*26))
    for i,a in enumerate(X):
        for c in a:
            if(ord(c)-97<0) or (ord(c)-97>=26) : continue
            else : _X[i][ord(c)-97] +=1

        last_1 = ord(a[-1])-97
        if(len(a)>=2): 
            last_2 = ord(a[-2])-97
        else:
            last_2=0
        
        # last 1 character
        if 0<=last_1<26:
            _X[i][26+last_1] +=1
        # last 2 characters
        if 0<=last_1<26 and 0<=last_2<26:
            _X[i][26+last_2*26 +last_1] +=1

        
    return _X


if __name__ == '__main__':
    df = make_df('name_gender_dataset.csv')
    X,y = find_X_y(df)
    X = lower_case(X)
    X = create_BOL(X)

    X_train,y_train,X_test,y_test = split(X,y,0.2)
    with open('names_dataset_v1.pkl','wb') as f:
        pkl.dump({'X_train':X_train,'y_train':y_train,'X_test':X_test,'y_test':y_test},f)




