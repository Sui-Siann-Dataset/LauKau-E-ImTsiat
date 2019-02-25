import json


def main():
    pio = ko_pio()
    suisiann = suisiann_pio()
    tsha = pio - suisiann
    print(
        json.dumps(
            sorted(tsha),
            ensure_ascii=False,
            sort_keys=True,
            indent=2,
        )
    )


def ko_pio():
    pio = set()
    with open('Ko-kuelih_imtsiat.txt', encoding='utf-8') as tong:
        for tsua in tong.readlines():
            pio.add(tsua.rstrip())
    return pio


def suisiann_pio():
    with open('suisiann.json', encoding='utf-8') as tong:
        return set(json.load(tong)['無聲調'])


if __name__ == '__main__':
    main()
