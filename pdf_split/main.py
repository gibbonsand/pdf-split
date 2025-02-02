"""Main entrypoint for the pdf_split project"""

# Standard libraries
import argparse
import glob
import logging
import os
import pathlib

# Local libraries
import pdf_split.constants as c
from pdf_split.pdf_split import pdf_split
from shared_libraries.setup_utilities import init_logger, ensure_folders


def main():
    """Main entrypoint of the pdf_ocr project."""
    # Ensure the input and output folder exist
    ensure_folders([c.OUTPUT_DIR, c.INPUT_DIR, str(pathlib.Path(c.LOGFILE_PATH).parent)])

    # Initialize logging
    init_logger(log_to_file=True, log_to_stream=True, logfile_path=c.LOGFILE_PATH)

    # Initialize argument parser
    parser = argparse.ArgumentParser(description="pdf splitter")
    parser.add_argument("--input_file", required=True, help="Input file path")
    parser.add_argument("--input_dir", required=False, help="Input file parent directory")
    parser.add_argument("--output_dir", required=False, help="Output file parent directory")
    parser.add_argument(
        "--pages",
        nargs="+",
        required=False,
        type=list,
        help="Pages to split from PDF file (comma-separated values e.g. 2,4). Leave blank to split all pages",
    )

    args = parser.parse_args()
    logging.debug("Input arguments: %s", vars(args))

    pages = args.pages if args.pages is not None else ["*"]

    # Parse all files in default input directory
    for input_path in glob.glob(f"{c.INPUT_DIR}*.pdf"):
        file_name = os.path.basename(input_path)

        # Call pdf_split function that wraps the necessary steps
        logging.info("Processing file %s...", file_name)
        pdf_split(input_file_path=input_path, output_dir=c.OUTPUT_DIR, pages=pages)

        logging.info("Finished processing file %s", file_name)
