from flask import Flask, request, jsonify, render_template
import whisper

app = Flask(__name__)
model = whisper.load_model("base")  # Load the Whisper model

@app.route('/')  # Root route
def index():
    return render_template('index.html')  # Serve the HTML file

@app.route('/transcribe', methods=['POST'])  # Transcription endpoint
def transcribe_audio():
    try:
        file = request.files['file']
        if not file:
            return jsonify({"error": "No file provided"}), 400

        # Save the file temporarily
        file.save("temp_audio.wav")

        # Transcribe the audio file using Whisper
        result = model.transcribe("temp_audio.wav")

        # Return the transcription result
        return jsonify({"text": result["text"]})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)  # Run the app in debug mode
