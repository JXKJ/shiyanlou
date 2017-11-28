#!/usr/bin/env python3
import json

def _read_title(paths):
	titel_list = list()
	for path in paths:
		with open(path,'r') as file:
			jsonStr=json.loads(file.read())
			titel_list.append(jsonStr['title'])
	return titel_list

def _read_file(path):
	with open(path,'r') as file:
		jsonStr=json.loads(file.read())
	return jsonStr

if __name__ =='__main__':
	paths=['../files/helloworld.json','../files/helloshiyanlou.json']
	titles=_read_file('../files/helloworld.json')
	print(titles)