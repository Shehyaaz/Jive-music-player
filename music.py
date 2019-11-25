from mutagen.mp3 import MP3

# Enrique Iglesias - Bailando ft. Sean Paul, Descemer Bueno, Gente De Zona (English Version)
''' 
if __name__=='__main__':
    audio = MP3("/Users/apple/Downloads/music/song1.mp3")
    print(audio.info.length)
    print(audio.info.bitrate)
    print(audio.info.pprint()) 
'''


'''from mutagen.mp3 import EasyMP3

mp3 = EasyMP3("/Users/apple/Downloads/music/song1.mp3")
mp3["title"] = "Bailando"
mp3["tracknumber"] = "some_tracknumber"
mp3["artist"] = "enri"
mp3["album"] = "songs"
mp3.save()
'''


from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
import mutagen.id3

filename = '/Users/apple/Downloads/music/song1.mp3'

# Example which shows how to automatically add tags to an MP3 using EasyID3

mp3file = MP3(filename, ID3=EasyID3)

try:
    mp3file.add_tags(ID3=EasyID3)
except mutagen.id3.error:
    print("has tags")

# mp3file['title'] = 'Newly tagged'
mp3file.save()
print(mp3file.pprint())
