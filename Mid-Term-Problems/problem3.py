# Import gTTS and os
from gtts import gTTS
import os
import time

# Ask the username
username = input('Enter your name: ')

# Define the text to convert to speech
eng_msg = f"Happy birthday! {username} I hope your special day is filled with joy, laughter, and wonderful memories!"
urdu_msg = f"جنم دن مبارک ہو، {username}! آپکو یہ دن خوشیوں اور محبت بھرا گزرے۔ ہمیشہ خوش رہیں اور ہر خوشی آپکے قدموں میں ہو۔"

# Create a gTTS object and specify the language and slowdown rate
urdu_speech = gTTS(text=urdu_msg, lang='ur', slow=False)
eng_speech = gTTS(text=eng_msg, lang='en', slow=False)

# Save the urdu speech to a file
urdu_file_name = "urdu_wish.mp3"
urdu_speech.save(urdu_file_name)

# Save the eng speech to a file
eng_file_name = "eng_wish.mp3"
eng_speech.save(eng_file_name)

# Play the generated audio file
os.system(f"start {urdu_file_name}")
time.sleep(10)
os.system(f"start {eng_file_name}")
