import sys

count = len(sys.argv)
total = 0
check = 0
while count > 1:
    check=1
    count -= 1
    total += float(sys.argv[count])
if check:
    print("Total is", total)
    print("Average is", total/(len(sys.argv)-1))
else:
    print("no arguments were provided")