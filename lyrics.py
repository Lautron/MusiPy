import lyricsgenius, re, pyperclip
from config import genius_api_key

genius = lyricsgenius.Genius(genius_api_key)

def get_lyrics_list(song_title, author):
    lyrics = genius.search_song(song_title, artist=author).lyrics
    cleaned_lyrics = lyrics
    for rep in ['\n', '\u2005', "'s", "'", '?', ',']:
        cleaned_lyrics = cleaned_lyrics.replace(rep, ' ')
    lyrics_set = set(cleaned_lyrics.split(' '))
    return [word.strip() for word in lyrics_set if word and '[' not in word and ']' not in word]

if __name__ == "__main__":
    for i in get_lyrics_list("Military fashion show", 'And One'):
        print(i)
    # get_lyrics_list("Military fashion show")