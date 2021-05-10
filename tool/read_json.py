import json


def read_json(path):
    data = []
    with open(path, 'r', encoding='utf-8') as f:
        # 将读取的json字符串转换为dict类型
        list_data = json.loads(f.read())
        for i in list_data:
            data.append(tuple(i.values()))
    return data


if __name__ == '__main__':
    print(read_json("../data/mp_login.json"))