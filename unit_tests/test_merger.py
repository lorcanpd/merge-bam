
import unittest
from unittest.mock import patch, MagicMock
from merge_bam.merger import Merger

# TODO revisit the tests later. Maybe need to construct a pair of dummy BAM
#  files to test the merge function.

class TestMergerInitialization(unittest.TestCase):
    def test_initialization_with_valid_parameters(self):
        bam_files = [MagicMock(), MagicMock()]
        merger = Merger(bam_files, "output.bam")
        self.assertEqual(merger.num_files, 2)

    def test_initialization_with_invalid_parameters(self):
        with self.assertRaises(Exception):
            Merger([], "output.bam")

class TestMergerMerge(unittest.TestCase):
    @patch('pysam.AlignmentFile')
    def test_merge(self, mock_alignment_file):
        bam_files = [MagicMock(filename='file1.bam'), MagicMock(filename='file2.bam')]
        merger = Merger(bam_files, "output.bam")
        merger.merge()
        # Check if AlignmentFile is called with output file and new_header
        mock_alignment_file.assert_called_with("output.bam", "wb", header=unittest.mock.ANY)
        # Ensure reads from both files are processed
        self.assertEqual(mock_alignment_file.call_count, 3)  # Including the output file

class TestMergerSortAndIndex(unittest.TestCase):
    @patch('pysam.sort')
    @patch('pysam.index')
    def test_sort_and_index(self, mock_index, mock_sort):
        bam_files = [MagicMock(filename='file1.bam'), MagicMock(filename='file2.bam')]
        merger = Merger(bam_files, "output.bam")
        merger.merge()
        merger.sort()
        merger.index()
        mock_sort.assert_called_once_with("-o", "output.bam", "output.bam")
        mock_index.assert_called_once_with("output.bam")

class TestMergerMetadata(unittest.TestCase):
    @patch('os.path.getsize')
    @patch('builtins.open', unittest.mock.mock_open())
    def test_construct_metadata(self, mock_getsize):
        mock_getsize.return_value = 1234
        bam_files = [MagicMock(filename='file1.bam'), MagicMock(filename='file2.bam')]
        merger = Merger(bam_files, "output.bam")
        merger.construct_metadata()
        mock_getsize.assert_called_once_with("output.bam")
        # Check if metadata file is written correctly (simplified check)
        builtins.open.assert_called_once_with("output.bammerge_metadata.json", "w")

# Run the tests using:
# python -m unittest unit_tests/test_merger.py
