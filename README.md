
# Gender Prediction from Name — Naive Bayes + Flask (v3)

This project predicts whether a name is typically associated with a boy or a girl using a Naive Bayes classifier implemented from scratch, with character n-gram features.

 

## Features
- Trained on a dataset of 150,000+ names
- Achieved a 0.715 F1 Score on test data
- Naive Bayes model written entirely from scratch
- Character n-gram feature encoding (unigram + bigram)
- Flask API for real-time predictions

 

## Model Overview
The model uses:
- Unigram counts (a–z)
- Last-character unigram
- Last bigram (combination of last two letters)

The classifier compares the log-likelihood of the name belonging to a boy vs a girl.

If score > 0 → Boy  
Else → Girl

 

## Project Structure
```
.
├── app.py               
├── naive_bayes.py       
├── templates/
│   └── index.html       
├── static/
│   ├── boy.png
│   └── girl.png
├── cond_prob.pkl        
└── names_dataset_v1.pkl 
```
 

## Run Locally

1. Install dependencies:

```
pip install flask numpy pandas
```

2. Train the model (only if not trained):
```
python naive_bayes.py
```


3. Start the Flask app:
```
python app.py
```

Open http://127.0.0.1:5000/ in your browser.

 

## Technologies Used
- Python
- Flask
- Bootstrap
- NumPy
- Pandas
