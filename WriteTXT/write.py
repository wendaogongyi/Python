import csv
import random


def text_create(name, msg):
    desktop_path = 'D:\\PaddleClas\\'
    full_path = desktop_path + name + '.txt'
    file = open(full_path, 'w')
    file.write(msg)


def data_split(full_list, ratio1, ratio2, shuffle=True):
    n_total = len(full_list)
    offset1 = int(n_total * ratio1)
    offset2 = int(offset1 + n_total * ratio2)
    if n_total == 0 or offset1 < 1:
        return [], full_list
    if shuffle:
        random.shuffle(full_list)
    sublist_1 = full_list[:offset1]
    sublist_2 = full_list[offset1:offset2]
    sublist_3 = full_list[offset2:]
    return sublist_1, sublist_2, sublist_3


def writestr(list_name):
    s = ''
    for i in list_name:
        for j in i:
            if j == 'yes':
                j = '1'
            if j == 'no':
                j = '0'
            if j == '1' or j == '0':
                s = s + '\t' + '\r\n'
            else:
                s = s + 'Data/' + j
    return s


with open('D:\\PaddleClas\\data.csv', 'r') as f:
    reader = csv.reader(f)
    result = list(reader)

train, val, test = data_split(result, 0.6, 0.2)

str_train = writestr(train)
str_val = writestr(val)
str_test = writestr(test)

text_create('train', str_train)
text_create('val', str_val)
text_create('test', str_test)
