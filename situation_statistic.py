# encoding: utf8

import json
import re
import os
from collections import defaultdict
import pandas as pd
import config


def transfer_rp_pair(pair: str):
    e = pair.split('-', maxsplit=1)
    return f'{e[0]}-{e[1]}' if e[0] < e[1] else f'{e[1]}-{e[0]}'


def get_rp_pairs(string: str):
    rp_pairs = re.findall(r'【【.{1,2}→.{1,2}】】', string)
    rp_pairs = [transfer_rp_pair(i.replace('【', '').replace('】', '').replace('→', '-'))
                for i in rp_pairs]
    return rp_pairs


def main():
    all_labeled = []
    for f in [os.path.join(config.all_label, i) for i in os.listdir(config.all_label)]:
        with open(f, mode='r', encoding='utf8') as json_f:
            all_labeled.extend(json.load(json_f))
    label_0_dict = defaultdict(int)
    label_1_dict = defaultdict(int)
    label_2_dict = defaultdict(int)
    label_3_dict = defaultdict(int)
    for item in all_labeled:
        for p in get_rp_pairs(item['rp_pair'][0]):
            match item['label']:
                case 0:
                    label_0_dict[p] += 1
                case 1:
                    label_1_dict[p] += 1
                case 2:
                    label_2_dict[p] += 1
                case 3:
                    label_3_dict[p] += 1
                case _:
                    raise ValueError('the judge {} is illegal'.format(item['label']))
    df = pd.DataFrame.from_dict(
        [label_0_dict, label_1_dict, label_2_dict, label_3_dict],
    ).T
    df = df.fillna(0)
    df.to_excel(config.statistic_excel)


if __name__ == "__main__":
    main()