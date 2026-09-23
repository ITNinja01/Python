from MorseCodePy import encode

txt_file = input("Enter the path to the text file: ")

with open(txt_file, 'r') as file:
    txt_input = file.read()

encoded_string = encode(txt_input, language='english')
print(encoded_string)