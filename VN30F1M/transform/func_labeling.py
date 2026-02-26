

def labeling_data(df):
    label_data = df.copy()
    new_entry_allowed = []
    for i, row in label_data.iterrows():
        current_date = row.name.strftime('%Y-%m-%d ').format()
        current_time = row.name
        data_to_end_day = label_data[(label_data.index > current_time) & (label_data.index < current_date + ' 14:30:00')]
        if not len(data_to_end_day):
            new_entry_allowed.append(0)
            continue
        #
        if row['Bearish_Divergence']:
            if len(data_to_end_day[data_to_end_day.High > row['High']]) > 0:
                new_entry_allowed.append(1)
            else:
                new_entry_allowed.append(0)
        else:
            if len(data_to_end_day[data_to_end_day.Low < row['Low']]) > 0:
                new_entry_allowed.append(1)
            else:
                new_entry_allowed.append(0)
    label_data['allow_entry'] = new_entry_allowed
    return label_data