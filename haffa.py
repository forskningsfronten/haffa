#!/usr/bin/env python

import json
from pprint import pprint


json_data=open("haffa.json").read()
data = json.loads(json_data)

for lang in data:
	#print lang
	for key in data[lang].keys():
		print key+": "+data[lang][key]
