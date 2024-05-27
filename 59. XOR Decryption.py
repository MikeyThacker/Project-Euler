from statistics import *


def get_message():
    with open("cipher.txt") as file:
        numbers = file.readline()
    numbers = numbers.split(",")
    return [int(number) for number in numbers]


def decrypt_letter(letter, key):
    return letter ^ key


def split_by_thirds(message):
    count = -1
    list1 = []
    list2 = []
    list3 = []

    for letter in message:
        count += 1
        if count % 3 == 0:
            list1.append(letter)
        elif count % 3 == 1:
            list2.append(letter)
        elif count % 3 == 2:
            list3.append(letter)
    return list1, list2, list3


def main():
    """
    Key is made up of Three lower case characters
    All keys between 97 and 122 (inclusive)
    """

    encrypted_message = get_message()
    one, two, three = split_by_thirds(encrypted_message)
    mode_one = ord(chr(mode(one)).lower())

    mode_two = ord(chr(mode(two)).lower())

    mode_three = ord(chr(mode(three)).lower())

    decrypted_message = ""
    sum = 0
    count = -1
    for letter in encrypted_message:
        count += 1
        if count % 3 == 0:
            decrypted_message += chr(decrypt_letter(letter, mode_one))
            sum += decrypt_letter(letter, mode_one)
        elif count % 3 == 1:
            decrypted_message += chr(decrypt_letter(letter, mode_two))
            sum += decrypt_letter(letter, mode_two)
        elif count % 3 == 2:
            test = decrypt_letter(letter, mode_three)
            decrypted_message += chr(decrypt_letter(letter, mode_three))
            sum += decrypt_letter(letter, mode_three)
    print(decrypted_message)
    return sum


print(ord(" "))
print(main())
