
import unittest

from change_log import *

class TestCommits(unittest.TestCase):

    def setUp(self):
        self.data = load_data('changes_python.log')
        self.NewCommitFile = CreateMatrix(self.data)

    def test_number_of_lines(self):
        self.assertEqual(5255, len(self.data))
        
    def test_number_of_deletions(self):
        self.assertEqual(767,return_no_of_change_types(self.NewCommitFile, 'D'))
        self.assertEqual(663,return_no_of_change_types(self.NewCommitFile, 'D', 'Thomas'))
        self.assertEqual(32,return_no_of_change_types(self.NewCommitFile, 'D', 'Vincent'))
        
    def test_number_of_reads(self):
        self.assertEqual(2,return_no_of_change_types(self.NewCommitFile, 'R'))
        self.assertEqual(0,return_no_of_change_types(self.NewCommitFile, 'R', 'Thomas'))
        self.assertEqual(1,return_no_of_change_types(self.NewCommitFile, 'R', 'Jimmy'))
        
    def test_number_of_add(self):
        self.assertEqual(1056,return_no_of_change_types(self.NewCommitFile, 'A'))
        self.assertEqual(87,return_no_of_change_types(self.NewCommitFile, 'A', 'Thomas'))
        self.assertEqual(690,return_no_of_change_types(self.NewCommitFile, 'A', 'Jimmy'))
        
    def test_number_of_mrg(self):
        self.assertEqual(1186,return_no_of_change_types(self.NewCommitFile, 'M'))
        self.assertEqual(609,return_no_of_change_types(self.NewCommitFile, 'M', 'Thomas'))
        self.assertEqual(401,return_no_of_change_types(self.NewCommitFile, 'M', 'Jimmy'))
 
    def test_number_of_commits(self):
        self.assertEqual(422, return_no_of_commits(self.NewCommitFile))
        self.assertEqual(26, return_no_of_commits(self.NewCommitFile, "Vincent"))
        self.assertEqual(191, return_no_of_commits(self.NewCommitFile, "Thomas"))
        self.assertEqual(152, return_no_of_commits(self.NewCommitFile, "Jimmy"))
        self.assertEqual(5, return_no_of_commits(self.NewCommitFile, "Alan"))
        
    def test_number_of_comments(self):
        self.assertEqual(3,return_comments(self.NewCommitFile,"r1540809"))
        self.assertEqual(5,return_comments(self.NewCommitFile,"r1539662"))
        

if __name__ == '__main__':
    unittest.main()
