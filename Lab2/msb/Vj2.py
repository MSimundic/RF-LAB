import hashlib

file1 = "test.txt" 
file2 = "test1.txt"
BLOCK_SIZE = 65536

file_hash1 = hashlib.sha1()
with open(file1, 'rb') as f:
    fb = f.read(BLOCK_SIZE)
    while len(fb) > 0:
        file_hash1.update(fb)
        fb = f.read(BLOCK_SIZE)

file_hash2 = hashlib.sha1()
with open(file2, 'rb') as f:
    fb = f.read(BLOCK_SIZE)
    while len(fb) > 0:
        file_hash2.update(fb)
        fb = f.read(BLOCK_SIZE)


print("--test.txt--")
print (file_hash1.hexdigest())

print("--test1.txt--")
print (file_hash2.hexdigest())

