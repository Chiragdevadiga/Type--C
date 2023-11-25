from flask import Flask, render_template, request, jsonify
from PIL import Image
import numpy as np
import tensorflow as tf

app = Flask(__name__)

# Load your pre-trained machine learning model
# Replace this with the actual loading code for your model
model = tf.keras.models.load_model('./object_classifier.h5')

def preprocess_image(image_path):
    # Replace this with the actual preprocessing code for your model
    img = Image.open(image_path)
    img = img.resize((224, 224))  # Adjust size according to your model's input size
    img_array = np.array(img)
    img_array = img_array / 255.0  # Normalize pixel values
    return np.expand_dims(img_array, axis=0)

@app.route('/')
def index():
    return render_template('scanner.html')

@app.route('/compare', methods=['POST'])
def compare_images():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    # Save the uploaded file
    file_path = 'temp_image.jpg'
    file.save(file_path)

    # Preprocess the captured image
    captured_image = preprocess_image(file_path)

    # Perform inference using your pre-trained model
    prediction = model.predict(captured_image)

    # You need to implement the logic to determine if the images match
    # This is just a placeholder; modify it based on your model's output
    match_threshold = 0.5
    if prediction[0][0] > match_threshold:
        result = {'message': 'The images are matched!'}
    else:
        result = {'message': 'The images do not match.'}

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
