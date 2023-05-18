# from poc import core
from poc import core
def check(url):
	name='xxe'
	core.start_echo(name)

	use = ["/services/HrpService"]
	header = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36', }
	for i in range(0,1):
		path=use[i]
		r = core.get(url, path)
		#
		# m = url + path
		# print(m)
		# r = requests.get(url=m,headers=header,timeout=3, verify=False)
		# print(r.status_code)
		if r:
			if r.status_code==200:
				core.end_echo(name,'Payload：'+url+'/'+path)
				core.result(name,url+'/'+path)
				# print('yes')
			else:
				# core.end_echo(name)
				pass
		else:
			# rm = requests.get(url=m)
			# if rm.status_code == 200:
			#
			# 	print('cuowu')
			core.end_echo(name)
# url = "https://gccrc.wsjkw.zj.gov.cn:8081"
# check(url)
#
# header = {
# 	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36', }
# url222 = 'https://gccrc.wsjkw.zj.gov.cn:8081//crmapi/metrics'
# rmm = requests.post(url=url222,headers=header,timeout=3, verify=False)
# print(rmm.status_code)