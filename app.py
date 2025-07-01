from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS
from utils.utils import decodeSound
from speechToText import speech2Text
import nltk

def download_nltk_corpora():
    try:
        nltk.data.find('tokenizers/punkt')
        nltk.data.find('taggers/averaged_perceptron_tagger')
        nltk.data.find('corpora/brown')
        nltk.data.find('corpora/wordnet')
        nltk.data.find('corpora/movie_reviews')
        nltk.data.find('corpora/stopwords')
        nltk.data.find('sentiment/vader_lexicon')
        nltk.data.find('corpora/omw-1.4')
    except LookupError:
        nltk.download('punkt')
        nltk.download('averaged_perceptron_tagger')
        nltk.download('brown')
        nltk.download('wordnet')
        nltk.download('movie_reviews')
        nltk.download('stopwords')
        nltk.download('vader_lexicon')
        nltk.download('omw-1.4')

download_nltk_corpora()

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def home():
    return render_template("index1.html")

@app.route("/predict", methods=["POST"])
def predictRoute():
    try:
        data = request.get_json()
        sound_data = data["sound"]
        decodeSound(sound_data, "audio123.wav")
        response = speech2Text("audio123.wav")
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
