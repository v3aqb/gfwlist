#!/usr/bin/env python
# coding:utf-8

import sys
import os
import base64

os.chdir(os.path.dirname(os.path.abspath(__file__).replace('\\', '/')))

more = '''
!########### v3aqb addon ##########
'''

for ntd in 'ac|ad|ae|af|al|am|as|at|az|ba|be|bf|bg|bi|bj|bs|bt|by|ca|cat|cd|cf|cg|ch|ci|cl|cm|co.ao|co.bw|co.ck|co.cr|co.id|co.il|co.in|co.jp|co.ke|co.kr|co.ls|co.ma|com|com.af|com.ag|com.ai|com.ar|com.au|com.bd|com.bh|com.bn|com.bo|com.br|com.bz|com.co|com.cu|com.cy|com.do|com.ec|com.eg|com.et|com.fj|com.gh|com.gi|com.gt|com.hk|com.jm|com.kh|com.kw|com.lb|com.ly|com.mm|com.mt|com.mx|com.my|com.na|com.nf|com.ng|com.ni|com.np|com.om|com.pa|com.pe|com.pg|com.ph|com.pk|com.pr|com.py|com.qa|com.sa|com.sb|com.sg|com.sl|com.sv|com.tj|com.tr|com.tw|com.ua|com.uy|com.vc|com.vn|co.mz|co.nz|co.th|co.tz|co.ug|co.uk|co.uz|co.ve|co.vi|co.za|co.zm|co.zw|cv|cz|de|dj|dk|dm|dz|ee|es|eu|fi|fm|fr|ga|ge|gg|gl|gm|gp|gr|gy|hk|hn|hr|ht|hu|ie|im|iq|is|it|it.ao|je|jo|kg|ki|kz|la|li|lk|lt|lu|lv|md|me|mg|mk|ml|mn|ms|mu|mv|mw|mx|ne|nl|no|nr|nu|org|pl|pn|ps|pt|ro|rs|ru|rw|sc|se|sh|si|sk|sm|sn|so|sr|st|td|tg|tk|tl|tm|tn|to|tt|us|vg|vn|vu|ws'.split('|'):
    more += '||google.%s\n' % ntd


if sys.version_info > (3, 0):
    raw_input = input

try:
    import urllib2
except ImportError:
    import urllib.request as urllib2
try:
    print('downloading gfwlist')
    r = urllib2.urlopen('https://raw.githubusercontent.com/gfwlist/gfwlist/master/gfwlist.txt')
except Exception as e:
    print(repr(e))
else:
    data = r.read()
    if r.getcode() == 200 and data:
        if b'!' not in data:
            data = b''.join(data.split())
            data = base64.b64decode(data).decode()
        with open('./gfwlist.txt', 'w') as localfile:
            localfile.write(data)
            localfile.write(more)

raw_input('press Enter to exit...')
