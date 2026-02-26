import warnings

warnings.filterwarnings('ignore')

from pathlib import Path
from . import stockHistory

ticker = "VN30F1M"
STOCK_DATA_DIR = Path(__file__).parent.parent

data = stockHistory.get_vn30f1m_ohcl_history_data(ticker="VN30F1M", resolution=5,
                                                     from_=1, broker="DNSE")
data.to_csv(str(STOCK_DATA_DIR) + '/data_ohlcv/VN30F1M_5m.csv')
exit()
