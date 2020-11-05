from sp_playlist import get_song_dict
from lyrics import get_lyrics_list
from translate import translate_verse
import time, pprint

def musipy():
    link = input('Paste playlist URL...\n')
    song_dict = get_song_dict(link)
    song_vocab_dict = {}
    start = time.time()
    for song in song_dict.keys():
        verse_list = get_lyrics_list(song, song_dict[song]['artist'])
        song_vocab_dict.update({
            song: {'lyrics': {translate_verse(verse): verse for verse in verse_list},
                    'artist': song_dict[song]['artist']}
                })

    with open('test.py', 'w') as f:
        f.write(pprint.pformat(song_vocab_dict))

    print(f'The program took {time.time() - start} seconds\n')
    
if __name__ == "__main__":
    musipy()

