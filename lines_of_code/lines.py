import sys
def main():
    check_command_line()
    with open(sys.argv[1]) as file:
        count = 0
        lines = file.readlines()
        for line in lines:
            if not line.isspace() and not line.lstrip().startswith("#"):
                count += 1
        print(count)

def check_command_line():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) == 2 and ".py" not in sys.argv[1]:
        sys.exit("Not a python file")

if __name__ == "__main__":
    main()