import json
from 看無聲調的音節 import ko_pio
import subprocess
from sys import stderr


def main():
    #
    # 知影目前全部音節表內底，啥人有出現佇語料庫
    #
    imTsiatPio = ko_pio()
    thongKePio = getThongKePio()
    逐个音節的數量表 = dict()
    for im in imTsiatPio:
        try:
            times = thongKePio[im]
        except KeyError:
            times = 0
        逐个音節的數量表[im] = times

    # printCompareResult() # 共印出來看覓

    指定數量 = 0
    writeGrep(逐个音節的數量表, 指定數量)
#     指定數量 = 1
#     writeGrep(指定數量)


def printCompareResult(arr):
    print(
        json.dumps(
            sorted(arr.items(), key=lambda x: (x[1], x[0])),
            ensure_ascii=False,
            sort_keys=True,
            indent=2,
        )
    )


def getImTsiatByNumber(imTsiatArr, times):
    return sorted([i for i in imTsiatArr if imTsiatArr[i] == times])


def writeGrep(逐个音節的數量表, 指定數量):
    #
    # 撈出有遮濟擺的音節
    #
    arr = getImTsiatByNumber(逐个音節的數量表, 指定數量)
    #
    # 撈出佇教會公報有這个音節的句
    #
    for im in arr:
        with open('統計/{}_{}.txt'.format(指定數量, im), 'wb') as outputFile:
            cmd = ["zgrep", "-w", '{}[0-9]'.format(im), 'tsuanlo.txt.gz']
            proc = subprocess.run(
                cmd, stderr=stderr, stdout=outputFile, check=True)


def getThongKePio():
    #
    # 語料庫目前有的音節數量
    #
    with open('../Sui-Siann-Dataset/統計全部音節.json', 'r', encoding='utf-8') as file:
        return json.load(file)


if __name__ == '__main__':
    main()
