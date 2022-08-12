import csv
import sys
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) == 3 and (".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]):
    sys.exit("Not a CSV file")
else:
    try:
        splited = []
        with open(sys.argv[1]) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                names = row["name"].split(",")
                splited.append({"first": names[1].lstrip(), "last": names[0].lstrip(), "house": row["house"]})
    except:
        sys.exit(f"could not read {sys.argv[1] or sys.argv[2]}")

    with open(sys.argv[2],"w") as file:
            writer = csv.DictWriter(file,fieldnames=["first","last","house"])
            writer.writerow({"first": "first","last": "last","house": "house"})
            for row in splited:
                writer.writerow({"first":row["first"], "last" : row["last"], "house": row["house"]})