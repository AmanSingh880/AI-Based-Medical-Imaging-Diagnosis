import os
import sqlite3
from tensorflow.keras.applications.imagenet_utils import preprocess_input
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from datetime import datetime
import numpy as np
MODEL_PATH = 'model.h5'
model = load_model(MODEL_PATH)

def data_trans(result):
    def print_name(filename="data.txt"):
        try:
            with open(filename, "r") as file:
                lines = file.readlines()
                for line in lines:
                    if line.startswith("Name"):
                        return line.strip()[6:]
        except Exception as e:
            print(f"Error: {e}")
            return ""
    def print_age(filename="data.txt"):
        try:
            with open(filename, "r") as file:
                lines = file.readlines()
                for line in lines:
                    if line.startswith("Age"):
                        return line.strip()[5:]
        except Exception as e:
            print(f"Error: {e}")
            return ""
    def select_latest_id():
        mydb=sqlite3.connect('diagonis.db')
        mycursor=mydb.cursor()
        mycursor.execute("SELECT MAX(ID) FROM HISTORY")
        latest_id=mycursor.fetchone()
        mydb.commit()
        return latest_id[0]
    def insert(id,name,age,P_Pos,result,date):
        mydb=sqlite3.connect('diagonis.db')
        mycursor=mydb.cursor()
        mycursor.execute("INSERT INTO History(ID,NAME,AGE,P_POS, RESULT ,DATE) VALUES(?,?,?,?,?,?) ",(id,name,age,P_Pos,result,date))
        mydb.commit()
    def get_current_date():
        return datetime.now().strftime("%Y-%m-%d")
    id=select_latest_id()
    if(id==""):
        return False
    id=int(id)
    id+=1
    name=print_name()
    age=print_age()
    if(name==""):
        return False
    if result > 0.5:
        pe="PNEUMONIA"
    else:
        pe="NORMAL"
    result*=100
    datee=get_current_date()
    insert(id,name,age,result,pe,datee)
    os.system("digresult.py")


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
    data_trans(result)
    
else:
    print(f"Image not found at {img_path}")
