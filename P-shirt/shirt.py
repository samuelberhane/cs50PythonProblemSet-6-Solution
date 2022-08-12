import sys
import os
from PIL import Image, ImageOps
def main():
    check_command_line()
    try:
        first_image = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")

    shirt = Image.open("shirt.png")
    size = shirt.size
    second_image = ImageOps.fit(first_image,size)
    second_image.paste(shirt,shirt)
    second_image.save(sys.argv[2])

def check_command_line():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    splited_fil1 = os.path.splitext(sys.argv[1])
    splited_fil2 = os.path.splitext(sys.argv[2])
    if splited_fil1[1] not in [".jpg",".jpeg",".png"]:
        sys.exit("Invalid input")
    elif splited_fil2[1] not in [".jpg",".jpeg",".png"]:
        sys.exit("Invalid input")
    elif splited_fil1[1] != splited_fil2[1]:
        sys.exit("Input and output have different extensions")


if __name__ == "__main__":
    main()
