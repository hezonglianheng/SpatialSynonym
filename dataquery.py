# encoding:utf8
import re
import json
from typing import Literal
import utils
import logging
import config


# 查询指定数据的类
class DataQuery:
    def __init__(self,
                 filename: str,
                 query: str = '.+',
                 multiple_replace: bool = True,
                 condition: Literal['true', 'false', 'all'] = 'all',
                 log_file: str = './log.txt',
                 return_or_not: bool = False
                 ):
        self._filename = filename
        self._query = query
        self._mul_replace = multiple_replace
        self._condition = condition
        self._log_file = log_file
        self._return = return_or_not

    def get_query(self):
        # 获取所有数据
        all_data = []
        utils.get_logger(self._log_file)
        with open(self._filename,
                  mode='r', encoding='utf8') as file:
            raw_data = json.load(file)
            for dataset in raw_data:
                all_data.extend(
                    [item
                     for item in raw_data[dataset]]
                )

        query_match = [
            item for item in all_data
            if re.search(rf'{self._query}', item['_rp_id'])
        ]
        if len(query_match) == 0:
            print(f'match for {self._query} not found.')
            return
        if self._condition == 'all':
            query_res = query_match
        elif self._condition == 'true':
            query_res = [
                item for item in query_match
                if item['judge'] == 1
            ]
        elif self._condition == 'false':
            query_res = [
                item for item in query_match
                if item['judge'] == 0
            ]
        else:
            query_res = []
        logging.info(
            f'''
            查询表达式：{self._query}，
            查询语料正误：{self._condition}
            结果占比：{len(query_res)}/{len(query_match)}={len(query_res) / len(query_match)}
            '''
        )

        if self._return:
            return query_res
        else:
            # print(self._query)
            with open(f'{config.pair_data7}/{self._query}.json',
                      mode='w', encoding='utf8') as qfile:
                # print(self._query)
                json.dump(query_res, qfile, indent=4,
                          ensure_ascii=False)


def pair_query(filename: str,
               query: str,
               multiple_replace: bool = True,
               condition: Literal['true', 'false', 'all'] = 'all',
               log_file: str = './log.txt',
               return_or_not: bool = False):
    query_list = query.split('-')
    query1 = f'{query_list[0]}-{query_list[1]}'
    query2 = f'{query_list[1]}-{query_list[0]}'
    dq1 = DataQuery(
        filename=filename,
        query=query1,
        multiple_replace=multiple_replace,
        condition=condition,
        log_file=log_file,
        return_or_not=return_or_not
    )
    dq1.get_query()
    dq2 = DataQuery(
        filename=filename,
        query=query2,
        multiple_replace=multiple_replace,
        condition=condition,
        log_file=log_file,
        return_or_not=return_or_not
    )
    dq2.get_query()


if __name__ == '__main__':
    # pair_query(filename=config.all_data, query='下-外', condition='true')
    dq = DataQuery(config.all_data, '侧面-外面', condition='true')
    dq.get_query()
