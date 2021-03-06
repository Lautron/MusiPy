from google_trans_new import google_translator
import time

def translate_verse(verse, desti='en'):
    trans = google_translator(timeout=5)
    translation = trans.translate(verse, lang_tgt=desti)
    if type(translation) is list:
        translation = translation[0]
    return translation
