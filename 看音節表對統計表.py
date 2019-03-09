import json
from 看無聲調的音節 import ko_pio


def main():
    #
    # 知影目前全部音節表內底，啥人有出現佇語料庫
    #
    imTsiatPio = ko_pio()
    thongKePio = getThongKePio()
    arr = dict()
    for im in imTsiatPio:
        try:
            times = thongKePio[im]
        except KeyError:
            times = 0
        arr[im] = times

    print(
        json.dumps(
            sorted(arr.items(), key=lambda x: (x[1], x[0])),
            ensure_ascii=False,
            sort_keys=True,
            indent=2,
        )
    )


def getThongKePio():
    #
    # 語料庫目前有的音節數量
    #
    with open('../Sui-Siann-Dataset/統計全部音節.json', 'r', encoding='utf-8') as file:
        return json.load(file)


if __name__ == '__main__':
    main()
