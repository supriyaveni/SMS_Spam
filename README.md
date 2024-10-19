# SMS Spam Detection Web App
This is a web application that detects whether an SMS message is spam or not using a machine learning model. The app is deployed and available at [SMS Spam Detection](https://sms-spam-8r68.onrender.com).
## Features
- **Input**: Users can input an SMS message into the app.
- **Output**: The app predicts whether the SMS is spam or not based on the trained model.
## Dataset
The dataset used to train the model is publicly available on Kaggle: [Spam SMS Dataset](https://www.kaggle.com/datasets/tmehul/spamcsv).

## Model and Vectorizer
- The spam detection model is trained using a **TF-IDF Vectorizer** and a **Naive Bayes Classifier**.
- The trained model and vectorizer are saved as `spam_classifier_model.pkl` and `tfidf_vectorizer.pkl`, respectively.

## Deployment
The application is deployed using **Render** and can be accessed at the following link: [SMS Spam Detection App](https://sms-spam-8r68.onrender.com).

## How to Run Locally
1. Clone the repository:
   ```bash
   git clone <repository_url>
2.Navigate to the project directory:
 ```bash
 cd sms_spam_detection
3.Install the required dependencies::
```bash
 pip install -r requirements.txt
4.Run the application:
```bash
 python app.py
5.Open the app in your browser at http://localhost:5000.

## Requirements
- Python 3.x
- Flask
- Scikit-learn
- Pandas

Install the required libraries by running:
```bash
pip install -r requirements.txt



