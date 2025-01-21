from flask import Flask, render_template, request
import pandas as pd
import matplotlib.pyplot as plt
import os
from utils.model_utils import load_model_vectorizer, predict_cyberbullying
from utils.tweet_utils import extract_tweet_id, get_tweet_comments
from utils.preprocess import clean_text
from flask import Flask, request, jsonify


app = Flask(__name__)

# Load the model and vectorizer
model, tfidf_vectorizer = load_model_vectorizer()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict_comment', methods=['POST'])
def predict_comment():
    comment = request.form['comment']
    
    # Clean and predict the comment
    prediction = predict_cyberbullying([comment], tfidf_vectorizer, model)
    categories = ['toxic', 'obscene', 'insult', 'threat', 'identity hate']
    
    # Create a dictionary of predicted categories with their probabilities
    percentages = {categories[i]: round(prob * 100, 2) for i, prob in enumerate(prediction[0])}

    return render_template(
        'results_comment.html',
        comment=comment,
        percentages=percentages
    )

@app.route('/predict_tweet', methods=['POST'])
def predict_tweet():
    tweet_url = request.form['tweet_url']
    
    # Extract tweet ID from the URL
    tweet_id = extract_tweet_id(tweet_url)
    if not tweet_id:
        return "Invalid Tweet URL."

    comments = get_tweet_comments(tweet_id)
    if not comments:
        return "No comments found or an error occurred."

    comment_texts = [comment['text'] for comment in comments]
    
    # Predict cyberbullying categories for each comment
    predictions = predict_cyberbullying(comment_texts, tfidf_vectorizer, model)
    categories = ['toxic', 'obscene', 'insult', 'threat', 'identity hate']

    # First 10 comments
    first_10 = [{
        "text": comment,
        "percentages": {categories[i]: round(prob * 100, 2) for i, prob in enumerate(pred)}
    } for comment, pred in zip(comment_texts[:10], predictions[:10])]

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

    return render_template(
        'results_tweet.html',
        tweet_url=tweet_url,
        first_10=first_10,
        chart=chart_filename
    )


@app.route('/chatbot', methods=['POST'])
def chatbot():
    # Get the user's message from the JSON body
    user_message = request.json.get('message')
    
    # Clean and predict the user message using the model
    prediction = predict_cyberbullying([user_message], tfidf_vectorizer, model)
    categories = ['toxic', 'obscene', 'insult', 'threat', 'identity hate']
    
    # Create a dictionary of predicted categories with their probabilities
    percentages = {categories[i]: round(prob * 100, 2) for i, prob in enumerate(prediction[0])}
    
    # Respond based on the prediction result
    if max(percentages.values()) > 50:
        bot_response = f"Warning! This message seems to contain harmful content: {percentages}"
    else:
        bot_response = f"This message seems safe: {percentages}"

    # Return the response as JSON
    return jsonify({'reply': bot_response})
    user_message = request.form['user_message']
    
    # Clean and predict the user message using the model
    prediction = predict_cyberbullying([user_message], tfidf_vectorizer, model)
    categories = ['toxic', 'obscene', 'insult', 'threat', 'identity hate']
    
    # Create a dictionary of predicted categories with their probabilities
    percentages = {categories[i]: round(prob * 100, 2) for i, prob in enumerate(prediction[0])}
    
    # Respond based on the prediction result
    if max(percentages.values()) > 50:
        bot_response = f"Warning! This message seems to contain harmful content: {percentages}"
    else:
        bot_response = f"This message seems safe: {percentages}"

    return render_template('chatbot_response.html', user_message=user_message, bot_response=bot_response)

if __name__ == "__main__":
    app.run(debug=True)
