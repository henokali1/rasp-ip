import os
import urllib.request

name = 'green'
ip = os.popen('hostname -I').readlines()[0].replace(' \n', '')
ident = os.popen('ifconfig').readlines()[1].split(' ')[9]

d = {'ip': ip, 'name': name, 'ident': ident}
# print(d)

url = f'http://18.117.252.6:8001/save_ip?ip={ip}&name={name}&ident={ident}'
f = urllib.request.urlopen(url)
print(f.read())
