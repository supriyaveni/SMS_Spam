from flask import Flask, render_template, request
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__)

# Load the pre-trained model and TfidfVectorizer
model = joblib.load('spam_classifier_model.pkl')  # Replace with your saved model file path
tfidf = joblib.load('tfidf_vectorizer (1).pkl')  # Replace with your saved vectorizer file path


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get the message from the form
        message = request.form['message']

        # Transform the message using the saved TF-IDF Vectorizer
        message_transformed = tfidf.transform([message])

        # Make the prediction (0 for non-spam, 1 for spam)
        prediction = model.predict(message_transformed)[0]

        # Prepare the result to send back to the frontend
        result = "Spam" if prediction == 1 else "Non-Spam"

        return render_template('index.html', message=message, prediction=result)


if __name__ == "__main__":
    app.run(debug=True)
