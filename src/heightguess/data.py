"""Loading the height data."""
from pathlib import Path

import pandas as pd

DATA_FILE = Path(__file__).resolve().parents[2] / "data" / "heights.csv"

# No adult is 100 inches (8 ft 4 in) tall, so any height above this must have
# been recorded in centimeters by mistake. In this data nobody falls between
# 79 and 147, so any cutoff in that gap gives the same result.
CM_CUTOFF_IN = 100.0
CM_PER_INCH = 2.54


def load_heights(path=DATA_FILE):
    """Load the adult height table, with every height in inches.

    Columns: participant_id, sex, age, height_in, survey_weight, plus
    height_was_cm (True for rows we converted from centimeters).
    The file on disk is left untouched; the fix happens only in memory.
    """
    df = pd.read_csv(path)
    df["height_was_cm"] = df["height_in"] > CM_CUTOFF_IN
    df.loc[df["height_was_cm"], "height_in"] /= CM_PER_INCH
    return df
