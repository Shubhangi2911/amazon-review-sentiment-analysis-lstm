from flask import Flask, render_template, request
import pickle
import numpy as np

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

app = Flask(__name__)

# Load model + tokenizer
model = load_model("lstm_model.h5")

tokenizer = pickle.load(open("tokenizer.pkl", "rb"))

# Labels
sentiment_map = {
    0: "Negative",
    1: "Neutral",
    2: "Positive"
}

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    review = request.form['review']

    # Convert text → sequence
    sequence = tokenizer.texts_to_sequences([review])

    padded_sequence = pad_sequences(sequence, maxlen=200, padding='post')

    prediction = model.predict(padded_sequence, verbose=0)

    predicted_class = int(np.argmax(prediction))

    # Raw confidence (0–100)
    confidence_value = float(np.max(prediction) * 100)

    # Clean confidence (2 decimals)
    confidence_text = f"{confidence_value:.2f}%"

    sentiment = sentiment_map[predicted_class]

    # Color mapping
    if predicted_class == 2:
        color = "#2ecc71"   # green

    elif predicted_class == 0:
        color = "#e74c3c"   # red

    else:
        color = "#f39c12"   # orange

    return render_template(
        "index.html",
        prediction_text=sentiment,
        confidence=confidence_value,   # for progress bar
        confidence_text=confidence_text,  # for display
        review=review,
        color=color
    )


if __name__ == "__main__":
    app.run(debug=True)