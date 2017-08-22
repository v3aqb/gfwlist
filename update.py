#!/usr/bin/env python
# coding:utf-8

import sys
import os
import base64

os.chdir(os.path.dirname(os.path.abspath(__file__).replace('\\', '/')))

more = '''
!########### v3aqb addon ##########
||google.ae
||google.as
||google.am
||google.at
||google.az
||google.ba
||google.be
||google.bg
||google.cat
||google.cd
||google.ci
||google.co.id
||google.co.jp
||google.co.kr
||google.co.ma
||google.co.uk
||google.com
||google.de
||google.dj
||google.dk
||google.es
||google.fi
||google.fm
||google.fr
||google.gg
||google.gl
||google.gr
||google.ie
||google.is
||google.it
||google.jo
||google.kz
||google.lv
||google.mn
||google.ms
||google.nl
||google.nu
||google.no
||google.ro
||google.ru
||google.rw
||google.sc
||google.sh
||google.sk
||google.sm
||google.sn
||google.tk
||google.tm
||google.to
||google.tt
||google.vu
||google.ws
'''

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
