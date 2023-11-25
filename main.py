from flask import Flask, request, jsonify, render_template
from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

app = Flask(__name__)
model = load_model('./origami_shape_classifier.h5')

def predict_origami_model(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    predictions = model.predict(img_array)
    return predictions

@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    img = Image.open(file)
    img.save('temp.jpg')  # Save the image temporarily
    predictions = predict_origami_model('temp.jpg')

    # You need to define how to interpret the predictions based on your model and data
    # For simplicity, let's assume you have a list of origami model names
    origami_models = ['Model A', 'Model B', 'Model C']
    predicted_model = origami_models[np.argmax(predictions)]

    return render_template('index2.html', predicted_model=predicted_model)

if __name__ == '__main__':
    app.run(debug=True)
