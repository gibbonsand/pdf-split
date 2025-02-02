"""Module containing the constant definitions for the pdf_split project"""

# Pathing configuration
LOGFILE_PATH = "/Users/andrewgibbons/Projects/logs/pdf-split/pdf-split.log"
DATA_ROOT_DIR = "/Users/andrewgibbons/Projects/data/pdf-split/"
INPUT_DIR = f"{DATA_ROOT_DIR}input/"
OUTPUT_DIR = f"{DATA_ROOT_DIR}output/"

# Help messages for argparse
HELP_MESSAGES = {
    "pages": """\
Specify which page(s) you want to extract from the input PDF.\
""",
}

# argparse config
ARG_NAMES = HELP_MESSAGES.keys()
VALUE_ARGS = {
    "pages": list,
}
