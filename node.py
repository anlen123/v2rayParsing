#!/root/miniconda3/bin/python
# -*- coding: utf-8 -*- 
from main import *
link = ""
with open('node') as f :
    link = f.read().strip()
switchNode(link)
print("切换节点成功")
