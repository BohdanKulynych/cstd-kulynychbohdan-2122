from audiogeneration.db.db import MongoDB
import unittest
import numpy as np


class TestDBClient(unittest.TestCase):

    def setUp(self):
        self.__db_driver = MongoDB()
        self.__generated_song = {"12242021134317": """X:130
                                T:Golder
                                Z: id:dc-reel-291
                                M:C
                                L:1/8
                                K:G Major
                                F|AGEG BGG2|BABc AGFG|ABAG FDCF|GFG ABcB|!
                                cG Ace|AGA cBc|B2G BAG F2d|!
                                [1 fed faf bag|fed fdB|cBA BAG|FDA cAG|F2E E2:|!
                                B|BAB dBB|dcB BAG|BGB Major
                                dB|Ac ABc|def ged|efe dBA|dAG FGA|!
                                B2c G2B|d2e fdB|A3 A2f|gfe dfe|ded cde|!
                                f3 efg|fdf ecA|Bge B2f|edB AFA:|!"""}

    def test_model_params(self):
        idx2char, char2idx = self.__db_driver.get_model_params()
        self.assertIsInstance(idx2char, np.ndarray)
        self.assertIsInstance(char2idx, dict)

    def test_song_inserts(self):
        self.assertRaises(TypeError, self.__db_driver.insert_generated_song, {"song": self.__generated_song})