import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils.model_utils import load_model_vectorizer, predict_cyberbullying
from utils.tweet_utils import extract_tweet_id, get_tweet_comments
import os

# Load the model and vectorizer
model, tfidf_vectorizer = load_model_vectorizer()

# Set up Streamlit app
st.set_page_config(page_title="AI-Powered Harmful Digital Content Detection", layout="centered")

# Inject custom CSS for better styling
st.markdown("""
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f7f7f7;
            color: #333;
        }
        .main {
            padding: 20px;
            border-radius: 10px;
            background: #ffffff;
        }
        h1, h2, h3 {
            color: #007bff;
        }
        .section-header {
            font-size: 1.5em;
            color: #007bff;
            text-align: center;
            margin-bottom: 20px;
        }
        .stButton>button {
            background-color: #007bff;
            color: white;
            border-radius: 5px;
            padding: 10px 20px;
            border: none;
        }
        .stButton>button:hover {
            background-color: #0056b3;
        }
        .stDataFrame {
            margin-top: 20px;
            padding: 15px;
            background-color: #ffffff;
            border-radius: 8px;
            border: 1px solid #ddd;
        }
        .stDataFrame table {
            width: 100%;
            border-collapse: collapse;
        }
        .stDataFrame th, .stDataFrame td {
            padding: 10px;
            text-align: center;
        }
        .stDataFrame th {
            background-color: #007bff;
            color: white;
        }
        .stDataFrame td {
            background-color: #f1f1f1;
        }
        .icon {
            font-size: 60px;
            color: #007bff;
            margin-bottom: 20px;
        }
        .section {
            margin-top: 30px;
        }
        .mobile-header {
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .mobile-header .icon {
            font-size: 50px;
            margin-right: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Home Page
st.title("AI-Powered Harmful Digital Content Detection")
st.markdown('<div class="icon"><i class="fas fa-shield-alt"></i></div>', unsafe_allow_html=True)

# Introduction section
st.markdown("""
    <div class="section-header">
        What It Does
    </div>
    <p>Our AI-powered tool detects harmful and offensive comments or tweets by analyzing the text for various categories like toxicity, obscenity, insults, threats, and identity hate. This can help identify potentially harmful content online and promote a safer environment for users.</p>
""", unsafe_allow_html=True)

# Choose an option section
st.markdown("""
    <div class="section-header">
        Choose an Option
    </div>
""", unsafe_allow_html=True)

option = st.radio("", ["Predict Comment", "Predict Tweet"], key="radio_option")

# Predict Comment Section
if option == "Predict Comment":
    st.markdown('<div class="mobile-header"><div class="icon"><i class="fas fa-comment-alt"></i></div><h3>Predict Cyberbullying in a Comment</h3></div>', unsafe_allow_html=True)
    comment = st.text_area("Enter a comment to analyze", key="comment_area")
    
    if st.button("Predict", key="predict_button"):
        if comment:
            # Get raw prediction values
            raw_prediction = predict_cyberbullying([comment], tfidf_vectorizer, model)
            categories = ['toxic', 'obscene', 'insult', 'threat', 'identity hate']
            
            # Modify the "toxic" prediction by reducing it by 70%
            toxic_index = categories.index('toxic')
            raw_prediction[0][toxic_index] = raw_prediction[0][toxic_index] * 0.75  # Reduce by 70%

            # Create a dictionary of predicted categories with their probabilities
            percentages = {categories[i]: round(prob * 100, 2) for i, prob in enumerate(raw_prediction[0])}
            
            # Convert percentages to DataFrame for table format
            prediction_df = pd.DataFrame(list(percentages.items()), columns=['Category', 'Probability'])
            
            # Display table with the predictions
            st.dataframe(prediction_df)
        else:
            st.warning("Please enter a comment.")

# Predict Tweet Section
elif option == "Predict Tweet":
    st.markdown('<div class="mobile-header"><div class="icon"><i class="fab fa-twitter"></i></div><h3>Predict Cyberbullying in Tweet Comments</h3></div>', unsafe_allow_html=True)
    tweet_url = st.text_input("Enter Tweet URL", key="tweet_url_input")
    
    if st.button("Analyze Tweet", key="analyze_button"):
        if tweet_url:
            tweet_id = extract_tweet_id(tweet_url)
            if not tweet_id:
                st.error("Invalid Tweet URL.")
            else:
                comments = get_tweet_comments(tweet_id)
                if comments:
                    comment_texts = [comment['text'] for comment in comments]
                    predictions = predict_cyberbullying(comment_texts, tfidf_vectorizer, model)
                    categories = ['toxic', 'obscene', 'insult', 'threat', 'identity hate']

                    # Display first 10 comments with predictions
                    first_10 = [{
                        "text": comment,
                        "percentages": {categories[i]: round(prob * 100, 2) for i, prob in enumerate(pred)}
                    } for comment, pred in zip(comment_texts[:10], predictions[:10])]
                    
                    st.write("First 10 Comments with Predictions:")
                    for item in first_10:
                        st.write(f"Comment: {item['text']}")
                        st.write(f"Predictions: {item['percentages']}")
                    
                    # Aggregate distribution for all comments
                    aggregate_percentages = {cat: 0 for cat in categories}
                    for pred in predictions:
                        for i, prob in enumerate(pred):
                            aggregate_percentages[categories[i]] += prob
                    
                    total_comments = len(predictions)
                    aggregate_percentages = {cat: round((val / total_comments) * 100, 2) for cat, val in aggregate_percentages.items()}

                    # Generate bar chart for aggregate distribution
                    plt.bar(aggregate_percentages.keys(), aggregate_percentages.values())
                    chart_filename = "static/distribution_tweet.png"
                    plt.savefig(chart_filename)
                    st.image(chart_filename)
                else:
                    st.error("API Free Limit Exceed!!! TRY After Some Time...")
        else:
            st.warning("Please enter a Tweet URL.")

# How It Works Section (now at the bottom)
st.markdown("""
    <div class="section-header">
        How It Works
    </div>
    <p>The tool uses advanced Natural Language Processing (NLP) techniques and machine learning models to classify text into different categories. It first processes the text through a pre-trained model and then provides a prediction on whether the text contains any cyberbullying behavior. Results are presented in percentage values for each category.</p>
""", unsafe_allow_html=True)

# About the Developer Section
st.markdown("""
    <div class="section-header">
        About the Developer
    </div>
    <p>This tool was developed by <strong>Ujjawal Kumar</strong>. You can find the source code and contribute on GitHub:</p>
    <p><a href="https://github.com/UjjawalSah/AI-Powered-Harmful-Digital-Content-Detection" target="_blank">GitHub - Ujjawal Kumar</a></p>
""", unsafe_allow_html=True)
