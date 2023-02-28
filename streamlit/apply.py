# import time
# import streamlit as st
# import pandas as pd
# from utils import recognize_from_microphone, generate_prompt
# from PIL import Image

# image = Image.open("C:/Users/utilisateur/Pictures/openai.png")
# st.image(image, width=2*300)

# # Ajoute un titre à la page
# st.title("Cliquez sur le Bouton est parlez")

# # Initialise la variable pour stocker l'état de la synthèse vocale
# is_running = False

# if st.button("Cliquez ici pour parlez"):
#     is_running = True
#     while True:
#         text = recognize_from_microphone()
#         if not text:
#             print(text)
#             continue
#         user = st.empty()
#         user.write(text)
#         for i in range (len(text)):
#             #afficher progressivement une chaîne de caractères lettre par lettre dans l'interface utilisateur
#             user.write(text[:i+1])

#         reponse_bot = generate_prompt(text)
        
#         print(reponse_bot)
#         bot = st.empty()
#         for i in range (len(reponse_bot)):
#             bot.write(reponse_bot[:i+1])
            
#             #fait une pause de 0.03 seconde dans l'exécution du programme.
#             time.sleep(0.03)
#             if not is_running:
#                 break
            
# # Arret de la sythese vocale
# if st.button("Arrêter la synthèse vocale"):
#     is_running = True

import time
import streamlit as st
import pandas as pd
from utils import recognize_from_microphone, generate_prompt
from PIL import Image

image = Image.open("C:/Users/utilisateur/Pictures/openai.png")
st.image(image, width=2*300)

# Ajoute un titre à la page
st.title("Conversation avec l'intelligence artificielle")

# Initialise la variable pour stocker l'état de la synthèse vocale
is_running = False

if st.button("Cliquez ici pour parler"):
    # Créer un bouton dans la barre latérale pour arrêter la synthèse vocale
    stop_button = st.button("Arrêter la synthèse vocale")
    is_running = True
    while True:
        text = recognize_from_microphone()
        if not text:
            print(text)
            continue
        user = st.empty()
        user.write(text)
        for i in range (len(text)):
            #afficher progressivement une chaîne de caractères lettre par lettre dans l'interface utilisateur
            user.write(text[:i+1])

        reponse_bot = generate_prompt(text)
        
        print(reponse_bot)
        
        bot = st.empty()
        for i in range (len(reponse_bot)):
            bot.write(reponse_bot[:i+1])
            
            #pour entendre la voix du bot
            # speech_voc =  recognize_from_microphone()
            # speech_voc.speak_text_async(reponse_bot).get()
            
            #fait une pause de 0.03 seconde dans l'exécution du programme.
            time.sleep(0.03)
            if not is_running:
                break
            
        if stop_button:
            is_running = False
            break
