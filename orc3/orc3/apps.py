from django.apps import AppConfig
import pickle
import os


class PredictorConfig(AppConfig):

    path = os.path.join('../models/TrainedModel.p')

    with open(path, 'rb') as pickled:
        data = pickle.load(pickled)
    print(data)

    regressor = data['regressor']
    vectorizer = data['vectorizer']
