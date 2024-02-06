
import pysam
import os
import json
import sys
from .version import __version__

# TODO: Add some functionality to label reads with read grouping? Would this be
#  useful?
class Merger:
    """Merges multiple BAM files into a single BAM file."""
    def __init__(self, bam_files, output_file):
        self.bam_files = bam_files
        self.output_file = output_file
        self.num_files = len(bam_files)
        # Check if the BAM files are valid.
        if self.num_files < 2:
            raise ValueError("At least two BAM files are required to merge.")

    def merge(self):
        pg_dict = {
            "ID": "merger",
            "PN": "merge-bam",
            "VN": __version__,
            "CL": " ".join(sys.argv),
            "DS": "Merges BAM files into a single BAM file."
        }
        # new_header = self.bam_files[0].header.to_dict()
        # Load in first bam file to get header
        with pysam.AlignmentFile(
                self.bam_files[0], "rb"
        ) as input_bam:
            new_header = input_bam.header.to_dict()

        if 'PG' not in new_header:
            new_header['PG'] = []
        new_header['PG'].append(pg_dict)

        # Iterate through the BAM files and merge them into the output file.
        with pysam.AlignmentFile(
                self.output_file, "wb", header=new_header
        ) as output_bam:
            i = 1
            # Iterate through the BAM files and merge them into the output file.
            for bam_file in self.bam_files:
                # Load the BAM file and iterate through the reads.
                print(
                    f"Merging file ({i}/{self.num_files}): {bam_file}",
                    file=sys.stderr
                )
                with pysam.AlignmentFile(
                        bam_file, "rb"
                ) as input_bam:
                    for read in input_bam:
                        output_bam.write(read)
                i += 1
            print("Merging complete.", file=sys.stderr)

    def sort(self):
        # Sort the merged BAM file.
        print("Sorting merged BAM file.", file=sys.stderr)
        pysam.sort("-o", self.output_file, self.output_file)

    def index(self):
        # Create BAI format index for the output file.
        print("Indexing merged BAM file.", file=sys.stderr)
        pysam.index(self.output_file)

    def construct_metadata(self):
        # Construct metadata for the output file.
        metadata = {
            "file_type": "BAM",
            # strip extension from output file
            "file_name": self.output_file,
            "file_size": os.path.getsize(self.output_file),
            "created_from": [bam_file for bam_file in self.bam_files],
        }

        # Save the metadata to a JSON file.
        with open(
            os.path.basename(self.output_file).split(".")[0] + "_metadata.json",
            "w"
        ) as metadata_file:
            json.dump(metadata, metadata_file)

