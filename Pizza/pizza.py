import sys
import csv
from tabulate import tabulate
if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) == 2 and ".csv" not in sys.argv[1]:
    sys.exit("Not a CSV file")
else:
    table = []
    try:
        count_lines = 0
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            for row in reader:
                table.append(row)
        print(tabulate(table[1:], headers = table[0], tablefmt="grid"))
    except:
        sys.exit("File does not exist")