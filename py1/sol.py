#nc 115.68.30.145 8080
#http://apply.sejongssg.kr/py/py1.py 
table = [249, 61, 48, 21, 201, 231, 131, 137, 208, 163, 117, 215, 62, 112, 70, 141, 90, 239, 191, 250, 16, 239, 84, 230, 137, 109, 182, 184, 132, 185, 101, 211, 229, 28, 69, 46, 220, 150, 220, 215, 188, 132, 242, 193, 85, 68, 156, 243, 173, 51, 107, 30, 158, 75, 116, 44, 216, 250, 164, 144, 149, 227, 133, 38, 101, 74, 231, 81, 125, 167, 247, 32, 236, 88, 8, 0, 113, 214, 3, 14, 140, 50, 33, 185, 130, 223, 240, 254, 215, 253, 123, 166, 86, 31, 14, 179, 195, 165, 157, 25, 127, 216, 219, 103, 220, 45, 60, 158, 18, 251, 27, 67, 105, 230, 52, 30, 139, 216, 239, 148, 180, 209, 78, 104, 165, 96, 103, 148, 102, 120, 102, 236, 119, 159, 165, 234, 244, 0, 70, 7, 220, 113, 81, 75, 45, 251, 106, 216, 53, 172, 96, 141, 40, 33, 85, 144, 129, 116, 191, 243, 137, 26, 91, 78, 197, 196, 141, 129, 144, 85, 200, 74, 206, 63, 61, 48, 206, 117, 162, 200, 235, 203, 87, 218, 44, 206, 134, 35, 248, 4, 158, 22, 151, 83, 51, 50, 57, 210, 29, 177, 217, 192, 23, 14, 205, 186, 197, 228, 239, 236, 145, 119, 93, 126, 189, 255, 240, 171, 94, 117, 103, 128, 138, 158, 99, 197, 189, 134, 122, 105, 152, 251, 207, 87, 155, 65, 169, 50, 190, 2, 135, 237, 34, 100, 186, 65, 231, 165, 133, 50, 167, 139, 134, 50, 45, 41, 20, 248, 107, 207, 80, 92, 194, 243, 153, 165, 118, 112, 209, 73, 142, 34, 99, 129, 42, 23, 239, 42, 163, 253, 238, 166, 16, 85, 244, 38, 193, 22, 125, 48, 52, 128, 218, 23, 142, 44, 157, 76, 113, 171]

ans2 = '430ff24e628858cd8f8acc64269a51b27c135450eaae64fb4bf92105c38e'
#ans2 = [ans2[i:i+2] for i in xrange(0, len(ans2), 2)][::-1]

ans3 = 'c88d4d5b72b087e1fbb9dc18b4540529fb299cd88d'
#ans3 = [ans3[i:i+2] for i in xrange(0, len(ans3), 2)][::-1] #reverse ans3

def encoding(str1):
    result = ''

    for i in xrange(len(str1)):
        result += chr(ord(str1[i]) ^ int(table[i*-1]))
    return result[::-1].encode('hex')

def encoding1(str1):
    result = ''
    for i in xrange(len(str1)):
        result += chr(ord(str1[::-1][i]) ^ int(table[::-1][i*-1]))
    result1 = ''
    for i in xrange(len(result)):
        if ord(result[i]) > 0x90:
            result1 += chr(ord(result[i])+1)
        else:
            result1 += chr(ord(result[i])-1)
    return result1.encode('hex')

#pwd2 pass
ans3 = 'c88d4d5b72b087e1fbb9dc18b4540529fb299cd88d'
ans3 = [ans3[i:i+2] for i in xrange(0, len(ans3), 2)][::-1] #reverse ans3

result = ''
for i in xrange(len(ans2)):
    result += chr(int(ans2[i], 16) ^ table[i*-1])
#print "pwd2: " + result

#pwd2 other pass
pass2 = '430ff24e628858cd8f8acc64269a51b27c135450eaae64fb4bf92105c38e'
result = ''
pass2 = pass2.decode('hex')[::-1]
for i in xrange(len(pass2)):
    result += chr(ord(pass2[i]) ^ int(table[-i]))
print result

#pwd3 pass
ans3 = 'c88d4d5b72b087e1fbb9dc18b4540529fb299cd88d'
ans3 = ans3.decode('hex')

result = ''
for i in xrange(len(ans3)):
    if ord(ans3[i]) > 0x90:
        result += chr(ord(ans3[i])-1)
    else:
        result += chr(ord(ans3[i])+1)

result1 = ''
for i in xrange(len(result)):
    result1 = chr(ord(result[i]) ^ int(table[::-1][-i])) + result1

print result1

#test case
ans3 = encoding1('abc')
print ans3
print len(ans3)
ans3 = ans3.decode('hex')
print len(ans3)
result = ''
for i in xrange(len(ans3)):
    if ord(ans3[i]) > 0x90:
        result += chr(ord(ans3[i])-1)
    else:
        result += chr(ord(ans3[i])+1)

result1 = ''
for i in xrange(len(result)):
   result1 += chr(ord(result[i]) ^ int(table[::-1][-i]))
print 'test: ' + result1[::-1]

"""
A = B ^ C

B = A ^ C


chr <> ord=order
result += chr(ord(str[::-1][i])^int(table[::-1][i*-1]))



ord(result) = ord(str[::-1][i] ^ int(table)

ord(str[::-1][i] = ord(result) ^ int(table)

result1[i] = str[::-1][i] = chr(ord(result[i]) ^ int(table[::-1][-i]))





result = str[::-1]

"""

