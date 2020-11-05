import lyricsgenius, re, pyperclip
from config import genius_api_key

genius = lyricsgenius.Genius(genius_api_key)

def get_lyrics_list(song_title, author):
    lyrics = genius.search_song(song_title, artist=author).lyrics
    cleaned_lyrics = lyrics.replace('\u2005', ' ')
    # for rep in ['\n', '\u2005', "'s", "'", '?', ',', '!']:
    #     cleaned_lyrics = cleaned_lyrics.replace(rep, ' ')
    lyrics_set = set(cleaned_lyrics.split('\n'))
    is_allowed = lambda verse: 'Chorus' not in verse and 'Verse' not in verse
    return [verse.strip() for verse in lyrics_set if is_allowed(verse)]

if __name__ == "__main__":
    # for i in get_lyrics_list("Military fashion show", 'And One'):
    #     print(i)
    for i in get_lyrics_list("Chorus", 'Erasure'):
        print(i)
    # get_lyrics_list("Military fashion show")