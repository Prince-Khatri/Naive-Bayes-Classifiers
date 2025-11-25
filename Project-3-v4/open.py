import pickle
with open ('names_dataset_v1.pkl','rb') as f:
    data = pickle.load(f)
    # basic loading of the dataset
    X_t,X_test,y_t,y_test = data['X_train'],data['X_test'],data['y_train'],data['y_test']
    print(X_t[20000],'\n',X_test[20000],'\n',y_t[20000],'\n',y_test[20000])
