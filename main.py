from flask import Flask, render_template, request
from youtube_transcript_api import YouTubeTranscriptApi
import google.generativeai as genai
from dotenv import load_dotenv
from urllib.parse import quote  # Import quote from urllib.parse
import os

def configure():
    load_dotenv()

app = Flask(__name__)
api_key = os.getenv('api_key')
genai.configure(api_key=api_key)

@app.route('/', methods=['GET', 'POST'])
def index():
    configure()
    if request.method == 'POST':
        video_url = request.form['video_url']
        video_id = video_url.split("v=")[1]

        # Define a list of preferred languages
        language_codes = ["en", "hi", "es", "fr"]

        for lang in language_codes:
            try:
                data = YouTubeTranscriptApi.get_transcript(video_id, languages=[lang])
                lst = []
                for i in range(len(data)):
                    lst.append(data[i]["text"])

                break  # Exit the loop if a valid transcript is found
            except Exception as e:
                print(f"No transcript found in {lang}. Error: {e}")
                continue  # Try the next language in the list
        else:
            return "No transcript found in any of the specified languages."

        text = str(lst)

        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content("Write a summary of the following text in about 200 words: " + text)
        summary = response.text

        return render_template('summary.html', summary=summary)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)