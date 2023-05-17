# encoding: utf8

import pandas as pd
import config
from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np


def main():
    word_count = 0
    true_count = 0
    false_count = 0
    type_count = [0]*7
    corpus_length = []
    length_distribution = defaultdict(int)
    for i in range(8):
        df = pd.read_excel(config.corpus_excel, 2*i)
        for j in df.index:
            try:
                if df['review_opinion'][j] != '弃用':
                    word_count += len(df['context1'][j]) + len(df['context2'][j])
                    corpus_length.append(len(df['context1'][j]))
                    length_distribution[str(len(df['context1'][j])//50)] += 1
                    if df['judge'][j]:
                        true_count += 1
                        type_count[int(df['note'][j])-1] += 1
                    else:
                        false_count += 1
            except:
                print(df['context1'][j])

    var = np.var(corpus_length)
    mean = np.mean(corpus_length)
    std = np.std(corpus_length)
    print(word_count, true_count, false_count, type_count, mean, var, std, length_distribution, sep='\n')



if __name__ == "__main__":
    main()