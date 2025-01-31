# AI-Powered Harmful Digital Content Detection 🤖🚫

This repository contains an AI-powered tool designed to detect harmful and offensive comments or tweets. Using advanced Natural Language Processing (NLP) techniques and machine learning, the tool analyzes text for various categories such as toxicity, obscenity, insults, threats, and identity hate. This project aims to provide a safer digital space by identifying cyberbullying and harmful online content.

## Features 🌟

- **Real-time Comment Analysis**: Predict harmful content in user comments with a simple input.
- **Tweet Analysis**: Analyze tweets and detect harmful content in their replies.
- **Visualized Results**: Display prediction results in a user-friendly table format and generate bar charts for visual feedback.
- **Customizable Categories**: Detect various types of harmful content, including toxicity, obscenity, insults, threats, and identity hate.

## Demo 🎬

You can view the tool in action on the [Streamlit App](https://ai-powered-harmful-digital-content-detection.streamlit.app/).

## Technologies Used 💻

- **Python** 🐍
- **Streamlit** 📊
- **Scikit-learn** 🧠
- **Matplotlib** 📈
- **Natural Language Processing (NLP)** 💬
- **TF-IDF Vectorizer** 🔍

## Installation 🔧

### Prerequisites

To run the project locally, ensure you have Python 3.6+ installed.

### Clone the Repository

```
git clone https://github.com/UjjawalSah/AI-Powered-Harmful-Digital-Content-Detection.git
cd AI-Powered-Harmful-Digital-Content-Detection
```

## Installation 🔧

### Install Dependencies

Create a virtual environment and install the required dependencies.

```
pip install -r requirements.txt
```
#Run the Application
Start the Streamlit application by running the following command:
```
streamlit run app.py
```
## Usage 🛠️

### Predict a Comment
- Input a comment into the provided text box.
- Click **Predict** to analyze the comment for harmful content.
- The app will display the prediction results, including percentages for different categories such as toxicity, obscenity, and more.

### Predict Tweets
- Input a valid Tweet URL.
- Click **Analyze Tweet** to fetch comments from the tweet.
- The app will display predictions for the first 10 comments.

---

## How It Works 🧠

The tool uses a pre-trained machine learning model that classifies text into five categories:

- **Toxicity**: Harsh or abusive language.
- **Obscenity**: Inappropriate or offensive content.
- **Insults**: Disrespectful language targeted at individuals.
- **Threats**: Content that threatens harm to others.
- **Identity Hate**: Hate speech directed at specific groups based on identity.

It first preprocesses the text using TF-IDF vectorization and then feeds it into a machine learning model for classification. The results are presented as probabilities for each category.

---

## Contributing 🤝

We welcome contributions to improve the tool. To contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push the branch (`git push origin feature-name`).
5. Create a new Pull Request.

---

## License 📄

This project is **free to use** and is developed by **Ujjawal Kumar**.

---

## About the Developer 👨‍💻

This tool was developed by **Ujjawal Kumar**. You can find the source code and contribute on GitHub.

- [GitHub - Ujjawal Kumar](https://github.com/UjjawalSah)

---

## Acknowledgements 🙏

- **[Streamlit](https://streamlit.io/)** for providing an easy-to-use framework for building interactive apps.
- **[Scikit-learn](https://scikit-learn.org/)** for providing powerful machine learning tools.
- **[Matplotlib](https://matplotlib.org/)** for visualizing the prediction results.
