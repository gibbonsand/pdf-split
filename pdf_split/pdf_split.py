"""pdf_split module splits PDF files into separate files."""

# Standard libraries
import glob
import logging
import os

# External libraries
import PyPDF2

# Local libraries
import pdf_split.constants as c


def pdf_split(input_file_path: str, output_dir: str = c.OUTPUT_DIR, pages: list = ["*"]) -> None:
    """
    Split PDF file in separate file for each page.

    Args:
        input_file_path (str): Path to the input PDF file.
        output_dir (str): Path to the folder containing the output files.
        pages (list): List of pages to extract from PDF file. Currently only supports extracting
                      all pages individually.
        Valid example input pages parameters:
        - ['*']

    Returns:
        None
    """

    input_pdf = PyPDF2.PdfReader(input_file_path)
    basename = os.path.splitext(os.path.basename(input_file_path))[0]

    # Get set of file basenames present in the default ouput directory
    already_processed_files = {os.path.basename(file) for file in glob.glob(f"{c.OUTPUT_DIR}*.pdf")}
    logging.debug("Already processed files: %s", already_processed_files)

    if pages == ["*"]:
        logging.info("Splitting file %s in separate PDF files (1 per page).", input_file_path)
        pages = list(range(len(input_pdf.pages)))
        for page in pages:
            logging.info("Processing PDF page %s out of %s", page + 1, max(pages) + 1)

            output_file = basename + "-" + str(page + 1) + ".pdf"
            if output_file in already_processed_files:
                logging.info(
                    "Output file %s already present in output folder, skipping.", output_file
                )
                continue

            output_file_path = output_dir + output_file

            pdf_writer = PyPDF2.PdfWriter()
            pdf_writer.add_page(input_pdf.pages[page])

            with open(output_file_path, "wb") as f:
                pdf_writer.write(f)
                f.close()
    else:
        logging.info("Feature not yet implemented: selecting pages to extract.")
