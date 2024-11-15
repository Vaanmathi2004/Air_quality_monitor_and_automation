import os
import urllib.request
import http
import pandas as pd
import re
from time import sleep
from datetime import datetime
import numpy as np
import pickle

base = "http://192.168.137.175/"

def transfer(my_url):   # Function to send and receive data
    try:
        n = urllib.request.urlopen(base + my_url).read()
        n = n.decode("utf-8")
        return n
    except http.client.HTTPException as e:
        return e

# Load the KNN model
model_path = 'knn_model.sav'  # Path to the KNN model file
with open(model_path, 'rb') as model_file:
    knn_model = pickle.load(model_file)


data_list = []


ct = 0
while True:
    res = transfer(str(ct))
    response = str(res)
    print(response)
    
    # Split the received data
    values = response.split('-')
    if len(values) == 5:
        v1, v2, v3, v4,v5 = values
        # Prepare the data for KNN prediction
        reports = np.array([[float(v1), float(v2), float(v3)]])
        
        # Predict using the KNN model
        predicted_class = knn_model.predict(reports)[0]
        
        # Send prediction to ThingSpeak
        print(predicted_class)
        if predicted_class == "ABNORMAL":
            ct=1
            dr = "AIR_QUALITY_ABNORMAL"
            print("AIR QUALITY ABNORMAL")
        else:
            ct=0
            dr = "AIR_QUALITY_NORMAL"
            print("AIR QUALITY NORMAL")
        
        conn = urllib.request.urlopen(
            "https://api.thingspeak.com/update?api_key=QIXHGRZ00NB0BGZU&field1=" + str(v1) +
            "&field2=" + str(v2) + "&field3=" + str(v3) + "&field4=" + str(dr)
        )
        response = conn.read()
        print("HTTP status code=%s" % (conn.getcode()))
        print("")
    
    sleep(1)

