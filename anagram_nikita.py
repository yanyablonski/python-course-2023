first_word = input('Введите первое слово: ')
second_word = input('Введите второе слово: ')
if sorted(first_word) == sorted(second_word):
    print('Да')
else:
    print('Нет')