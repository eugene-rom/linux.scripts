#!/usr/bin/env python3

#for get_word()
import pyperclip, time
#for keypress_checker()
import tty, sys
#for translate()
import googletrans, os

def keypress_checker():
    tty.setraw(sys.stdin)
    x = 0
    while x != chr(96): # ESC
        x=sys.stdin.read(1)[0]
    else:
        pass

def get_word():
    clipboard  = pyperclip.paste()
    while True:
        time.sleep(.1)
        if pyperclip.paste() != clipboard: break

    return pyperclip.paste()

def translate(new_word):
    translator=googletrans.Translator()
    translated=translator.translate(new_word, dest='tr')
    os.system('notify-send BERKLOCK-TRANSLATOR "{} -> {}"'.format(new_word, translated.text))

def main():
    print('running keypress_checker() ...')
    keypress_checker()
    print('keypress_checker() is done!')
    print('running get_word() ...')
    new_word = get_word()
    print('get_word is done! new word is: {}'.format(new_word))
    print('running translate() ...')
    translate(new_word)

if __name__ == '__main__':
    while True: main()
