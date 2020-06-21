def hex_to_rgb():
    hexadecimal = input('Enter hex: ').lstrip('#')
    return print('RGB =', tuple(int(hexadecimal[i:i+2], 16) for i in (0, 2, 4)))
hex_to_rgb()