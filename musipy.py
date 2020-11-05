from sp_playlist import get_song_dict
from lyrics import get_lyrics_trans
import time, pprint, csv

def write_csv(data, filename='test'):
    with open(f'{filename}.csv', 'a', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for track in data.keys():
            writer.writerow([' ', ' '])
            writer.writerow([track, ' '])
            if data[track]['lyrics']:
                for verse, trans in data[track]['lyrics'].items():
                    row = [verse, trans]
                    writer.writerow(row)

def musipy():
    link = input('Paste playlist URL...\n')
    song_dict = get_song_dict(link)
    song_vocab_dict = {}
    start = time.time()
    for song in song_dict.keys():
        verse_list = get_lyrics_trans(song, song_dict[song]['artist'])
        song_vocab_dict.update({
            song: {'lyrics': verse_list,
                    'artist': song_dict[song]['artist']}
                })

    with open('test.py', 'w') as f:
        f.write(pprint.pformat(song_vocab_dict))

    write_csv(song_vocab_dict)
    print(f'The program took {time.time() - start} seconds\n')
    
if __name__ == "__main__":
    musipy()

