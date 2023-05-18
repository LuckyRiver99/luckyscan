# -*- coding: utf-8 -*-

from poc import core
def check(url):
	name= 'spring未授权访问'
	core.start_echo(name)
	use = ["article?id=${7*7}","actuator","actuator/auditLog","actuator/auditevents","actuator/autoconfig","actuator/beans","actuator/caches","actuator/conditions","actuator/configurationMetadata","actuator/configprops","actuator/dump","actuator/env","actuator/events","actuator/exportRegisteredServices","actuator/features","actuator/flyway","actuator/health","actuator/healthcheck","actuator/httptrace","actuator/hystrix.stream","actuator/info","actuator/integrationgraph","actuator/jolokia","actuator/logfile","actuator/loggers","actuator/loggingConfig","actuator/liquibase","actuator/metrics","actuator/mappings","actuator/scheduledtasks","actuator/swagger-ui.html","actuator/prometheus","actuator/refresh","actuator/registeredServices","actuator/releaseAttributes","actuator/resolveAttributes","actuator/scheduledtasks","actuator/sessions","actuator/springWebflow","actuator/shutdown","actuator/sso","actuator/ssoSessions","actuator/statistics","actuator/status","actuator/threaddump","actuator/trace","auditevents","autoconfig","api.html","api/index.html","api/swagger","api/swagger/ui","api/swagger-ui.html","api/v2/api-docs","api/actuator","api-docs","beans","caches","cloudfoundryapplication","conditions","configprops","distv2/index.html","docs","druid/index.html","druid/login.html","druid/websession.html","dubbo-provider/distv2/index.html","dump","entity/all","env","env/(name)","eureka","flyway","gateway/actuator","gateway/actuator/auditevents","gateway/actuator/beans","gateway/actuator/conditions","gateway/actuator/configprops","gateway/actuator/env","gateway/actuator/health","gateway/actuator/httptrace","gateway/actuator/hystrix.stream","gateway/actuator/info","gateway/actuator/jolokia","gateway/actuator/logfile","gateway/actuator/loggers","gateway/actuator/mappings","gateway/actuator/metrics","gateway/actuator/scheduledtasks","gateway/actuator/swagger-ui.html","gateway/actuator/threaddump","gateway/actuator/trace","health","heapdump","heapdump.json","httptrace","hystrix","h2-console","htcim/swagger/swagger-ui.html","info","integrationgraph","jolokia","jolokia/list","jeecg-boot/actuator/metrics","libs/swaggerui","liquibase","list","logfile","loggers","liquibase","metrics","mappings","monitor","prometheus","product/list","refresh","scheduledtasks","sessions","shutdown","society/olap/doc.html","spring-security-oauth-resource/swagger-ui.html","spring-security-rest/api/swagger-ui.html","static/swagger.json","sw/swagger-ui.html","swagger","swagger/codes","swagger/index.html","swagger/static/index.html","swagger/swagger-ui.html","swagger-dubbo/api-docs","swagger-ui","swagger-ui.html","swagger-ui/html","swagger-ui/index.html","swagger/ui/index","swagger/v1/swagger.json","swagger/v2/swagger.json","swagger/v3/swagger.json","swagger-resources/configuration/ui","swagger-resources/configuration/security","system/druid/index.html","threaddump","template/swagger-ui.html","trace","user/swagger-ui.html","version","v1.1/swagger-ui.html","v1.2/swagger-ui.html","v1.3/swagger-ui.html","v1.4/swagger-ui.html","v1.5/swagger-ui.html","v1.6/swagger-ui.html","v1.7/swagger-ui.html","/v1.8/swagger-ui.html","/v1.9/swagger-ui.html","/v2.0/swagger-ui.html","v2.1/swagger-ui.html","v2.2/swagger-ui.html","v2.3/swagger-ui.html","v2/swagger.json","v1/api-docs","v3/api-docs","v2/api-docs","webpage/system/druid/index.html","%20/swagger-ui.html","/actuator/heapdump;.css","/api/blade-user/user-list"]
	for i in range(0,167):
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