# -*- coding: utf-8 -*-

from poc import core
def check(url):
	name= '普罗米修斯未授权访问'
	core.start_echo(name)
	use = ["/info.php", "/phpinfo.php","/PhpInfo.php","/1.php","/readme.txt","/wp-json/wp/v2/users","/../../servlet/OutputCode?path=Ix1E5Anj26gg4vfnak8pSKVU3Fi5TGhY","/doc.html","/pmh/doc.html","/?rest_route=/wp/v2/users","/?author=1"]
	for i in range(0,11):
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

