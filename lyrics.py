import lyricsgenius, re, pyperclip
from config import api_key

genius = lyricsgenius.Genius(api_key)

def get_lyrics_list(song_title):
    lyrics = genius.search_song(song_title).lyrics
    cleaned_lyrics = lyrics
    for rep in ['\n', '\u2005', "'s", "'", '?', ',']:
        cleaned_lyrics = cleaned_lyrics.replace(rep, ' ')
    lyrics_set = set(cleaned_lyrics.split(' '))
    return [word.strip() for word in lyrics_set if word and '[' not in word and ']' not in word]

if __name__ == "__main__":
    for i in get_lyrics_list("Military fashion show"):
        print(i)
    # get_lyrics_list("Military fashion show")