alphabet = 'abcdefghijklmnopqrstuvwyz' \
               'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя' \
               '1234567890'
while True:
    print('Введiть З щоб Зашифрувати повідомлення, Р щоб розшифрувати і В щоб вийти')
    menu = input('Введіть текст ').lower()
    if menu == 'в':
        break
    elif not (menu == 'з' or menu == 'р'):
        continue
    output = ''
    message = input('Введіть текст: ').lower()
    key = +1
    if menu == 'р':
        key = -1
    for letter in message:
        if letter in alphabet:
            t = alphabet.find(letter)
            new_key = (t + key) % len(alphabet)
            output += alphabet[new_key]
        else:
            output += letter
    print('Результат: ' + output)