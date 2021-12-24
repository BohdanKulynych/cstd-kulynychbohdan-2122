from keras.models import load_model
from musicgeneration.midi2abc import convert
from .configs import UPLOAD_DIR
from audiogeneration.db.db import MongoDB
import os
from musicgeneration.songs import extract_song_snippet, generate_text
import re


class GenerateTrack:
    def __init__(self, midi_filename):
        self.__midi_filename = midi_filename
        self.__initial_abc_track_duration = 0
        self.__track_name = f"{''.join(self.__midi_filename.split('.')[:-1])}"
        self.__db = MongoDB()

    @property
    def __path_to_midi(self):
        return os.path.join(UPLOAD_DIR, self.__midi_filename)

    def __midi2abc_track(self):
        try:
            abc_track = convert(self.__path_to_midi)
            self.__initial_abc_track_duration = len(abc_track)
            return abc_track
        except:
            raise TypeError(
                "We run into problems while processed your file.Please make sure you're using valid .mid file")

    def __generated_abc_notation(self):
        idx2char, char2idx = self.__db.get_model_params()
        model = load_model(f"{os.getcwd()}/audiogeneration/models/mgen.h5")
        return generate_text(model, self.__midi2abc_track(), char2idx, idx2char)

    def __choose_closest_song(self, generated_songs):
        if len(generated_songs) > 0:
            songs_durations = [len(song) for song in generated_songs]
            closest_duration = min(range(len(songs_durations)),
                                   key=lambda i: abs(
                                       songs_durations[i] - self.__initial_abc_track_duration))

            return generated_songs[closest_duration]

    def __insert_to_db(self, song):
        return self.__db.insert_generated_song(song)


    def __process_song(self):
        generated_songs = [*filter(lambda song: re.match("X:[0-9]+\nT:.+\nZ:.+\nM:.+\nL:.+\nK:.+\n.+", song),
                                   extract_song_snippet(self.__generated_abc_notation()))]
        closest_song = self.__choose_closest_song(generated_songs)
        self.__insert_to_db(closest_song)

        track_2abcfile = self.__track_name + ".abc"
        abcfile_path = f"{UPLOAD_DIR}/{track_2abcfile}"
        with open(abcfile_path, "w") as f:
            f.write(closest_song)
            f.close()
        return abcfile_path

    def __abc2wav(self, abc_song):
        path_to_tool = f"{os.getcwd()}/audiogeneration/bin/abc2wav.sh"
        cmd = f"bash {path_to_tool} {abc_song}"
        os.system(cmd)

    def play_song(self):
        song = self.__process_song()
        self.__abc2wav(song)
        track_name = self.__track_name + ".wav"
        return track_name
