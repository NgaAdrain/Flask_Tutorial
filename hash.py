import hashlib
psd = str(hashlib.sha1(b'1'))[-19:-1]
print(psd)
a = bytes(str(input()),'utf-8')
b = b'1'
print(type(a))
print(type(b))
psd_inp = str(hashlib.sha1(a))[-19:-1]
print(psd_inp)
print(psd == psd_inp)