#/usr/bin/env python
import json
import yaml

#create a list
list = [range(7), {'ip':'10.0.0.1', 'mask':'255.255.255.0', 'attributes':['test1', 'test2', 'test3']}]
print list

with open("mylist.yml", "w") as f:
	f.write(yaml.dump(list, default_flow_style=False))
f.close()

with open("mylist.json", "w") as f:
	json.dump(list, f)
f.close()

