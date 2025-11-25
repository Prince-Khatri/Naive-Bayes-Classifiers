import numpy as np
import pickle
X = np.zeros((400,26))
y = np.zeros(400)
it=0
with open('boys.txt','r') as b:

    names = b.readlines()
    
    for name in names:
        for c in name:
            if 'a' <= c <= 'z' : 
                X[it][ord(c)-97]+=1
        y[it] = 1
        it+=1
with open('girls.txt','r') as g:

    names = g.readlines()
    for name in names:
        for c in name:
            if 'a' <= c <= 'z' : 
                X[it][ord(c)-97]+=1
        y[it] = 0
        it+=1

with open('dataset.pkl','wb') as f:
    pickle.dump({'X':X,'y':y},f)

print(X[0:400:50])
print(y[0:400:50])





