# Python Text-to-Speech Application

This is a simple Python application that uses the Google Text-to-Speech (gTTS) library to convert text to speech. The speech is saved to an mp3 file and then played using the pygame library.

## Dependencies

This application requires the following Python libraries:

- gTTS: For converting text to speech.
- pygame: For playing the speech.

You can install these dependencies using pip:

```bash
pip install gTTS pygame
```

## Usage

1. Import the necessary modules:

```python
from gtts import gTTS
import pygame
```

2. Define a function that takes text and converts it to speech:

```python
def text_to_speech(text, lang, slow, filename):
    speech = gTTS(text = text, lang = lang, slow = slow, tld="co.uk")
    speech.save(filename)
```

This function creates a gTTS object with the given text, language, speed, and TLD (top-level domain). The TLD "co.uk" is used to get the British accent for the speech. The speech audio is then saved into a file.

3. Define a function to play the speech from the file:

```python
def play_speech(filename):
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():  
        pygame.time.Clock().tick(10)  
```

This function initializes the pygame mixer, loads the speech file, and plays the speech. It uses a while loop to prevent the program from ending before the speech has finished playing.

4. Define the sentence to be converted to speech:

```python
sentence = "___________" # Enter text here
```

Replace `___________` with the text you want to convert to speech.

5. Convert the sentence to speech and save it as an mp3 file:

```python
text_to_speech(sentence, 'en', False , "speech.mp3")
```

6. Play the speech from the mp3 file:

```python
play_speech("speech.mp3")
```

Run the program and listen to the converted text!

Please note that this is a simple application and may not fulfill all your requirements for a text-to-speech application. You may need to modify the code to suit your needs.