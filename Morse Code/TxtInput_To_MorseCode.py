from MorseCodePy import encode

txt_input = input("Enter text to convert to Morse code: ")

encoded_string = encode(txt_input, language='english')
print(encoded_string)