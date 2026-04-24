# sudo apt install calibre

import subprocess

input_file = "dokumen.pub_football-analytics-with-python-amp-r-9781492099628-9781492099567.epub"
output_file = "book22.pdf"

"""
subprocess.run([
    "ebook-convert",
    input_file,
    output_file
])
"""

subprocess.run([
    "ebook-convert",
    input_file,
    output_file,
    "--paper-size", "a4",
    "--margin-top", "20",
    "--margin-bottom", "20",
    "--margin-left", "15",
    "--margin-right", "15"
])
