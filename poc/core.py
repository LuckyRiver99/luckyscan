# -*- coding: utf-8 -*-

import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def result(name,payload,info=None):
	f=open('result.txt','a')
	if info:
		f.write(name+':    '+payload+'    '+info+'\n')
	else:
		f.write(name+':    '+payload+'\n')
	f.close()

def start_echo(name):
	print('\033[34m[#]check:{}\033[0m'.format(name))

def end_echo(name,payload=None):
	if payload:
		print('\033[32m[#]存在{}\033[0m'.format(name))
		print('\033[32m[#]{}\033[0m'.format(payload))
		print('\033[34m----------------------------------------------------\033[0m')
	else:
		print('\033[34m[#]不存在{}\033[0m'.format(name))
		print('\033[34m----------------------------------------------------\033[0m')
		pass


def post(url,path,header,data,files=None):
	url = url+'/'+path
	try:
		if files:
			# r=requests.post(url=url,data=data,headers=header,files=files,timeout=3)
			r = requests.post(url=url, data=data, headers=header, files=files, timeout=3, verify=False)
			return r
		else:
			# r=requests.post(url=url,data=data,headers=header,timeout=3)
			r = requests.post(url=url, data=data, headers=header, timeout=3, verify=False)
			return r
	except Exception as e:
		pass

def get(url,path):
	url = url+'/'+path
	header = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',}
	try:
		# r=requests.get(url=url,timeout=3)

		r = requests.get(url=url, headers=header,timeout=3, verify=False)
		return r
	except Exception as e:
		pass
