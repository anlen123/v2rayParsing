import json 
with open("config.json") as f :
    txt = f.read()
    config  = json.loads(txt)

with open("node.json") as f :
    txt = f.read()
    new_node  = json.loads(txt)['outbounds']
config['outbounds'] = new_node 
with open("config.json","w") as f :
    json.dump(config,f, ensure_ascii=False)
