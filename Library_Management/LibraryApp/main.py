import hashlib
import binascii
import os

def binary_search(fname, search_key):
	t = []
	fin = open(fname,'r')
	for lx in fin:
		lx = lx.rstrip()
		wx = lx.split('|')
		t.append((wx[0], wx[1]))
	fin.close()
	l = 0
	r = len(t) - 1
	while l <= r:
		mid = (l + r)//2
		if t[mid][0] == search_key:
			return int(t[mid][1])
		elif t[mid][0] <= search_key:
			l = mid + 1
		else:
			r = mid - 1
	return -1


def key_sort(fname):
	t=list()
	fin=open(fname,'r')
	for line in fin:
		line=line.rstrip('\n')
		words=line.split('|')
		t.append((words[0],words[1]))
	fin.close()
	t.sort()
	with open("temp.txt",'w') as fout:
		for pkey,addr in t:
			pack=pkey+"|"+addr+"|#"
			fout.write(pack+'\n')
	os.remove(fname)
	os.rename("temp.txt",fname)

def verify_password(stored_password, provided_password):
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512',
                                  provided_password.encode('utf-8'),
                                  salt.encode('ascii'),
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password

def hash_password(password):
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')


