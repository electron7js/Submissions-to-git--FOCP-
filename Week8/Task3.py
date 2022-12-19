from sys import argv

if __name__ == "__main__":

    if len(argv) == 3:

        searchterm = argv[1]
        try:
            with open(argv[2]) as file:
                data = file.readlines()
        except FileNotFoundError:
            print("The file given was not found.")
        for line in data:
            if (searchterm in line):
                print(line)
                found = True
        if not found:
            print("The given string couldn't be found")
    else:
        print("Error: insufficient arguments")
