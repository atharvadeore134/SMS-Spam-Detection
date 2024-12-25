import streamlit as st 
import pickle

# Let's load the saved vectorizer and naive model 
tfidf = pickle.load(open('vectorizer.pkl', 'rb')) 
model = pickle.load(open('model.pkl', 'rb'))

# Saving Streamlit code

st.title("Email Spam Classifier")

input_sms = st.text_area("Enter message")

if st.button('Predict'):
    # Preprocess
    transformed_sms = transform.text(input_sms)

    # Vectorize
    vector_input = tfidf.transform([transformed_sms])

    # Predict
    result = model.predict(vector_input)[0]

    # Display
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")
