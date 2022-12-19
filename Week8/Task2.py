from sys import argv

if __name__ == "__main__":

    if len(argv) == 3:
        try:
            with open(argv[1]) as file1:
                data1 = file1.read()
            with open(argv[2]) as file2:
                data2 = file2.read()
        except FileNotFoundError:
            print("The file given was not found.")
        if (data1 == data2):
            print("The given files are the same")
        else:
            print("The given files are different.")
    else:
        print("Error: not enough files input")
