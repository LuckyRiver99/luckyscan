# -*- coding: utf-8 -*-

from poc import core
def check(url):
	name='SFTP未授权访问'
	core.start_echo(name)
	use = ["/.vscode/sftp.json"]
	for i in range(0,1):
		path=use[i]
		r=core.get(url,path)
		if r:
			if r.status_code==200 or r.status_code==302:
				core.end_echo(name,'Payload：'+url+'/'+path)
				core.result(name,url+'/'+path)
			else:
				# core.end_echo(name)
				pass
		else:
			core.end_echo(name)


# use = ["/v2/api-docs", "/swagger-ui.html", "/swagger", "/api/swagger", "/Swagger/ui/index", "/api/swaggerui",
# 	   "/swagger/ui", "/api/swagger/ui", "/api/swagger-ui.html", "/user/swagger-ui.html", "/libs/swaggerui",
# 	   "/swagger/index.html", "/swagger-resources/configuration/ui", "/swagger-resources/configuration/security",
# 	   "/api.html", "/druid/index.html", "/sw/swagger-ui.html", "/api/swagger-ui.html", "/template/swagger-ui.html",
# 	   "/spring-security-rest/api/swagger-ui.html", "/spring-security-oauth-resource/swagger-ui.html",
# 	   "/swagger/v1/swagger.json", "/swagger/v2/swagger.json", "/api-docs", "/api/doc", "/docs/", "/doc.html",
# 	   "/v1/api-docs", "/v3/api-docs"]
# path=use[0]
# print(path)