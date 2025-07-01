import speech_recognition as sr
from textblob import TextBlob

def speech2Text(file_path):
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(file_path) as source:
            audio = recognizer.record(source)

        text = recognizer.recognize_google(audio)

        # NLP Analysis using TextBlob
        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity
        noun_phrases = list(blob.noun_phrases)

        return {
            "transcription": text,
            "nlp": {
                "sentiment": sentiment,
                "subjectivity": subjectivity,
                "noun_phrases": noun_phrases
            }
        }

    except sr.UnknownValueError:
        return {"error": "Could not understand audio"}
    except sr.RequestError as e:
        return {"error": f"Google API error: {e}"}
