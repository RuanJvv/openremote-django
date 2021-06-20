from django.apps import AppConfig
from django.conf import settings
import pickle
import os


class ModelConfig(AppConfig):

    # path to model
    path = os.path.join('./models/TrainedModel.p')

    # load model into value, accessible via class
    with open(path, 'rb') as pickled:
        data = pickle.load(pickled)
    print(data)

    regressor = data['regressor']
    vectorizer = data['vectorizer']
