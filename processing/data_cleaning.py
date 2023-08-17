from __future__ import annotations


def clean_data(data, target):
    data_clear = drop_na(data, [target])
    return data_clear


def drop_na(data, columns):
    return data.dropna(subset=columns)


def fill_na():
    pass
