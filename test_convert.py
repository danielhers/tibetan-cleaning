import unittest

from convert_matches_to_raw import convert_matches


class ConversionTest(unittest.TestCase):
    def test_convert_matches_to_raw(self):
        convert_matches("test_files/clean_matches.csv",
                        ("test_files/raw1.txt", "test_files/raw2.txt"),
                        "test_files/raw_matches.csv")
        with open("test_files/raw_matches.csv") as f:
            res = f.readlines()
        with open("test_files/raw_matches_ref.csv") as f:
            ref = f.readlines()
        self.assertSequenceEqual(ref, res)


if __name__ == '__main__':
    unittest.main()
