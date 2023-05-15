import unittest
import os
import sys
from pathlib import Path
import csv
FILE = Path(__file__).resolve()
test_dir = FILE.parents[0]
project_dir = FILE.parents[1]
sys.path.append(str(project_dir))
sys.path.append(str(test_dir))
os.chdir(test_dir)

# project modules
from basic_nlp.words_base import calc_edit_distance, pattern_matching


class TestWordsBase(unittest.TestCase):

    def setUp(self):
        self.long_text = "Crescent Bay was hidden under a white sea-mist. The big Bay bush-covered hills at the back were smothered basins and out again; and there was Round the corner of Crescent Bay, between the piled-up masses of broken"

    def test_givenAListOfWords_whenProvideAKeyword_thenCalculateModificationDistances(self):
        keyword = 'edward'
        expected_result = [2, 1, 6, 8]
        result = calc_edit_distance(keyword, ['eaaward', 'bdward', 'EDWARD', 'Isabella'])
        self.assertEqual(result, expected_result)

    def test_givenALongStringAndAKeyPattern_whenNoSupressRequired_thenReturnAllMatchingResults(self):
        pattern = r'Ba\w+'
        result = pattern_matching(pattern=pattern, full_str=self.long_text, surpress=False)
        expected_result = ['Bay', 'Bay', 'Bay']
        self.assertEqual(result, expected_result)

    def test_givenALongStringAndAKeyPattern_whenSupressRequired_thenReturnUniqueMatchingResults(self):
        pattern = r'Ba\w+'
        result = pattern_matching(pattern=pattern, full_str=self.long_text, surpress=True)
        expected_result = ['Bay']
        self.assertEqual(result, expected_result)
