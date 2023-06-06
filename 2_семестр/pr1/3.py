from dataclasses import dataclass
from typing import Union


class Musician:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, name_song):
        self.songs.append(Song(name_song, [self], None))
        return self.songs[-1]

    def create_album(self, name_album):
        return Album(name_album, self)


@dataclass
class Song:
    name_song: str
    musician: list
    album: Union['Album', None]


class Album:
    def __init__(self, name_album, musician):
        self.name_album = name_album
        self.musicians = [musician]
        self.songs = []

    def add_musician(self, new_musician):
        self.musicians.append(new_musician)
        for i in self.songs:
            i.musician.append(new_musician)
        self.musicians[-1].songs += self.songs
        return self.musicians[-1]

    def add_song(self, new_song):
        new_song.musician = self.musicians
        for i in self.musicians:
            i.songs.append(new_song)
        new_song.album = self
        self.songs.append(new_song)
        return self.songs[-1].name_song


class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)
        return self.songs[-1]


musician = Musician('музыкант')
song = musician.add_song('название песни')
album = musician.create_album('название альбома')
musician2 = Musician('музыкант2')
album.add_musician(musician2)
song2 = Song('2', [], album)
album.add_song(song2)
playlist = Playlist("плейлист")
playlist.add_song(song)
print('Песни музыканта: ', musician.songs)
print('Песни в альбоме: ', album.songs)
print('Песни музыканта2: ', musician2.songs)
print('Песни в плейлисте: ', playlist.songs)
print('Авторы песни: ', song.musician)
print('Авторы песни: ', song2.musician)
