
import streamlit as st
import speech_recognition as sr
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init(driverName='espeak')

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Please say your symptoms...")
        st.write("Please say your symptoms...")
        audio = recognizer.listen(source)
        try:
            symptoms = recognizer.recognize_google(audio)
            speak("You said: " + symptoms)
            st.write("You said: " + symptoms)
            return symptoms
        except sr.UnknownValueError:
            speak("Sorry, I could not understand the audio.")
            st.write("Sorry, I could not understand the audio.")
        except sr.RequestError:
            speak("Could not request results; check your network connection.")
            st.write("Could not request results; check your network connection.")

def normalize_symptom(symptom):
    symptom = symptom.lower().replace(" ", "_")
    return symptom

st.title("Disease Prediction App")
st.write("Click the button below and speak your symptoms.")

if st.button("Start Voice Input"):
    symptoms = get_voice_input()
    if symptoms:
        user_symptoms = [normalize_symptom(s.strip()) for s in symptoms.split(',')]
        try:
            predicted_disease = given_predicted_value(user_symptoms)
            desc, pre, med, die, wrkout = helper(predicted_disease)

            st.write("=================predicted disease============")
            speak("predicted disease")
            st.write(predicted_disease)
            speak(predicted_disease)
            st.write("=================description==================")
            speak("description")
            st.write(desc)
            speak(desc)
            st.write("=================precautions==================")
            speak("precautions")
            for i, p_i in enumerate(pre, 1):
                st.write(f"{i}: {p_i}")
                speak(f"{i}: {p_i}")

            st.write("=================medications==================")
            speak("medications")
            for i, m_i in enumerate(med, 1):
                st.write(f"{i}: {m_i}")
                speak(f"{i}: {m_i}")

            st.write("=================workout==================")
            speak("workout")
            for i, w_i in enumerate(wrkout, 1):
                st.write(f"{i}: {w_i}")
                speak(f"{i}: {w_i}")

            st.write("=================diets==================")
            speak("diets")
            for i, d_i in enumerate(die, 1):
                st.write(f"{i}: {d_i}")
                speak(f"{i}: {d_i}")
        except KeyError as e:
            st.write(f"Error: {e} not found in the dataset.")
            speak(f"Error: {e} not found in the dataset.")
    else:
        st.write("No symptoms were provided.")
        speak("No symptoms were provided.")

