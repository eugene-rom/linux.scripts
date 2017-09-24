import pyperclip, pyxhook, googletrans, os

def pressChecker():
    clipboard=pyperclip.paste()

    while True:
        clipboard1=pyperclip.paste()
        if clipboard1 != clipboard:
            break
        else:
            continue

    return clipboard1

def OnKeyPress(event) :
    if event.Ascii == 96 :
        word=pressChecker()
        translator=googletrans.Translator()
        translated=translator.translate(word, dest='tr')
        print(word, translated)
        os.system('notify-send PYTRANSLATOR "{} -> {}"'.format(word, translated.text))

new_hook = pyxhook.HookManager()
new_hook.KeyDown=OnKeyPress
new_hook.HookKeyboard()
new_hook.start()
