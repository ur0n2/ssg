from socket import *
import threading
import time


table = [249, 61, 48, 21, 201, 231, 131, 137, 208, 163, 117, 215, 62, 112, 70, 141, 90, 239, 191, 250, 16, 239, 84, 230, 137, 109, 182, 184, 132, 185, 101, 211, 229, 28, 69, 46, 220, 150, 220, 215, 188, 132, 242, 193, 85, 68, 156, 243, 173, 51, 107, 30, 158, 75, 116, 44, 216, 250, 164, 144, 149, 227, 133, 38, 101, 74, 231, 81, 125, 167, 247, 32, 236, 88, 8, 0, 113, 214, 3, 14, 140, 50, 33, 185, 130, 223, 240, 254, 215, 253, 123, 166, 86, 31, 14, 179, 195, 165, 157, 25, 127, 216, 219, 103, 220, 45, 60, 158, 18, 251, 27, 67, 105, 230, 52, 30, 139, 216, 239, 148, 180, 209, 78, 104, 165, 96, 103, 148, 102, 120, 102, 236, 119, 159, 165, 234, 244, 0, 70, 7, 220, 113, 81, 75, 45, 251, 106, 216, 53, 172, 96, 141, 40, 33, 85, 144, 129, 116, 191, 243, 137, 26, 91, 78, 197, 196, 141, 129, 144, 85, 200, 74, 206, 63, 61, 48, 206, 117, 162, 200, 235, 203, 87, 218, 44, 206, 134, 35, 248, 4, 158, 22, 151, 83, 51, 50, 57, 210, 29, 177, 217, 192, 23, 14, 205, 186, 197, 228, 239, 236, 145, 119, 93, 126, 189, 255, 240, 171, 94, 117, 103, 128, 138, 158, 99, 197, 189, 134, 122, 105, 152, 251, 207, 87, 155, 65, 169, 50, 190, 2, 135, 237, 34, 100, 186, 65, 231, 165, 133, 50, 167, 139, 134, 50, 45, 41, 20, 248, 107, 207, 80, 92, 194, 243, 153, 165, 118, 112, 209, 73, 142, 34, 99, 129, 42, 23, 239, 42, 163, 253, 238, 166, 16, 85, 244, 38, 193, 22, 125, 48, 52, 128, 218, 23, 142, 44, 157, 76, 113, 171]

def get_file_contents(filename):
	f = open(filename , "rb")
	result = f.read()
	f.close()
	return result

def getkey():
	return get_file_contents("key.txt")

def encoding(str):
	result = ""

	for i in range(0, len(str)):
		result += chr(ord(str[i])^int(table[i*-1]))
	return result[::-1].encode("hex")

def encoding1(str):
	result = ""
	for i in range(0, len(str)):
		result += chr(ord(str[::-1][i])^int(table[::-1][i*-1]))
	result1 = ""
	for i in range(0, len(result)):
		if ord(result[i]) > 0x90:
			result1 += chr(ord(result[i])+1)
		else:
			result1 += chr(ord(result[i])-1)
	return result1.encode("hex")

def tmain(s):
	a = False
	b = False
	c = False
	s.send("MAX password length : 250byte\n")
	s.send("key Example : key{this_is_key} => this_is_key\n")
	s.send("First Password : \n")
	pwd1 = s.recv(2048)
	if len(pwd1) >= 250:
		s.send("max length : 250byte\n")
		s.close()
	if pwd1.replace("\x0a", "") == "h3l1ow0r!d":
		s.send("Second Password : \n")
		pwd2 = s.recv(2048)
		if encoding(pwd2.replace("\x0a", "")) == "430ff24e628858cd8f8acc64269a51b27c135450eaae64fb4bf92105c38e":
			s.send("Third Password : \n")
			pwd3 = s.recv(2048)
			if encoding1(pwd3.replace("\x0a", "")) == "c88d4d5b72b087e1fbb9dc18b4540529fb299cd88d":
				s.send("Congretualtion! the password is.....\n")
				time.sleep(3)
				s.send(getkey())

	else:
		print pwd1.encode("hex")
	s.close()
if __name__ == '__main__':
	ip = "0.0.0.0"
	port = 8080

	ss = socket(AF_INET, SOCK_STREAM)

	ss.bind((ip, port))
	ss.listen(6)

	while 1:
		s, sss = ss.accept()
		threading._start_new_thread(tmain,(s,))
