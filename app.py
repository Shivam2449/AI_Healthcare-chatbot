import streamlit as st
import nltk
from transformers import pipeline
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


chatbot =pipeline("text-generation",model="distilgpt2")

def healtcare_chatbot(user_input):
   if "Symptom" in user_input:
        return "Please consult Doctor for accurate advice."
   elif"Appointment" in user_input:
        return"Would you like to schedule an Appointment with the Docter?"
   elif "Medication" in user_input:
         return"It's important to take prescribed Medicine regulary. If you have any conserns,consult your doctor."  
   else:
     response =chatbot(user_input,max_length=500,num_return_sequences=1)               
     return response[0]['generated_text']

def main():
    st.title("Healtcare Assistance Chatbot")
    user_input = st.text_input("How can I assist you today?")
    if st.button("submit"):
        if user_input:
          st.write("User :",user_input) 
          with st.spinner("Prossesing your query,Please wait ...."):
               response= healtcare_chatbot(user_input)
          st.write("Healthcare Assistance :",response) 
          print(response)
        else:
            st.write("Please enter a message to get a response")

               

main()   
