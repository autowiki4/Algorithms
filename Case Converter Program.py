def convert_to_snake_case(pascal_or_camel_cased_string):

    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()
        else char
        for char in pascal_or_camel_cased_string
    ]

    return ''.join(snake_cased_char_list).strip('_')
def main():
    print(convert_to_snake_case('IAmAPascalCasedString'))

if __name__ == '__main__':
    main()

sample = 'IAmAPascalCasedString'
print(sample.lower())
def convert_to_proper_name(raw_name):
    work = raw_name.lower()
    new_name = work[0].upper() + work[1:]
    return new_name

print(convert_to_proper_name('TuesDay'))
