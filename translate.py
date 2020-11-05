import googletrans
from googletrans import Translator

def translate_verse(verse, desti='es'):
    trans = Translator()
    try:
        translation = trans.translate(verse, dest=desti)
    except:
        return 'N/A'

    return translation.text
