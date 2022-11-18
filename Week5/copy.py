from shutil import copyfile
from sys import argv
if len(argv)>1:
    for i in argv[1:]:
        copyfile(i,"".join(i.split(".")[0:-1])+" Copy ."+str(i.split(".")[-1]))
else:
    print("No files given")