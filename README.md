# 🚀 AI-Driven Social Media Comment Classifier

## 🌟 Overview  
The **AI-Driven Social Media Comment Classifier** is a web-based application designed to analyze and classify comments from social media platforms, with a focus on Twitter. This system leverages an intelligent AI bot to classify comments based on user-defined criteria such as sentiment, relevance, or harmfulness. Users can input a tweet URL or manually input comments for analysis, and the results, including the top 10 comments, are displayed on a separate results page with clear visualizations.

---

## ✨ Features  
- **📝 Input Options**:  
  - 📎 Tweet URL input for fetching comments using the `X API`.  
  - 🖊️ Manual input box for user-provided comments.  

- **🤖 AI Classification**:  
  - Utilizes an intelligent AI bot to process and classify comments effectively.  

- **📊 Results Visualization**:  
  - Displays classification results in a detailed and visually appealing format.  
  - Lists the top 10 classified comments along with their scores or categories.  

- **💻 User-Friendly Interface**:  
  - Simple and intuitive UI for seamless interaction.  

---

## 📂 File Structure  
```plaintext
project-root/
├── models         # models pkl file
├── statics        # Static files (CSS, JavaScript, Images)
├── templates      # HTML templates for web pages
├── utils          # x or twitter api code and comments cleaning
├── app.py         # flask backend code
├── imghdr.py

**🛠️ Installation**
🔑 Prerequisites
Ensure you have the following installed on your system:

🐍 Python 3.8+
🌐 Flask
🔑 A valid X API key for fetching Twitter comments.
 
