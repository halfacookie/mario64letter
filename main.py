from PIL import Image

string = 'a a'
letters_folder = 'letters'
letter_unknown = 'unknown'
letter_space = "sp"
letter_format = 'png'
letter_index = 0
letter_size = (16, 16)

letter_map = {
    '?': 'qm',
    '"': 'dq',
    ' ': 'sp'
}

image_size = (0, 16)


string = str(input('Enter the text you want: '))


def open_image(x):
    return Image.open(letters_folder + '/' + x + '.' + letter_format)


def find_letter(letter):
    img = None
    try:
        img = open_image(letter)
    except OSError:
        if letter in letter_map:
            img = open_image(letter_map[letter])
        else:
            img = open_image(letter_unknown)
    except FileNotFoundError:
        if letter == ' ':
            img = open_image(letter_space)
        else:
            img = open_image(letter_unknown)

    return img


for letter in string:
    letter_index += 1

img_size = (letter_index * 16, image_size[1])
base_img = Image.new('RGBA', img_size, 'green')

letter_index = -1

for letter in string:
    letter_index += 1
    letter_img = find_letter(letter)
    base_img.paste(letter_img, (letter_index * 16, 0))

output_img = base_img.copy()
output_img.save('output.png')
