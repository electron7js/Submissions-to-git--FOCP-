from sys import argv

if __name__ == "__main__":
    if len(argv) > 1:
        try:
            with open("words.txt") as wordfile:
                wordslist=wordfile.read().split("\n")
            with open(argv[1]) as current_file:
                cf=current_file.readlines()
                inp=(list(filter(lambda a:a!="",(' '.join((''.join(cf).split("\n"))).split(" ")))))
                for x in inp:
                    if x not in wordslist:
                        print(x)
        except FileNotFoundError:
            print("The file given was not found")

    else:
        print("Error: no file input")
