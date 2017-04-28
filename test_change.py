
import unittest

from change_log import *

class TestCommits(unittest.TestCase):

    def setUp(self):
        self.data = load_data('changes_python.log')
        self.NewCommitFile = CreateMatrix(self.data)

    def test_number_of_lines(self):
        self.assertEqual(5255, len(self.data))
        
    def test_number_of_deletions(self):
        self.assertEqual(743,return_no_of_change_types(self.NewCommitFile, 'D'))
        self.assertEqual(646,return_no_of_change_types(self.NewCommitFile, 'D', 'Thomas'))
        self.assertEqual(31,return_no_of_change_types(self.NewCommitFile, 'D', 'Vincent'))
        
    def test_number_of_commits(self):
        self.assertEqual(422, return_no_of_commits(self.NewCommitFile))
        self.assertEqual(26, return_no_of_commits(self.NewCommitFile, "Vincent"))
        self.assertEqual(190, return_no_of_commits(self.NewCommitFile, "Thomas"))
        self.assertEqual(152, return_no_of_commits(self.NewCommitFile, "Jimmy"))
        self.assertEqual(5, return_no_of_commits(self.NewCommitFile, "Alan"))
        

if __name__ == '__main__':
    unittest.main()
