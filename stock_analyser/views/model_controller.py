from stock_analyser.models.lstm import lstm_actual_prediction
from stock_analyser.models.all_models_test import simple_test, predict_from_model


def simple_api(request, id):
    return simple_test(id)

def predictor(request, id):
    return predict_from_model(id)

def lstm_model(request, id):
    return lstm_actual_prediction(id)
