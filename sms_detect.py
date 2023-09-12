import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()


def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

st.title("Email/SMS Spam Classifier")


# Checking user Enter message correctly or not.
def isInput_valid(check):
    check=check[12:]
    res=True
    for i in check:
        if(i not in " "):
            res=False
            break
    return res
# checking User only Enter puctuation or Valid message
def is_only_puctuation(check):
    check=check[12:]
    res=True
    for i in check:
        if(i not in  string.punctuation and i not in " "):
            res=False
            break
    return res


input_sms = st.text_area("Enter the message","Type Here...  ")
if st.button('Predict'):
    # Cheching You enter the message or not.
    check=input_sms.title()
    # Checking input is only spaces or something.
    if(isInput_valid(check)):
        st.header("You did not write anything:Please Type Again...")
    # checking input is only punctuation. or something
    elif is_only_puctuation(check):
        st.warning("Spam")
    else:
        # 1. preprocess the message (text)
        transformed_sms = transform_text(input_sms)
        # 2. vectorize the message
        vector_input = tfidf.transform([transformed_sms])
        # 3. predict the output of message wheather it is spam or ham.
        result = model.predict(vector_input)[0]
        # 4. Display the result.
        if result == 1:
            st.warning("Spam")
        else:
            st.success("Not Spam")
