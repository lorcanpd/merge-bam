# merge-bam

`merge-bam` is a command-line tool designed to efficiently merge multiple BAM files into a single BAM file. It is built on top of `pysam`, leveraging the power of SAMtools for handling BAM files. This tool is particularly useful in bioinformatics workflows where consolidating sequencing data from multiple sources or samples is required.

## Features

- **Simple Command-Line Interface**: Easy to use command-line interface for merging BAM files.
- **Efficient Processing**: Utilizes `pysam` for efficient reading and writing of BAM files.
- **Metadata Tracking**: Generates metadata for the merged BAM file, including source files and merge timestamp.

## Installation

To install `merge-bam`, you will need Python 3.6 or higher. It is recommended to install `merge-bam` within a virtual environment:

```bash
# Clone the repository (if available)
git clone https://github.com/lorcanpd/merge-bam.git
cd merge-bam

# Or download and extract the source code into a directory named merge-bam

# Install using pip
pip install .
```

## Usage
To merge BAM files, use the merge-bam command followed by the paths to the BAM files you wish to merge and the -o option to specify the output file name:

```bash
merge-bam --bam_files path/to/file1.bam path/to/file2.bam -o path/to/output.bam
```

### Arguments
- `--bam_files`: Paths to the BAM files to be merged. You can specify multiple files to merge seperated with a space.
- `-o`, `--output`: Path to the output BAM file.

## Acknowledgments
- This project utilizes `pysam`, a Python module for reading, manipulating and writing genomic data sets.

