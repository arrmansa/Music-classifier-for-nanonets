import os
import requests, json
from requests.auth import HTTPBasicAuth
import wave
import numpy as np
import matplotlib.pyplot as plt
import pylab
import gc
def classify_single_image(filename):
    path = str(filename)
    data = {'file':open(path, "rb"), \
    'modelId':("", "<PUT MODEL ID HERE>")}  # modelid
    url = 'https://app.nanonets.com/api/v2/ImageCategorization/LabelFile/'
    r = requests.post(url, files=data, auth=HTTPBasicAuth('xTPbsH2qY28K6ZFs43vwXlEgzL4BhB_3LrthTLNhl4e', ''))
    data = json.loads(r.content)
    dictionary = {}
    genres_number = len(data['result'][0]['prediction'])
    for i in range(genres_number):
        genre = str(data['result'][0]['prediction'][i]['label'])
        probability = float(data['result'][0]['prediction'][i]['probability'])
        dictionary[genre] = probability
    return dictionary
def classify_images(wavname):
    filestart = wavname[:-4]
    netdictionary = {}
    for filename in os.listdir('.'):
        if filename.startswith(filestart):
            d2 = classify_single_image(filename)
            netdictionary = {k : netdictionary.get(k, 0) + d2.get(k,0) for k in set(netdictionary.keys()) | set(d2.keys())}
    return netdictionary
def classify_songs():
    filegenre = {}
    for filename in os.listdir("songs/"):
        if filename.endswith(".wav"):
            filegenre[filename] = classify_images(filename)
    return filegenre
with open('file.txt', 'w') as file:
    file.write(str(classify_songs()))
#print(classify_songs())
