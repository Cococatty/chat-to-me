import unittest
import os
import sys
from pathlib import Path
FILE = Path(__file__).resolve()
test_dir = FILE.parents[0]
project_dir = FILE.parents[1]
sys.path.append(str(project_dir))
sys.path.append(str(test_dir))
os.chdir(test_dir)

# project modules
from basic_nlp.words_base import calc_edit_distance


class TestWordsBase(unittest.TestCase):

    def test_givenAListOfWords_whenProvideAKeyword_thenCalculateModificationDistances(self):
        keyword = 'edward'
        expected_result = [2, 1, 6, 8]
        result = calc_edit_distance(keyword, ['eaaward', 'bdward', 'EDWARD', 'Isabella'])
        self.assertEqual(result, expected_result)
