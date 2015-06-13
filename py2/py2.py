from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from socket import *
import threading
import time

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[0:-ord(s[-1])]

flag = "blind"

def s256(message):
	hash = SHA256.new()
	hash.update(message)
	result = hash.hexdigest()
	return result

def recv_(s):
	obj = AES.new('mbn9wngjuwmwgo3_', AES.MODE_CBC, 'key_is_flaggg999')
	a = s.recv(2048)
	a = unpad(obj.decrypt(a))
	return a

def tmain(s):
	admin_id = "sweetchip"
	admin_pw = "d623500cb17fab3f66314e1d4023ab31422098bc4ce47f4bc2a0d828ee16c048"

	guest_id = "guest"
	guest_pw = "3a37914287db9391891e4a335fa71d024652c076b98f63212820c72eae29139f"

	cookie = "59e5baa57f0556df3416d024bb43ad7b77a90038aeafad310be5fdb23e34a084"

	s.send("Pyton Challenge - Admin area.\n")
	s.send("Login\nID : ")
	i_id = recv_(s)

	s.send("\nPassword : ")
	i_pw = recv_(s)

	s.send("\nToken : ")
	i_to = recv_(s)

	i_pw = s256(i_pw)
	i_to = s256(i_to)

	i_result = i_id	+"|"+ i_pw +"|"+ i_to

	buf = i_result.split('|')

	if buf[0] == admin_id:
		if buf[1] == admin_pw:
			if buf[2] == cookie:
				s.send("Hello admin! Key is \n"+flag)
	elif buf[0] == guest_id:
		if buf[1] == guest_pw:
			if buf[2] == cookie:
				s.send("You are Guest! Good bye.")

	s.close()

if __name__ == '__main__':
	ip = "0.0.0.0"
	port = 8081

	ss = socket(AF_INET, SOCK_STREAM)

	ss.bind((ip, port))
	ss.listen(6)

	while 1:
		s, sss = ss.accept()
		threading._start_new_thread(tmain,(s,))


