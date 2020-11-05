import lyricsgenius, re, pyperclip, pprint
from config import genius_api_key

genius = lyricsgenius.Genius(genius_api_key)

def get_lyrics_list(song_title, author):
    lyrics = genius.search_song(song_title, artist=author).lyrics
    regx = re.compile(r'\[.*\]|')
    cleaned_lyrics = re.sub(regx, '', lyrics.replace('\u2005', ' '))
    lyrics_set = set(cleaned_lyrics.split('\n'))
    pprint.pprint(cleaned_lyrics.split('\n'))
    return [verse.strip() for verse in lyrics_set if verse]

if __name__ == "__main__":
    for i in get_lyrics_list("ZEIG DICH (traducción al español)", 'Rammstein'):
        print(i)