import json
from 看無聲調的音節 import ko_pio
import subprocess
from sys import stderr
from tauphahji_cmd import tàuphahjī, liânKù
from asyncio.subprocess import PIPE
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器


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


def getImTsiatWithNumber(imTsiatArr, times):
    return sorted([i for i in imTsiatArr if imTsiatArr[i] == times])


def execGrep(im):
    #     cmd = ["zgrep", "-w", '{}[0-9]'.format(im), 'tsuanlo.txt.gz']
    cmd = ["grep", "-w", '{}[0-9]'.format(im), 'tsuanlo.txt']
    proc = subprocess.Popen(
        cmd, stdout=PIPE, stderr=subprocess.DEVNULL)
    outs, _errs = proc.communicate()
    return outs.splitlines()


def writeGrep(逐个音節的數量表, 指定數量):
    #
    # 撈出有遮濟擺的音節
    #
    arr = getImTsiatWithNumber(逐个音節的數量表, 指定數量)
    #
    # 撈出佇教會公報有這个音節的句
    #
    for im in arr:
        輸出句數 = 0
        句墩 = execGrep(im)
        print('{}, len={}'.format(im, len(句墩)))
        with open('統計/{}_{}.txt'.format(指定數量, im), 'w') as outputFile:
            for linebyte in 句墩:
                POJ = linebyte.decode('utf-8')
                # 斷長句
                章物件 = 拆文分析器.建立章物件(POJ)
                
                for 句物件 in 章物件.內底句:
                    句型 = 句物件.看型('-', ' ')
                    # 含此音的子句
                    if im in 句型:
                        try:
                            鬥拍字 = tàuphahjī(句型)
                            print('句型=', 句型)
                            print('鬥拍字=', 鬥拍字)
                            漢字 = liânKù(鬥拍字['多元書寫'], '漢字')
                            臺羅 = liânKù(鬥拍字['多元書寫'], '臺羅')
                        except KeyError:
                            漢字 = 鬥拍字['分詞']
                            臺羅 = 句型
                        except Exception:
                            print('tauphahji error, POJ=', 句型, '=')
                        print('{}\n{}\n{}\n'.format(
                            句型, 漢字, 臺羅), file=outputFile)
                        輸出句數 += 1
                if 輸出句數 > 200:
                    break


# def concateToGuanSuSia(toGuanArr):
#     return [i for i in ]


def getThongKePio():
    #
    # 語料庫目前有的音節數量
    #
    with open('../Sui-Siann-Dataset/統計全部音節.json', 'r', encoding='utf-8') as file:
        return json.load(file)


if __name__ == '__main__':
    main()
