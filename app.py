import pickle
import streamlit as st
import  string
import  nltk
from nltk.stem.porter import  PorterStemmer
ps = PorterStemmer()
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB

tf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))



st.set_page_config(page_title="SMS Spam detection", page_icon="📧", layout="wide")


st.title('Email/SMS Spam Classifier')
input_sms = st.text_area('Enter the message')

if st.button('Predit'):

    # 1.Preprocess
    n = ['would','ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once',
         'during', 'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours',
         'such', 'into', 'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each',
         'the', 'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were',
         'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their', 'while', 'above', 'both', 'up', 'to', 'ours',
         'had', 'she', 'all', 'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on',
         'does', 'yourselves', 'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now', 'under',
         'he', 'you', 'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom',
         't', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'furthe', 'was', 'here', 'than']

    def transform_text(text):
        # Lower
        text = text.lower()
        # Tokenization
        text = nltk.word_tokenize(text)
        # Removing spacial characters
        y = []
        for i in text:
            if i.isalnum():
                y.append(i)
        # Removing Stop-words and Punctutation marks
        text = y[:]
        y.clear()
        for i in text:
            if i not in string.punctuation and i not in n:
                y.append(i)
        # Stemming
        text = y[:]
        y.clear()
        for i in text:
            y.append(ps.stem(i))

        return " ".join(y)

    transform_sms = transform_text(input_sms)





    # 2. Vectorize
    vector_input = tf.transform([transform_sms])



    # 3. Predict
    result = model.predict(vector_input)[0]



    # 4. Display
    if result == 1 :
        st.header("Spam")
    else:
        st.header('Not Spam')
