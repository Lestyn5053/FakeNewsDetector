import pickle

model_file = "final_model.sav"
with open(model_file, 'rb') as file:
    model = pickle.load(file)

test_article = "articles.csv"


def predict_real_fake():
    prediction = model.predict([test_article])
    return prediction[0]
