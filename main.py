""" data-engineering-exercise main.py """
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
    """main function"""
    delete_cols = [
        "MBR_SUD",
        "ATTRIBUTED_PCP",
        "ATTRIBUTED_PCP_NPI",
        "ATTRIBUTED_PCP_VENDOR_NAME",
        "ATTRIBUTED_PCP_VENDOR_PHONE",
    ]

    try:
        dataframe = pd.read_csv(input_file, dtype=str)
    except FileNotFoundError as err_msg:
        logger.error("FileNotFoundError: %s", err_msg)
        sys.exit(1)

    try:
        for col in delete_cols:
            dataframe = dataframe.drop(columns=col)

          col_to_move = dataframe.pop("MBR_INSUR_PLAN")
          dataframe.insert(len(dataframe.columns), "MBR_INSUR_PLAN", col_to_move)
    except KeyError as err_msg:
        logger.warning("KeyError: Some columns failed to drop. Error: %s", err_msg)
        pass

    try:
        output_file = os.path.splitext(input_file)[0] + "_out.csv"
        dataframe.to_csv(output_file, index=False)
    except PermissionError as err_msg:
        logger.error("PermissionError: %s", err_msg)
        sys.exit(1)

    logger.info("Output file: %s", output_file)
    logger.info("Done!")

    return "Done!"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", type=str, help="input csv file")
    args = parser.parse_args()

    main(args.input_file)
