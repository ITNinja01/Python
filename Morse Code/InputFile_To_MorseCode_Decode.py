from MorseCodePy import decode

txt_file = input("Enter the path to the text file: ")

with open(txt_file, 'r') as file:
    txt_input = file.read()

decoded_string = decode(txt_input, language='english')
print(decoded_string)