import json
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 看無聲調的音節 import ko_pio
from 看無聲調的音節 import suisiann_pio


def main():
    ko = siannun(ko_pio())
    suisiann = siannun(suisiann_pio())
    tsha = ko - suisiann
    print(
        json.dumps(
            sorted(tsha),
            ensure_ascii=False,
            sort_keys=True,
            indent=2,
        )
    )

def siannun(pio):
    kiatko=set()
    for lmj in pio:
        tl=臺灣閩南語羅馬字拼音(lmj)
        kiatko.add(tl.聲)
        kiatko.add(tl.韻)
    return kiatko
if __name__ == '__main__':
    main()
