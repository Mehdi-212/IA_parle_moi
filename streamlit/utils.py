import os
import streamlit as st
import azure.cognitiveservices.speech as speechsdk
import openai

#clé d'API openai
openai.api_key ="API OPENAI"

#configuration de reconnaissance vocale
speech_config = speechsdk.SpeechConfig(
    speech_recognition_language="fr-FR",
    subscription="AZURE KEY",
    region="francecentral"
)

#paramètres de synthèse vocale avec les memes que la reconnaissance vocale.
speech_synthesizer = speechsdk.SpeechSynthesizer(
    speech_config= speechsdk.SpeechConfig(
        speech_recognition_language="fr-FR",
        subscription="AZURE KEY",
        region="francecentral"
    )
)

#transcrire en texte ce qui est enregistré à partir du microphone de l'utilisateur.
def recognize_from_microphone():
    # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_config.speech_recognition_language="fr-FR"
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    #Ajoute des mots non detecter
    List_mots = speechsdk.PhraseListGrammar.from_recognizer(speech_recognizer)
    List_mots.addPhrase("Sophana")
    List_mots.addPhrase("C#")
    List_mots.addPhrase("Scikit-learn")
    List_mots.addPhrase("scipy")
    List_mots.addPhrase("R")
    List_mots.addPhrase("serverless")
    List_mots.addPhrase("PyTorch")
    List_mots.addPhrase("Tensorflow")
    List_mots.addPhrase("seaborn")
    List_mots.addPhrase("simplonien")
    List_mots.addPhrase("simplonline")
    List_mots.addPhrase("syrine")
    
    #Traduit ce que tu a dis 
    print("Parlez dans votre microphone.")
    speech_recognition_result = speech_recognizer.recognize_once_async().get()

    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(speech_recognition_result.text))
        
        return speech_recognition_result.text
    
    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(speech_recognition_result.no_match_details))
    elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_recognition_result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
            print("Did you set the speech resource key and region values?")
    return ""

#utilise l'API OpenAI pour générer une réponse à partir du prompt
def generate_prompt(prompt):
    
    response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.7,
            max_tokens = 1700,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )
    return response.choices[0].text.strip()