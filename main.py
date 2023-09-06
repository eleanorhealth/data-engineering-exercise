import argparse
import logging
import os
import sys

import pandas as pd
from pythonjsonlogger import jsonlogger

logger = logging.getLogger()
logHandler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter()
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)
logger.setLevel(logging.INFO)


def main(input_file: str) -> None:
    delete_cols = [
        "MBR_SUD",
        "ATTRIBUTED_PCP",
        "ATTRIBUTED_PCP_NPI",
        "ATTRIBUTED_PCP_VENDOR_NAME",
        "ATTRIBUTED_PCP_VENDOR_PHONE",
        "MBR_INSUR_PLAN",
    ]

    try:
        df = pd.read_csv(input_file, dtype=str)
    except FileNotFoundError as e:
        logger.error(f"FileNotFoundError: {e}")
        sys.exit(1)

    try:
        for col in delete_cols:
            df = df.drop(columns=col)
    except KeyError as e:
        logger.warning(f"KeyError: Some columns failed to drop. Error: {e}")
        pass

    try:
        output_file = os.path.splitext(input_file)[0] + "_out.csv"
        df.to_csv(output_file, index=False)
    except PermissionError as e:
        logger.error(f"PermissionError: {e}")
        sys.exit(1)

    logger.info(f"Output file: {output_file}")
    logger.info("Done!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", type=str, help="input csv file")
    args = parser.parse_args()

    main(args.input_file)
