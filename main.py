from album import Album
from artist import Artist
from genre import Genre
from track import Track
import csv


def import_artists(artists, fname):
    in_file = open(fname, 'r')
    for line in in_file:
        line = line.strip()
        pos = line.find(';')
        id = int(line[:pos])
        name = line[pos+1:]
        if id not in artists:
            artist = Artist(name)
            artists[id] = artist
    in_file.close()

def import_genres(genres, fname):
    in_file = open(fname, 'r')
    for line in in_file:
        line = line.strip()
        pos = line.find(';')
        id = int(line[:pos])
        name = line[pos+1:]
        if id not in genres:
            genre = Genre(name)
            genres[id] = genre
    in_file.close()

def import_albums(albums, fname):
    in_file = open(fname, 'r')
    for line in in_file:
        line = line.strip()
        pos = line.find(';')
        id = int(line[:pos])
        line = line[pos + 1:]
        pos = line.find(';')
        name = line[:pos]
        line = line[pos + 1:]
        artist_id = int(line)
        if id not in albums:
            album = Album(name, artist_id)
            albums[id] = album
    in_file.close()

def import_tracks(tracks, fname):
    in_file = open(fname, 'r')
    for line in in_file:
        line = line.strip()
        pos = line.find(';')
        id = int(line[:pos])
        line = line[pos + 1:]
        pos = line.find(';')
        track_name = line[:pos]
        line = line[pos + 1:]
        pos = line.find(';')
        id_album = int(line[:pos])
        line = line[pos + 1:]
        pos = line.find(';')
        id_genre = int(line[:pos])
        line = line[pos + 1:]
        pos = line.find(';')
        duration = int(line[:pos])
        line = line[pos + 1:]
        pos = line.find(';')
        size = int(line[:pos])
        line = line[pos + 1:]
        price = int(line)

        track = Track(track_name, id_album, id_genre, duration, size, price)
        tracks[id] = track

    in_file.close()

def comp(p1, p2):
    return p1.get_name() > p2.get_name()

artists = {}
genres = {}
albums = {}
tracks = {}
track = None
album = None
genre = None
artist = None
artist2 = None
import_tracks(tracks, "tracks.csv")
import_artists(artists, "artists.csv")
import_albums(albums, "albums.csv")
import_genres(genres, "genres.csv")
id_alb = 0
id_art = 0
id_gen = 0
s = {}
sorted_s = dict(sorted(s.items(), reverse=True))
for itt in artists:
    artist2 = artists[itt]
    sum = 0
    sorted_s = dict(sorted(s.items(), reverse=True))
    for it in tracks:
        track = tracks[it]
        id_gen = track.get_id_genre()
        id_alb = track.get_id_album()
        id_art = albums[id_alb].get_id_artist()
        artist = artists[id_art]
        genre = genres[id_gen]
        if genre.get_name() == "Rock" and artist.get_name() == artist2.get_name():
            sum += (track.get_duration()) / 1000
    if sum != 0:
        s[sum] = artist2.get_name()
for k, v in sorted_s.items():
  if v == "Dread Zeppelin":
    key = str(k // 1)
    print(key, "Сек")