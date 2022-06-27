import hashlib
import magic
import glob
# file1 = "test.docx" 
# file2 = "test.jpg"
# BLOCK_SIZE = 65536

# file_hash1 = hashlib.md5()
# with open(file1, 'rb') as f:
#     fb = f.read(BLOCK_SIZE)
#     while len(fb) > 0:
#         file_hash1.update(fb)
#         fb = f.read(BLOCK_SIZE)

# file_hash2 = hashlib.md5()
# with open(file2, 'rb') as f:
#     fb = f.read(BLOCK_SIZE)
#     while len(fb) > 0:
#         file_hash2.update(fb)
#         fb = f.read(BLOCK_SIZE)


# print("--test.docx--")
# print (file_hash1.hexdigest())

# print("--test.jpg--")
# print (file_hash2.hexdigest())




filenames = glob.glob("Dokaz/*.*")
for filename in filenames:
    #print(filename)
    print(filename, magic.from_file(filename))
