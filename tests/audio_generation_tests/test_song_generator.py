import os

from audiogeneration.track.generate_track import GenerateTrack
import unittest
import requests
import os

class TestAudioGenerator(unittest.TestCase):

    def setUp(self):
        self.__invalid_track_name = "sample12242021134301.mid"
        self.__fail = GenerateTrack(self.__invalid_track_name)
        self.__valid_track_name = "samplemp3.mid"
        self.__valid = GenerateTrack(self.__valid_track_name)

    def test_invalid_audio_format(self):
        with self.assertRaises(TypeError) as em:
            self.__fail.play_song()
            self.assertEqual("It is not a valid midi file!", str(em.exception))

    def test_valid_audio_format(self):
        try:
            self.__valid.play_song()
        except Exception as e:
            self.fail(f"function raised {e} unexpectedly!")

    def test_web_audio_generator(self):
        url = f'http://audiogenerationapp.herokuapp.com/generate?filename={self.__invalid_track_name}'
        r = requests.post(url)
        assert r.status_code == 500
