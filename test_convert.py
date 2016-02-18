import unittest

from os import unlink

from convert_syllable_to_char_matches import convert_matches


class ConversionTest(unittest.TestCase):
    def test_convert_matches_to_raw(self):
        raw_matches_csv = "test_files/raw_matches.csv"
        convert_matches("test_files/clean_matches.csv",
                        ("test_files/raw1.txt", "test_files/raw2.txt"),
                        raw_matches_csv)
        with open(raw_matches_csv) as f:
            res = f.readlines()
        with open("test_files/raw_matches_ref.csv") as f:
            ref = f.readlines()
        self.assertSequenceEqual(ref, res)
        unlink(raw_matches_csv)


if __name__ == '__main__':
    unittest.main()
