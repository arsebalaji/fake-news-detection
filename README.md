# 📰 Fake News Detection System

An AI-powered web application that analyzes news text and predicts whether it is **REAL** or **FAKE** using Machine Learning and Natural Language Processing (NLP).

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Flask](https://img.shields.io/badge/Flask-Backend-black)
![JavaScript](https://img.shields.io/badge/JavaScript-Frontend-yellow)
![Vercel](https://img.shields.io/badge/Deployed%20on-Vercel-black)
![GitHub](https://img.shields.io/badge/Source-GitHub-lightgrey)

---

## 📖 Project Overview

Misinformation spreads faster than ever, and separating real news from fake news has become a genuine challenge in today's digital world. The **Fake News Detection System** is a web application that helps users check the credibility of a news article by analyzing its text.

The user simply enters or pastes a news article into the web interface, and the system processes the text through an NLP pipeline and a Machine Learning model to classify it as **REAL** or **FAKE**. This project demonstrates how ML and NLP techniques can be combined with a modern web interface and a deployable backend to build a practical, real-world application.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔍 Real/Fake Prediction | Classifies input news text as REAL or FAKE |
| 🤖 Machine Learning | Uses a trained ML model for classification |
| 🧠 NLP | Processes and analyzes raw text before prediction |
| 🌐 Modern Web Interface | Clean and simple UI for entering news content |
| ⚡ API Integration | Frontend communicates with backend via REST API |
| ☁️ Vercel Deployment | Fully configured for deployment on Vercel |
| 📱 Responsive Design | Works smoothly across devices and screen sizes |

---

## ⚙️ How It Works

```text
User enters news
       ↓
Frontend
       ↓
API Request
       ↓
Python/ML Backend
       ↓
NLP Processing
       ↓
ML Prediction
       ↓
REAL / FAKE Result
```

1. The user enters a piece of news text into the frontend interface.
2. The frontend sends this text to the backend via an API request.
3. The Python backend processes the text using NLP techniques.
4. The processed text is passed to the ML model for prediction.
5. The result (REAL or FAKE) is sent back and displayed to the user.

---

## 🛠️ Technology Stack

| Category | Technologies |
|---|---|
| Frontend | HTML5, CSS3, JavaScript |
| Backend | Python, Flask |
| Core Logic | Machine Learning, NLP |
| Version Control | Git, GitHub |
| Deployment | Vercel |

---

## 🏗️ Project Architecture

| File/Folder | Purpose |
|---|---|
| `Backend/app.py` | Core Python backend application that handles NLP processing and ML-based prediction logic |
| `Frontend/index.html` | Main HTML structure of the web interface |
| `Frontend/script.js` | Handles frontend logic, user interaction, and API calls to the backend |
| `Frontend/style.css` | Provides styling and responsive design for the web interface |
| `api/index.py` | Vercel serverless API entry point that connects the frontend to backend logic in production |
| `requirements.txt` | Lists all Python dependencies required to run the project |
| `vercel.json` | Configuration file that defines how the project is built and deployed on Vercel |
| `.env.example` | Template file showing required environment variables without exposing actual secrets |

---

## 📂 Project Folder Structure

```text
fake-news-detection/
│
├── Backend/
│   └── app.py
│
├── Frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
│
├── api/
│   └── index.py
│
├── .env.example
├── .gitignore
├── requirements.txt
└── vercel.json
```

---

## 💻 Installation

Follow these steps to set up the project locally (Windows):

```bash
# 1. Clone the repository
git clone https://github.com/arsebalaji/fake-news-detection.git

# 2. Open the project folder
cd fake-news-detection

# 3. Create a virtual environment
python -m venv venv

# 4. Activate the virtual environment
venv\Scripts\activate

# 5. Install the required dependencies
pip install -r requirements.txt
```

---

## ▶️ Run Locally

1. Make sure your virtual environment is activated.
2. Start the Python backend:

```bash
cd Backend
python app.py
```

3. Open the `Frontend/index.html` file in your browser to access the web interface.
4. Enter a news text in the input field and submit it to get the prediction result.

---

## 📡 API Documentation

### Endpoint

```
/predict
```

### Method

```
POST
```

### Request Format

The API expects a JSON body containing the news text to be analyzed:

```json
{
  "text": "Enter the news article text here"
}
```

### Response Format

The API returns a JSON response containing the prediction result:

```json
{
  "prediction": "REAL"
}
```

*(Response can be either `"REAL"` or `"FAKE"` depending on the analysis.)*

---

## ☁️ Vercel Deployment

This project is configured to be deployed directly from GitHub to Vercel.

### Steps to Deploy

1. Push your project to a GitHub repository.
2. Go to [Vercel](https://vercel.com) and log in.
3. Click **New Project** and import your GitHub repository.
4. Vercel will automatically detect the `vercel.json` file in the repository root, which defines the build and routing configuration.
5. The `api/index.py` file serves as the serverless API entry point used by Vercel to run backend logic in production.
6. The `Frontend` folder contains the static frontend files served to users.
7. If your project requires environment variables (as defined in `.env.example`), configure them in the **Vercel Project Settings → Environment Variables** section before deploying.
8. Click **Deploy** and Vercel will build and host your project automatically.

---

## 🔐 Environment Variables

The `.env.example` file lists the environment variables required by the project, without containing any real values.

To use it locally:

1. Create a copy of `.env.example` and rename it to `.env`.
2. Fill in the required values in your local `.env` file.

> ⚠️ **Warning:** Never upload your actual `.env` file or any real API keys/secrets to GitHub. Always keep `.env` listed in `.gitignore` to prevent accidental exposure.

---

## 📸 Screenshots

### Home Page
![Home Page](screenshots/home.png)

### Prediction Result
![Prediction Result](screenshots/result.png)

---

## 🚀 Future Improvements

* Real-time news verification
* News URL analysis
* Confidence score for predictions
* Advanced Transformer-based models
* Multi-language support
* Integration with fact-checking APIs
* Prediction history tracking
* User authentication
* Admin dashboard

---

## 🎓 Learning Outcomes

This project demonstrates practical experience in:

* Python programming
* Machine Learning fundamentals
* Natural Language Processing (NLP)
* Building and consuming REST APIs
* Frontend web development (HTML, CSS, JavaScript)
* Git and GitHub version control
* Deploying full-stack applications
* Working with Vercel for deployment

---

## 💡 Use Cases

* Students and researchers checking the credibility of a news article before citing it.
* Readers verifying suspicious news content shared on social media.
* Journalists doing a quick preliminary check on submitted content.
* Developers and learners exploring how NLP and ML can be applied to real-world text classification problems.

---

## ⚠️ Limitations

* The model's predictions are based on patterns learned from training data and are **not guaranteed to be 100% accurate**.
* This tool should be used as a **supporting aid**, not a replacement for professional fact-checking or journalistic verification.
* Results may vary depending on the length, language, and context of the input text.

---

## 👤 Author

**Balaji Arse**

GitHub: [https://github.com/arsebalaji](https://github.com/arsebalaji)

---

## 📄 License

This project is created for **educational purposes** as part of a college/portfolio project. You are free to use, modify, and learn from this project for non-commercial and educational purposes. Please provide appropriate credit if you use this project as a reference.

---

⭐ If you found this project helpful, consider giving it a star on GitHub!
