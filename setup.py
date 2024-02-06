
from setuptools import setup, find_packages

with open('merge_bam/version.py') as f:
    for line in f:
        if line.startswith('__version__'):
            version = line.split('=')[1].strip().strip("'\"")
            break

# from merge_bam import __version__

setup(
    name='merge-bam',
    version=version,
    packages=find_packages(),
    install_requires=[
        'pysam>=0.22.0'
    ],
    entry_points={
        'console_scripts': [
            'merge-bam=merge_bam.main:main',
        ],
    },
    # Additional metadata about your package
    author='Lorcán Pigott-Dix',
    author_email='lp23@sanger.ac.uk',
    description='Merges multiple BAM files into a single BAM file.',
    license='MIT',
    keywords='bioinformatics',
    url='https://github.com/lorcanpd/merge-bam'
)

