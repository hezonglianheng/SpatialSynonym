# encoding: utf8
import json
import config
import random
import os
import labeldata


class DataCompare:
    def __init__(self,
                 data_files: list[str], res_file: str):
        self._data_files = data_files
        self._res_file = res_file

    def compare(self, label_rate: float = .1):
        if os.path.exists(self._res_file):
            with open(self._res_file,
                      mode='r', encoding='utf8') as file:
                labeled_data = json.load(file)
        else:
            labeled_data = []
        labeled_qid = [i['qid'] for i in labeled_data]
        # print(labeled_qid)

        need_label = []
        for filename in self._data_files:
            with open(filename,
                      mode='r', encoding='utf8') as file:
                all_data = json.load(file)
                # print(len(all_data))
                choose_from = [i for i in all_data
                               if i['qid'] not in labeled_qid]
                if len(choose_from) / len(all_data) <= label_rate:
                    need_label += [i for i in choose_from]
                else:
                    need_label += random.sample(
                        population=choose_from,
                        k=int(len(all_data) * label_rate)
                    )

        need_label = [labeldata.LabelData(i)
                      for i in need_label]
        index = -1
        while index < len(need_label) - 1:
            index += 1
            print(need_label[index].contain_rp)
            label = input('语义是否相同（0，完全不同；1，完全相同；2：可能相同；3，原始标注有误；b，回滚）：')
            if label == 'b':
                index -= 2
            else:
                need_label[index].change_label(int(label))

        list_to_save = labeled_data + [item.get_data_dict()
                                       for item
                                       in need_label]
        with open(self._res_file,
                  'w', encoding='utf8') as res_file:
            json.dump(
                list_to_save, fp=res_file,
                ensure_ascii=False, indent=4
            )


if __name__ == '__main__':
    c = DataCompare(
        config.label_source6,
        config.label_file6
    )
    c.compare()
