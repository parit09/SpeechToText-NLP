from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS
from utils.utils import decodeSound
from speechToText import speech2Text
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('brown')
nltk.download('wordnet')
nltk.download('movie_reviews')
nltk.download('stopwords')
nltk.download('vader_lexicon')
nltk.download('omw-1.4')
from textblob import download_corpora
download_corpora()

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
