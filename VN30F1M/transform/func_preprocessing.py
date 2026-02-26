DROP_COLUMNS = ['time_d', 'couple_cs_1st_cond', 'couple_cs_2rd_cond']


def preprocessing_data(df):
    df.drop(columns=DROP_COLUMNS, inplace=True)
    df.dropna(inplace=True)
    return df