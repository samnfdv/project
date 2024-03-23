import pickle


def create_model():
    with open('/Users/semennefedov/PycharmProjects/pythonProject7/pickle_mode_pycharm.pkl', 'rb') as file:
        pickle_model = pickle.load(file, )
    return pickle_model


def prediction(userdata, user_id):
    pickle_model = create_model()
    print(userdata[user_id])
    u = [[int(userdata[user_id][f]) for f in userdata[user_id]]]
    p = pickle_model.predict(u)
    return p



