from sys import argv

if __name__ == "__main__":
    if len(argv) > 1:
        for i in argv[1:]:
            try:
                with open(i) as current_file:
                    cf=current_file.readlines()
                    print(f"\n\n\nFilename:{i}\n\n")
                    print(f"Number of lines:{len(cf)}")
                    wc=len(list(filter(lambda a:a!="",(' '.join((''.join(cf).split("\n"))).split(" ")))))
                    cc=len(list(" ".join(cf)))+1
                    print(f"Word Count:{wc}\nCharacter Count:{cc}")
            except FileNotFoundError:
                print("The file given was not found")
                continue

    else:
        print("Error: no file input")
