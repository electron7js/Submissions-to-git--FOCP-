from sys import argv

if __name__ == "__main__":
    if len(argv) > 1:
        for i in argv[1:]:
            try:
                with open(i) as current_file:
                    line_no = 0
                    print(f"\n\n\nFilename:{i}\n\n")
                    for x in current_file:
                        print(line_no, x, end="")
                        line_no += 1
            except FileNotFoundError:
                print("The file given was not found")
                continue

    else:
        print("Error: no file input")
