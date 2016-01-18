#/usr/bin/env python

import yaml
import json
from pprint import pprint as pp

with open("mylist.yml") as f:
	yaml_list = yaml.load(f)

print "yaml list:"
#print yaml_list
pp(yaml_list)

with open("mylist.json") as f:
	json_list = json.load(f)

print "json list:"
#print json_list
pp(json_list)
