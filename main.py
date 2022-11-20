# +++++++++++++++++++++++++++++++++++++++++++++++++++
#  Copyright (c) 2022 TE1ch0st (Vitaliy Timtsurak). +
# +++++++++++++++++++++++++++++++++++++++++++++++++++

from time import sleep

import colorama
from tqdm import tqdm

colorama.init(autoreset=True)

logo = r'''
$$$$$$$$\ $$$$$$$$\   $$\             $$\        $$$$$$\              $$\     
\__$$  __|$$  _____|$$$$ |            $$ |      $$$ __$$\             $$ |    
   $$ |   $$ |      \_$$ |   $$$$$$$\ $$$$$$$\  $$$$\ $$ | $$$$$$$\ $$$$$$\   
   $$ |   $$$$$\      $$ |  $$  _____|$$  __$$\ $$\$$\$$ |$$  _____|\_$$  _|  
   $$ |   $$  __|     $$ |  $$ /      $$ |  $$ |$$ \$$$$ |\$$$$$$\    $$ |    
   $$ |   $$ |        $$ |  $$ |      $$ |  $$ |$$ |\$$$ | \____$$\   $$ |$$\ 
   $$ |   $$$$$$$$\ $$$$$$\ \$$$$$$$\ $$ |  $$ |\$$$$$$  /$$$$$$$  |  \$$$$  |
   \__|   \________|\______| \_______|\__|  \__| \______/ \_______/    \____/ 
   
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  Copyright (c) 2022 TE1ch0st (Vitaliy Timtsurak). "Угадывание слов"       +
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   '''


def init():
    words = []
    with open('russian_nouns.txt', mode='r', encoding='utf-8') as f:
        for i in f:
            words.append(i[:-1])
    return words


def set_word_length(words: list, lenght: int):
    for word in tqdm(words[:], desc='Set word length'):
        if len(word) != lenght:
            words.remove(word)
    return words


def delete_unused_char(words: list, chars: tuple):
    for char in chars:
        for word in tqdm(words[:], desc='Delete unused char'):
            if char in word:
                words.remove(word)
    return words


def choose_the_correct_char(words: list, chars: tuple):
    for char in chars:
        for word in tqdm(words[:], desc='Сhoose the correct char'):
            if char not in word:
                words.remove(word)
    return words


def choose_the_correct_letter(words: list, chars: tuple):
    for word in tqdm(words[:], desc='Choose the correct letter'):
        if chars[0] != word[chars[1] - 1]:
            words.remove(word)
    return words


def choose_the_incorrect_letter(words: list, chars: tuple):
    for word in tqdm(words[:], desc='Choose the incorrect letter'):
        if chars[0] == word[chars[1] - 1]:
            words.remove(word)
    return words


def main():
    print(colorama.Fore.RED + logo)
    foo = init()
    print(colorama.Fore.YELLOW + 'Введите длину угадываемых слов')
    lenght = int(input(colorama.Fore.BLUE + '~: '))
    if lenght != '':
        set_word_length(foo, lenght)

    while True:
        print(colorama.Fore.YELLOW + 'Введите буквы (слитно) которые отсутствуют в слове')
        unused = tuple(input(colorama.Fore.BLUE + '~: ').lower())
        if unused != ():
            delete_unused_char(foo, unused)
        del unused

        sleep(1)

        print(colorama.Fore.YELLOW + 'Введите буквы (слитно) которые присутствуют в слове')
        used = tuple(input(colorama.Fore.BLUE + '~: ').lower())
        if used != ():
            choose_the_correct_char(foo, used)
        del used

        sleep(1)

        print(colorama.Fore.YELLOW + 'Введите букву и ее положение (через пробел) в слове если вы уверены '
                                     'в ее расположении')
        correct = tuple(input(colorama.Fore.BLUE + '~: ').lower().split(' '))
        if correct != ('',):
            print(correct)
            choose_the_correct_letter(foo, (correct[0], int(correct[1])))
        del correct

        sleep(1)

        print(colorama.Fore.YELLOW + 'Введите букву и ее положение (через пробел) в слове если вы уверены '
                                     'что на данной позиции ее нет')
        incorrect = tuple(input(colorama.Fore.BLUE + '~: ').lower().split(' '))
        if incorrect != ('',):
            choose_the_incorrect_letter(foo, (incorrect[0], int(incorrect[1])))
        del incorrect

        sleep(1)

        # вывод слов
        for _ in foo:
            print(colorama.Fore.GREEN + _)

        sleep(1)

        if input(colorama.Fore.RED + 'Завершить программу Y\\N? -- ' + colorama.Fore.BLUE).lower() == 'y' or 'у':
            exit()


if __name__ == '__main__':
    main()
