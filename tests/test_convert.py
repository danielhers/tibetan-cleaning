import unittest
from os import unlink

import clean_and_map
import convert_clean_to_raw_matches
import convert_syllable_to_char_matches


class ConversionTest(unittest.TestCase):
    def test_clean_and_map(self):
        for i in (1, 2):
            clean_file = "test_files/clean%d.txt" % i
            map_file = "test_files/map%d.txt" % i
            clean_and_map.clean_and_map(
                "test_files/raw%d.txt" % i,
                clean_file,
                map_file)
            with open(clean_file) as f:
                res_clean = f.readlines()
            with open("test_files/clean%d_ref.txt" % i) as f:
                ref_clean = f.readlines()
            self.assertSequenceEqual(ref_clean, res_clean)
            unlink(clean_file)
            with open(map_file) as f:
                res_map = f.readlines()
            with open("test_files/map%d_ref.txt" % i) as f:
                ref_map = f.readlines()
            for x in ref_map:
                self.assertIn(x, res_map)
            unlink(map_file)

    def test_convert_syllable_to_char_matches(self):
        raw_matches_csv = "test_files/char_matches.csv"
        convert_syllable_to_char_matches.convert_matches(
            "test_files/syllable_matches.csv",
            ("test_files/raw1.txt", "test_files/raw2.txt"),
            raw_matches_csv)
        with open(raw_matches_csv) as f:
            res = f.readlines()
        with open("test_files/char_matches_ref.csv") as f:
            ref = f.readlines()
        self.assertSequenceEqual(ref, res)
        unlink(raw_matches_csv)

    def test_convert_clean_to_raw_matches(self):
        raw_matches_csv = "test_files/raw_matches.csv"
        convert_clean_to_raw_matches.convert_matches(
            "test_files/clean_matches.csv",
            ("test_files/map1_ref.txt", "test_files/map1_ref.txt"),
            raw_matches_csv)
        with open(raw_matches_csv) as f:
            res = f.readlines()
        with open("test_files/char_matches_ref.csv") as f:
            ref = f.readlines()
        self.assertSequenceEqual(ref, res)
        unlink(raw_matches_csv)


if __name__ == '__main__':
    unittest.main()
