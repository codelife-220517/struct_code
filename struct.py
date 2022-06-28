import struct
"""struct demo1
{
    unsigned char   byProtocol;
    int             nRetCode;
    char            szAccount[80];
    char            szRandomKey[50];
}"""

f = open('hahaha2.txt', 'rb')
res = f.read(135)
#print(res)
a, b, c, d = struct.unpack('=Bi10s70x30s20x', res)
print(a, b, c.decode(), d.decode())

f2 = open('hahaha.txt', 'rb')
res2 = f2.read(44)
#print(res2)
a2 = struct.unpack('<H10i', res2)
print(a2)


f3 = open('g2cSendServerListRespond.txt', 'rb')
res3 = f3.read(132)
#print(res3)
a3 = struct.unpack('<HBhi0BIIB32sIIB32sIIB32s', res3)
print(a3[0], a3[1], a3[2],a3[3])
print(a3[4], a3[5], a3[6],a3[7].decode('UTF-8', errors='ignore'))
print(a3[8], a3[9], a3[10], a3[11].decode('UTF-8', errors='ignore'))
print(a3[12], a3[13], a3[14], a3[15].decode('UTF-8', errors='ignore'))


f4 = open('pb.txt', 'rb')
res4 = f4.read(679)
#print(res4)
a4 = struct.unpack('<Hi2x42s1x32s2x40s3x19s8x472s1x51s', res4)
print(a4[0], a4[1])
print(a4[2].decode())
print(a4[3].decode('utf-8', errors='ignore'))
print(a4[4].decode('utf-8', errors='ignore'))
print(a4[5].decode('utf-8', errors='ignore'))
print(a4[6].decode('utf-8', errors='ignore'))
print(a4[7].decode('utf-8', errors='ignore'))
