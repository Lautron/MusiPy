from google_trans_new import google_translator
import time

def translate_verse(verse, trans, desti='es'):
    translation = None
    while translation == None:

        translation = trans.translate(verse, lang_tgt=desti)
        try:
            pass
        except Exception as e:
            #TODO find a better way to translate verses
            print(f'\nVerse: {verse}\nException: {e}')
            return 'N/A'
            # trans = Translator()
            # time.sleep(0.5)
            # pass

    return translation
