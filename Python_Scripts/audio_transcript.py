import speech_recognition as sr

# Initialize the recognizer
r = sr.Recognizer()

# Open the audio file
with sr.AudioFile("anish.m4a") as source:
    # Collect audio data
    audio_data = r.record(source)

# Convert audio data to text
text = r.recognize_google(audio_data)

# Print the text
print(text)
