import numpy as np
import pickle
import random 
with open('dataset.pkl','rb') as f:
    data = pickle.load(f)
    X,y = data['X'],data['y']
Xn = np.zeros((400,26))
yn = np.zeros(400)

indicies = np.arange(len(X))

np.random.shuffle(indicies)

X = X[indicies]
y = y[indicies]

with open('dataset.pkl','wb') as f:
    pickle.dump({'X':X,'y':y},f)






    
