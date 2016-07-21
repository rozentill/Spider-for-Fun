# !/usr/bin/env python
#-*- coding:utf8 -*-

import requests
import getpass
class Spider(object):

	def __init__(self):
		pass


	def get_user(self):
		self.username = raw_input('Username: ')
		self.password = getpass.getpass('Password: ')

# postdata={
# 	'username':
# }


pt = Spider()
pt.get_user()

# directory = 'Torrents'
# logFile = 'PutaoMonitor.log'
#
# cookieJar = http.cookiejar.CookieJar()
# opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookieJar))
# opener.add_headers = [('User-Agent', \
# 	'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36')]
# urllib.request.install_opener(opener)
#
# username = input('Username: ')
# password = getpass.getpass('Password: ')
#
# postdata = urllib.parse.urlencode({
# 	'username':username,
# 	'password':password,
# 	'checkcode':'XxXx',
# 	'logout':'no',
# 	'submit':'登陆'
# }).encode('utf-8')
#
# request = urllib.request.Request(url = 'https://pt.sjtu.edu.cn/takelogin.php', data = postdata)
# request.add_headers = [('User-Agent', \
# 	'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36')]
# response = urllib.request.urlopen(request)
#
# username = 0
# password = 0
# postdata = 0
#
# times = 0
#
# while True:
# 	times += 1
# 	try:
# 		print('\n\n')
# 		print(str(times))
# 		print('Checking the server...')
# 		print('Time', end = ' ')
# 		print(datetime.datetime.now())
# 		request = urllib.request.Request(url = 'https://pt.sjtu.edu.cn/torrents.php')
# 		response = urllib.request.urlopen(request)
# 		soup = BeautifulSoup(response.read(), 'html.parser')
# 		table = soup.find('table', {'class':'torrents'})
#
# 		for item in table.findAll('table', {'class':'torrentname'}):
# 			if (item.find('font', {'class':'hot'}) or item.find('font', {'class':'free'})):
# 				downloadLink = 'https://pt.sjtu.edu.cn/' + item.find('a', {'href':re.compile('^download*')})['href']
# 				filename = downloadLink[downloadLink.find('=') + 1:] + '.torrent'
# 				path = os.path.join(directory, filename)
# 				if os.path.exists(path + '.added'):
# 					continue
# 				request = urllib.request.Request(url = downloadLink)
# 				request.add_headers = [('User-Agent', \
# 					'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36')]
# 				response = urllib.request.urlopen(request)
# 				content = response.read()
# 				file = open(path, 'wb')
# 				file.write(content)
# 				file.close()
# 				print(filename + ' added.')
# 				log = open(logFile, 'a')
# 				log.write(str(datetime.datetime.now()))
# 				log.write('\t')
# 				log.write(filename + ' added.\n\n')
# 				log.close()
# 	except Exception as e:
# 		log = open(logFile, 'a')
# 		log.write(str(datetime.datetime.now()))
# 		log.write('\t')
# 		log.write(str(e))
# 		log.write('\n\n')
# 		log.close()
# 		print(str(e))
#
# 	print('Go to sleep...')
# 	time.sleep(random.randint(500, 700))
