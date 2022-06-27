import magic
import glob

print(magic.from_file("file1"))
print(magic.from_file("file2.txt"))
print(magic.from_file("file3"))

# filenames = glob.glob("Lab2_download_1/*.*")
# for filename in filenames:
#     print(magic.from_file(filename))
