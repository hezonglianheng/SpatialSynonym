# encoding: utf8
import json
import config


class DataCombine:
    def __init__(self,
                 files_to_combine: list[str],
                 name_after_combine: str):
        self._name_after_combine = name_after_combine
        self._files_to_combine = files_to_combine

    def combine(self):
        data_to_combine = []
        for filename in self._files_to_combine:
            with open(filename,
                      mode='r', encoding='utf8') as file:
                data_to_combine += json.load(file)

        with open(self._name_after_combine,
                  mode='w', encoding='utf8') as combined:
            json.dump(
                obj=data_to_combine,
                fp=combined,
                indent=4,
                ensure_ascii=False
            )


if __name__ == '__main__':
    c = DataCombine(
        config.round6_list,
        config.round6_file
    )
    c.combine()