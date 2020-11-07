from googletrans import Translator
import time

def translate_verse(verse, trans, desti='es'):
    translation = None
    while translation == None:
        try:
            translation = trans.translate(verse, dest=desti)
        except Exception as e:
            #TODO find a better way to translate verses
            print(f'\nVerse: {verse}\nException: {e}')
            return 'N/A'
            # trans = Translator()
            # time.sleep(0.5)
            # pass

    return translation.text
