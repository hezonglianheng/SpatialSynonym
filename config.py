# encoding: utf8
import os

all_data = './语料/SpaCE22-task1-data.json'
all_label = './label_res'
pair_data1 = './语料/pair1'
pair_data2 = './语料/pair2'
pair_data3 = './语料/pair3'
pair_data4 = './语料/pair4'
pair_data5 = './语料/pair5'
pair_data6 = './语料/pair6'
pair_data7 = './语料/pair7'
antonym = './others/Antonym.json'
antonym_excel = './others/antonym_excel byQYH.xlsx'

# for data combine
combined_data = './combined_data'
single_opposite_list = [
    './语料/pair1/上-下.json',
    './语料/pair1/下-上.json',
    './语料/pair1/前-后.json',
    './语料/pair1/后-前.json',
    './语料/pair1/右-左.json',
    './语料/pair1/左-右.json',
    './语料/pair1/外-里.json',
    './语料/pair1/里-外.json'
]
single_opposite_file = './combined_data/single_opposite.json'
plural_opposite_list = [
    './语料/pair1/上[来去]-下[来去].json',
    './语料/pair1/下[来去]-上[来去].json',
    './语料/pair1/出[来去]-进[来去].json',
    './语料/pair1/进[来去]-出[来去].json',
    './语料/pair1/回[来去]-过[来去].json',
    './语料/pair1/过[来去]-回[来去].json'
]
plural_opposite_file = './combined_data/plural_opposite.json'
mian_list = [
    './语料/pair1/.面-.面.json'
]
mian_file = './combined_data/mian.json'
center_around_list = [
    './语料/pair1/-[旁外]-中.json',
    './语料/pair1/-中-[旁外].json'
]
center_around_file = './combined_data/center_around.json'

single_not_opposite_list = [
    os.path.join('语料/pair2', f)
    for f in os.listdir('语料/pair2')
]
single_not_opposite_file = './combined_data/single_not_opposite.json'

plural_same_list = [
    os.path.join('./语料/pair3', f)
    for f in os.listdir('./语料/pair3')
    if '[' in f
]
plural_same_file = './combined_data/plural_same.json'

single_part2_list = [
    os.path.join(pair_data4, f)
    for f in os.listdir(pair_data4)
]
single_part2_file = f'{combined_data}/single_part2.json'
round6_list = [
    os.path.join(pair_data6, f)
    for f in os.listdir(pair_data6)
]
round6_file = f'{combined_data}/round6.json'

# for label
label_file1 = './label_res/label_1.json'
label_source1 = [
    './combined_data/center_around.json',
    './combined_data/mian.json',
    './combined_data/plural_opposite.json',
    './combined_data/single_opposite.json'
]
label_source2 = [
    './combined_data/single_not_opposite.json',
    './语料/pair2/.-边.json'
]
label_file2 = './label_res/label_2.json'
label_source3 = [
    './combined_data/plural_same.json',
    './语料/pair3/.侧-.侧.json',
    './语料/pair3/.边-.边.json'
]
label_file3 = './label_res/label_3.json'
label_source4 = ['./combined_data/single_part2.json']
label_file4 = './label_res/label_4.json'
label_source5 = [
    os.path.join(pair_data5, f)
    for f in os.listdir(pair_data5)
]
label_file5 = './label_res/label_5.json'
label_source6 = [round6_file]
label_file6 = './label_res/label_6.json'

# for excel
excel1 = './excels/excel_1.xlsx'
excel2 = './excels/excel_2.xlsx'
excel3 = './excels/excel_3.xlsx'
excel4 = './excels/excel_4.xlsx'
excel5 = './excels/excel_5.xlsx'
excel6 = './excels/excel_6.xlsx'
qyh_excel1 = './excels/语料种子4task3 byQYH v1.0.xlsx'
dsr_excel = './excels/task3语料扩充_dsr.xlsx'
qyh_excel2 = './excels/语料种子4task3 byQYH v2.0.xlsx'
qyh_excel3 = './excels/语料种子4task3 byQYH v3.0.xlsx'

transferred_excel1 = './transferred_excel/trans_1.xlsx'
transferred_excel2 = './transferred_excel/trans_2.xlsx'
transferred_dsr = './transferred_excel/trans_dsr.xlsx'
transferred_qyh1 = './transferred_excel/trans_qyh1'
transferred_qyh2 = './transferred_excel/trans_qyh2.xlsx'
transferred_qyh3 = './transferred_excel/trans_qyh3.xlsx'

statistic_excel = './excels/statistic_excel.xlsx'
corpus_excel = './附件下载_SpaCE2023 task3 数据收集/SpaCE2023 task3 数据收集 5.16version.xlsx'

# selected data
selected_excel = './others/SpaCE2023 task3 精选10例.xlsx'
selected_json = './others/SpaCE2023_task3_selected10.json'

if __name__ == '__main__':
    print(label_file1)
