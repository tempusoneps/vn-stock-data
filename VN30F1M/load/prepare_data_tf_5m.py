import warnings
warnings.filterwarnings('ignore')
import os
import pandas as pd
from pathlib import Path
import argparse
from VN30F1M.transform import OHLCV_DIR, DATA_READY_DIR
from VN30F1M.transform.func_validating import validate_ohlcv_dataset
from VN30F1M.transform.func_cleaning import clean_ohlcv
from VN30F1M.transform.func_features import feature_engineering
from VN30F1M.transform.func_preprocessing import preprocessing_data, numeric_data
from VN30F1M.transform.func_labeling import labeling_data

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Prepare OHLCV 5m data")

    parser.add_argument(
        "--limit",
        type=int,
        default=0,
        help="Number of last rows to load"
    )

    parser.add_argument(
        "--to_number",
        action="store_true",
        help="Convert all object columns to numeric"
    )

    parser.add_argument(
        "--dry_run",
        action="store_true",
        help="Dry run, save file to current directory"
    )

    args = parser.parse_args()

    ohlcv_file = str(OHLCV_DIR) + '/VN30F1M_5m.csv'
    if args.dry_run:
        CURRENT_DIR = Path(__file__).parent
        csv_ready_file = str(CURRENT_DIR) + '/VN30F1M_5m_ready.csv'
        csv_ready_file_num = str(CURRENT_DIR) + '/VN30F1M_5m_numeric_ready.csv'
    else:
        csv_ready_file = str(DATA_READY_DIR) + '/VN30F1M_5m_ready.csv'
        csv_ready_file_num = str(DATA_READY_DIR) + '/VN30F1M_5m_numeric_ready.csv'

    if os.path.isfile(ohlcv_file):

        ohlcv_data = pd.read_csv(
            ohlcv_file,
            index_col='Date',
            parse_dates=True
        )
        if args.limit:
            ohlcv_data = ohlcv_data.tail(args.limit)

        is_validate, _ = validate_ohlcv_dataset(ohlcv_data)

        if is_validate:
            clean_data = clean_ohlcv(ohlcv_data)

            if len(clean_data) > 0:
                featured_data = feature_engineering(clean_data)
                labeled_data = labeling_data(featured_data)
                preprocessed_data = preprocessing_data(labeled_data)
                preprocessed_data.to_csv(csv_ready_file, index=True)
                # Optional numeric conversion
                if args.to_number:
                    num_data = numeric_data(preprocessed_data)
                    num_data.to_csv(csv_ready_file_num, index=True)
        else:
            print(f"File {ohlcv_file} is invalid.")
    else:
        print(f"File {ohlcv_file} not found.")