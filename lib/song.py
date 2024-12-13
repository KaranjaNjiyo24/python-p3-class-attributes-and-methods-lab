class Song:

    count = 0
    genres = []
    artists = []
    genre_count = {} #dictionary
    artist_count = {}
    
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        Song.genres.append(genre)
        Song.artists.append(artist)
        self.add_to_genre_count()
        self.add_to_artist_count()

    def add_song_to_count(self):
        Song.count += 1

    def add_to_genre_count(self):
        if self.genre in Song.genre_count:
            Song.genre_count[self.genre] +=1
        else: 
            Song.genre_count[self.genre] = 1

    def add_to_artist_count(self):
        if self.artist in Song.artist_count:
            Song.artist_count[self.artist] +=1
        else:
            Song.artist_count[self.artist] = 1

    @classmethod
    def add_to_genres(cls):
        cls.genres = list(set(cls.genres))

    @classmethod
    def add_to_artists(cls):
        cls.artists = list(set(cls.artists))
    
    
    