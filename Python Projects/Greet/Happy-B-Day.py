
import datetime


i = input('Who\'s Birthday is it? ')


def english():
    print('Happy birthday to you,')
    print('Happy birthday to you,')
    print('Happy birthday dear ' + str(i))
    print('Happy birthday to you.')


def french():
    print('Bon anniversaire,')
    print('Bon anniversaire,')
    print('Bon anniversaire mon cher ' + str(i))
    print('Bon anniversaire.')


def spanish():
    print('Cumpleaños feliz,')
    print('Cumpleaños feliz,')
    print('Cumpleaños feliz querida ' + str(i))
    print('Cumpleaños feliz,')


def check():
    lang = input('In which language would you like it? Spanish, French or English?  ')
    if lang == 'spanish' or lang == 'Spanish' or lang == 'SPANISH':
        spanish()
    elif lang == 'french' or lang == 'French' or lang == 'FRENCH':
        french()
    elif lang == 'english' or lang == 'English' or lang == 'ENGLISH':
        english()
    else:
        print('I do not think that was an option. Please try again. ')
        check()


check()
input('Press ENTER when you have finished.')
