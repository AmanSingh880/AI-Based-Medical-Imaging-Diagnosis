import os
from tensorflow.keras.applications.imagenet_utils import preprocess_input
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
MODEL_PATH = 'model.h5'
model = load_model(MODEL_PATH)

def model_predict(img, model):
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)  # Add batch dimension
    x = preprocess_input(x)  # 'mode' argument removed
    preds = model.predict(x)
    return preds

print('Model loaded. Start serving...')
img_path = os.path.join('uploads', 'image.jpeg')

if os.path.isfile(img_path):
    img = image.load_img(img_path, target_size=(128, 128))
    preds = model_predict(img, model)
    result = preds[0, 0]
    print(f"Prediction Confidence: {result}")
    if result > 0.5:
        print("Prediction: PNEUMONIA")
    else:
        print("Prediction: NORMAL")
else:
    print(f"Image not found at {img_path}")
