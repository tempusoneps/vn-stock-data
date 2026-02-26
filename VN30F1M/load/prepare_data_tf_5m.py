import warnings
warnings.filterwarnings('ignore')
import os
import pandas as pd
from VN30F1M.transform import OHLCV_DIR, DATA_READY_DIR
from VN30F1M.transform.func_validating import validate_ohlcv_dataset
from VN30F1M.transform.func_cleaning import clean_ohlcv
from VN30F1M.transform.func_features import feature_engineering
from VN30F1M.transform.func_preprocessing import preprocessing_data
from VN30F1M.transform.func_labeling import labeling_data

if __name__ == '__main__':
    ohlcv_file = str(OHLCV_DIR) + '/VN30F1M_5m.csv'
    csv_ready_file = str(DATA_READY_DIR) + '/VN30F1M_5m_ready.csv'
    is_file = os.path.isfile(ohlcv_file)
    if is_file:
        ohlcv_data = pd.read_csv(ohlcv_file, index_col='Date', parse_dates=True).tail(2000)
        is_validate, _ = validate_ohlcv_dataset(ohlcv_data)
        if is_validate:
            clean_data = clean_ohlcv(ohlcv_data)
            if len(clean_data) > 0:
                featured_data = feature_engineering(clean_data)
                labeled_data = labeling_data(featured_data)
                preprocessed_data = preprocessing_data(labeled_data)
                preprocessed_data.to_csv(csv_ready_file, index=True)
        else:
            print(f"File {ohlcv_file} is invalid.")
    else:
        print(f"File {ohlcv_file} not found.")