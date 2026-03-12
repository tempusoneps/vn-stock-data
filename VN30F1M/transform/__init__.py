from pathlib import Path

VN30F1M_DIR = Path(__file__).parent.parent
OHLCV_DIR = VN30F1M_DIR / "data_ohlcv"
DATA_READY_DIR = VN30F1M_DIR / "data_ready"

COLUMN_SCHEMA = {

    # =========================
    # ORIGINAL OHLCV
    # =========================
    "Open": {"name": "Opening Price", "type": "float", "comment": "Giá mở cửa"},
    "High": {"name": "Highest Price", "type": "float", "comment": "Giá cao nhất"},
    "Low": {"name": "Lowest Price", "type": "float", "comment": "Giá thấp nhất"},
    "Close": {"name": "Closing Price", "type": "float", "comment": "Giá đóng cửa"},
    "Volume": {"name": "Trading Volume", "type": "float", "comment": "Khối lượng giao dịch"},

    # =========================
    # DAY DATA RESAMPLE
    # =========================
    "day_open": {"name": "Daily Opening Price", "type": "float", "comment": "Giá mở cửa trong ngày"},
    "day_high": {"name": "Daily Highest Price", "type": "float", "comment": "Giá cao nhất trong ngày"},
    "day_low": {"name": "Daily Lowest Price", "type": "float", "comment": "Giá thấp nhất trong ngày"},
    "day_close": {"name": "Daily Closing Price", "type": "float", "comment": "Giá đóng cửa trong ngày"},
    "day_volume": {"name": "Daily Trading Volume", "type": "float", "comment": "Khối lượng giao dịch trong ngày"},

    # =========================
    # TIME FEATURES
    # =========================
    "hour": {"name": "Trading Hour", "type": "int", "comment": "Giờ giao dịch"},
    "minute": {"name": "Trading Minute", "type": "int", "comment": "Phút giao dịch"},
    "session_progress": {"name": "Session Position", "type": "float", "comment": "Vị trí trong phiên"},
    "week_day": {"name": "Day of Week", "type": "int", "comment": "Ngày trong tuần"},

    # =========================
    # CANDLESTICK FEATURES
    # =========================
    "body": {"name": "Candlestick Body", "type": "float", "comment": "Thân nến abs(Close - Open)"},
    "upper_wick": {"name": "Upper Wick", "type": "float", "comment": "Bóng nến trên"},
    "lower_wick": {"name": "Lower Wick", "type": "float", "comment": "Bóng nến dưới"},
    "upper_wick_ratio": {"name": "Upper Wick Ratio", "type": "float", "comment": "Tỷ lệ bóng nến trên"},
    "lower_wick_ratio": {"name": "Lower Wick Ratio", "type": "float", "comment": "Tỷ lệ bóng nến dưới"},
    "candlestick_height": {"name": "Candlestick Height", "type": "float", "comment": "Chiều cao nến"},
    "ibs": {"name": "Internal Bar Strength", "type": "float", "comment": "Internal Bar Strength"},
    "clv": {"name": "Close Location Value", "type": "float", "comment": "Close Location Value ((Close-Low) - (High-Close)) / (High - Low)"},
    "cbr": {"name": "Candlestick Body Ratio", "type": "float", "comment": "Candlestick Body Ratio (|Close - Open| / (High - Low))"},
    "candle_color": {"name": "Candle Color", "type": "string", "comment": "Màu nến (green/red/doji)"},

    # =========================
    # VOLUME FEATURES
    # =========================
    "volume_avg20": {"name": "20-Period Average Volume", "type": "float", "comment": "Trung bình khối lượng 20 phiên"},
    "volume_zscore": {"name": "Volume Z-Score", "type": "float", "comment": "Z-score khối lượng"},
    "is_volume_above_avg": {"name": "Is Volume Above Average", "type": "bool", "comment": "Volume cao hơn trung bình"},

    # =========================
    # PRICE STRUCTURE
    # =========================
    "is_fvg": {"name": "Fair Value Gap", "type": "bool", "comment": "Fair Value Gap"},
    "is_lower_low_higher_volume": {"name": "Lower Low Higher Volume", "type": "bool", "comment": "Đáy thấp hơn với volume cao hơn"},
    "high_position": {"name": "High Position vs Bollinger Band", "type": "string", "comment": "Vị trí High so với Bollinger Band"},
    "low_position": {"name": "Low Position", "type": "string", "comment": "Vị trí Low"},


    # =========================
    # TECHNICAL INDICATORS
    # =========================
    "EMA20": {"name": "Exponential Moving Average 20", "type": "float", "comment": "Exponential Moving Average 20"},
    "EMA250": {"name": "Exponential Moving Average 250", "type": "float", "comment": "Exponential Moving Average 250"},
    "ATR14": {"name": "Average True Range 14", "type": "float", "comment": "Average True Range 14"},
    "ADX14": {"name": "Average Directional Index 14", "type": "float", "comment": "Average Directional Index 14"},
    "RSI20": {"name": "Relative Strength Index 20", "type": "float", "comment": "Relative Strength Index 20"},
    "RSI10": {"name": "Relative Strength Index 10", "type": "float", "comment": "Relative Strength Index 10"},
    "VWAP": {"name": "Volume Weighted Average Price", "type": "float", "comment": "Volume Weighted Average Price"},
    "RSI_slope": {"name": "RSI Slope", "type": "float", "comment": "Slope của RSI"},
    "EMA20_slope": {"name": "EMA20 Slope", "type": "float", "comment": "Slope của EMA20"},
    "z_score": {"name": "Close Z-Score", "type": "float", "comment": "Z-score của Close = (Price-MA)/Std"},
    "pct_change": {"name": "Percentage Change", "type": "float", "comment": "Phần trăm thay đổi"},
    "skew_100": {"name": "100-Period Skewness", "type": "float", "comment": "df['pct_change'].rolling(100).skew()"},
    "kurt_100": {"name": "100-Period Kurtosis", "type": "float", "comment": "df['pct_change'].rolling(100).kurt()"},
    "typical_price": {"name": "Typical Price", "type": "float", "comment": "(High+Low+Close)/3"},
    "money_flow": {"name": "Money Flow", "type": "float", "comment": "Money Flow = Typical Price * Volume"},
    "money_flow_type": {"name": "Money Flow Type", "type": "float", "comment": "Positive Flow if typical_price > prev_typical_price else Negative Flow"},
    "money_flow_score": {"name": "Money Flow Score", "type": "float", "comment": "Money Flow Score = sum(Positive Flow) / sum(Negative Flow)"},
    "DM": {"name": "Distance Moved", "type": "float", "comment": "Distance Moved (DM) = (Current High + Current Low) / 2 - (Previous High + Previous Low) / 2"},
    "VBR": {"name": "Volume Box Ratio", "type": "float", "comment": "Volume Box Ratio = Volume / (High - Low)"},
    "EOM": {"name": "Ease of Movement", "type": "float", "comment": "Ease of Movement = DM / VBR"},
    "keltner_channel": {"name": "Keltner Channel", "type": "float", "comment": "Keltner Channel = EMA20 ± ATR14"},
    "hurst_exponent": {"name": "Hurst Exponent 10", "type": "float", "comment": "Hurst Exponent 10"},
    "hurst_exponent_100": {"name": "Hurst Exponent 100", "type": "float", "comment": "Hurst Exponent 100"},
    "parkinson_vol_20": {"name": "20-Period Parkinson Volatility", "type": "float", "comment": "Rolling 20 Parkinson Volatility"},
    "up_streak": {"name": "Up Streak", "type": "int", "comment": "Số phiên tăng liên tiếp"},
    "down_streak": {"name": "Down Streak", "type": "int", "comment": "Số phiên giảm liên tiếp"},
    # ====
    # CUSTOM MONEY FLOW
    # ====
    "MFM": {"name": "Money Flow Multiplier", "type": "float", "comment": "Money Flow Multiplier (MFM)"},
    "MFV": {"name": "Money Flow Volume", "type": "float", "comment": "Money Flow Volume (MFV)"},
    "CMF": {"name": "Chaikin Money Flow", "type": "float", "comment": "Chaikin Money Flow (CMF) - volume-weighted momentum"},
    "CMF_3D": {"name": "3-Day Chaikin Money Flow", "type": "float", "comment": "Chaikin Money Flow 3 ngày(3 * 49 bars)"},
    "CMF_5D": {"name": "5-Day Chaikin Money Flow", "type": "float", "comment": "Chaikin Money Flow 5 ngày(5 * 49 bars)"},
    "CMF_10D": {"name": "10-Day Chaikin Money Flow", "type": "float", "comment": "Chaikin Money Flow 10 ngày(10 * 49 bars)"},
    "MFI_1D": {"name": "1-Day Money Flow Index", "type": "float", "comment": "Money Flow Index 1 ngày"},
    "MFI_3D": {"name": "3-Day Money Flow Index", "type": "float", "comment": "Money Flow Index 3 ngày(3 * 49 bars)"},
    "MFI_5D": {"name": "5-Day Money Flow Index", "type": "float", "comment": "Money Flow Index 5 ngày(5 * 49 bars)"},
    "MFI_10D": {"name": "10-Day Money Flow Index", "type": "float", "comment": "Money Flow Index 10 ngày(10 * 49 bars)"},

    # ====
    # BOLLINGER BANDS
    # ====
    "BB_middle": {"name": "Bollinger Bands Middle", "type": "float", "comment": "Middle Band (SMA20)"},
    "BB_std": {"name": "20-Period Standard Deviation", "type": "float", "comment": "Độ lệch chuẩn 20 phiên"},
    "BB_upper": {"name": "Bollinger Bands Upper", "type": "float", "comment": "Upper Bollinger Band"},
    "is_bb_rejection": {"name": "Is Bollinger Bands Rejection", "type": "bool", "comment": "Tín hiệu từ chối Bollinger Bands"},

    # =========================
    # PREVIOUS (SHIFTED) DATA
    # =========================
    "prev_Open": {"name": "Previous Open", "type": "float", "comment": "Open phiên trước"},
    "prev_High": {"name": "Previous High", "type": "float", "comment": "High phiên trước"},
    "prev_Low": {"name": "Previous Low", "type": "float", "comment": "Low phiên trước"},
    "prev_Close": {"name": "Previous Close", "type": "float", "comment": "Close phiên trước"},
    "prev_Volume": {"name": "Previous Volume", "type": "float", "comment": "Volume phiên trước"},
    "prev_body": {"name": "Previous Body", "type": "float", "comment": "Body phiên trước"},
    "prev_upper_wick": {"name": "Previous Upper Wick", "type": "float", "comment": "Upper wick phiên trước"},
    "prev_lower_wick": {"name": "Previous Lower Wick", "type": "float", "comment": "Lower wick phiên trước"},
    "prev_EMA20": {"name": "Previous EMA20", "type": "float", "comment": "EMA20 phiên trước"},
    "prev_EMA250": {"name": "Previous EMA250", "type": "float", "comment": "EMA250 phiên trước"},
    "prev_MFI_1D": {"name": "Previous 1-Day MFI", "type": "float", "comment": "MFI phiên trước"},
    "prev_ibs": {"name": "Previous IBS", "type": "float", "comment": "IBS phiên trước"},

    # =========================
    # CUSTOM INDICATORS
    # =========================
    "fea_001": {"name": "Feature 001", "type": "float", "comment": "100 * (Close - day_close.shift(1)) / day_close.shift(1)"},
    "fea_002": {"name": "Feature 002", "type": "float", "comment": "(Close - close.shift(49)) / (max_high_49bars - min_low_49bars)"},
    "fea_003": {"name": "Feature 003", "type": "float", "comment": "abs(EMA20 - EMA250) / ATR"},

    # =========================
    # GROUPED FEATURES
    # =========================
    "high_volume_group": {"name": "High and Volume Group", "type": "string", "comment": "Nhóm High và Volume"},
    "volume_group": {"name": "Volume Group", "type": "string", "comment": "Nhóm Volume"},
    "price_body_group": {"name": "Price Body Group", "type": "string", "comment": "Nhóm giá so với body"},
    "upper_wick_group": {"name": "Upper Wick Group", "type": "string", "comment": "Nhóm upper wick"},
    "lower_wick_group": {"name": "Lower Wick Group", "type": "string", "comment": "Nhóm lower wick"},
    "ibs_volume_group": {"name": "IBS and Volume Group", "type": "string", "comment": "Nhóm IBS và Volume"},
    "volume_avg_group": {"name": "Average Volume Group", "type": "string", "comment": "Nhóm volume trung bình"},
    "high_rsi_group": {"name": "High and RSI Group", "type": "bool", "comment": "Nhóm High và RSI"},
    "close_position_group": {"name": "Close Position Group", "type": "string", "comment": "Nhóm vị trí Close"},
    "open_position_group": {"name": "Open Position Group", "type": "string", "comment": "Nhóm vị trí Open"},

    # =========================
    # SIGNALS
    # =========================
    "couple_candle_cond_1": {"name": "Couple Candle Condition 1", "type": "string", "comment": "Điều kiện 1 cặp nến"},
    "couple_candle_cond_2": {"name": "Couple Candle Condition 2", "type": "string", "comment": "Điều kiện 2 cặp nến"},
    "couple_candle_signal": {"name": "Couple Candle Signal", "type": "string", "comment": "Tín hiệu cặp nến"},
    "ema_cross_signal": {"name": "EMA20/EMA250 Cross Signal", "type": "string", "comment": "Tín hiệu giao cắt EMA20/EMA250"},
}