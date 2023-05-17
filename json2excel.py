# encoding: utf8
import pandas as pd
import json
import config


def json2excel(json_file: str, excel_file: str):
    with open(json_file, 'r', encoding='utf8') as json_file:
        data = json.load(json_file)

    df = pd.DataFrame(data)
    df.to_excel(excel_file)


if __name__ == '__main__':
    json2excel(
        config.label_file6, config.excel6
    )