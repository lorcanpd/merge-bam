#!/usr/bin/env python3

import argparse
from merge_bam.merger import Merger

def main():
    parser = argparse.ArgumentParser(
        description='Merges multiple BAM files into a single BAM file.'
    )
    parser.add_argument(
        '--bam_files',
        nargs='+',
        required=True,
        help='The BAM files to merge.'
    )
    parser.add_argument(
        '-o',
        '--output',
        required=True,
        help='The file name to be assigned to the merged BAM file.'
    )

    args = parser.parse_args()

    merger = Merger(bam_files=args.bam_files, output_file=args.output)

    merger.merge()
    merger.sort()
    merger.index()
    merger.construct_metadata()

if __name__ == '__main__':
    main()

#
# import pysam
#
# try:
#     with pysam.AlignmentFile(
#             # filename="TEST_DATA/HG00326.chrom20.ILLUMINA.bwa.FIN.low_coverage.20120522.bam",
#             filename="TEST_DATA/HG00326.chrom11.ILLUMINA.bwa.FIN.low_coverage.20120522.bam",
#             mode="rb") as bam:
#         for read in bam:
#             print(read)
# except Exception as e:
#     print(f"Error reading BAM file: {e}")