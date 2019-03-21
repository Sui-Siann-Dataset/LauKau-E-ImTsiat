#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import re

txt_bun = sys.argv[1]

wrapper = """<!DOCTYPE html><html>
    <head>
    <meta charset="utf-8"/>
    <title>Un2-gian5 lun5-bun5</title>
    <style>
    p {{margin-top:1.2rem;margin-bottom:1.2rem;font-family:"HanaMinB","HanaMinA","WenQuanYi Micro Hei";}}
    .han{{font-size:13pt; font-family:'jf-jinxuan-Medium';}}
    .lo {{font-size:10pt; font-family:'jf-jinxuan-Book';}}
    </style>
    </head>
    <body>{}</body>
    </html>"""

kiat_ko = ""

# Tak8 txt
with open(txt_bun, 'r') as txt_tong2:
    han = []
    lo = []
    countHanLo = 0

    for tsua in txt_tong2:
        #print(tsua)
        if tsua[0] in '（[':
            kiat_ko += "<p class='lo'>{}</p>".format(''.join(tsua))
        elif re.findall(r'[\u4e00-\u9fff]+', tsua):
        #elif () or ('，' in tsua) or ('。' in tsua):
            kiat_ko += "<p class='han'>{}</p>".format(''.join(tsua))
        elif tsua.strip() == '':
            kiat_ko += "<br/>"
        else:
            kiat_ko += "<p class='lo'>{}</p>".format(''.join(tsua))

# In3 html
with open('output.html', 'w') as html_tong2:
    print(wrapper.format(kiat_ko), file=html_tong2)
    #html_tong2.write(wrapper.format(kiat_ko))
