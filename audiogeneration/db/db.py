from time import strftime
from pymongo import MongoClient
import numpy as np


class MongoDB:
    def __init__(self):
        self.__db = MongoClient(
            'mongodb+srv://bohdankulynych:admin@cluster0.pkkg7.mongodb.net/audiogenerationapp?retryWrites=true&w=majority')[
            "audiogenerationapp"]
        self.__model_params_table = self.__db["model_params"]
        self.__generated_songs_table = self.__db["generated_songs"]

    def get_model_params(self):
        required_model_params = ("idx2char", "char2idx")
        cursors = map(lambda param: self.__model_params_table.find({param: {"$exists": True}}), required_model_params)
        params = []
        for cursor in cursors:
            for data in cursor:
                for param in required_model_params:
                    params.append(data.get(param))
        params = [i for i in params if i is not None]
        return np.array(params[0]), params[1]

    def insert_generated_song(self, song):
        if not isinstance(song, str):
            raise TypeError("Song must be a string")
        return self.__generated_songs_table.insert_one({strftime('%m%d%Y%H%M%S'): song})
