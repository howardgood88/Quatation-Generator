import csv
from utility import (wideNumInStr, print_spliter)
import os
import copy
import time

def prepare_item_list():
    global item_index
    def load_data(file, item_list):
        global item_index
        with open(file, newline='', encoding='utf-8') as csvfile:
            rows = csv.DictReader(csvfile)
            _type = file.split(' ')[-1][:-4]
            item_list[_type] = []
            for row in rows:
                row['項次'] = item_index
                row['數量'] = int(row['數量'])
                row['未稅單價'] = int(row['未稅單價'])
                item_list[_type].append(row)
                item_index += 1
    item_list = {}
    item_index = 1
    data_dir = './data/'
    load_data(data_dir + '1 燈頭.csv', item_list)
    load_data(data_dir + '2 燈光配件.csv', item_list)
    load_data(data_dir + '3 旗框、布類.csv', item_list)
    load_data(data_dir + '4 場務、雜項.csv', item_list)
    load_data(data_dir + '5 燈腳、夾具.csv', item_list)
    load_data(data_dir + '6 機身組合.csv', item_list)
    load_data(data_dir + '7 額外加價（需搭配機身組合）.csv', item_list)
    load_data(data_dir + '8 攝影配件（單件）.csv', item_list)
    load_data(data_dir + '9 收音器材.csv', item_list)

    _sum = 0
    for item in item_list.values():
        _sum += len(item)
    return item_list, _sum

def print_item_list():
    print(f' 項次 | {"器材內容":^{71}}| 數量 | 器材編號 | 未稅單價')
    for _type, items in item_list.items():
        print_spliter(f'{_type:^{30 - len(_type)}}', 40)
        for item in items:
            context_ch_width = wideNumInStr(item["器材內容"])
            print(f'{item["項次"]:4d}  | {item["器材內容"]:{75 - context_ch_width}}|{item["數量"]:>5d} |          |{item["未稅單價"]:>9d}')
    print()

def show_item_list():
    os.system('cls')
    print('【目前已加入之品項清單】\n')
    def comp(item):
        return item['項次']
    export_item_list.sort(key=comp)
    print(f' 項次 | {"器材內容":^{71}}| 數量 | 器材編號 | 未稅單價')
    for item in export_item_list:
        context_ch_width = wideNumInStr(item["器材內容"])
        print(f'{item["項次"]:4d}  | {item["器材內容"]:{75 - context_ch_width}}|{item["數量"]:>5d} |          |{item["未稅單價"]:>9d}')
    print()
    return True

def add_item():
    def find_and_insert_item(command):
        for items in item_list.values():
            if command <= len(items):
                item = items[command - 1]
                while 1:
                    try:
                        nums = int(input('請輸入數量：'))
                        if nums <= item['數量']:
                            new_item = copy.copy(item)
                            new_item['數量'] = nums
                            export_item_list.append(new_item)
                            export_item_index_set.add(new_item['項次'])
                            return
                        else:
                            print('輸入數量大於庫存數量，請重新輸入！')
                    except:
                        print('只接受整數輸入，請重新輸入！')
            command -= len(items)
        print(f'成功加入品項')
    while (1):
        os.system('cls')
        print('【加入新品項】\n')
        print_item_list()
        try:
            command = int(input('輸入項次編號以加入新品項(若不須再加入按下Ctrl+C以停止)：'))
            if command <= item_list_sum and command not in export_item_index_set:
                find_and_insert_item(command)
            elif command > item_list_sum:
                print('項次編號超出範圍，請重新輸入！')
                time.sleep(1)
            elif command in export_item_index_set:
                print('該品項已存在，請重新輸入或刪除原先品項！')
                time.sleep(1)
        except KeyboardInterrupt:
            break
        except:
            print('只接受整數輸入，請重新輸入！')
            time.sleep(1)
    return True


def delete_item():
    return True

def terminate():
    return False

item_list, item_list_sum = prepare_item_list()
command_list = {
    '1' : show_item_list,
    '2' : add_item,
    '3' : delete_item,
    '4' : terminate,
}
export_item_list = []
export_item_index_set = set()
while (1):
    command = input('指令清單：\n'
        '1  顯示目前品項清單\n'
        '2  加入品項至器材清單\n'
        '3  自器材清單刪除品項\n'
        '4  輸出CSV檔案並結束程式\n'
        '請輸入指令：')
    try:
        flag = command_list[command]()
        if not flag:
            break
    except KeyError:
        print('指令錯誤，請重新輸入！')
print('執行完成，結束程式')