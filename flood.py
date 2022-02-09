import requests, threading, random, string, names, time
from bs4 import BeautifulSoup
from tqdm import tqdm

amount = int(input('Enter amount to flood: '))
url = input('Enter url: ')
r = requests.get(url)
soup = BeautifulSoup(r.content, features="html.parser")
form = soup.find('form')
post_fname = form['action']

input1 = form.find('input', type='text')
input2 = form.find('input', type='password')
key1=input1['name']
key2=input2['name']

def flood(key1, key2):
	rmail = names.get_full_name().replace(' ','')+'@gmail.com'
	rpass = ''.join(random.choices(string.digits+string.ascii_letters,k=random.randint(8,14)))
	data = {key1:rmail,key2:rpass}
	r = requests.post(url+post_fname, data=data)

def loading(amount):
	for i in tqdm(range(0, int(amount)), desc='Flooding'):
		time.sleep(.1)

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
