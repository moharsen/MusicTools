from bs4 import BeautifulSoup
import requests

from mutagen.id3 import ID3, APIC, _util
from mutagen.mp3 import EasyMP3
import spotipy
from urllib.request import urlopen

from .improve import improve_name, img_search_google

class MusicRepair(object):

    def __init__(self):
        pass


    @staticmethod
    def get_details_spotify(file_name):
        '''
        Tries finding metadata through Spotify
        '''

        song_name = improve_name(file_name)

        spotify = spotipy.Spotify()
        results = spotify.search(song_name, limit=1)  # Find top result
        try:
            album = (results['tracks']['items'][0]['album']
                     ['name'])  # Parse json dictionary
            artist = (results['tracks']['items'][0]['album']['artists'][0]['name'])
            song_title = (results['tracks']['items'][0]['name'])

            return artist, album, song_title, ''


        except Exception as error:
            return ' ',' ', song_name, error

    @staticmethod
    def add_albumart(file_name, song_title):

        albumart = img_search_google(song_title)
        try:
            img = urlopen(albumart)  # Gets album art from url

        except Exception:
            return None

        audio = EasyMP3(file_name, ID3=ID3)
        try:
            audio.add_tags()
        except _util.error:
            pass

        audio.tags.add(
            APIC(
                encoding=3,  # UTF-8
                mime='image/png',
                type=3,  # 3 is for album art
                desc='Cover',
                data=img.read()  # Reads and adds album art
            )
        )
        audio.save()

        return albumart


    @staticmethod
    def add_details(file_name, title, artist, album):
        tags = EasyMP3(file_name)
        tags["title"] = title
        tags["artist"] = artist
        tags["album"] = album
        tags.save()