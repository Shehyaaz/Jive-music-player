from mutagen.id3 import ID3
from lyrics_extractor import Song_Lyrics
import re
import urllib.request
from bs4 import BeautifulSoup


if __name__=='__main__':
    # audio = MP3("/home/shehyaaz/Music/Ishq Mubarak.mp3")
    # print(audio)

    audio = ID3("/home/shehyaaz/Music/04 Phir Mohabbat Murder 2-(Pagalworld.Com).mp3")
    #print(audio)
    print("Artist: %s" % audio['TPE1'].text[0])
    print("Track: %s" % audio["TIT2"].text[0])
    print("Release Year: %s" % audio["TDRC"].text[0])
    GCS_API_KEY = 'AIzaSyAZ59uTzToEyzWfBl7v-7yiCfTyZP94cBw'
    GCS_ENGINE_ID = '015343239474702540304:7l81lnsakdy'
    extract_lyrics = Song_Lyrics(GCS_API_KEY, GCS_ENGINE_ID)
    song_title, song_lyrics = extract_lyrics.get_lyrics('Phir Mohabbat')
    print(song_title)
    print(song_lyrics)
# API :  AIzaSyAZ59uTzToEyzWfBl7v-7yiCfTyZP94cBw
# Search Engine ID : 015343239474702540304:7l81lnsakdy