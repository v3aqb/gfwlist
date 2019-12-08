#!/usr/bin/env python
# coding:utf-8

import os
import base64
import urllib.request
import subprocess

os.chdir(os.path.dirname(os.path.abspath(__file__).replace('\\', '/')))

# pull
# print('git pull')
# subprocess.run(['git', 'pull'], check=True)

# prep
more = []

more.append('')
more.append('!########### v3aqb addon ##########')

for ntd in 'ac|ad|ae|af|al|am|as|at|az|ba|be|bf|bg|bi|bj|bs|bt|by|ca|cat|cd|cf|cg|ch|ci|cl|cm|co.ao|co.bw|co.ck|co.cr|co.id|co.il|co.in|co.jp|co.ke|co.kr|co.ls|co.ma|com|com.af|com.ag|com.ai|com.ar|com.au|com.bd|com.bh|com.bn|com.bo|com.br|com.bz|com.co|com.cu|com.cy|com.do|com.ec|com.eg|com.et|com.fj|com.gh|com.gi|com.gt|com.hk|com.jm|com.kh|com.kw|com.lb|com.ly|com.mm|com.mt|com.mx|com.my|com.na|com.nf|com.ng|com.ni|com.np|com.om|com.pa|com.pe|com.pg|com.ph|com.pk|com.pr|com.py|com.qa|com.sa|com.sb|com.sg|com.sl|com.sv|com.tj|com.tr|com.tw|com.ua|com.uy|com.vc|com.vn|co.mz|co.nz|co.th|co.tz|co.ug|co.uk|co.uz|co.ve|co.vi|co.za|co.zm|co.zw|cv|cz|de|dj|dk|dm|dz|ee|es|eu|fi|fm|fr|ga|ge|gg|gl|gm|gp|gr|gy|hk|hn|hr|ht|hu|ie|im|iq|is|it|it.ao|je|jo|kg|ki|kz|la|li|lk|lt|lu|lv|md|me|mg|mk|ml|mn|ms|mu|mv|mw|mx|ne|nl|no|nr|nu|org|pl|pn|ps|pt|ro|rs|ru|rw|sc|se|sh|si|sk|sm|sn|so|sr|st|td|tg|tk|tl|tm|tn|to|tt|us|vg|vn|vu|ws'.split('|'):
    more.append('||google.%s' % ntd)

more.append('')
more.append('!####common dns servers####')

dns_list = [
    # google
    '8.8.8.8',
    '8.8.4.4',
    # OpenDNS
    '208.67.222.222',
    '208.67.220.220',
    '208.67.222.123',
    '208.67.220.123',
    # Norton DNS
    '198.153.192.1',
    '198.153.194.1',
    # Verisign
    '64.6.64.6',
    '64.6.65.6',
    # Comodo
    '8.26.56.26',
    '8.20.247.20',
    # Cloudflare
    '1.1.1.1',
    '1.0.0.1',
]

for dns in dns_list:
    more.append('||%s' % dns)

# download / update
# proxy_handler = urllib.request.ProxyHandler({})
# opener = urllib.request.build_opener(proxy_handler)
# urlopen = opener.open
urlopen = urllib.request.urlopen

print('downloading gfwlist')
r = urlopen('https://raw.githubusercontent.com/gfwlist/gfwlist/master/gfwlist.txt', timeout=3)

data = r.read()
if r.getcode() == 200 and data:
    if b'!' not in data:
        data = b''.join(data.split())
        data = base64.b64decode(data).decode()
    with open('./gfwlist.txt', 'w') as localfile:
        localfile.write(data)
        for line in more:
            localfile.write(line + '\n')

# check file change

result = subprocess.check_output(['git', 'status', '-s'])
changed = b'gfwlist.txt' in result

# commit / push

if changed:
    subprocess.run(['git', 'add', 'gfwlist.txt'], check=True)
    subprocess.run(['git', 'commit', '-m', "update gfwlist (auto)"], check=True)
    subprocess.run(['git', 'push'], check=True)

with open('sckey') as f:
    import requests
    sckey = f.read('sckey')
    data = {'text': 'gfwlist', 'desp': 'updated'}
    requests.post('https://sc.ftqq.com/%s.send' % sckey, data=data)
