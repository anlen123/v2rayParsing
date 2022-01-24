#!/root/miniconda3/bin/python
# -*- coding: utf-8 -*-
import json

import requests
import base64


def getShareLinks(txt) -> list:
    share_links = base64.b64decode(txt).decode("utf-8").splitlines()
    return share_links


def getV2List(url: str) -> list:
    resp = requests.get(url=url)
    orginLinks = getShareLinks(resp.text)
    links = [link for link in orginLinks if str(link).startswith("vmess://")]
    return links


def base64StrFun(base64Str: bytes) -> bytes:
    try:
        base64Str = base64.urlsafe_b64decode(base64Str)
    except:
        lens = len(base64Str)
        lenx = lens - (lens % 4 if lens % 4 else 4)
        base64Str = base64.decode(base64Str[:lenx])
    return base64Str


def parse(link: str) -> dict:
    url = link.split("://")[1]
    net = str.encode(url)
    nodeStr = bytes.decode(base64StrFun(net))
    return json.loads(nodeStr)


def switchNode(link: str):
    jsonStr = parse(link)
    print(jsonStr)
    with open("ws_tls.json") as f:
        config = json.load(f)
    config['outbounds'][0]['settings']['vnext'][0]['address'] = jsonStr['add']
    config['outbounds'][0]['settings']['vnext'][0]['port'] = int(jsonStr['port'])
    config['outbounds'][0]['settings']['vnext'][0]['users'][0]['id'] = jsonStr['id']

    if not jsonStr.get('tls', ''):
        config['outbounds'][0]['streamSettings'].pop('security')

    if not jsonStr.get('sin', ''):
        config['outbounds'][0]['streamSettings']['tlsSettings'].pop('serverName')
    else:
        config['outbounds'][0]['streamSettings']['tlsSettings']['serverName'] = jsonStr.get('sin', '')

    if not jsonStr.get('host', ''):
        config['outbounds'][0]['streamSettings']['wsSettings'].pop('headers')
    else:
        config['outbounds'][0]['streamSettings']['wsSettings']['headers']['Host'] = jsonStr.get('host', '')

    if jsonStr.get('path', ''):
        config['outbounds'][0]['streamSettings']['wsSettings']['path'] = jsonStr.get('path', '')

    with open("config.json", 'w') as f:
        json.dump(config, f, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    with open('ding.inf') as f :
        urls = f.read().split('\n')
    urls =[url for url in urls if url]
    links = []
    for url in urls:
        try:
            links+=(getV2List(url))
        except:
            print(f"{url}: 解析错误")
    for index, value in enumerate(links):
        print(f'{index + 1} : {parse(value)["ps"]}')
    node = int(input("你切换的节点: "))
    switchNode(links[node - 1])

