from flask import Flask, request, jsonify
import numpy as np
import librosa
import tensorflow as tf
import os

# Initialize Flask app
app = Flask(__name__)

# Load trained model
MODEL_PATH = "best_model.h5"
model = tf.keras.models.load_model(MODEL_PATH)

# Audio preprocessing settings
SR = 16000
N_MFCC = 40

def extract_features(file_path):
    y, sr = librosa.load(file_path, sr=SR)
    y, _ = librosa.effects.trim(y, top_db=25)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=N_MFCC)
    mfcc_scaled = np.mean(mfcc.T, axis=0)
    return mfcc_scaled

@app.route('/')
def home():
    return jsonify({"message": "Cough Analyzer API is running ✅"})

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    file_path = os.path.join("temp.wav")
    file.save(file_path)

    try:
        features = extract_features(file_path)
        X = np.expand_dims(features, axis=0)
        preds = model.predict(X)
        class_id = int(np.argmax(preds))
        confidence = float(np.max(preds))

        # Example class names (update to match your folders)
        classes = ['dry_cough', 'other', 'wet_cough']
        predicted_label = classes[class_id] if class_id < len(classes) else "Unknown"

        result = {
            "predicted_class": predicted_label,
            "confidence": round(confidence, 3)
        }

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)

if __name__ == "__main__":
    app.run(debug=True)
