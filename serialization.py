import pickle
import json

obj = {1: 'one', 2: 'two', 3: 'three'}


def pickle_example():
    with open('data.pickle', 'wb') as file:
        pickle.dump(obj, file)


def json_example():
    with open('data.json', 'w') as file:
        json.dump(obj, file)

    with open('data.json', 'r') as file:
        data = {int(k): v for k, v in json.load(file).items()}
        print(data)

json_example()
