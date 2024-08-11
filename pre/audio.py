import csv
from gtts import gTTS
import os

# Read words from CSV
with open('words.csv', 'r') as file:
    reader = csv.reader(file)
    words = [row[0] for row in reader]
    
if not os.path.exists("audio"):
    os.makedirs("audio")

# Generate audio files
for word in words:
    tts = gTTS(text=word, lang='en')
    tts.save(f"audio/{word}.mp3")