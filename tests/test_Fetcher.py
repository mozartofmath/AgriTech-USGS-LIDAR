import unittest
import sys, os
sys.path.append(os.path.abspath(os.path.join('..')))
from scripts.Fetcher import Fetcher

class TestFetcher(unittest.TestCase):
    def test_set_boundary(self):
        """
        Test that it sets the boundary correctly
        """
        fetcher = Fetcher()
        fetcher.set_boundary(1,2,3,4)
        result = fetcher.pipeline['pipeline'][0]['bounds']
        self.assertEqual(result, f"([1, 2], [3, 4])")

    def test_set_region(self):
        """
        Test that it sets the region correctly
        """
        fetcher = Fetcher()
        fetcher.set_region("NY_FullState")
        result = fetcher.pipeline['pipeline'][0]['filename'].split('/')[-2]
        self.assertEqual(result, "NY_FullState")

    def test_set_outfile_laz(self):
        """
        Test that it sets the output filenames correctly
        """
        fetcher = Fetcher()
        fetcher.set_out_filename("new_york")
        laz = fetcher.pipeline['pipeline'][4]['filename']
        self.assertEqual(laz, "new_york.laz")

    def test_set_outfile_tif(self):
        """
        Test that it sets the output filenames correctly
        """
        fetcher = Fetcher()
        fetcher.set_out_filename("new_york")
        tif = fetcher.pipeline['pipeline'][5]['filename']
        self.assertEqual(tif, "new_york.tif")



if __name__ == '__main__':
    unittest.main()
