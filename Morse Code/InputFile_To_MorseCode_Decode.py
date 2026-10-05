from MorseCodePy import decode
from pathlib import Path

# Can have both input and path on same line
txt_file = Path(input("Enter the path to the text file: "))

if txt_file.is_file():
    #Opening file to read it
    with open(txt_file, 'r') as file:
        txt_input = file.read()

    decoded_string = decode(txt_input, language='english')
    print(decoded_string)
else:
    print("The file does not exist.")