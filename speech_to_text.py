import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Path to the audio file
audio_file = "Y2meta.app-Daily-Conversations-_1-Learn-Hindi-through-English-_320-kbps_.wav"

# Open the audio file
with sr.AudioFile(audio_file) as source:
    # Listen for the data (load audio to memory)
    audio_data = recognizer.record(source)

    try:
        # Recognize the speech
        text = recognizer.recognize_google(audio_data)
        print("Text:", text)
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
