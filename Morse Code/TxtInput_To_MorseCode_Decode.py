from MorseCodePy import decode

txt_input = input("Enter text to convert to Morse code: ")

decoded_string = decode(txt_input, language='english')
print(decoded_string)