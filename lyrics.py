import lyricsgenius, re, pyperclip, pprint, csv
from config import genius_api_key
from translate import translate_verse

genius = lyricsgenius.Genius(genius_api_key)

def get_lyrics_list(song_title, author):
    try:
        lyrics = genius.search_song(song_title, artist=author).lyrics
    except:
        return None
    regx = re.compile(r'\[.*\]|')
    cleaned_lyrics = re.sub(regx, '', lyrics.replace('\u2005', ' '))
    lyrics_list = cleaned_lyrics.split('\n')
    return [verse.strip() for verse in lyrics_list if verse]

def get_lyrics_trans(song_title, author, trans_lang='es'):
    lang_dict = {
        'es': ' (traducción al español)'
    }
    songs = [song_title, song_title + lang_dict[trans_lang]]
    lyrics = [get_lyrics_list(song, author) for song in songs]
    if lyrics[1]:
        res = dict(zip(lyrics[0], lyrics[1]))
    else:
        #TODO handle translation not available on GENIUS
        lyrics = lyrics[0]
        print('\nTranslating song...')
        res = {translate_verse(verse): verse for verse in lyrics}

    with open('test.py', 'w') as f:
        f.write(pprint.pformat(res))
    return res

if __name__ == "__main__":
    print(get_lyrics_trans("PUPPE", 'Rammstein', trans_lang='es'))