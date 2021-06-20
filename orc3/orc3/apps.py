from django.apps import AppConfig
import pickle
import html
import pathlib
import os


class PredictorConfig(AppConfig):
    # create path to models
    path = os.path.join('../models/TrainedModel.p')

    # load models into separate variables
    # these will be accessible via this class
    with open(path, 'rb') as pickled:
        data = pickle.load(pickled)
    print(data)

    regressor = data['regressor']
    vectorizer = data['vectorizer']
