from sp_playlist import get_song_dict
from lyrics import get_lyrics_list
import time, pprint

def musipy():
    link = input('Paste playlist URL...\n')
    song_dict = get_song_dict(link)
    song_vocab_dict = {}
    for song in song_dict.keys():
        vocab_list = get_lyrics_list(song, song_dict[song]['artist'])
        song_vocab_dict.update({song: {'vocabulary': vocab_list, 'artist': song_dict[song]['artist']}})

    with open('test.py', 'w') as f:
        f.write(pprint.pformat(song_vocab_dict))

    pprint.pprint(song_vocab_dict)

if __name__ == "__main__":
    musipy()

