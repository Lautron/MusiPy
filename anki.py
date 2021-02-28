import genanki, random
from test import test_dict

def get_model():
    style = """
    * {
        font-size: 1.1rem;
    }
    h2 {
        font-size: 1.5rem;
    }
    """
    model = genanki.Model(
      1106024768,
      'translated words model',
      fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
      ],
      templates=[
        {
          'name': 'Card 1',
          'qfmt': '<h2>{{Question}}</h2>',
          'afmt': '<h2>{{FrontSide}}</h2><hr id="answer">{{Answer}}',
        },
      ],
      css= style
      )
    return model

def get_deck_obj(name):
    deck = genanki.Deck(
        random.randrange(1 << 30, 1 << 31), name
        )
    return deck
def make_anki_deck(name, song_dict):
    decks = []
    model = get_model()
    for song in song_dict.keys():
        print(f'Creating {song} deck...')
        my_deck = get_deck_obj(song)
        for verse, trans in song_dict[song]['lyrics'].items():
            my_note = genanki.Note(
                model=model,
                fields=[verse, trans]
                )
            my_deck.add_note(my_note)
        decks.append(my_deck)
    print('Writing package...')
    genanki.Package(decks).write_to_file(f'{name.replace(" ", "-")}.apkg')
    print('Done')

if __name__ == "__main__":
    make_anki_deck('package', test_dict)
