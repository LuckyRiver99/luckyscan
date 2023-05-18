# -*- coding: utf-8 -*-

from poc import core
def check(url):
	name= 'druid未授权访问'
	core.start_echo(name)
	use = ["/druid/index.html", "/druid/sql.html", "/druid/weburi.html", "/druid/websession.html", "/druid/weburi.json",
		   "/druid/websession.json",
		   "/druid/login.html", "/system/druid/login.html", "/webpage/system/druid/login.html",
		   "/system/druid/index.html", "/system/druid/sql.html", "/system/druid/weburi.html",
		   "/system/druid/websession.html", "/system/druid/weburi.json", "/system/druid/websession.json",
		   "/webpage/druid/index.html", "/webpage/druid/sql.html", "/webpage/druid/weburi.html",
		   "/webpage/druid/websession.html", "/webpage/druid/weburi.json", "/webpage/druid/websession.json"]
	for i in range(0,21):
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


# use = ["/v2/api-docs", "/swagger-ui.html", "/swagger", "/api/swagger", "/Swagger/ui/index", "/api/swaggerui",
# 	   "/swagger/ui", "/api/swagger/ui", "/api/swagger-ui.html", "/user/swagger-ui.html", "/libs/swaggerui",
# 	   "/swagger/index.html", "/swagger-resources/configuration/ui", "/swagger-resources/configuration/security",
# 	   "/api.html", "/druid/index.html", "/sw/swagger-ui.html", "/api/swagger-ui.html", "/template/swagger-ui.html",
# 	   "/spring-security-rest/api/swagger-ui.html", "/spring-security-oauth-resource/swagger-ui.html",
# 	   "/swagger/v1/swagger.json", "/swagger/v2/swagger.json", "/api-docs", "/api/doc", "/docs/", "/doc.html",
# 	   "/v1/api-docs", "/v3/api-docs"]
# path=use[0]
# print(path)