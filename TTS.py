# Import the necessary modules
from gtts import gTTS
import pygame

# Define a function that takes text and converts it to speech
def text_to_speech(text, lang, slow, filename):
    # Create a gTTS object with the given text, language, speed, and TLD (top-level domain)
    # The TLD "co.uk" will use the British version of the chosen language
    speech = gTTS(text = text, lang = lang, slow = slow, tld="co.uk")
    
    # Save the speech audio into a file
    speech.save(filename)

# Define a function to play the speech from the file
def play_speech(filename):
    # Initialize the pygame mixer
    pygame.mixer.init()
    
    # Load the speech file
    pygame.mixer.music.load(filename)
    
    # Play the speech
    pygame.mixer.music.play()
    
    # Check if the music is still playing
    while pygame.mixer.music.get_busy():  
        # Wait for a while before checking again
        pygame.time.Clock().tick(10)  

# Define the sentence to be converted to speech
sentence = "___________" # Enter text here

# Convert the sentence to speech and save it as an mp3 file
text_to_speech(sentence, 'en', False , "speech.mp3")

# Play the speech from the mp3 file
play_speech("speech.mp3")
