# -*- coding: utf-8 -*-

import os
from pyfiglet import Figlet
from optparse import OptionParser
from poc import spring,joomla,urss,phpuse,ElasticSearch,druid,bt,apache,gitlab,webmail,session_upload,getSessionList,information,sql,htmlofficeservlet,ajax,nacos,sftp

if __name__ == '__main__':
	# os.system('@echo off')
	os.system('chcp 936 >nul')
	f=Figlet(font='slant')
	print('\033[31m====================================================\033[0m')
	print('\033[34m{}\033[0m'.format(f.renderText('Swagger')))
	print('   \033[33mAuthor:LuckyRiver  ver:1.0  time:2022-06-27\033[0m')
	print('\033[31m====================================================\033[0m'+'\n')
	usage="\n"+"python3 %prog -u url"+"\n"+"python3 %prog -u url --att"+"\n"+"python3 %prog -f url.txt"+"\n"+"python3 %prog -f url.txt --att"
	parser=OptionParser(usage=usage)
	parser.add_option('-u','--url',dest='url',help="target url")
	parser.add_option('-f','--file',dest='file',help="url file")
	parser.add_option('--att',dest='attack',default=False,action='store_true',help="getshell")
	(options,args)=parser.parse_args()
	if options.file:
		f=open(options.file,'r')
		urls=f.readlines()
		for url in urls:
			url=url.strip('\n')
			sftp.check(url)
			phpuse.check(url)
			urss.check(url)
			ElasticSearch.check(url)
			druid.check(url)
			bt.check(url)
			apache.check(url)
			spring.check(url)
			joomla.check(url)
			gitlab.check(url)
			information.check(url)
			getSessionList.get_sessionlist(url)
			webmail.check(url)
			sql.run(url,options.attack)
			session_upload.get_session(url,options.attack)
			htmlofficeservlet.check(url,options.attack)
			ajax.check(url,options.attack)
			nacos.check(url)
		print('\033[34m[#]扫描已完成，结果保存至result.txt\033[0m')

	if options.url:
		sftp.check(options.url)
		spring.check(options.url)
		joomla.check(options.url)
		urss.check(options.url)
		phpuse.check(options.url)
		ElasticSearch.check(options.url)
		druid.check(options.url)
		bt.check(options.url)
		apache.check(options.url)
		gitlab.check(options.url)
		information.check(options.url)
		getSessionList.get_sessionlist(options.url)
		webmail.check(options.url)
		sql.run(options.url,options.attack)
		session_upload.get_session(options.url,options.attack)
		htmlofficeservlet.check(options.url,options.attack)
		ajax.check(options.url,options.attack)
		nacos.check(options.url)
		print('\033[34m[#]扫描已完成，结果保存至result.txt\033[0m')
