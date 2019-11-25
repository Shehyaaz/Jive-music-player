import sqlite3

db = sqlite3.connect('UserPlaylist.db')
print('Database open')
cursor = db.cursor()
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS playlist(SongName TEXT,Artist TEXT,Released VARCHAR(10),Path VARCHAR(100),
    NumberOfTimes INT);''')
song_name = input('Song Name: ')
artist = input('Artist: ')
released = input('Song Released: ')
path = input('Path: ')
times = input('Number of times played: ')
put = '''Insert into playlist(SongName,Artist,Released,Path,NumberOfTimes)  Values(?,?,?,?,?);'''
values = (song_name, artist, released, path, times)
cursor.execute(put, values)
cursor.execute('SELECT * FROM playlist')
result = cursor.fetchall()
for r in result:
    print(r)
cursor.execute('SELECT * FROM playlist')
cursor.close()


def number(self):
    if self.playlist.mediaCount() > 0:
        self.playlist += 1
