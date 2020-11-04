import spotipy, pprint, re, pyperclip
from spotipy.oauth2 import SpotifyClientCredentials
from config import sp_id, sp_secret

sp = spotipy.Spotify(
    auth_manager=SpotifyClientCredentials(
        client_id=sp_id,
        client_secret=sp_secret)
        )

def get_plst_by_link(link):
    playlist_id = re.compile(r'/(\w{22})')\
                    .search(link)\
                    .group(1)
    return playlist_id

def get_plst_by_name(name, author):
    found = False
    results = sp.search(name, limit=50, type="playlist")
    for playlist in results['playlists']['items']:
        if playlist['owner']['display_name'] == author:
            found = True
            return playlist['id']

    if not found:
        print("Couldn't find playlist. Try searching by link instead.")

def main():
    playlist_id = get_plst_by_link('https://open.spotify.com/playlist/1BaY2hW7IKZt6ZJYIceSoJ?si=ibY5QL3qR12HL9q3mh0zLQ')
    playlist = sp.playlist(playlist_id)
    # with open('test.py', 'w') as f:
    #     f.write(pprint.pformat(playlist['tracks']['items']))
    print(playlist['tracks']['items'][0]['track']['name'])
    

if __name__ == "__main__":
    main()
