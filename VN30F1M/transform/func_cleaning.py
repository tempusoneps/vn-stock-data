import pandas as pd


REQUIRED_COLUMNS = ["Open", "High", "Low", "Close", "Volume"]


def clean_ohlcv(
    data: pd.DataFrame,
    dropna: bool = True,
    remove_negative: bool = True,
    remove_duplicates: bool = True,
    sort_by_index: bool = True,
) -> pd.DataFrame:
    """
    Clean OHLCV DataFrame với Date là index.
    """

    df = data.copy()

    # ==============================
    # 1️⃣ Validate index
    # ==============================
    if not isinstance(df.index, pd.DatetimeIndex):
        try:
            df.index = pd.to_datetime(df.index)
        except Exception:
            raise ValueError("DataFrame index must be DatetimeIndex or convertible to datetime")

    # ==============================
    # 2️⃣ Validate required columns
    # ==============================
    missing_cols = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing_cols:
        raise ValueError(f"Missing required columns: {missing_cols}")

    # ==============================
    # 3️⃣ Convert numeric columns
    # ==============================
    df[REQUIRED_COLUMNS] = df[REQUIRED_COLUMNS].apply(
        pd.to_numeric, errors="coerce"
    )

    # ==============================
    # 4️⃣ Drop NaN
    # ==============================
    if dropna:
        df = df.dropna(subset=REQUIRED_COLUMNS)

    # ==============================
    # 5️⃣ Remove negative values
    # ==============================
    if remove_negative:
        df = df[
            (df[["Open", "High", "Low", "Close"]] >= 0).all(axis=1)
            & (df["Volume"] >= 0)
        ]

    # ==============================
    # 6️⃣ Fix logical OHLC errors
    # ==============================
    df = df[
        (df["High"] >= df[["Open", "Close", "Low"]].max(axis=1))
        & (df["Low"] <= df[["Open", "Close", "High"]].min(axis=1))
    ]

    # ==============================
    # 7️⃣ Remove duplicate index (Date)
    # ==============================
    if remove_duplicates:
        df = df[~df.index.duplicated(keep="first")]

    # ==============================
    # 8️⃣ Sort by index
    # ==============================
    if sort_by_index:
        df = df.sort_index()

    return df