from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image


def predict(images_list):
    model = load_model('model.h5')
    y_pred = []
    for i in images_list:
        img = i.convert('RGB')
        img = img.resize((200, 200))
        arr = np.asarray(img, dtype='uint8')
        k = np.array([[[0.2989, 0.587, 0.114]]])
        sums = np.round(np.sum(arr*k, axis=2)).astype(np.uint8)
        sums = sums.reshape(1, 200, 200)
        y_pred.append(model.predict(sums)[0][0])
    return y_pred