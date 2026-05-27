COMPLETE README.md FILE
# 📊 Customer Feedback Sentiment Analysis Using NLP & Deep Learning (LSTM)

<p align="center">
  <img src="https://raw.githubusercontent.com/Shubhangi2911/amazon-review-sentiment-analysis-lstm/main/static/screenshots/app.png" width="800">
</p>

---

## 📌 Project Overview

This project is an NLP-based **Sentiment Analysis System** that classifies customer reviews into:

- 😊 Positive  
- 😐 Neutral  
- 😡 Negative  

It uses a **Deep Learning LSTM (Long Short-Term Memory)** model to understand the context and sequence of words in reviews and predict sentiment in real time.

A **Flask web application** is used to deploy the model for user interaction.

---

## 🚀 Features

- 🔥 Real-time sentiment prediction  
- 🧠 LSTM Deep Learning model  
- 🔤 Tokenization + Padding pipeline  
- 📊 Confidence score display  
- 🎨 Clean and responsive UI  
- 🎯 Color-coded sentiment output  
- 🌐 Flask backend integration  

---

## 🧠 Tech Stack

- Python  
- Flask  
- TensorFlow / Keras  
- NumPy  
- HTML / CSS  
- NLP (Tokenizer, Padding)  

---

## 🔁 Model Workflow

```text
Review Input
   ↓
Tokenizer
   ↓
Text → Sequences
   ↓
Padding (Fixed Length)
   ↓
LSTM Model
   ↓
Dense Layer (Softmax)
   ↓
Sentiment Prediction
📁 Project Structure
project/
│
├── app.py
├── lstm_model.h5
├── tokenizer.pkl
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── screenshots/
│       └── app.png
📂 Dataset Information

The dataset contains Amazon food product reviews, including:

Snacks
Coffee / Tea
Chocolates
Baby food
Organic products
Sentiment Labels:
Score	Sentiment
1–2	Negative
3	Neutral
4–5	Positive
⚙️ Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/Shubhangi2911/amazon-review-sentiment-analysis-lstm.git
cd amazon-review-sentiment-analysis-lstm
2️⃣ Create Virtual Environment
python -m venv venv

Activate environment:

venv\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run Application
python app.py
🌐 Open in Browser
http://127.0.0.1:5000
🧪 Example Test Cases
😊 Positive Review

This product is amazing and worth every penny. Excellent quality and fast delivery.

😡 Negative Review

Worst product ever. Very poor quality and waste of money. Completely disappointed.

😐 Neutral Review

The product is okay. Not too good and not too bad.

📈 Model Output
Sentiment Prediction
Confidence Score (e.g., 98.51%)
Visual Color-coded Result
🔮 Future Improvements
BiLSTM / GRU improvement
Transformer models (BERT)
Dashboard analytics
Cloud deployment (Render / AWS)
CSV batch prediction
🎯 Conclusion

This project demonstrates how Deep Learning (LSTM) can be used for automated sentiment analysis of customer reviews.

It helps businesses understand customer feedback efficiently and in real time.

👨‍💻 Author

Shubhangi Salve
